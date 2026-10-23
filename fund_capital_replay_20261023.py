"""Re-express frozen H-141 selections as hypothetical dollars; no new selector."""
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
from pathlib import Path
import sys

CAPITALS = (200, 500, 1000, 2000, 10000)
EXAMPLE_YEARS = (2008, 2016, 2020, 2022, 2025, 2026)


def dollars(initial, factor):
    if initial <= 0 or factor < 0:
        raise ValueError("Capital must be positive and wealth factor nonnegative")
    return {"initial_usd": initial, "ending_usd": initial * factor,
            "profit_usd": initial * (factor - 1)}


def load_engine(root):
    path = root / "tools/fund_durability.py"
    sys.path.insert(0, str(root))
    spec = importlib.util.spec_from_file_location("h141_frozen_engine", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def replay(root, cache, results_path):
    engine = load_engine(root)
    pd = engine.pd
    prior = json.loads(results_path.read_text())
    protocol_path = root / "reports/symbol_durability_protocol_2026-10-23.json"
    protocol_bytes = protocol_path.read_bytes()
    protocol = json.loads(protocol_bytes)
    if hashlib.sha256(protocol_bytes).hexdigest() != prior["protocol_sha256"]:
        raise ValueError("Frozen protocol hash changed")
    manifest = json.loads((cache / "manifest.json").read_text())
    series = engine.load_series(cache, manifest)
    for symbol, original in prior["manifest"].items():
        if manifest[symbol]["sha256"] != original["sha256"]:
            raise ValueError("Input manifest differs from original study")
    end = pd.Timestamp(protocol["last_complete_day"])
    series = {s: p.loc[p.index <= end] for s, p in series.items()}
    benchmark = series["SPY"]
    universe = protocol["universes"]["us_equity_mutual"]
    frame = pd.concat({s: series[s] for s in universe}, axis=1).reindex(benchmark.index)
    cost = protocol["per_side_cost_bps"] / 10000
    records, summaries = [], []
    perturbation_checks = 0
    for trial in prior["trials"]:
        if trial["universe"] != "us_equity_mutual":
            continue
        selector = trial["selector"]
        schedules = [
            {**s, **{k: pd.Timestamp(s[k]) for k in ("signal", "entry", "exit")}}
            for s in trial["schedule"]
        ]
        full = engine.book_returns(frame, schedules, cost)
        reproduced = engine.metrics(full.loc[full.index >= protocol["reporting_holdout_start"]])
        for metric in ("compound_pct", "cagr_pct", "mdd_pct"):
            if abs(reproduced[metric] - trial["holdout_2016_plus"][metric]) > 1e-8:
                raise ValueError("Prior result reproduction failed: " + metric)
        for schedule in schedules:
            cut = schedule["signal"]
            ranked = engine.rank_at(frame, cut, selector, protocol["minimum_trailing_observations"])
            if [s for s, _ in ranked[:3]] != schedule["selected"]:
                raise ValueError("Original selection differs from past-only ranking")
            altered = frame.copy()
            altered.loc[altered.index > cut] *= 1000
            if engine.rank_at(altered, cut, selector, protocol["minimum_trailing_observations"]) != ranked:
                raise ValueError("Future-price perturbation changed ranking")
            perturbation_checks += 1
            path = engine.basket_path(frame.loc[schedule["entry"]:schedule["exit"]],
                                      schedule["selected"], cost)
            factor = float((1 + path).prod())
            bench_path = engine.basket_path(
                benchmark.loc[schedule["entry"]:schedule["exit"]].to_frame("SPY"), ["SPY"], cost)
            bench_factor = float((1 + bench_path).prod())
            trailing = frame.loc[(frame.index <= cut) &
                                 (frame.index >= cut - pd.DateOffset(years=3))]
            selection_facts = []
            for symbol in schedule["selected"]:
                prices = trailing[symbol]
                daily = prices.pct_change().iloc[1:]
                selection_facts.append({
                    "symbol": symbol, "observations": len(prices),
                    "trailing_total_return_pct": float((prices.iloc[-1] / prices.iloc[0] - 1) * 100),
                    "trailing_sharpe_zero_cash_rate": float(daily.mean() / daily.std() * 252 ** .5),
                    "trailing_volatility_pct": float(daily.std() * 252 ** .5 * 100),
                })
            records.append({
                "selector": selector, "signal_date": str(cut.date()),
                "entry_date": str(schedule["entry"].date()), "exit_date": str(schedule["exit"].date()),
                "partial_final_period": schedule["exit"].year == schedule["entry"].year,
                "selected": schedule["selected"], "selection_facts": selection_facts,
                "net_return_pct": (factor - 1) * 100, "benchmark_net_return_pct": (bench_factor - 1) * 100,
                "daily_mdd_pct": engine.metrics(path)["mdd_pct"],
                "capital_examples": [dollars(c, factor) for c in CAPITALS],
                "benchmark_examples": [dollars(c, bench_factor) for c in CAPITALS],
            })
        fresh = [s for s in schedules if s["entry"] >= pd.Timestamp("2016-01-01")]
        fresh_path = engine.book_returns(frame, fresh, cost)
        wealth = float((1 + fresh_path).prod())
        benchmark_path = engine.basket_path(
            benchmark.loc[fresh_path.index[0]:fresh_path.index[-1]].to_frame("SPY"), ["SPY"], cost)
        bench_wealth = float((1 + benchmark_path).prod())
        annual = [r for r in records if r["selector"] == selector]
        summaries.append({
            "selector": selector, "entry_date": str(fresh_path.index[0].date()),
            "exit_date": str(fresh_path.index[-1].date()), "metrics": engine.metrics(fresh_path),
            "benchmark_metrics": engine.metrics(benchmark_path),
            "capital_examples": [dollars(c, wealth) for c in CAPITALS],
            "benchmark_examples": [dollars(c, bench_wealth) for c in CAPITALS],
            "profitable_holding_periods": sum(r["net_return_pct"] > 0 for r in annual),
            "completed_holding_periods": sum(not r["partial_final_period"] for r in annual),
            "holding_periods_including_partial": len(annual),
            "worst_standalone_holding_return_pct": min(r["net_return_pct"] for r in annual),
        })
    return {
        "study": "H-141 frozen-schedule capital replay, not a new hypothesis or optimization",
        "currency": "USD", "capitals": CAPITALS, "examples_years": EXAMPLE_YEARS,
        "protocol_sha256": prior["protocol_sha256"],
        "original_results_file_sha256": hashlib.sha256(results_path.read_bytes()).hexdigest(),
        "engine_sha256": hashlib.sha256((root / "tools/fund_durability.py").read_bytes()).hexdigest(),
        "input_hashes": {s: manifest[s]["sha256"] for s in universe + ["SPY"]},
        "future_perturbation_checks_passed": perturbation_checks,
        "prior_trial_metric_reproductions_passed": 9,
        "historical_executability": "UNKNOWN: fund minimums, closures, broker access, loads, taxes and currency conversion not verified",
        "survivorship_bias": True,
        "future_eligibility_changed_selected_top_three": False,
        "summaries": summaries, "annual_selections": records,
    }


def render(data):
    names = {"trailing_total_return": "Past return",
             "trailing_sharpe": "Past risk-adjusted return",
             "trailing_low_volatility": "Past low volatility"}
    out = [
        "# Historical mutual-fund capital case study: frozen H-141 replay",
        "",
        "**Agent:** GHCopilot, AI assistant using Copilot SDK in VS Code.",
        "**Date:** October 23, 2026. Research only; not financial advice.",
        "Past performance does not guarantee future results.",
        "",
        "## What this case study answers",
        "",
        "What did three rules specified before the original study select at each",
        "year-end, and what happened to hypothetical $200/$500/$1,000/$2,000/$10,000",
        "**US-dollar** starting accounts? This is not a Canadian-dollar purchase plan.",
        "No new rule, threshold search or fund universe was introduced.",
        "",
        "At each signal date: use only the previous three years (at least 700 daily",
        "observations), select the top three by past return, past Sharpe ratio",
        "(return divided by volatility, zero cash-rate assumption), or lowest",
        "volatility. Buy equal dollar amounts at the next close; hold until the",
        "next annual close/rebalance. No leverage, profit target or stop loss.",
        "Charge 0.10% per side. Net asset value (NAV) already reflects ongoing",
        "fund expenses; we do not subtract them twice. Assume distributions reinvest.",
        "",
        "**ELI5:** Write three recipes before each year's race. Use only the old",
        "scoreboard to choose three runners. Then count both the money won and",
        "the scary falls. Putting in more money changes the dollars, not the",
        "percentage performance under this simplified cost model.",
        "",
        "## Important limits before reading any dollar table",
        "",
        "- These are mathematically funded, equal-dollar portfolios with divisible",
        "  units. Historical initial/subsequent minimums, purchase closures, broker",
        "  eligibility and loads are UNKNOWN. No amount is certified executable.",
        "- $200 means about $66.67 per fund before entry costs; $500 about $166.67;",
        "  $1,000 about $333.33; $2,000 about $666.67; $10,000 about $3,333.33.",
        "  Failure to meet any selected fund's minimum blocks this exact basket.",
        "- Even $10,000 does not guarantee access to closed or restricted funds.",
        "- US mutual funds are not assumed available in ordinary Canadian accounts.",
        "- Historical fees/access cannot be inferred from today's prospectus.",
        "- Taxes, currency conversion, fixed account charges and sales loads omitted.",
        "- The universe consists of funds surviving today. Dead/merged funds are",
        "  missing; share classes can duplicate the same underlying portfolio.",
        "- The original protocol required future data completeness. In this replay,",
        "  all 66 top-three selections match a separate past-only ranking, and",
        "  changing all future prices did not alter any ranking. This checks that",
        "  filtering did not change these selected baskets; it does NOT eliminate",
        "  survivorship, data-revision or historical-availability bias.",
        "- Samples overlap in market regimes; 22 years are not 66 independent",
        "  trials. The 2026 holding period is incomplete and ends October 21.",
        "- Amounts shown are hypothetical liquidation values after modeled costs.",
        "  A profitable year can hide a large temporary loss.",
        "- 'Selected' means top three under that frozen ranking recipe, NOT",
        "  certified trustworthy, low-risk, open to purchases or suitable.",
        "  Exact historical pass/fail under a complete mandate/access screen",
        "  cannot be certified without archived documents and access rules.",
        "",
        "## Fresh investor: January 4, 2016 to October 21, 2026",
        "",
        "This starts a NEW account at the scheduled close, without inheriting",
        "the prior year's overnight return or liquidation. Thus boundary-correct",
        "fresh-account metrics can differ slightly from H-141's original sliced",
        "2016+ continuing-book summary. The full original results were reproduced",
        "before making this presentation change.",
        "",
        "| Rule | Annual compounded growth | Largest daily fall from peak | $200 ends | $500 ends | $1,000 ends | $2,000 ends | $10,000 ends |",
        "|---|---:|---:|---:|---:|---:|---:|---:|",
    ]
    for row in data["summaries"]:
        m = row["metrics"]
        values = " | ".join(f"${v['ending_usd']:,.2f}" for v in row["capital_examples"])
        out.append(f"| {names[row['selector']]} | {m['cagr_pct']:.2f}% | {m['mdd_pct']:.2f}% | {values} |")
    first = data["summaries"][0]
    b = first["benchmark_metrics"]
    values = " | ".join(f"${v['ending_usd']:,.2f}" for v in first["benchmark_examples"])
    out.append(f"| SPY broad-market comparator | {b['cagr_pct']:.2f}% | {b['mdd_pct']:.2f}% | {values} |")
    out += ["", "## Was it steady?", "",
            "Each rule had 17 profitable and 4 losing completed annual holding",
            "periods out of 21 (2005-2025 entries); the incomplete 2026 period",
            "is excluded from that count. Past-return selection lost 37.74%",
            "in the 2008 holding period and 34.85% in the 2022 holding period.",
            "Low-volatility selection still lost 35.14% in 2008, although its",
            "2022 loss was smaller at 13.44%. Those are not steady-gain guarantees.",
            "",
            "## All annual decisions, including losing years", "",
            "Rows are entry-year holding periods, NOT calendar-year returns.",
            "They run from the stated next-close entry to the following annual",
            "execution, or final sample valuation. Each is a fresh standalone",
            "one-period investment; not an annual contribution to the long account.",
            "",
            "| Rule | Signal date | Entry to exit | Selected funds | Net return | SPY same dates | Daily drawdown |",
            "|---|---|---|---|---:|---:|---:|"]
    for row in data["annual_selections"]:
        out.append(f"| {names[row['selector']]} | {row['signal_date']} | {row['entry_date']} to {row['exit_date']} | {', '.join(row['selected'])} | {row['net_return_pct']:+.2f}% | {row['benchmark_net_return_pct']:+.2f}% | {row['daily_mdd_pct']:.2f}% |")
    out += ["", "## Selected crisis/recent years: actual dollars, not forecasts", "",
            "Negative profit means a loss. The complete machine-readable companion",
            "also includes every year's trailing selection metrics and five budgets.",
            "",
            "| Entry year / rule | Initial | Ending | Profit or loss |",
            "|---|---:|---:|---:|"]
    for row in data["annual_selections"]:
        if int(row["entry_date"][:4]) in EXAMPLE_YEARS:
            for c in row["capital_examples"]:
                out.append(f"| {row['entry_date'][:4]} / {names[row['selector']]} | ${c['initial_usd']:,.0f} | ${c['ending_usd']:,.2f} | ${c['profit_usd']:+,.2f} |")
    out += ["", "## What the results do and do not show", "",
            "The frozen rules select different kinds of past winners, but selecting",
            "the top three is NOT passing our stricter trustworthy/steady-gains",
            "screen. H-141's descriptive screen required at least ten years,",
            "annualized Sharpe at least 1, maximum daily drawdown at most 20%,",
            "positive benchmark excess in both halves and sufficient positive",
            "three-year excess windows. No fund passed that full screen.",
            "That last statement grades the completed historical study; it is NOT",
            "a future-informed screen used to decide the earlier annual holdings.",
            "",
            "All nine original fund/ETF/combined selector trials failed to prove",
            "selection skill. The best risk-adjusted random-selection percentile",
            "was 31, below 95. Every paired annual-excess 95% uncertainty interval",
            "had a lower bound below zero. These unchanged results are not",
            "rescued by displaying attractive dollar growth.",
            "",
            "**Our call:** evidence certainty E3 for reproduced historical dollars;",
            "excess-return signal S0 for the frozen selectors; no prospective",
            "signal confirmation. Historical active survivors remain diligence",
            "leads, not a reliable recipe for strong and steady gains.",
            "",
            "## Patterns worth understanding, without pretending they predict",
            "",
            "1. Large gains can come with growth/sector concentration and severe",
            "   falls. Current historical champions are not low-risk secrets.",
            "2. Low past volatility is not a guarantee against a future crash.",
            "3. A fund can beat the market over decades without winning every year.",
            "4. Fees matter most in comparable exposures; a cost advantage is not",
            "   proof of manager skill or a guaranteed positive total return.",
            "5. Minimums and fixed costs matter more for small accounts. For",
            "   illustration ONLY, three $9.95 purchases plus three $9.95 sales",
            "   cost $59.70: 29.85% of $200, 11.94% of $500, 5.97% of $1,000,",
            "   2.985% of $2,000 or 0.597% of $10,000 before price changes.",
            "   This is NOT an asserted mutual-fund tariff or a cost in the tables.",
            "",
            "## How we would evaluate trustworthiness separately",
            "",
            "Match the exact fund/share class, stated mandate, appropriate market/",
            "style benchmark, distribution-adjusted performance, document dates,",
            "fees and actual access. Compare both good and bad periods, changing",
            "managers, closures and dead-fund controls. Then test a frozen selector",
            "on new data. A clearly run fund can be trustworthy without delivering",
            "steady gains; a high CAGR alone cannot establish either property.",
            "",
            "## Verification and reproducibility", "",
            f"- Past-only/future-perturbation checks passed: {data['future_perturbation_checks_passed']}.",
            "- Reproduced nine original metric values across three mutual-fund",
            "  trials (compound growth, annual growth, daily drawdown).",
            f"- Frozen protocol SHA-256: `{data['protocol_sha256']}`.",
            "- SHA-256 means Secure Hash Algorithm, 256-bit; it detects changed inputs.",
            "- Every cached input was checked against the original manifest.",
            "- No new market-data request, parameter search or hypothesis was run.",
            "- Companion code takes the original research root, cache and results",
            "  as arguments; JSON includes input/engine hashes and all 66 decisions.",
            "",
            "Terminology: CAGR = compound annual growth rate; MDD = maximum",
            "drawdown; ETF = exchange-traded fund; ELI5 = explain like I am five;",
            "USD = US dollars; SPY = SPDR S&P 500 ETF Trust; S&P = Standard & Poor's.",
            "Tickers are fund identifiers, not independent funds when share classes",
            "refer to the same portfolio. Full fund universe and protocol:",
            "[H-141 research](https://github.com/eltonaguiar/findtorontoevents_antigravity.ca/blob/research/ghcopilot-symbol-durability/reports/symbol_durability_protocol_2026-10-23.json).",
            "",
            "## Selected fund identities",
            "",
            "| Ticker | Fund name / vehicle |",
            "|---|---|",
            "| DODGX | Dodge & Cox Stock Fund |",
            "| FBGRX | Fidelity Blue Chip Growth Fund |",
            "| FCNTX | Fidelity Contrafund |",
            "| FDGRX | Fidelity Growth Company Fund |",
            "| FLPSX | Fidelity Low-Priced Stock Fund |",
            "| FSCSX | Fidelity Select Software and Information Technology Services Portfolio |",
            "| FSPHX | Fidelity Select Health Care Portfolio |",
            "| FXAIX | Fidelity 500 Index Fund |",
            "| SWPPX | Schwab S&P 500 Index Fund |",
            "| TRBCX | T. Rowe Price Blue Chip Growth Fund |",
            "| VFIAX | Vanguard 500 Index Fund Admiral Shares |",
            "| VFINX | Vanguard 500 Index Fund Investor Shares |",
            "| VIMAX | Vanguard Mid-Cap Index Fund Admiral Shares |",
            "| VPMCX | Vanguard PRIMECAP Fund Investor Shares |",
            "| VSMAX | Vanguard Small-Cap Index Fund Admiral Shares |",
            ""]
    return "\n".join(out)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--study-root", type=Path, required=True)
    parser.add_argument("--cache", type=Path, required=True)
    parser.add_argument("--results", type=Path, required=True)
    parser.add_argument("--output-prefix", type=Path, required=True)
    args = parser.parse_args()
    data = replay(args.study_root, args.cache, args.results)
    args.output_prefix.with_suffix(".json").write_text(json.dumps(data, indent=2, allow_nan=False) + "\n")
    args.output_prefix.with_suffix(".MD").write_text(render(data))
    print("Reproduced", len(data["annual_selections"]), "decisions;",
          data["future_perturbation_checks_passed"], "future-price checks passed")


if __name__ == "__main__":
    main()
