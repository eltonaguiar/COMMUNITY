"""Describe signal-to-bookkeeping-close lag; do not infer true fills or capped returns."""
from collections import Counter, defaultdict
from datetime import timedelta
import hashlib
import json
from pathlib import Path

from evaluate_live_snapshot_20261023 import clean, stats, timestamp

HERE = Path(__file__).resolve().parent
BUCKETS = ("<=48h", "2-7d", "7-30d", ">30d")


def bucket(hours):
    if hours < 0:
        raise ValueError("Closure precedes signal; cannot assign a holding-time bucket")
    return BUCKETS[0 if hours <= 48 else 1 if hours <= 168 else 2 if hours <= 720 else 3]


def summarize(rows, est_as_daylight=False, excluded_batch=None):
    groups = {label: [] for label in BUCKETS}
    for row in rows:
        if excluded_batch is not None and row["closed_at"] == excluded_batch:
            continue
        end = timestamp(row["closed_at"])
        start = timestamp(row["timestamp"])
        if est_as_daylight:
            # Sensitivity only: some providers incorrectly label daylight time "EST".
            if row["closed_at"].endswith(" EST"):
                end -= timedelta(hours=1)
            if row["timestamp"].endswith(" EST"):
                start -= timedelta(hours=1)
        groups[bucket((end - start).total_seconds() / 3600)].append(row)
    return {name: {
        **stats(group), "timeframe_counts": dict(Counter(r.get("trade_timeframe") for r in group)),
        "direction_counts": dict(Counter(r["direction"] for r in group)),
        "top_strategy_counts": Counter(r["strategy"] for r in group).most_common(5),
    } for name, group in groups.items()}


def main():
    snapshot = HERE / "peer-round-1856"
    raw = (snapshot / "dashboard_data.json").read_bytes()
    data = json.loads(raw)
    rows = data["picks"]["recent_closed"]
    cohorts = defaultdict(list)
    for row in rows:
        cohorts[(row["asset_class"], row["source_system"], row["strategy"])].append(row)
    largest_batch, largest_count = Counter(r["closed_at"] for r in rows).most_common(1)[0]
    overall = summarize(rows)
    assert sum(v["records"] for v in overall.values()) == len(rows)
    by_strategy = []
    for (asset, source, strategy), records in sorted(cohorts.items()):
        by_strategy.append({
            "asset_class": asset, "source_system": source, "strategy": strategy,
            "all_records": stats(records), "lag_buckets": summarize(records),
        })
    result = {
        "source_sha256": hashlib.sha256(raw).hexdigest(),
        "dashboard_generated_at": data["generated_at"],
        "observations": json.loads((snapshot / "observations.json").read_text()),
        "definition": "closed_at minus timestamp; elapsed signal-to-bookkeeping-close lag, "
                      "not verified economic holding duration or first-touch exit time",
        "base_timestamp_convention": "Explicit EST = fixed UTC-05; naive = assumed UTC for diagnostics",
        "rows": len(rows), "lag_buckets": overall,
        "strategy_source_cohorts": by_strategy,
        "by_direction": {direction: summarize([r for r in rows if r["direction"] == direction])
                         for direction in sorted({r["direction"] for r in rows})},
        "exclude_largest_batch_sensitivity": {
            "batch_timestamp": largest_batch, "excluded_records": largest_count,
            "remaining_lag_buckets": summarize(rows, excluded_batch=largest_batch),
            "interpretation": "Diagnostic only; deleting the batch is not a corrected performance result.",
        },
        "EST_as_daylight_sensitivity": summarize(rows, est_as_daylight=True),
        "required_horizon_replay": {
            "status": "NOT_COMPUTABLE_FROM_THIS_SNAPSHOT",
            "missing": [
                "Frozen per-strategy issue-time expiry rules and applicable market calendar",
                "Tradable instrument/contract mapping, actual entry fills and price paths at expiry",
                "First-barrier-touch times, gap/fill conventions and all entry/exit/funding costs",
                "Complete active/closed population beyond the bounded export",
            ],
            "warning": "Removing late outcomes or capping elapsed time without horizon prices "
                       "does not compute horizon-capped returns.",
        },
        "causal_claim": "NOT_ESTABLISHED: duration association alone cannot identify beta, "
                        "waiting-to-target bias or skill; strategy/source/side composition differs.",
    }
    output = HERE / "GHCOPILOT_20261023_1856_PEER_LAG_EVIDENCE.json"
    output.write_text(json.dumps(clean(result), indent=2, allow_nan=False) + "\n")
    for name, value in overall.items():
        print(name, value["records"], value["pf_published_pnl_only"],
              value["direction_counts"], value["top_strategy_counts"][:2])
    print("LARGEST BATCH EXCLUDED (diagnostic, not corrected performance)")
    for name, value in result["exclude_largest_batch_sensitivity"]["remaining_lag_buckets"].items():
        print(name, value["records"], value["pf_published_pnl_only"])
    print("EST SENSITIVITY")
    for name, value in result["EST_as_daylight_sensitivity"].items():
        print(name, value["records"], value["pf_published_pnl_only"])
    print("COHORTS WITH BOTH SHORT AND LONG LAG")
    for row in by_strategy:
        short, long = row["lag_buckets"]["<=48h"], row["lag_buckets"][">30d"]
        if short["records"] >= 10 and long["records"] >= 10:
            print(row["strategy"], row["source_system"],
                  short["records"], short["pf_published_pnl_only"],
                  long["records"], long["pf_published_pnl_only"])


if __name__ == "__main__":
    main()
