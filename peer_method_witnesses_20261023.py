"""Read-only arithmetic witnesses; never execute a peer module's top-level code."""
import argparse
import ast
import hashlib
import json
from pathlib import Path

import pandas as pd


def inspect_peer(source):
    tree = ast.parse(source.read_text())
    names = {"month_ends", "forward_outcome", "spy_forward", "run_rule"}
    functions = [node for node in tree.body
                 if isinstance(node, ast.FunctionDef) and node.name in names]
    if {node.name for node in functions} != names:
        raise ValueError("Peer source does not contain the expected functions")
    namespace = {"TIERS": [200.0], "YEARS": [2020, 2021], "CASH_RATE": 0.02}
    exec(compile(ast.Module(body=functions, type_ignores=[]), str(source), "exec"), namespace)
    months = {"2020-12": 100.0}
    months.update({f"2021-{m:02}": 100.0 + m for m in range(1, 13)})
    namespace.update(raw={"TEST": months}, er=lambda ticker: 0.0,
                     spy_me=list(months.items()))
    forward = namespace["forward_outcome"]("TEST", "2020-12", 12)
    benchmark = namespace["spy_forward"]("2020-12", 12)
    if (forward["months"] != 11 or abs(forward["net_return"] - .11) > 1e-10
            or abs(benchmark - .11) > 1e-10):
        raise ValueError("Historical date defect no longer reproduced; reassess the report")
    namespace.update(
        raw={"A": {}, "B": {}, "C": {}},
        trailing_features=lambda *args: {"consistency": 1},
        afford=lambda *args: (True, 9.95),
        er=lambda *args: 0.0,
        forward_outcome=lambda *args: {"net_return": 0.0, "months": 12},
        spy_forward=lambda *args: 0.0,
    )
    ending = namespace["run_rule"]("cheapest3")[200.0]["final_value"]
    if ending != 200.0:
        raise ValueError("Historical fee omission no longer reproduced; reassess the report")
    return {
        "inspected_source_sha256": hashlib.sha256(source.read_bytes()).hexdigest(),
        "requested_months": 12, "actual_monthly_intervals": forward["months"],
        "synthetic_reported_return_pct": round(forward["net_return"] * 100, 8),
        "correct_december_to_december_return_pct": 12,
        "synthetic_start": 200, "entry_fee_per_fund": 9.95,
        "number_of_funds": 3, "reported_end_without_fee_effect": ending,
        "ending_if_three_entry_fees_deducted_and_zero_market_return": 170.15,
        "model_minimum_per_selected_fund": 100,
        "three_minima_total": 300, "equal_dollar_allocation_from_200": 200 / 3,
        "interpretation": "Tests inspected local functions, not all peer results or their exact production source revision",
    }


def benchmark(cache):
    manifest = json.loads((cache / "manifest.json").read_text())
    raw = (cache / "SPY.json").read_bytes()
    digest = hashlib.sha256(raw).hexdigest()
    if digest != manifest["SPY"]["sha256"]:
        raise ValueError("SPY cache hash mismatch")
    data = json.loads(raw)["chart"]["result"][0]
    index = pd.to_datetime(data["timestamp"], unit="s", utc=True).tz_convert(None).normalize()
    prices = pd.Series(data["indicators"]["adjclose"][0]["adjclose"],
                       index=index).dropna().loc["2007-01-01":"2026-10-21"]
    if len(prices) < 1000 or (prices <= 0).any():
        raise ValueError("Insufficient valid full-cycle benchmark data")
    wealth = prices / prices.iloc[0]
    drawdown = 1 - wealth / wealth.cummax()
    trough = drawdown.idxmax()
    peak = wealth.loc[:trough].idxmax()
    return {
        "symbol": "SPY", "currency": "USD", "start": str(prices.index[0].date()),
        "end": str(prices.index[-1].date()), "peak": str(peak.date()),
        "trough": str(trough.date()), "daily_max_drawdown_pct": float(drawdown.max() * 100),
        "source": manifest["SPY"]["source"], "input_sha256": digest,
        "method": "Daily adjusted vendor total-return proxy; descriptive, not a new strategy test",
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--peer-source", type=Path, required=True)
    parser.add_argument("--cache", type=Path, required=True)
    parser.add_argument("--out", type=Path, required=True)
    args = parser.parse_args()
    result = {"peer_witnesses": inspect_peer(args.peer_source),
              "benchmark_reconstruction": benchmark(args.cache)}
    args.out.write_text(json.dumps(result, indent=2, allow_nan=False) + "\n")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
