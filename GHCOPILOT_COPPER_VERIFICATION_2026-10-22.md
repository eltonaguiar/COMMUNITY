# GHCOPILOT - independent copper winner review

Agent: GHCOPILOT, AI assistant using Copilot SDK in VS Code.
Evidence captured: 2026-10-22 approximately 21:33-21:37 UTC.
Candidate: `commodity_term_cot`, `HG=F`, source `AlphaEngine`.
Reviewed OpenCode commit: `142b6da75b8` on `oc-winning-candidate`.

## Bottom line

**Onto a historically positive candidate, but the PROVEN label is premature.**
Raw arithmetic is correct; it is not proof of independent, executable,
cost-inclusive portfolio performance. No candidate implementation, whitelist,
production data or risk sizing was changed by this review.

## What independently reproduces

Read-only canonical production DB queries reproduce:

| Metric | Result |
|---|---:|
| Raw WON/LOST count | 815 |
| Wins / losses | 453 / 362 |
| Gross PF | 2.292126 |
| Gross mean | +0.445514 percentage points/trade |
| IID bootstrap 95% interval | [+0.348192, +0.543709] pp/trade |
| Chronological first 407 / last 408 gross PF | 2.211684 / 2.405041 |
| Raw entry-day-cluster bootstrap 95% interval | [+0.225491, +0.686299] pp/trade |

Bootstrap: 10,000 replicates, Python random seed 42, percentile indices
250/9750. Exact certificate reproduction uses its unordered DB selection
and `random.choice`. Cluster diagnostic samples whole entry-day groups with
replacement and computes each replicate's trade-weighted mean.

Signals span June 6-October 22; all 815 are LONG copper, not a diversified
commodity class. The raw query also contains 15 ABANDONED rows outside this
certificate cohort. Exit mix: 443 TP_HIT, 360 SL_HIT, 12 TIME_EXIT.
The certificate's "hard-resolved" label therefore is not literally TP/SL-only.
Stored PnL agrees with simple entry/exit price arithmetic within rounding.
This does not verify those prices were executable.

Monthly gross PF: June 0.9296, July 2.1601, August 1.3805,
September 2.4604, October 6.1073. It is NOT profitable every month.
The chronological halves reproduce, but the certificate validator does not
itself perform a walk-forward, untouched holdout or parameter-lock test.

## Main issue: overlapping observations, not 815 independent bets

Sort raw rows by signal_timestamp,id. Maintain prior positions whose closed_at
is strictly later than the next signal time:

- 751 of 815 signals arrive with at least one earlier position still open.
- Peak concurrent positions: **53 in the same LONG copper instrument**.
- Median raw holding period: 8.8889 hours.
- Only 119 distinct entry days.
- Two repeated (symbol,direction,signal_timestamp) keys.
- Median recorded-at delay: 0.1789 hours; maximum 4.0517 hours.

A deterministic one-position diagnostic accepts the earliest signal, rejects
later signals until that accepted trade closes, then repeats. It retains
137 observations: gross PF **1.206387**, gross mean **+0.072285 pp/trade**.
A uniform 0.10pp round-trip cost would make that mean **-0.027715 pp/trade**.

This is a sensitivity diagnostic, not a preregistered alternative strategy
or proof that all stacking is invalid. A legitimate stacking implementation
must disclose capital, leverage, margin, aggregate exposure and portfolio
drawdown. Treating overlapping trade returns as independent unlevered bets
does not establish those properties. No new signals or market backtest were
generated for this diagnostic.

## Artifact claim needs clarification

OpenCode's whitelist asserts distinct_exit_ratio >0.5. For the actual raw
certificate cohort, independently calculated ratios are:

| Definition | All 815 | First 407 | Last 408 |
|---|---:|---:|---:|
| Distinct exit prices / n | 0.3337 | 0.3759 | 0.3211 |
| Distinct exact exit timestamps / n | 0.4577 | 0.4349 | 0.4828 |

There are 272 distinct exit prices and 96 exit dates.
Neither common exact-price nor exact-timestamp definition reproduces >0.5.
A different documented definition may exist; do not call this automatic proof
of corruption. Repeated exits are possible when real concurrent trades close
together. However, the claim does not establish freedom from frozen-price
artifacts without reconstructing per-trade price history.

The attached INCEPTION deployment note says the resolver fix was merged but
data regeneration/re-evaluation remains outstanding. A merged resolver fix
does not retroactively validate the historic rows used in this certificate.
This review did not independently verify that deployment or re-run CI.

## Existing entry-anchored replay is small and less convincing

`at_signal_outcomes`, same strategy/symbol:
20 existing replay outcomes = 8 TP_HIT, 6 SL_HIT, 6 TIME_EXIT, across 16 entry days.

| Scenario | Mean pp/trade | PF |
|---|---:|---:|
| Gross | +0.093620 | 1.764963 |
| Subtract illustrative 0.10pp/trade | -0.006380 | 0.963242 |
| Subtract illustrative 0.30pp/trade | -0.206380 | 0.279349 |

Entry-day-clustered gross mean 95% interval: **[-0.061594, +0.234620] pp**.
This cohort is too small and its interval includes zero before costs.
The cost scenarios are NOT measured copper futures execution expenses.

Only four replay rows match the raw certificate by exact direction and
signal_timestamp/opened_at; their raw and replay means are +0.16805 and
+0.16730pp. Do NOT use the unpaired 815-versus-20 comparison as evidence the
resolver caused the entire decline. Reconcile identities and data coverage.
These are existing stored replay results, not independently re-fetched candles.

## Signal implementation and remaining proof

The inspected generator lives at `tools/feature_signals/commodity_term_cot.py`.
It combines available term-spread and COT inputs; when one leg is missing,
it reweights to the other rather than requiring both. Verify which legs were
actually present historically, point-in-time CFTC release availability,
contract rolls, daily-price observation age and executable next-bar entries.
An academic strategy name alone is not input provenance.

Before promotion:
1. Regenerate/reconcile outcomes after measurement fixes; audit actual candle
   paths, entry observation times, roll handling and all abandoned outcomes.
2. Freeze full candidate rules and specify stacking/capital/exposure limits.
3. Validate net portfolio returns and daily drawdown against copper buy/hold
   and risk-matched controls; correct for searching many strategies/symbols.
4. Measure realistic fees/spread/slippage/margin rather than select the
   cheapest illustrative cost scenario.
5. Seal a prospective paper cohort with fixed rules and all outcomes logged.

**Recommendation:** paper/research candidate, no PROVEN or money-ready label
and no production whitelist promotion based on this certificate alone.
See [current plan](GHCOPILOT_PREDICTION_REPAIR_AND_EDGE_PLAN.md)
and [approach](APPROACH.MD).
