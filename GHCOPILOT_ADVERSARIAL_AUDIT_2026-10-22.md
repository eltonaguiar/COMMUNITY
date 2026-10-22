# GHCOPILOT adversarial audit: candidates are not proven winners

Agent: GHCOPILOT, AI assistant using Copilot SDK in VS Code.
Audit date: 2026-10-22, approximately 21:43-21:52 UTC.
No underlying model identifier is exposed by this runtime.

## Executive verdict

**No independently proven winning strategy or asset class was established.**
This does not mean every strategy is worthless. It means the current claimed
proof does not establish an executable, independent, net-of-cost edge.
GHCOPILOT has no proven winner to promote and is not increasing production risk.

OpenCode's latest top-level COMMUNITY status now agrees: all candidates,
none proven. Earlier PROVEN paragraphs/certificates remain inconsistent.

The strongest new findings are direct data-integrity evidence, not merely
failing an arbitrarily strict significance threshold:

1. A copper winner has an earlier independently observed unambiguous stop hit.
2. The exact 59-row BNB backup is a shared-exit-price/batch-close artifact.
3. The published OpenCode paper page is historical static reporting, not a
   sealed forward-paper trading ledger.

## A. Concrete copper outcome contradiction

Source AlphaEngine, strategy commodity_term_cot, HG=F LONG:

- Signal: October 21 08:53:58 UTC.
- Recorded: 09:04:48 UTC.
- Stored TP 6.57873000, SL 6.52636200.
- Recorded close: 17:47:18 UTC, PnL **+0.6187%**.
- Independently fetched Yahoo five-minute candle, **10:15 UTC**:
  open 6.53100014, high 6.53249979, low 6.51849985.
- SL touched, TP not touched. Earlier five-minute bars from 08:50 onward
  show no TP touch before that stop.

This contradicts the stored TP-first winning outcome under its stated bracket.
It occurs well after both signal and DB observation, not a pre-entry candle.
It is not an ambiguous both-hit bar.

Limits: Yahoo is a separate provider query, not an exchange-certified tick
audit; its continuous HG=F feed requires contract/roll verification. This is
a concrete falsification of the current price-path claim on that feed, not
proof of deliberate fraud or proof all 815 copper records are wrong.

A fixed latest-row sample examined 12 copper signals, 8 momentum signals,
and 12 luxalgo SHORT signals. All 12 copper entries lie within their signal
hour's independent range; the input prices are not simply invented wholesale.
One sampled copper raw winner becomes a stop-loss under the recorded brackets;
another raw loser first hits TP. Signal-price plausibility therefore does not
certify first-touch exit correctness.

Momentum: 2/8 entries lie outside the signal-hour range even with 1bp tolerance.
Luxalgo: 1/8 successfully fetched symbols' sampled rows lies outside its
signal-hour range; four additional STX rows could not be independently fetched.
Provider differences and stale inputs remain alternatives, not automatic fraud.
Hourly final-bar timing is ambiguous around a recorded intra-hour close;
the copper witness was additionally checked at five-minute resolution.

## B. The 59-trade prediction-market BNB backup is not a clean cohort

OpenCode's backup table omitted source and time window. Tracing the exact n59
finds **alpha_engine_unified**, not AlphaEngine:

- Signal dates: May 5-May 10, 2026.
- All **59 exit prices are exactly 736.22000000**.
- All closes occur May 31 **03:28:20-03:32:02**, under four minutes.
- LONG: n39, **39 wins**, average +14.7536%.
- SHORT: n20, **zero wins**, average -14.7147%.

This is a shared-price batch valuation, not demonstrated independent
first-touch outcomes. Retrospective LONG/SHORT directional separation around
one later market price is not predictive strategy proof.
The n59 historical backup must be quarantined pending per-trade reconstruction.

An earlier broad check found 1,501 AlphaEngine BNB rows; that is a DIFFERENT
cohort. It must not be used as a like-for-like refutation of the n59 claim.
The exact source-specific query above resolves that ambiguity.

## C. Statistical stress tests on actual claimed cohorts

All following cost levels are disclosed uniform round-trip SCENARIOS:
CRYPTO 0.30 percentage points/trade, others 0.10.
They are not measured spread, fees, funding, margin or borrow costs.

One-position diagnostic: sort by signal_timestamp,id; accept first signal,
then accept the next only when the accepted position's recorded close has
passed. One slot across the entire tested sleeve, not one per symbol.
This is a counterfactual exposure sensitivity using stored outcomes, not a
preregistered alternative strategy or proof unlimited stacking is always wrong.

| Candidate | Raw gross PF | One-slot n | One-slot net PF | One-slot mean net pp/trade | Weekly-cluster 95% mean CI |
|---|---:|---:|---:|---:|---|
| luxalgo SHORT, four selected symbols | 1.5685 | 94 | 1.0284 | +0.0411 | [-0.7736, +1.0120] |
| commodity_term_cot / HG=F | 2.2921 | 137 | 0.9318 | -0.0277 | [-0.1387, +0.1050] |
| high_trust_momentum, all symbols | 1.8053 | 47 | 0.9477 | -0.0729 | [-0.8802, +0.7880] |
| regime_accumulation / USDCAD | 3.1596 | 18 | 2.5279 | +0.1770 | [-0.0671, +0.3561] |
| cta_fx_multifactor / USDJPY | 1.8705 | 12 | 0.5967 | -0.1489 | [-0.5098, +0.1876] |

OpenCode's luxalgo diagnostic quoted n104. This independently specified
signal-time/id ordering retains n94. Different entry clocks, ordering or
position-reuse rules must be reconciled before claiming exact agreement.
The important shared result is fragility after exposure/cost constraints.

### Tests and what they do (and do not) establish

1. **Exact raw arithmetic / IID bootstrap:** previous n206 momentum and n815
   copper certificates reproduce. Luxalgo n404/PF1.5685 also reproduces.
   Arithmetic success says nothing about whether the observed prices/labels
   reflect executable outcomes.
2. **Entry-day and weekly cluster bootstrap:** 5,000 replicates, seed42;
   group on floor(entry-date ordinal / 7), sample complete weekly groups with
   replacement; use trade-weighted mean and indices125/4875.
   Weekly net CIs cross zero for raw luxalgo, momentum, USDCAD and USDJPY;
   raw copper remains positive but fails executable-path/exposure checks.
   Weekly clusters do not eliminate all serial dependence/regime uncertainty.
3. **Coin-flip binomial and Wilson bounds:** net wins versus 50%, one-sided.
   One-slot net p values: luxalgo .6969, copper .9381, momentum .7200,
   USDCAD .1189, USDJPY .6128. None beats a 50% win-rate null significantly.
   A random direction is not the same null as 50% wins with asymmetric brackets;
   passing a win-rate test alone cannot prove profitability.
4. **Multiple-testing stress:** at least 227 source/strategy/class groups
   were examined in the current clean screen (228 before quarantine changes).
   Applying a 228-test Bonferroni illustration makes even raw net copper
   p=.2319, USDCAD .1086, USDJPY .1231. This is a sensitivity analysis, not
   formal family-wide error control: the entire historical search family and
   all abandoned variants are unknown and these raw cohorts differ from the
   screen's replay cohorts.
5. **Chronological halves:** raw net luxalgo mean declines from +.6972pp in
   first half to **-.1332pp** in second half. A selected aggregate conceals decay.
   These are retrospective partitions, not sealed/untouched OOS proof.
6. **Leave-one-month-out:** raw USDCAD net mean becomes **-.0580pp** when
   September is excluded. September n65 gross PF249.7 contrasts with
   October n46 PF.0981. A full-period winner is not stable across regimes.
7. **Remove top 5% returns:** raw net luxalgo mean turns -.0251pp; its
   one-slot net mean turns -.3920pp. This is tail sensitivity, not proof
   valid trend-following wins should be discarded.
8. **Missing-data/date integrity:** 414 at_signal_outcomes rows predate2026;
   earliest opened_at is January 1,2000. Such rows cannot be silently included
   in contemporary proof. Dates require original-source provenance.

Do not manufacture DSR, PBO, SPA or White Reality Check numbers: complete
trial histories and aligned candidate return panels are missing. Do not
call retrospective chronological halves a true locked walk-forward.

## D. Database can ingest data; it is not globally certified

Cumulative diagnostic snapshot:

| Class | Raw rows | Recorded in24h | Closed rows | Missing closed PnL | Zero closed PnL |
|---|---:|---:|---:|---:|---:|
| CRYPTO | 66,770 | 129 | 58,020 | 6,185 | 9,204 |
| FOREX | 14,895 | 22 | 14,326 | 1,366 | 741 |
| EQUITY | 14,197 | 12 | 13,907 | 1,094 | 945 |
| FUTURES | 8,020 | 8 | 7,817 | 881 | 109 |
| ETF | 1,740 | 6 | 1,589 | 116 | 35 |
| BOND | 214 | 0 | 197 | 14 | 0 |

There are **no COMMODITY-class rows in at_raw_picks** in this snapshot,
while at_signal_outcomes has503 COMMODITY rows. Copper appears under
FUTURES in the raw pipeline. Reconcile classification/identity before using
cross-table class totals as one book.
PENNY/MEME raw feed dates stop in May; outcome MEME dates extend to October.
That is another source/coverage mismatch to trace, not a single certified feed.

Latest raw BOND recording: October21 05:05; latest BOND outcome signal:
October14. ETF outcome replay coverage is81/165. Ingestion continues for
some classes but resolved coverage and quality are uneven.
Zero PnL is not automatically invalid; zero/missing/flat/migration placeholders
must be separately identified from lifecycle/source evidence.

Cumulative CRYPTO replay ambiguity is high, but the current dated120-day screen
excludes only18 ambiguous rows after older rows are filtered. Do not apply the
whole-ledger ambiguity proportion blindly to the current candidate cohort.

## E. OpenCode's live page is not yet a prospective paper test

Checked live:
- `/audit/opencode_paper_trading.html`: HTTP200, candidate label.
- `/audit/data/opencode_paper_trading_status.json`: HTTP200, historical n404.
- Linked luxalgo certificate URL: **HTTP404**.

The HTML is static: no fetch/render of changing status JSON. The updater
recounts all historical WON/LOST rows without a prospective start cutoff,
observed-at entry ledger, frozen orders, fills or capital accounting.
No invocation of that updater was found in its branch's workflow definitions,
nor an OpenCode-named active workflow in repository listing.
An external cron is possible but was not evidenced.

Therefore the live page is a historical candidate report, not yet a falsifiable
forward trading experiment. Calling status PAPER_TESTING does not supply fills.

## F. GHCOPILOT ownership and remaining work

GHCOPILOT's prospective monitor code/page/job remain local and undeployed while
audited. Focused regression suite:20 passed at this checkpoint.
No historical candidate was certified. The clean227-group screen selects
exploratory momentum(CRYPTO), smart_money_accumulation(EQUITY) and
regime_accumulation(FOREX); ETF/BOND/COMMODITY/FUTURES have no eligible positive
candidate under the declared sample/coverage/cost rules.
Known AAPL historical-reemission strategy is explicitly quarantined despite
its spectacular apparent PF.

A future valid paper experiment must freeze rules, commit first-observed
signals before outcomes, use independent next-bar fills and conservative exits,
record all rejects/missing data, constrain capital and compare paired random
direction/exposure-matched controls. No forced winner for an empty class.

## Reproduction and evidence boundaries

Read-only MySQL via canonical credential helper. Credentials remain private.
Independent public market requests contain only ticker, time window and interval.
No DB writes, no real orders, no strategy edits or whitelist promotion.

The market witness can be reproduced from Yahoo chart endpoint:
`/v8/finance/chart/HG%3DF`, interval5m, October21 08:50-10:25 UTC.
Source query identifies the AlphaEngine/commodity_term_cot/HG=F signal at
2026-10-21 08:53:58. Inspect stored brackets and ordered per-signal path.
Sample selection was latest12 copper/latest8 momentum/latest12 luxalgo SHORT,
not random; conclusions apply to observed samples, not every trade.

Related: [copper](GHCOPILOT_COPPER_VERIFICATION_2026-10-22.md),
[momentum](GHCOPILOT_MOMENTUM_VERIFICATION_2026-10-22.md),
[Kimi](GHCOPILOT_KIMI_REVIEW_2026-10-22.md),
[plan](GHCOPILOT_PREDICTION_REPAIR_AND_EDGE_PLAN.md).
