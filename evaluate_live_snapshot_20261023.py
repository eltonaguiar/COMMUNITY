"""Read-only descriptive snapshot audit; no strategy search or approval."""
from collections import Counter
from datetime import datetime, timedelta, timezone
import hashlib
import json
import math
from pathlib import Path

HERE = Path(__file__).resolve().parent
SNAPSHOT = HERE / "live-review-1812"


def finite(value):
    return isinstance(value, (float, int)) and not isinstance(value, bool) and math.isfinite(value)


def timestamp(value):
    if not value:
        return None
    if value.endswith(" EST"):
        value = value[:-4] + "-05:00"
    result = datetime.fromisoformat(value.replace("Z", "+00:00"))
    # Only used for descriptive sorting; the original string remains preserved.
    return result.replace(tzinfo=timezone.utc) if result.tzinfo is None else result


def clean(value):
    if isinstance(value, float) and not math.isfinite(value):
        return None
    if isinstance(value, dict):
        return {key: clean(item) for key, item in value.items()}
    if isinstance(value, list):
        return [clean(item) for item in value]
    return value


def stats(rows):
    values = [row["pnl_pct"] for row in rows if finite(row.get("pnl_pct"))]
    wins = [v for v in values if v > 0]
    losses = [v for v in values if v < 0]
    return {
        "records": len(rows), "numeric_pnl": len(values), "positive": len(wins),
        "negative": len(losses), "zero": sum(v == 0 for v in values),
        "pf_published_pnl_only": sum(wins) / -sum(losses) if losses else None,
        "pf_undefined_no_losses": not losses,
        "distinct_ids": len({row["id"] for row in rows}),
        "distinct_close_dates": len({str(row.get("closed_at"))[:10] for row in rows}),
        "source_counts": dict(Counter(row["source_system"] for row in rows)),
        "exit_reason_counts": dict(Counter(str(row.get("exit_reason")) for row in rows)),
        "net_cost_populated": sum(row.get("after_cost_net_per_trade") is not None for row in rows),
    }


def main():
    data = json.loads((SNAPSHOT / "dashboard_data.json").read_text())
    registry = json.loads((SNAPSHOT / "pf_registry.json").read_text())
    verdict = json.loads((SNAPSHOT / "money_ready_verdict.json").read_text())
    observations = json.loads((SNAPSHOT / "observations.json").read_text())
    now = max(timestamp(row["observed_at"]) for row in observations)
    active = data["picks"]["active"]
    closed = data["picks"]["recent_closed"]
    active_fields = (
        "id", "symbol", "asset_class", "strategy", "source_system", "direction",
        "entry_price", "current_price", "take_profit", "stop_loss", "timestamp",
        "entry_time", "pnl_pct", "forward_validated", "forward_trades", "forward_wr",
        "strat_fwd_trades", "strat_fwd_pf", "strat_fwd_wr", "sym_dir_fwd_n",
        "sym_dir_fwd_pf", "sym_track_total_pit", "sym_track_wr_pit",
        "_gate_passed", "_below_gate", "_direction_conflict", "_pick_lifecycle_id",
        "recent_max_dd", "strat_last10_wr", "strat_sample_quality", "trust_tier",
    )
    active_output = []
    for row in active:
        item = {key: row.get(key) for key in active_fields}
        entry, target, stop = [row.get(key) for key in ("entry_price", "take_profit", "stop_loss")]
        geometry = (finite(entry) and finite(target) and finite(stop) and entry > 0
                    and ((stop < entry < target) if row["direction"] == "LONG"
                         else target < entry < stop))
        item["barrier_geometry_valid"] = geometry
        item["reward_to_risk"] = abs(target - entry) / abs(stop - entry) if geometry else None
        item["signal_age_hours_at_observation"] = (
            (now - timestamp(row["timestamp"])).total_seconds() / 3600
            if row.get("timestamp") else None
        )
        matches = []
        for cohort in registry["by_asset_class_strategy_policy_clean_net"]:
            if (cohort["asset_class"] == row["asset_class"]
                    and cohort["strategy"] in {row["strategy"], row["source_system"]}):
                matches.append({
                    "match_level": "strategy" if cohort["strategy"] == row["strategy"] else "source",
                    **{key: cohort.get(key) for key in (
                        "asset_class", "strategy", "n", "wins", "losses", "profit_factor",
                        "win_rate_pct", "top_source", "single_source_pct")},
                })
        item["registry_exact_name_matches"] = matches
        active_output.append(item)
    class_summaries = []
    examples = []
    for asset in sorted({r["asset_class"] for r in closed}):
        rows = [r for r in closed if r["asset_class"] == asset]
        latest = sorted(rows, key=lambda r: timestamp(r["closed_at"]), reverse=True)
        record = {"asset_class": asset, "container": stats(rows),
                  "earliest_close": latest[-1]["closed_at"], "latest_close": latest[0]["closed_at"]}
        for hours in (48, 336):
            record[f"observed_last_{hours}h"] = stats([
                r for r in rows if now - timedelta(hours=hours) <= timestamp(r["closed_at"]) <= now
            ])
        class_summaries.append(record)
        examples.extend({key: row.get(key) for key in (
            "id", "symbol", "asset_class", "direction", "strategy", "source_system",
            "entry_price", "exit_price", "timestamp", "entry_time", "closed_at",
            "status", "pnl_pct", "exit_reason", "after_cost_net_per_trade",
        )} for row in latest[:2])
    active_cohorts = []
    for asset, strategy, source in sorted({
        (r["asset_class"], r["strategy"], r["source_system"]) for r in active
    }):
        rows = [r for r in closed if r["asset_class"] == asset and r["strategy"] == strategy
                and r["source_system"] == source]
        active_cohorts.append({"asset_class": asset, "strategy": strategy,
                               "source_system": source, **stats(rows)})
    fingerprints = Counter(tuple(str(row.get(k)) for k in (
        "symbol", "direction", "strategy", "source_system", "timestamp", "entry_price", "closed_at"
    )) for row in closed)
    result = {
        "observed_at": now.isoformat(), "dashboard_generated_at": data["generated_at"],
        "retrieval_observations": observations,
        "auxiliary_retrieval_observations": json.loads((SNAPSHOT / "extra-observations.json").read_text()),
        "registry_generated_at": registry["generated_utc"],
        "verdict_generated_at": verdict["generated_at"],
        "scope": "Only downloaded containers; not complete database or independently verified executions",
        "active_count": len(active), "active_symbols": len({r["symbol"] for r in active}),
        "smart_picks_count": len(data["picks"]["smart_picks"]),
        "active_raw_count": len(data["picks"]["active_raw"]),
        "active_raw_status_counts": dict(Counter(r["status"] for r in data["picks"]["active_raw"])),
        "closed_records": len(closed), "closed_distinct_ids": len({r["id"] for r in closed}),
        "closure_timestamp_assumptions": {
            "explicit_EST_treated_as_fixed_minus_05": sum(
                str(r["closed_at"]).endswith(" EST") for r in closed),
            "warning": "EST is interpreted literally, not as daylight-aware Eastern time. "
                       "Naive timestamps are assumed UTC for sorting only. Original strings retained.",
        },
        "closed_exact_fingerprint_duplicates": sum(n - 1 for n in fingerprints.values()),
        "largest_close_timestamp_clusters": Counter(
            row["closed_at"] for row in closed).most_common(5),
        "largest_close_cluster_details": [
            {
                "closed_at": time, "records": count,
                "source_counts": dict(Counter(r["source_system"] for r in closed
                                              if r["closed_at"] == time)),
                "source_signal_timestamp_min": min(str(r["timestamp"]) for r in closed
                                                   if r["closed_at"] == time),
                "source_signal_timestamp_max": max(str(r["timestamp"]) for r in closed
                                                   if r["closed_at"] == time),
                "published_pnl_counts": dict(Counter(str(r["pnl_pct"]) for r in closed
                                                     if r["closed_at"] == time)),
            }
            for time, count in Counter(r["closed_at"] for r in closed).most_common(1)
        ],
        "class_registry_policy_clean_net": registry["by_asset_class_policy_clean_net"],
        "registry_promotion_eligible": registry["promotion_eligible"],
        "registry_strategy_rows_screened": len(registry["by_asset_class_strategy_policy_clean_net"]),
        "registry_discovery_floor_inventory": [
            row for row in registry["by_asset_class_strategy_policy_clean_net"]
            if row["n"] >= 100 and finite(row.get("profit_factor")) and row["profit_factor"] >= 1.5
        ],
        "verdict_summary": verdict["summary"],
        "active_records": active_output, "recent_closed_by_class": class_summaries,
        "recent_close_examples": examples, "active_strategy_closed_container_matches": active_cohorts,
        "published_recency_panels": {
            label: json.loads((SNAPSHOT / f"data_pick_summary_stats_{label}.json").read_text())
            for label in ("14d", "48h")
        },
        "top_picks_now": {
            "generated_at": json.loads((SNAPSHOT / "picks_now.json").read_text())["generated_at"],
            "top25": [
                {key: row.get(key) for key in (
                    "symbol", "class", "direction", "score", "position_size_pct",
                    "intrabar_gate", "db_n", "db_wr", "db_avg_pnl",
                )}
                for row in json.loads((SNAPSHOT / "picks_now.json").read_text())["picks"]
            ],
        },
        "snapshot_hashes": {
            name: hashlib.sha256((SNAPSHOT / name).read_bytes()).hexdigest()
            for name in ("dashboard_data.json", "pf_registry.json", "money_ready_verdict.json",
                         "picks_now.json", "data_pick_summary_stats_14d.json",
                         "data_pick_summary_stats_48h.json", "ai_tournament_picks_latest.json",
                         "data_ai_tournament_leaderboard.json", "dashboard_payload.json")
        },
        "diagnostic_scope_warning": "Published pnl statistics are not a funded equity curve, "
                                    "not independently cost adjusted, and not population complete. "
                                    "Missing registry name match is unknown, not a failed strategy.",
    }
    assert result["active_count"] == sum(Counter(r["asset_class"] for r in active).values())
    assert len(active_output) == len(active)
    assert all(r["barrier_geometry_valid"] for r in active_output)
    assert sum(r["container"]["records"] for r in class_summaries) == len(closed)
    out = HERE / "GHCOPILOT_20261023_1812_LIVE_PICK_EVIDENCE.json"
    out.write_text(json.dumps(clean(result), indent=2, allow_nan=False) + "\n")
    print(json.dumps({
        key: result[key] for key in (
            "active_count", "active_symbols", "smart_picks_count", "active_raw_count",
            "closed_records", "closed_distinct_ids", "closed_exact_fingerprint_duplicates",
        )
    }, indent=2))
    for item in class_summaries:
        recent = item["observed_last_48h"]
        print(item["asset_class"], "last48h", recent["records"], recent["positive"],
              recent["negative"], recent["pf_published_pnl_only"], "latest", item["latest_close"])
    print("ACTIVE STRATEGY MATCHES")
    for row in active_cohorts:
        print(row["asset_class"], row["strategy"], row["source_system"],
              row["records"], row["pf_published_pnl_only"])
    print("CLOSE EXAMPLES")
    for row in examples:
        print(row["asset_class"], row["symbol"], row["closed_at"], row["pnl_pct"],
              row["exit_reason"], row["timestamp"])


if __name__ == "__main__":
    main()
