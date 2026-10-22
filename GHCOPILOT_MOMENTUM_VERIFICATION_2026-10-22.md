# GHCOPILOT - independent high_trust_momentum verification

Agent: GHCOPILOT, AI assistant using Copilot SDK in VS Code.
Evidence captured: 2026-10-22, approximately 21:24-21:31 UTC.
Implementation repository: eltonaguiar/findtorontoevents_antigravity.ca.
Candidate reviewed: OpenCode branch `oc-winning-candidate`,
commit `563c99bee5a010770656431e18bc8b224ac3821c`.

## Verdict

**Promising historical CRYPTO candidate, NOT independently proven.**
The raw arithmetic is reproducible. The proof designation exceeds the
evidence: the independent entry-anchored cohort is smaller and its
day-clustered confidence interval crosses zero even before costs.
No production filter, whitelist, position size or money-ready status was
changed by this review.

## Method and provenance

Read candidate code/certificate through git without executing its certificate
writer. Query production `at_raw_picks` and `at_signal_outcomes` using the
canonical credential helper and a read-only transaction.
No credential values or individual private DB records are published here.

Raw selection: source_system `AlphaEngine`, strategy `high_trust_momentum`,
status WON/LOST. No ORDER BY is used for exact certificate reproduction,
matching its original query. Independently calculate arithmetic mean, gross
profit divided by gross loss and 10,000 IID bootstrap means using Python
`random.Random(42).choice`. Sort bootstrap means; take indices 250 and 9750.
Ordering can affect finite Monte Carlo realizations, not the underlying edge.

Replay selection: same strategy, non-null `intrabar_pnl_pct` and status
TP_HIT/SL_HIT/TIME_EXIT, sorted by opened_at,id. These are existing stored
entry-anchored replay results, not newly fetched independent market candles.
Their bar coverage, price source and executable-entry realism still require
audit. This is stronger than checking raw arithmetic alone, not full provenance
certification.

For day-cluster bootstrap, group replay returns by `opened_at.date()`.
Draw 35 whole entry-day groups with replacement per replicate, seed 42,
10,000 replicates; calculate the trade-weighted mean within each replicate.
This accounts for within-entry-day grouping, not multi-day serial dependence
or all cross-symbol/overlapping-position dependence.

## Exact raw-certificate reproduction

| Metric | Independent result |
|---|---:|
| WON/LOST observations | 206 |
| Positive observations | 121 |
| Win rate | 58.7379% |
| Gross PF | 1.805328 |
| Gross mean return | +0.706222 percentage points/trade |
| IID bootstrap 95% interval | [+0.320376, +1.092199] pp/trade |
| Positive bootstrap replicate fraction | 0.9997 |

The replicate fraction is not a posterior probability that the strategy
genuinely works, nor correction for searching many candidate strategies.

There are 212 raw rows: WON 121, LOST 85, EXPIRED 5, OPEN 1.
All are CRYPTO. The 211 closed rows include 69 TP_HIT, 58 SL_HIT and
84 TIME_EXIT outcomes. Consequently the certificate's 206 WON/LOST rows
include **79 timed exits**, not exclusively hard TP/SL hits.
Including the five expired rows gives n=211, mean +0.689294 pp, PF 1.804328.
No duplicate raw (symbol,signal_timestamp) group was found.
No closed row lacked closed_at or exit_price in this scoped query.
Those checks do not prove market-price validity.

## Entry-anchored replay and costs

71 outcome rows: 21 TP_HIT, 17 SL_HIT, 16 TIME_EXIT, 17 without intrabar status.
The last 17 must not be silently assumed valid or zero-return.
The 54 replayed outcomes span June 30-October 20 and 35 distinct entry days.

| Round-trip cost scenario (pp/trade) | Mean net pp/trade | Net PF | Entry-day bootstrap 95% interval |
|---|---:|---:|---|
| 0 | +0.574391 | 1.723176 | [-0.104041, +1.208403] |
| 0.10 | +0.474391 | 1.565841 | [-0.204041, +1.108403] |
| 0.30 | +0.274391 | 1.294617 | [-0.404041, +0.908403] |
| 0.60 | -0.025609 | 0.976362 | [-0.704041, +0.608403] |

Costs here are uniform illustrative scenarios, not measured fees, funding,
spread, leverage or slippage. Do not subtract twice if an eventual source
already includes those costs.

Matching exact symbol, direction and signal_timestamp/opened_at gives 50
paired raw/replay rows. Their gross raw PF is 1.9594 versus replay PF 1.7967;
mean declines from +0.9454 to +0.615542 pp/trade.
Five raw positive outcomes become negative under replay.
The remaining four replay rows were not matched by this exact identity;
their provenance needs reconciliation, not guessed attribution.

Replay gross monthly means:
June n1 +1.0841pp; July n11 -0.2491pp; August n11 +1.0123pp;
September n19 +0.8656pp; October n12 +0.4243pp.
The 27/27 chronological halves at 0.30pp cost have PF 1.3942 and 1.2064.
These splits are retrospective diagnostics, NOT untouched holdouts.

## Remaining proof blockers and concrete next actions

1. Reconcile all raw, replayed and unresolved identities with complete candle
   coverage. Verify first-observed prices against delayed executable entries.
   Raw recording lag has median 0.2164 hours and maximum 8.5108 hours; a signal
   timestamp alone is not evidence a historical entry remained available.
2. Freeze the exact momentum rules/version and all eligibility guards; record
   all attempted variants and account for candidate-selection bias.
3. Reconstruct a cash-/capital-constrained portfolio with overlapping positions,
   concentration, daily drawdown, funding, fees and actual execution costs.
   Summed trade percentages cannot establish CAGR or mutual-fund outperformance.
4. Audit replay independence and missing rows, then use more conservative
   dependence-aware uncertainty and risk-matched benchmark/null comparisons.
5. Start a sealed prospective paper cohort with logged emitted/rejected picks,
   fixed costs/risk policy and no retrospective substitutions. It is not enough
   to quote an arbitrary future trade count without adequate calendar coverage.

No future winning trade, low risk or fund-beating performance is guaranteed.
No new strategy backtest or production deployment occurred in this review.
See [approach](APPROACH.MD) and
[ownership/current implementation plan](GHCOPILOT_PREDICTION_REPAIR_AND_EDGE_PLAN.md).
