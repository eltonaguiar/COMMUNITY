# GHCOPILOT review of Kilocode's two claimed clean winners

Agent: GHCOPILOT, AI assistant using Copilot SDK in VS Code.
Audit date: 2026-10-22. Scope: supplied screenshots, exact live MySQL cohorts.

## Verdict

**Both headline calculations reproduce. Neither qualifies as a verified clean
winner.** Absence of one frozen-exit timestamp pattern does not establish
timestamp provenance, execution realism, independent exposure or valid returns.

The findings below are stronger than simply requesting more future trades.
The mega_mutation cohort has no stored creation timestamps. The forex cohort
contains repeated winning price pairs during closed-market weekends.

## 1. mega_mutation four-symbol subset

Exact legacy selection: trading_picks, source_system mega_mutation, symbols
JUPUSDT/ENAUSDT/ADAUSDT/WIFUSDT, closed_at non-null, pnl_pct non-null,
status not OPEN/ABANDONED/FLAT.

- n171, wins138, WR80.7018%, PF7.66466, mean+4.60263pp/trade: **reproduced**.
- Uniform illustrative0.30pp round-trip cost leaves PF6.74836,
  mean+4.30263pp; this candidate is not explained away by small fees alone.
- Close dates April2-June11; no current October performance is established.
- **All171 created_at fields are NULL.**
- All171 lack intrabar_status/intrabar_pnl_pct validation (previous exact-ledger
  query; full340-row source cohort also lacks it).
- Only64 distinct entry prices across171 records.
- 136 distinct exact close timestamps; maximum four rows share one timestamp.
- 106 distinct exit prices.

An exact close-timestamp detector may therefore miss bulk/frozen-input
problems. "Zero frozen-exit clusters" cannot recover the missing entry clock.
Without an independently recoverable original observation timestamp, we cannot
determine whether the entry existed before the move, reconstruct overlapping
capital, or test causal first-touch outcomes.

Do not substitute closed_at as created_at, invent dates, or interpret a unique
close timestamp as a verified forward observation. Recover original source
artifacts/commit-time snapshots and stable trade identities, then price paths.

The four symbols were selected because their historical results were best:
this is selection on the outcome. The later June6-11 subset has22 wins/22,
which is interesting follow-up but already known now, too short and still
without entry timestamps. It is not a new untouched prospective test.

**Status: historically attractive, provenance-blocked research lead.**
Neither fake nor genuine trading alpha can be established from these rows alone.

## 2. regime_terminal FOREX

Exact n100 is recovered with trading_picks source_system regime_terminal,
category FOREX (case-insensitive DB collation), closed_at and pnl_pct present,
status not OPEN/ABANDONED/FLAT.

- n100, wins64, WR64%, PF2.74522, mean+0.259731pp: **reproduced**.
- Includes five different strategies: accumulation40, mild_bear21,
  mild_bull12, strong_bear9, strong_bull18. This is a source ensemble,
  NOT one proven algorithm.
- One row is **NIO**, a stock, classified FOREX. There are also forex-style
  ticker rows classified EQUITY/CRYPTO elsewhere; exact class-only and
  symbol-based cohorts are not interchangeable.
- Created April6-September27; last close October2.
- All100 intrabar fields lack independent replay validation.
- Only40 distinct entry prices.

### Concrete evidence against "zero contamination"

Nine USDJPY SHORT rows, created **September26 06:53:48 through September27
08:54 UTC**, share exactly:

- entry158.81100000
- exit157.18499756
- return approximately+1.0200%.

Those times are Saturday through Sunday morning, during the ordinary OTC FX
weekend closure, before the normal Sunday reopening.
Two example Sunday rows resolve within roughly ten minutes to that same exit.
Different exact exit timestamps do NOT establish a new price event.

Another repeated NZDUSD SHORT entry0.5868/exit0.58951837 appears five times
on Sunday August9 05:03-16:44 UTC. Overall24 of100 entries fall on Saturday/
Sunday UTC; not every Sunday timestamp is automatically invalid, but the
specific Saturday/Sunday-morning cluster requires a venue/timestamp/source
explanation before trusting those profits.

This is evidence of stale-price reuse, delayed ingestion/backfill or invalid
execution timing, not a certified independent win. We have not established
deliberate fabrication; recover original venue/source timestamps.

### Robustness checks

At illustrative0.10pp/trade round-trip cost:

- Net PF1.85124, mean+0.159731pp, net wins59%.
- One-sided net binomial p=.04431 before correcting for selection/search.
- Weekly-cluster mean95% CI **[-0.13031,+0.34454]pp**, crosses zero.
- Removing September: n60, net PF0.74870, mean-0.057045pp.
- September alone: n40, net PF4.77013; June positive, April/May/July/August
  negative under the scenario. Not steady month-by-month profitability.

One-slot diagnostic (created_at,id order, next trade only after accepted close):
n62, net PF1.72292, mean+0.16256pp; peak unrestricted overlap18 positions.
This is more resilient than copper on that single exposure diagnostic, so it
deserves reconstruction, not automatic dismissal. But it does not cure the
weekend price/timestamp contamination or cohort selection.

Do not use50% as universal economic break-even with asymmetric stops/targets.
No multiple-trial-adjusted claim, sealed holdout, measured cost, portfolio
daily drawdown or fund-beating proof was established.

**Status: potentially interesting source ensemble, contaminated execution
timestamps/price independence; NOT verified clean.**

## 3. What Kilocode got right and what to change

- Arithmetic and the commodity batch-artifact concern are credible leads.
- Looking across more than one ledger is necessary, but cohorts must retain
  source/class/time identity rather than silently pooling incompatible rows.
- Do not call data "extremely clean" based on one exact-timestamp detector.
  Add missing entry-time, repeated entry/exit-pair, closed-market session,
  original-observation, first-touch, stale-price and cross-class checks.
- Do not paper-trade the historical winners as if they were already proven.
  Freeze executable rules, choose a prospective start, use fresh independent
  prices, record rejects and costs, constrain exposure and compare controls.
- Recover original source files for mega_mutation; quarantine missing-time rows.
  Investigate/reconstruct the nine USDJPY weekend wins before promoting FOREX.

## Reproduction and documentation

All DB access read-only through tools.db_env.get_stocks_creds; no secret values,
raw IDs or payloads published. Queries use exact source, symbol/category,
closed_at and status conditions above. Statistics are in percentage points,
not portfolio returns.

Weekly bootstrap: group created_at dates by ordinal//7, sample whole groups
with replacement, seed42,5000 replicates, trade-weighted mean, sorted
indices125/4875. This does not eliminate all temporal dependence.

No strategy edits, demotions, live orders or risk increases.
See [adversarial audit](GHCOPILOT_ADVERSARIAL_AUDIT_2026-10-22.md)
and [current plan](GHCOPILOT_PREDICTION_REPAIR_AND_EDGE_PLAN.md).
