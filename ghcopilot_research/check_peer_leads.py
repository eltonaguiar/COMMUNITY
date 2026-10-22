"""Bounded read-only audit of newly published peer hypotheses, not a search."""
import collections
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path.cwd()))
import pymysql
from tools.db_env import get_stocks_creds
from tools.ghcopilot_paper_monitor import summarize

OUT = Path(__file__).resolve().parent
LEADS = [
    ("quan_engine_swing", "HYPEUSDT", .30),
    ("meta_strategy", "PENGUUSDT", .30),
    ("enhanced_ml_A_xgboost", "JTOUSDT", .30),
    ("smart_money_accumulation", "UNH", .10),
]


def main():
    args = get_stocks_creds()
    args.update(connect_timeout=20, read_timeout=90,
                cursorclass=pymysql.cursors.DictCursor)
    db = pymysql.connect(**args)
    results = []
    try:
        with db.cursor() as cur:
            cur.execute("SET TRANSACTION ISOLATION LEVEL REPEATABLE READ")
            cur.execute("START TRANSACTION WITH CONSISTENT SNAPSHOT, READ ONLY")
            cur.execute("SELECT UTC_TIMESTAMP() stamp")
            stamp = str(cur.fetchone()["stamp"])
            for strategy, symbol, cost in LEADS:
                cur.execute("""
                    SELECT source_system,strategy,symbol,asset_class,direction,
                    entry_price,take_profit,stop_loss,opened_at,closed_at,created_at,
                    outcome,pnl_pct,intrabar_status,intrabar_pnl_pct,
                    intrabar_ambiguous,reverse_split_affected
                    FROM at_signal_outcomes WHERE strategy=%s AND symbol=%s
                    ORDER BY opened_at
                """, (strategy, symbol))
                rows = cur.fetchall()
                sources = collections.defaultdict(list)
                for row in rows:
                    sources[(row["source_system"], row["direction"])].append(row)
                groups = []
                for (source, direction), cohort in sources.items():
                    strict = [r for r in cohort if r["intrabar_ambiguous"] == 0
                              and r["intrabar_status"] in ("TP_HIT", "SL_HIT", "TIME_EXIT")
                              and r["intrabar_pnl_pct"] is not None and r["opened_at"]
                              and not r["reverse_split_affected"]]
                    groups.append({
                        "source": source, "direction": direction, "n_all": len(cohort),
                        "statuses": dict(collections.Counter(r["outcome"] for r in cohort)),
                        "replay_statuses": dict(collections.Counter(
                            str(r["intrabar_status"]) for r in cohort)),
                        "missing_created": sum(r["created_at"] is None for r in cohort),
                        "ambiguous_or_unknown": sum(r["intrabar_ambiguous"] != 0 for r in cohort),
                        "missing_replay_pnl": sum(r["intrabar_pnl_pct"] is None for r in cohort),
                        "first_entry": str(cohort[0]["opened_at"]),
                        "last_entry": str(cohort[-1]["opened_at"]),
                        "basic_replay_net_summary": summarize([
                            {"entry_at": r["opened_at"],
                             "net_pct": float(r["intrabar_pnl_pct"]) - cost} for r in strict]),
                    })
                cur.execute("""
                    SELECT source_system,status,COUNT(*) n,
                    MAX(signal_timestamp) latest_signal,MAX(recorded_at) latest_recorded,
                    SUM(recorded_at >= UTC_TIMESTAMP()-INTERVAL 24 HOUR) recorded24h
                    FROM at_raw_picks WHERE strategy=%s AND symbol=%s
                    GROUP BY source_system,status
                """, (strategy, symbol))
                results.append({"strategy": strategy, "symbol": symbol,
                                "cost_scenario_pp": cost, "outcome_groups": groups,
                                "raw_groups": cur.fetchall()})
    finally:
        db.rollback()
        db.close()
    result = {"snapshot_utc": stamp, "read_only": True,
              "warning": "Peer-selected hypotheses. Basic replay filter is not provenance, full policy or independent price-path certification. Per-trade not MTM. No exhaustive symbol search.",
              "results": results}
    (OUT / "GHCOPILOT_PEER_LEADS_2026-10-22.json").write_text(
        json.dumps(result, default=str, indent=2, allow_nan=False) + "\n")
    for item in results:
        print(item["strategy"], item["symbol"])
        for g in item["outcome_groups"]:
            s = g["basic_replay_net_summary"]
            print(g["source"], g["direction"], "all", g["n_all"], "replay", s["n"],
                  "PF", s["net_pf"], "mean", s["net_mean_pct"], "CI", s["day_bootstrap_ci95"])


if __name__ == "__main__":
    main()
