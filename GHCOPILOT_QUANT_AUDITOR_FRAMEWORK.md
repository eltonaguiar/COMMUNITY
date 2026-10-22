# Quant-auditor framework: falsifiable edge, by asset class

Author: **GHCOPILOT - AI assistant using Copilot SDK in VS Code**.
Version: **proposal v1, 2026-10-22**. Goal #1, defensible `/audit` performance.
This is a proposed common certification standard, **not implemented enforcement**.
The current GHCOPILOT paper monitor implements only a disclosed preliminary
subset; its `PAPER_EVIDENCE_PASS` is not certification under this framework.

## 1. What a certificate can and cannot mean

No test proves a future pick will win, makes investment risk equivalent to a
fair coin toss, or guarantees that a past edge will persist. Our target is:

> Under a frozen, reproducible and executable protocol, a specified portfolio
> has credible net economic value beyond predefined tradable alternatives,
> after accounting for data error, dependence, selection and risk.

The unit of proof is **one versioned economic hypothesis and portfolio policy**,
not a strategy name, provider, asset-class aggregate or a single successful pick.
An edge can have WR below50%; a high WR can lose money.

Verdicts:

| Tier | Required evidence | Allowed public language |
|---|---|---|
| U0 | Missing identity, dates, prices, lineage or essential method inputs | Unverifiable; explain missing evidence |
| I0 | Reproduced outcome/provenance error | Invalid evidence for this cohort; do not infer every source is invalid |
| H1 | Reproducible net historical result; selection history disclosed | Historical candidate |
| O2 | Preregistered purged walk-forward result with validated portfolio/market data | Historical out-of-sample support, limitations stated |
| F3 | Sealed prospective experiment, valid collection, adequate power, confirmatory economic tests and risk gates passed | Confirmed prospective edge under protocol/version/window |
| M4 | Independent reproduction, implementation/capacity/execution audit and operational controls in addition to F3 | Consider staged deployment; not guaranteed profits |

No raw aggregate result in the current independent review establishes F3/M4.
Different instruments/classes require separate scope statements. One BTC
strategy does not prove the entire CRYPTO class.

## 2. Mandatory evidence contract

One append-only manifest per hypothesis must contain:

```
hypothesis_id, economic_mechanism, owner, version, code_commit
source_system, source_pick_id, source_trade_id, parent_signal_id
strategy_name, raw_class, canonical_class, instrument_type, venue, currency
symbol, contract_or_share_class, side, unit_conventions
source_signal_at, first_observed_at, decision_at, eligible_entry_at
actual_or_simulated_fill_at, fill_price, quote_side, quantity, notional
tp, sl, horizon, session_calendar_version, contract_specification
resolver_version, market_data_provider, retrieval_at, bar_timestamp_semantics
exit_at, exit_price, exit_reason, gross_pnl, itemized_costs, net_pnl
max_concurrent_exposure, capital_policy, sizing_policy, rejection_reason
data_status, stale_flags, all_trial_family_ids, holdout_boundary
primary_endpoint, benchmark_spec, null_spec, test_plan, planned_readout
raw_snapshot_hashes, derived_snapshot_hashes, prior_version_link
```

Private raw IDs/payloads may stay private; public salted/hashed IDs must allow
stable count/cohort reconciliation without publishing credentials or trader PII.
Hashes establish consistency with a saved observation, not exchange truth.
Trusted observation logs and independent source evidence remain necessary.

Time invariants:

- Source signal time need not equal observation time. A delayed copied trade
  may only enter **after we observed it**, not at the trader's earlier price.
- Decision uses only information available then, including economic-data
  publication lag, revised fundamentals, COT release time and universe changes.
- Completed bars only. Document whether timestamps label bar open or close.
  Prevent use of high/low that occurred before an intrabar entry.
- Clocks use UTC internally, explicit exchange-calendar conversion externally.
  `signal_at <= observed_at <= decision_at <= fill_at` is checked subject only
  to a documented measured clock tolerance; violations are quarantined.
- Missing dates or inferred historical creation times cannot be relabelled
  as verified forward observations.

## 3. Gate D: data and pipeline truth, before performance

Trace every class through:

**definition -> registration -> workflow invocation -> input availability ->
emitted signal -> gate decision -> persisted observation -> admitted order ->
entry -> independent exit -> portfolio -> dashboard**.

For every stage expose count, newest event time, observation time, latency,
version and explicit rejection/failure reason. A defined scanner is not a
working emitter; a fresh JSON generation time is not a fresh signal.

### Data checks

1. Reconcile raw/outcome/portfolio/display rows by immutable identity. Keep
   raw and canonical class, derive classification from instrument metadata,
   and flag disagreements (e.g. copper FUTURES versus COMMODITY; NIO in FOREX).
2. Distinguish true zero PnL, rounding-to-zero, pending, missing and corrupted.
   Never `COALESCE` unknown PnL into zero or discard all flat outcomes.
3. Check duplicates, replayed source IDs, parent clones, stale active rows,
   reused price pairs, stale quotes, sentinel prices and impossible dates.
   Artifact ratios trigger investigation, not automatic conviction.
4. Validate price scale, direction, percentage points versus fractions, FX
   quotation, contract multiplier, distributions, cash flows and currency.
5. Resolve using independent executable market data, not a second table
   calculated from the same shared snapshot. Preserve provider provenance.
6. TP/SL first touch, unfavorable ambiguity, adverse gaps, limit-fill rules,
   expiry at the correct completed bar and session-calendar validity are tested.
   Missing historical data stays unresolved; no current-price substitution.
7. Include TIME_EXIT and all registered lifecycle outcomes. "Hard-only" TP/SL
   can create selection bias if timeouts are excluded after results are known.
8. Rebuild contaminated history as a versioned sidecar, never silently
   overwrite the evidence used to select candidates.

### Measurable operational acceptance

- **100% of admitted confirmatory trades** have required provenance, valid
  chronology and valid entry/exit evidence. Any exception prevents certification
  of the affected cohort until reconciled, not necessarily the whole DB.
- Publish the full eligible denominator, rejected reasons and unresolved
  fraction. At readout resolve/reconcile100% of economically due observations
  or compute defensible bounds including missing outcomes. A small unknown
  subset is not assumed random.
- Suggested investigation alerts: no input after2 expected collection
  intervals; gate count moves more than50% versus a comparable rolling baseline;
  any sentinel/clock/class-unit violation; clustered identical exits not
  explained by documented contracts/market paths. These are proposed alerts,
  not claims that those checks are already deployed.

**No statistical test can rescue a failed data gate.**

## 4. Gate E: reconstruct the economic portfolio

### Grok critic baseline: ten mandatory outputs

Adopted from the user's October22 checklist, with the technical qualifications
below. Calculate these on dated **out-of-sample daily net equity**, with actual
or explicitly simulated position sizing. Trade-level fields additionally
require the corresponding cash-PnL ledger. Missing inputs mean **NOT EVALUABLE**.

| Output | Required calculation / decision |
|---|---|
| Trades and days | Publish trades, distinct entry days, exit days, active days and total observation days. N100 is a research floor, not a mathematical skill threshold; use cluster structure and prospective power. |
| Net expectancy / payoffs | Net percentage return per trade with explicit notional denominator, cash-weighted economic PnL, average win and average loss; repeat at2x realistic total costs. |
| PF and uncertainty | State whether PF uses net cash PnL or normalized trade returns. Resample whole synchronized days; include longer blocks for serial dependence. Report CI and no-loss/undefined bootstrap draws, not capped999. |
| Sharpe / Sortino | Daily net returns, fixed cash/risk-free return and minimum acceptable return. Declare252 versus365-day convention and dependence treatment. Baseline aims: Sharpe>=1, Sortino>=1.5; not proof by themselves. |
| Drawdown / recovery | Daily marked-to-market peak-to-trough decline, start/trough/recovery dates and maximum time underwater. Unrecovered drawdown remains unrecovered, not zero recovery time. Baseline MDD<=20%. |
| Calmar | Defined annualized return divided by absolute MDD over the same stated period. Baseline>=0.5; short history and zero MDD cannot produce an honest infinite-quality certificate. |
| Tails | Worst complete calendar month, disclosed partial months and daily CVaR/expected shortfall of the worst5% loss tail; specify quantile convention and effective tail sample. |
| Alpha / beta | Matched-date excess returns against a tradable benchmark: SPY total return for the relevant equity mandate, BTC for crypto; class-specific duration/carry/currency factors where needed. Dependence-robust uncertainty; beta-adjusted alpha is not causal proof. |
| Passive comparison | Same dates/capital/cash conventions: strategy versus buy-and-hold net total return and daily Sharpe, plus a risk/exposure-matched comparator. Raw return inferiority alone does not disprove defensive/diversifying value. |
| Exposure | Fraction of eligible market time invested, average/maximum gross and net notional, leverage, cash and turnover. Include partial-day holdings; close-only exposure can miss intraday risk. |

These are minimum report fields, not a waiver of data, OOS, selection or
prospective gates. The stronger institutional mandate below remains separate.
An additive strategy may be useful without beating passive raw return only
if its stated risk-matched or portfolio-contribution objective is preregistered
and passes net-of-cost inference. Do not change the objective after failure.

### Institutional-target clarification

The user's proposed Sharpe>2 and Calmar>2 are useful **aspirational mandate
targets**, not universal evidence thresholds or guarantees. They must be
computed from a net, ordered, marked-to-market portfolio with enough history
and confidence bounds. Sortino also requires a fixed minimum acceptable
return; Calmar requires a stated return/drawdown window. An annualized Sharpe
from a short or stale sample is not institutional evidence.

Use a preregistered confirmatory alpha0.01 when the mandate requires it,
controlled across the declared family; do not reinterpret every Monte Carlo
percentile as a p-value. "Positive DSR" is too weak/ambiguous: DSR is usually
reported as a probability-style statistic, with a declared confidence target,
trial-count/dependence assumptions and the underlying Sharpe benchmark.
No DSR, small p-value or large Sharpe proves an algorithm mathematically
distinct from every possible random process, or guarantees future profit.

CVaR/expected shortfall is tail-loss estimation, not market-impact analysis.
Specify confidence level, horizon, cash/margin book and stress scenarios.
Capacity needs participation limits, spread/depth, nonlinear impact,
turnover, execution delay and borrow/funding constraints. $1B capacity is an
instrument/venue/mandate question, not a claim that can be inferred from
retail OHLC bars. If those inputs are absent, capacity is NOT EVALUABLE.

Use a daily mark-to-market cash-and-position book, not a sum of trade
percentages. Track open and closed positions, cash, dividends/coupons, funding,
borrow, fees, margin, currency conversion and exposure.

- Freeze entry delay, order type, price side, size, rebalance/slot policy,
  per-instrument limits, stop/TP policy and capital before testing.
- Repeated/stacked signals may be legitimate, but need a real notional/margin
  policy. Also publish a one-slot sensitivity without calling it the original
  strategy or using its result selectively.
- Report total return, CAGR where meaningful, volatility, Sharpe/Sortino with
  autocorrelation caveats, net PF, expectancy, exposure, turnover, MDD/time under
  water, worst day/week, expected shortfall and liquidity/capacity.
- No annualized CAGR from a few days and no daily Sharpe from unordered trade
  returns. PF is undefined/infinite with no losses; report this and the sample,
  never a fabricated capped PF as a certified metric.
- Use measured venue/instrument execution costs where available. Publish
  fixed-cost scenarios as scenarios; include1x/2x measured total-cost stress,
  plausible delayed fills and adverse slippage.
- Include benchmark distributions, financing, currency and comparable exposure.
  Net strategy and benchmark must have the same investable dates/constraints.
- Compute attribution to market beta, duration, carry, volatility/liquidity
  premia and short exposure. A profitable long book during a bull market may
  be implementable beta, not timing skill.

## 5. Gate N: choose honest null hypotheses

Predeclare the primary economic endpoint: daily paired **net excess return**
against a specific investable risk-matched benchmark. Also test standalone
net profitability when that is part of the advertised claim.

Use at least these complementary diagnostics:

| Null | Question | Correct implementation |
|---|---|---|
| Random direction | Is directional choice useful? | Same observed opportunities, actual forward market path, brackets, capital, costs and exits; independently simulate both directions |
| Random timing | Does entry timing help? | Same asset/session/regime/holding distribution and executable horizon, without future-conditioned sampling |
| Passive/exposure match | Is it just market risk? | Tradable benchmark with matched dates/cash/duration/beta and real costs |
| Simple prespecified baseline | Does complexity add value? | Fixed simple rule, same data/capital and no retuning on test |
| Signal permutation/block shuffle | Does signal information matter? | Preserve session/serial structure and exposure constraints; do not shuffle individual dependent rows |

For fixed positive win size `W`, positive loss magnitude `L` and fixed
round-trip cost `c` in the same units:

`E[net] = p*W - (1-p)*L - c`, so `p_break_even = (L+c)/(W+L)`.

That formula is not a substitute for path simulation with varying R:R, time
exits, gaps and costs. A50% binomial test is appropriate only for its explicit
Bernoulli question under the necessary independence/null assumptions. It is
neither necessary nor sufficient for economic edge, and serial clustered wins
invalidate a naive IID p-value. A bootstrap positive-resample fraction is not
the probability that an economic hypothesis is true.

Coin-flip controls are subject to market drift, path asymmetry and costs too.
Do not compare strategy to sign-flipped stored outcomes or declare exactly50%
the executable null win rate without demonstrating it.

## 6. Gate S: dependence, uncertainty and selection

### Uncertainty

- Primary inference uses aligned daily **paired strategy-minus-benchmark
  net returns**, including truthful cash days. Do not zero-fill unresolved
  marks or absent data as if they were flat returns.
- Choose time blocks from holding horizon/autocorrelation before reading the
  confirmatory result. Publish day/week and stationary/moving-block sensitivity.
  Shared entry day, symbol, trader and overlapping holdings can create multiple
  dependence dimensions; use synchronized time blocks and appropriate clustered
  inference, not trade-count inflation.
- At least10,000 seeded resamples for final reporting; publish method, block
  lengths, CI type, null centering and Monte Carlo resolution. A few thousand
  resamples in exploration are not a final low-tail-accuracy certificate.
- Separate a confidence interval on an effect from a valid null-test p-value.
  For randomization tests include the observed statistic in finite-simulation
  p-value estimation; a displayed probability1.0000 is not certainty.
- Report results leaving out each month, symbol/source and major regime;
  top-tail removal and winsorization are sensitivities, not silent alteration
  of the primary endpoint. Single-symbol hypotheses remain valid in that scope;
  they cannot claim diversified class-wide generalization.

### Selection

- One immutable registry lists **every** attempted variant/filter/symbol subset,
  including failures and abandoned tests. The227 current GHCOPILOT screen groups
  are not the complete historical research family.
- Exploration: BH/FDR may prioritize further research if its assumptions are
  appropriate; dependence can require a more conservative method. Do not
  confuse exploratory FDR control with confirmatory familywise certification.
- Confirmation: freeze the tested family before first prospective observation.
  Use valid component tests and Holm familywise alpha0.01 across all advertised
  hypotheses/classes (or a documented alternative control). Co-primary claims
  must all pass; do not shop among endpoints/nulls.
- Predefine a minimum economically meaningful effect, expected variance,
  autocorrelation and80% or90% target power; determine the required independent
  history before starting. N100 is a floor, not a proof or adequate-power rule.
- One primary readout on a fixed endpoint/date; recurring dashboards are
  descriptive. Early promotion requires a preregistered sequential procedure,
  not rerunning p<.01 every hour. Early risk stops remain active and disclosed.
- Any post-selection filter/cost/holding/sizing change creates a new hypothesis
  and a new prospective cohort. Failed cohorts remain visible.

### Advanced tests: use only when inputs justify them

| Method | Required inputs and scope | Reject these shortcuts |
|---|---|---|
| DSR | Ordered return series, moments, sampling convention, effective trial count and trial dependence estimate | Setting number of trials to1 because one finalist remains |
| PBO/CSCV | Aligned strategy-return matrix for the complete searched family, defensible block design | One winner certificate; treating CSCV as future unseen validation |
| White Reality Check / Hansen SPA | Aligned differential return/loss matrix against an explicit benchmark; dependence-aware bootstrap | Comparing independent disjoint windows or fabricated trial family |
| Purged walk-forward | Decision labels/horizons, predeclared folds, training-only tuning and embargo | Ordinary50/50 split repeatedly inspected during selection |
| Factor/regime tests | Matched-time factor data, prespecified exposures/interactions, enough independent periods | Inventing a regime after a strategy fails |

Unknown trial history or missing matrices => **NOT EVALUABLE** for the
corresponding test. DSR/SPA/PBO are not ceremonial labels required to be faked
when their inputs are unavailable; an independently preregistered prospective
confirmation can establish new evidence without retroactively validating old
mined history.

## 7. Gate O: historical generalization and sealed forward confirmation

Historical development:

1. Split chronology before looking at outcomes; fit features/scales/universe
   using training information only.
2. Purge labels/positions crossing folds; embargo at least the maximum relevant
   label horizon and data-release lag, enlarged if the information structure
   requires it. Document the actual rule; no arbitrary magic interval.
3. Nested training-only selection, multiple walk-forward eras; untouched final
   holdout owned separately. Once read, it becomes development history.
4. Include delisted symbols, discontinued traders/funds and universe revisions.
   A survivor-only leaderboard fails the advertised universe claim.

Prospective confirmation:

- Seal hypothesis, artifacts, source revision, candidates, cost policy,
  calendar, benchmark, controls and intended readout before observation.
- Independent collector timestamps every observed eligible signal and
  rejection. Append-only logs and state hashes survive job restarts.
- Suggested **minimum floors**, subject to the larger power requirement:
  n>=100 clean executed outcomes, >=60 distinct entry-day clusters and >=180
  calendar days with relevant regime coverage. For slow ETF/BOND sleeves,
  insufficient independent rebalances means wait; do not duplicate observations
  to meet n. Long-horizon allocation is evaluated by daily portfolio evidence
  and power, not a mechanically inappropriate100-rebalance requirement.
- At fixed readout: provenance/missingness reconciled, adequate power,
  multiplicity-controlled lower confidence bound above zero for net excess
  and standalone profitability claims, PF>=1.5 where trade PF is meaningful,
  positive preregistered temporal robustness and the declared risk limits.
- Project Tier2 risk policy additionally requires MDD<20% on total daily
  equity, unlevered/explicitly levered capital, no hidden risk-stop breaches.
  WR>50% may remain a project-label requirement but is not proof of alpha.
- Suggested staged-research stop: drawdown10% of fixed test capital or any
  execution/data-integrity breach pauses admissions, retains all existing
  records and triggers review. Risk budget is strategy-specific and must be
  approved/frozen before new experiments, not imposed retroactively.
- Passing does not authorize real-money orders. Operational approval,
  position limits and a staged execution-cost audit remain separate.

**Existing monitor limitation:** its frozen90-day/30-entry-day/BH-WR screen and
hourly fixed-cost simulation are exploratory. Do not change its locked protocol
silently to match this proposal or promote its result as F3.

## 8. Per-asset-class audit requirements

| Class | Data/execution checks | Economic benchmark/null | Principal current blockers |
|---|---|---|---|
| CRYPTO | Venue/pair identity,24/7 timestamps, spot versus perpetual, fees/spread/funding, USDT/USD basis, liquidation/borrow, delisted tokens; independent OHLC from venue with provider disagreement checks | Matched BTC/ETH beta/cash, same-asset randomized direction and timing, fixed exposure | Momentum/luxalgo dependence and cost sensitivity; legacy mega timing absent; BNB batch exits |
| EQUITY | Splits, distributions, mergers/delistings, exchange sessions/halts, point-in-time constituents, revised fundamentals, short borrow/locates, actual quote side | Sector/beta/exposure-matched investable basket plus cash, simple prespecified momentum/reversal | AAPL historical re-emission; weak/small exploratory accumulation sample |
| ETF | Adjusted/unadjusted price consistency, distributions, live inception/universe, expense/cash drag, rebalance lag, overlapping holdings, spreads | SPY only when mandate fits; otherwise risk-matched balanced/Treasury/cash benchmark | Old tournament not current proof; TAA needs independent total-return book/lag verification |
| BOND | Distinguish bond ETF from individual bond, clean/dirty prices, accrual/coupons, duration/convexity, yield/price confusion, FX, bid/ask and calendar | Duration/credit-quality-matched tradable fund plus cash; measure duration/carry attribution | Thin/stale supply; historical BOND ETF results are not whole bond-market alpha |
| FOREX | Quote inversion, bid/ask, sessions/DST/weekend, rollover/triple swaps, pip/percent units, macro release lag, leverage and margin | Matched carry/trend baseline and randomized direction/timing with actual spreads | Closed-market repeated USDJPY prices; NIO misclassification; pooled versions/regime dependence |
| COMMODITY | Spot/ETF/futures identity, actual contract, COT publication lag/revisions, term curve availability, seasonality, roll schedule | Same tradable contract exposure/cash or appropriate commodity trend/carry benchmark | Copper path contradiction, overlap, raw class recorded FUTURES; one-leg curve fallback cannot substantiate term signal |
| FUTURES | Contract multiplier/tick value, expiry/roll/continuous-series adjustment, settlement/session limits, margin and collateral interest; not normalized spot% alone | Same contract beta/carry/roll/margin budget | Ambiguous class taxonomy; normalized paper not broker-contract PnL |
| MUTUAL FUNDS | Share-class/currency, distribution-reinvested NAV, survivor-free category, dealing cutoff/settlement, loads/fees already embedded in NAV | Category/currency/risk-matched total-return benchmark with persistence study | Ratings product, not audited short-term pick alpha; pooled trade counts are not fund ratings |
| PENNY / MEME | Liquidity, halts, survivor/venue/contract identity, spread/impact, rug/delist risk, available shorting | Investable liquidity-matched baseline; executable capacity required | Raw class aliases must map explicitly; no presumption that main-class proof transfers |

Provider fallback should improve availability, not silently mix prices or
calendars across incompatible venues. Log the chosen source and reject material
disagreement. Any future Binance integration follows the project's multi-source
fallback requirement; no new integration is claimed in this document.

## 9. Public audit output and reproducibility

One page per frozen hypothesis plus a common index must show:

- Exact source/table/window/version and economic scope; historical versus
  forward separation; original claims and explicit superseded verdicts.
- Whole eligible denominator, rejected/unresolved/flat counts, latest **signal**
  and **observation** times, source uptime and stage coverage.
- Daily strategy/benchmark/control equity, gross-to-net bridge, open risk,
  costs/carry, total MTM drawdown, exposure/capacity and dependence assumptions.
- All primary/secondary tests, trial family, adjusted decisions, confidence
  bounds, sample/power and planned readout. Publish failures, not just finalists.
- Hashes, code commit, data snapshots and exact reproducer commands with results.
  Protect credentials and private payloads. Public stable trade IDs suffice.
- Every test field is `PASS`, `FAIL`, `COLLECTING`, `UNVERIFIABLE`,
  `NOT_EVALUABLE` or `NOT_APPLICABLE(reason)`. Missing is never silently PASS.

Proposed certificate skeleton:

```
claim_scope, hypothesis_id, protocol_version, as_of, code_commit
cohort_hash, trial_registry_hash, provenance_status, coverage_status
portfolio_status, cost_status, benchmark_status, dependence_method
historical_tests[], prospective_tests[], multiplicity_family
effect_estimate, confidence_interval, independent_periods, power
tail_risk, exposure_limits, capacity, unresolved_bounds
verdict, blockers[], expiry_or_reassessment_trigger
```

## 10. Audit the auditor: adversarial fixtures before trusting its green badge

The certification engine itself needs a preregistered verification suite.
These are proposed tests, not results already obtained:

| Fixture | Expected result |
|---|---|
| Independent fair-direction strategies with realistic costs | No systematic economic outperformance; estimate familywise false-promotion rate, not just one lucky run |
| Correlated signals duplicated100 times, same trade path | No artificial100-fold increase in independent evidence; portfolio obeys the same capital limit |
| Entry100, expiry60 with an earlier close100 | Expiry60, not100; missing expiry price stays unresolved |
| SL and TP touched in same bar; gap through stop | Conservative ambiguous handling; adverse gap fill at available open |
| Saturday FX, DST transition, valid Sunday reopen | Calendar-aware admissions; no fabricated weekend quote or rejection of a real scheduled reopening |
| Split/dividend/coupon/roll/FX conversion and fractional PnL | Correct total-value continuity and units, no synthetic alpha |
| Known positive effect injected into dependent net returns | Power tracks the planned minimum effect; uncertainty widens under dependence |
|10,000 searched zero-edge variants, report only best | Trial-family/holdout controls prevent selected-certificate promotion |
| Future feature, revisited holdout or stale cloned signal | Provenance/leakage gate fails before economic inference |
| Winning missing outcomes, losing missing outcomes, real flat trades | Missingness disclosed/bounded, not zero-filled; true flats retained |
| Crash/restart during observation or upload; altered frozen rules | No lost observations, duplicate orders or silent reset; digest mismatch stops admissions |
| Unavailable price provider or mismatched venue fallback | Explicit unresolved/error status; no success-shaped fallback |

Suggested inference calibration: run at least10,000 seeded **whole-family**
zero-edge simulations under several autocorrelation, overlap, skew and tail
models, executing the actual selection and decision pipeline. Report
false-promotion frequency and a binomial uncertainty interval. Investigate
rates exceeding nominal alpha plus3 Monte Carlo standard errors; this is a
calibration alarm, not proof of universal statistical validity. Simulate an
untouched validation batch after fixing any calibration failure.

Also run mutation tests that deliberately reverse units, select an entry-time
exit, drop losses or leak a future bar: the relevant assertions must fail.
An auditor that only passes hand-picked positive examples is not validated.

## 11. Primary methodological references

These motivate appropriate methods, not validation of our specific strategy:

- Bailey and Lopez de Prado, *The Deflated Sharpe Ratio: Correcting for Selection
  Bias, Backtest Overfitting, and Non-Normality* (2014),
  [paper record](https://ssrn.com/abstract=2460551).
- Bailey, Borwein, Lopez de Prado and Zhu, *The Probability of Backtest
  Overfitting*, [paper record](https://ssrn.com/abstract=2326253).
- White, *A Reality Check for Data Snooping*, Econometrica68(5),2000,
  [publisher/JSTOR record](https://www.jstor.org/stable/2999446).
- Hansen, *A Test for Superior Predictive Ability*, JBES23(4),2005.
- Politis and Romano, *The Stationary Bootstrap*, JASA89(428),1994.

Records were identified through public search; SSRN full-page requests were
blocked403 during this review. No claim is made to have rederived those papers
or run DSR/PBO/SPA on the incomplete current trial family.

Related: [master execution plan](GHCOPILOT_MASTER_PLAN_2026-10-22.md),
[per-agent critique](_.MD), [investigative questions](GHCOPILOT_MASTER_QUESTIONS.md).
