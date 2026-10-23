"""Descriptive fund-risk comparison, not a selection strategy or forecast."""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

import numpy as np
import pandas as pd

SYMBOLS = ("FNILX", "FXAIX", "FCNTX", "IVV", "VUG", "VFV.TO",
           "VBAL.TO", "XEQT.TO", "SHY", "BND")


def price_metrics(prices):
    if (len(prices) < 253 or not isinstance(prices.index, pd.DatetimeIndex)
            or not prices.index.is_monotonic_increasing
            or prices.index.has_duplicates
            or not np.isfinite(prices.to_numpy()).all() or (prices <= 0).any()):
        raise ValueError("Need at least 253 ordered, unique, finite positive daily prices")
    returns = prices.pct_change().iloc[1:]
    wealth = prices / prices.iloc[0]
    years = (prices.index[-1] - prices.index[0]).days / 365.25
    if years <= 0:
        raise ValueError("Price interval must be positive")
    return {
        "start": str(prices.index[0].date()),
        "end": str(prices.index[-1].date()),
        "n_prices": len(prices),
        "cagr_pct": float((wealth.iloc[-1] ** (1 / years) - 1) * 100),
        "total_return_pct": float((wealth.iloc[-1] - 1) * 100),
        "max_drawdown_pct": float((1 - wealth / wealth.cummax()).max() * 100),
        "annualized_volatility_pct": float(returns.std(ddof=1) * np.sqrt(252) * 100),
        "worst_252_session_return_pct": float(prices.pct_change(252).min() * 100),
        "ending_10000_local_currency": float(10000 * wealth.iloc[-1]),
    }


def calendar_return(prices, year):
    prior = prices.loc[prices.index < f"{year}-01-01"]
    current = prices.loc[(prices.index >= f"{year}-01-01")
                         & (prices.index < f"{year + 1}-01-01")]
    if prior.empty or current.empty:
        raise ValueError("Missing calendar-year boundary prices")
    return float((current.iloc[-1] / prior.iloc[-1] - 1) * 100)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--cache", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    manifest = json.loads((args.cache / "manifest.json").read_text())
    series, provenance = {}, {}
    for symbol in SYMBOLS:
        meta = manifest[symbol]
        raw = (args.cache / f"{symbol}.json").read_bytes()
        if meta["status"] != "OK" or hashlib.sha256(raw).hexdigest() != meta["sha256"]:
            raise ValueError(f"Invalid cached source: {symbol}")
        data = json.loads(raw)["chart"]["result"][0]
        dates = pd.to_datetime(data["timestamp"], unit="s", utc=True).tz_convert(None).normalize()
        values = data["indicators"]["adjclose"][0]["adjclose"]
        series[symbol] = pd.Series(values, index=dates, dtype=float).dropna()
        provenance[symbol] = {"source": meta["source"], "sha256": meta["sha256"],
                              "currency": data["meta"]["currency"]}
    # Match endpoints, but preserve each market's sessions for drawdown measurement.
    frame = pd.DataFrame(series).loc["2020-01-02":"2026-10-21"].dropna()
    rows = {}
    for symbol in SYMBOLS:
        rows[symbol] = price_metrics(series[symbol].loc[frame.index[0]:frame.index[-1]])
        rows[symbol]["calendar_2022_return_pct"] = calendar_return(series[symbol], 2022)
        rows[symbol]["currency"] = provenance[symbol]["currency"]
    output = {
        "purpose": "Descriptive fixed-vehicle comparison; not predictive selection or RRSP execution",
        "method": "Vendor adjusted close, reinvested-distribution proxy, embedded expenses; no second expense deduction",
        "calendar_method": "Matched endpoints with each instrument's own observed sessions; no forward-fill",
        "limitations": ["Single-vendor revisions and survivor selection",
                        "CAD and USD returns are not directly ranked",
                        "Not broker NAV, verified fills or investor-tax-adjusted returns",
                        "No commissions, spread or currency conversion deducted",
                        "Historical adjusted prices are not historical dealing prices",
                        "No VOO or VGG cached history; IVV is not relabeled VOO"],
        "provenance": provenance, "results": rows,
    }
    args.output.write_text(json.dumps(output, indent=2, allow_nan=False) + "\n")
    for symbol, row in rows.items():
        print(f"{symbol:8} {row['currency']} CAGR {row['cagr_pct']:6.2f}%"
              f" MDD {row['max_drawdown_pct']:6.2f}%"
              f" 2022 {row['calendar_2022_return_pct']:7.2f}%"
              f" worst252 {row['worst_252_session_return_pct']:7.2f}%")


if __name__ == "__main__":
    main()
