"""Read-only exploratory census; never emits signals or changes a paper lock."""
import collections
import hashlib
import json
import math
import os
import subprocess
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path

ROOT = Path(os.environ.get("AUDIT_REPO_ROOT", Path.cwd())).resolve()
sys.path.insert(0, str(ROOT))
import pymysql
from audit_trail.quality_gates import (
    BLOCKED_ASSET_STRATEGY_PAIRS,
    BLOCKED_DIRECTION_TRIPLES,
    BLOCKED_SOURCE_SYSTEMS,
    PERMANENTLY_KILLED_STRATEGIES,
    PF_REGISTRY_POLICY_EXCLUDED,
)
from tools.db_env import get_backtests_creds, get_stocks_creds
from tools.ghcopilot_paper_monitor import geometry, number, source_key, summarize, utc

OUT = Path(os.environ.get("AUDIT_OUTPUT_DIR", Path(__file__).resolve().parent))
CLASSES = ("CRYPTO", "EQUITY", "FOREX", "COMMODITY", "FUTURES",
           "ETF", "BOND", "PENNY_STOCK", "MEMECOIN")
COSTS = {c: 0.30 if c in ("CRYPTO", "MEMECOIN") else 0.10 for c in CLASSES}
LIMITS = {"FOREX": 20, "COMMODITY": 30, "BOND": 25, "CRYPTO": 95}
FLAT = {str(x).lower() for x in (
    set(BLOCKED_SOURCE_SYSTEMS) | set(PERMANENTLY_KILLED_STRATEGIES)
    | set(PF_REGISTRY_POLICY_EXCLUDED))}
PAIRS = {(str(a).upper(), str(s).lower()) for a, s in BLOCKED_ASSET_STRATEGY_PAIRS}
TRIPLES = {(str(a).upper(), str(s).lower(), str(d).upper())
           for a, s, d in BLOCKED_DIRECTION_TRIPLES}


def connection(factory):
    args = factory()
    args.update(connect_timeout=20, read_timeout=120,
                cursorclass=pymysql.cursors.DictCursor)
    return pymysql.connect(**args)


def policy_blocked(row):
    cls = row["asset_class"]
    strategy = str(row["strategy"] or "").lower()
    return (strategy in FLAT or str(row["source_system"] or "").lower() in FLAT
            or (cls, strategy) in PAIRS or (cls, strategy, row["direction"]) in TRIPLES)


def finite_json(value):
    if isinstance(value, datetime):
        return utc(value).isoformat()
    if isinstance(value, dict):
        return {k: finite_json(v) for k, v in value.items()}
    if isinstance(value, (list, tuple)):
        return [finite_json(x) for x in value]
    if value is None or isinstance(value, (str, bool, int, float)):
        return value
    return float(value)


def fetch():
    db = connection(get_stocks_creds)
    try:
        with db.cursor() as cursor:
            cursor.execute("SET SESSION TRANSACTION READ ONLY")
            cursor.execute("SELECT UTC_TIMESTAMP() stamp")
            now = utc(cursor.fetchone()["stamp"])
            cursor.execute("""
                SELECT id,symbol,source_system,strategy,asset_class,direction,
                  entry_price,take_profit,stop_loss,opened_at,closed_at,created_at,
                  outcome,intrabar_status,intrabar_pnl_pct,intrabar_ambiguous,
                  intrabar_resolved_at,intrabar_horizon_bars,reverse_split_affected
                FROM at_signal_outcomes
                WHERE opened_at >= %s AND opened_at <= %s
                ORDER BY opened_at,id
            """, ((now - timedelta(days=120)).replace(tzinfo=None),
                  now.replace(tzinfo=None)))
            rows = cursor.fetchall()
            cursor.execute("""
                SELECT asset_class,source_system,strategy,COUNT(*) n,
                  COUNT(DISTINCT symbol) symbols,MAX(signal_timestamp) latest_signal,
                  SUM(recorded_at >= UTC_TIMESTAMP()-INTERVAL 24 HOUR) recorded_24h,
                  SUM(signal_timestamp IS NULL) missing_signal,
                  SUM(was_stale=1 OR was_banned=1 OR was_demoted=1) flagged,
                  SUM(status='OPEN') open_n
                FROM at_raw_picks
                GROUP BY asset_class,source_system,strategy
            """)
            feeds = cursor.fetchall()
            cursor.execute("SHOW TABLES")
            tables = [next(iter(r.values())) for r in cursor.fetchall()]
            market_tables = [t for t in tables if any(
                s in t.lower() for s in ("ohlcv", "price_history", "copy_trad", "hl_trad"))]
    finally:
        db.close()
    back = connection(get_backtests_creds)
    try:
        with back.cursor() as cursor:
            cursor.execute("SET SESSION TRANSACTION READ ONLY")
            cursor.execute("""
                SELECT asset_class,COUNT(*) runs,COUNT(DISTINCT strategy) strategies,
                  COUNT(DISTINCT symbol) symbols,MAX(imported_at) latest_import,
                  SUM(total_trades>=100 AND profit_factor>=1.5) nominal_pass_runs,
                  MAX(profit_factor) max_reported_pf
                FROM bt_backtest_runs GROUP BY asset_class
            """)
            archive = cursor.fetchall()
            cursor.execute("""
                SELECT COUNT(*) runs,COUNT(DISTINCT archetype) archetypes,
                  COUNT(DISTINCT symbol) symbols,MAX(created_at) latest_created,
                  SUM(total_trades>=100 AND profit_factor>=1.5) nominal_pass_runs
                FROM at_large_backtest_results
            """)
            large = cursor.fetchone()
    finally:
        back.close()
    return now, rows, feeds, market_tables, archive, large


def analyze(now, rows, feeds):
    grouped = collections.defaultdict(list)
    input_counts = collections.Counter()
    rejects = collections.Counter()
    seen = set()
    for row in rows:
        cls = row["asset_class"]
        input_counts[cls] += 1
        reason = None
        try:
            if cls not in CLASSES:
                raise ValueError("outside_scope")
            if not row["strategy"] or not row["source_system"]:
                raise ValueError("missing_identity")
            if policy_blocked(row):
                raise ValueError("policy_excluded")
            if row["strategy"] == "vt_equity_two_day_rsi_reversal":
                raise ValueError("known_historical_reemission")
            if row["reverse_split_affected"]:
                raise ValueError("reverse_split")
            if row["intrabar_status"] not in ("TP_HIT", "SL_HIT", "TIME_EXIT"):
                raise ValueError("no_resolved_replay")
            if row["intrabar_ambiguous"] is None or row["intrabar_ambiguous"]:
                raise ValueError("ambiguous_or_unknown_flag")
            if row["intrabar_resolved_at"] is None:
                raise ValueError("missing_replay_timestamp")
            stamp = utc(row["opened_at"])
            if not stamp <= utc(row["intrabar_resolved_at"]) <= now + timedelta(minutes=5):
                raise ValueError("invalid_replay_chronology")
            pnl = number(row["intrabar_pnl_pct"])
            if abs(pnl) > LIMITS.get(cls, 50):
                raise ValueError("outlier")
            geometry(row)
            key = cls, source_key(row["source_system"]), row["strategy"]
            identity = (*key, row["symbol"], row["direction"], stamp.isoformat())
            if identity in seen:
                raise ValueError("duplicate_identity")
            seen.add(identity)
            grouped[key].append(row)
        except (ValueError, KeyError, TypeError) as exc:
            reason = str(exc)
        if reason:
            rejects[f"{cls}:{reason}"] += 1
    feed_map = collections.defaultdict(list)
    for row in feeds:
        feed_map[row["asset_class"], source_key(row["source_system"]), row["strategy"]].append(row)
    results = []
    for (cls, source, strategy), values in sorted(grouped.items()):
        returns = [{"entry_at": utc(v["opened_at"]).isoformat(),
                    "net_pct": number(v["intrabar_pnl_pct"]) - COSTS[cls]}
                   for v in values]
        stats = summarize(returns)
        weekly = []
        for value in returns:
            stamp = utc(value["entry_at"])
            week = stamp - timedelta(days=stamp.weekday())
            weekly.append({**value, "entry_at": week.date().isoformat()})
        week_stats = summarize(weekly)
        pnls = sorted(v["net_pct"] for v in returns)
        trimmed = pnls[:-max(1, math.ceil(len(pnls) * 0.05))]
        months = collections.Counter(utc(v["opened_at"]).strftime("%Y-%m") for v in values)
        symbol_counts = collections.Counter(v["symbol"] for v in values)
        feed = feed_map[cls, source, strategy]
        latest = max(utc(v["opened_at"]) for v in values)
        eligible = (stats["n"] >= 20 and stats["entry_days"] >= 10
                    and stats["net_mean_pct"] > 0 and (stats["net_pf"] or 0) > 1)
        results.append({
            "asset_class": cls, "source": source, "strategy": strategy, **stats,
            "scenario_roundtrip_cost_pp": COSTS[cls],
            "week_bootstrap_ci95": week_stats["day_bootstrap_ci95"],
            "entry_month_counts": dict(months),
            "top_5pct_removed_mean_pct": sum(trimmed) / len(trimmed) if trimmed else None,
            "symbol_count": len(symbol_counts),
            "symbol_counts": dict(symbol_counts.most_common()),
            "largest_symbol_fraction": max(symbol_counts.values()) / len(values),
            "latest_replayed_signal": latest.isoformat(),
            "latest_replayed_signal_age_days": (now - latest).total_seconds() / 86400,
            "raw_recorded_24h": sum(int(f["recorded_24h"] or 0) for f in feed),
            "raw_historical_symbols": max([f["symbols"] for f in feed], default=0),
            "research_eligible": eligible,
            "status": "RESEARCH_CANDIDATE_NOT_PROVEN" if eligible else
                      "INSUFFICIENT_SAMPLE" if stats["n"] < 20 or stats["entry_days"] < 10
                      else "NEGATIVE_NET_EVIDENCE",
            "independent_market_path_certified": False,
        })
    classes = {}
    for cls in CLASSES:
        groups = [g for g in results if g["asset_class"] == cls]
        groups.sort(key=lambda g: (
            g["research_eligible"],
            g["net_mean_pct"] > 0 and g["n"] >= 10 and g["entry_days"] >= 5,
            g["n"] >= 20 and g["entry_days"] >= 10,
            (g["day_bootstrap_ci95"] or [-100])[0], g["n"]), reverse=True)
        classes[cls] = {
            "input_rows": input_counts[cls],
            "retained_rows": sum(g["n"] for g in groups), "groups": len(groups),
            "research_eligible_count": sum(g["research_eligible"] for g in groups),
            "requested": 5, "research_shortfall": max(0, 5 - sum(
                g["research_eligible"] for g in groups)),
            "top5_diagnostic_not_buy_recommendations": groups[:5],
        }
    return {"classes": classes, "all_groups": results, "exclusions": dict(rejects)}


def main():
    now, rows, feeds, market_tables, archive, large = fetch()
    report = analyze(now, rows, feeds)
    report.update({
        "schema_version": 1, "checked_at": now.isoformat(), "window_days": 120,
        "source_commit_local": subprocess.check_output(
            ["git", "rev-parse", "HEAD"], cwd=ROOT, text=True).strip(),
        "method": "Read-only exploratory ranking of entry-anchored replay rows; explicit policy/geometry/ambiguity/chronology checks. Not independent price-path certification.",
        "ranking": "Research eligible first; then positive mean with n>=10/5 days; then n>=20/10 days; then entry-day bootstrap lower bound; then n. Diagnostic ranks are not five buy recommendations. No symbolic subgroup search.",
        "limitations": [
            "No resolver_version exists on at_signal_outcomes; backfill/resolver lineage cannot be certified.",
            "Outcome creation timestamps are not original source observation timestamps.",
            "Reported coinflip_p is an IID descriptive diagnostic, not a dependent economic significance test.",
            "Costs are scenarios, not measured execution; statistics are trade returns, not a capital-constrained MTM portfolio.",
            "No strategy is certified. All familywise/holdout/independent market gates remain outstanding.",
            "Historical symbol counts are not current scanner universe or provider coverage.",
            "No automatic candidate changes or paper-lock modifications.",
        ],
        "raw_feed_groups": feeds, "market_or_copy_table_names": market_tables,
        "backtest_archive_class_census": archive, "large_backtest_census": large,
        "policy_hash": hashlib.sha256(json.dumps(
            [sorted(FLAT), sorted(PAIRS), sorted(TRIPLES)]).encode()).hexdigest(),
    })
    path = OUT / "GHCOPILOT_TOP5_EVIDENCE_2026-10-22.json"
    path.write_text(json.dumps(finite_json(report), indent=2, allow_nan=False) + "\n")
    print("Saved", path.name, "groups", len(report["all_groups"]),
          "input", len(rows), "retained", sum(g["n"] for g in report["all_groups"]))
    for cls, v in report["classes"].items():
        print(cls, "groups", v["groups"], "eligible", v["research_eligible_count"],
              "shortfall", v["research_shortfall"])
        for g in v["top5_diagnostic_not_buy_recommendations"]:
            print(g["strategy"], g["n"], round(g["net_pf"] or 0, 3),
                  g["entry_days"], g["symbol_count"], g["status"])


if __name__ == "__main__":
    main()
