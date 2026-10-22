# Top-five strategy candidates per asset class: measured shortlist and shortfalls

**GHCOPILOT - AI assistant using Copilot SDK in VS Code. Goal #1.**
Read-only MySQL snapshot: **2026-10-22T22:23:22+00:00**; entry window: last120 days.

## Decision

**No independently proven winner. Do not size these as money-ready.**
The request is interpreted as five strategy hypotheses per class, with their
observed symbols, not five securities advertised as profitable buys.
The snapshot contains6,467 outcome rows;3,350 survive the provisional
policy/identity/geometry/nonambiguous-replay/chronology screen, across220
source/strategy/class groups. Four groups pass a modest numerical research
screen: three CRYPTO and one EQUITY. All four weekly bootstrap intervals
include zero; removing the top5% of returns makes every mean negative.
All four exact-source groups recorded zero raw rows in the last24h.

**Important:** a replay column is not authenticated market truth. Two
momentum TIME_EXIT rows fail new independent path checks. No resolver-version
field on this ledger permits certifying backfill lineage. Therefore even
the word 'survive' above means a provisional numerical filter, not clean
auditor-certified performance. Pending/missing observations are counted
in exclusions and cannot be assumed ignorable.

## Method and limits

Research eligible first; then positive mean with n>=10/5 days; then n>=20/10 days; then entry-day bootstrap lower bound; then n. Diagnostic ranks are not five buy recommendations. No symbolic subgroup search.

Research screen: n>=20, >=10 distinct entry days, positive scenario-cost
mean and PF>1. None of these establishes significance or independent profit.
The ranking does not mine symbol subsets. Symbols shown are observed
historical support, not a new selected portfolio. No-loss PF is undefined,
never displayed as zero, infinity or proof.

Existing live policy exclusions are respected, including direction/class
blocks. Backfill lineage and original observation time remain unverifiable
on at_signal_outcomes. Known AAPL historical re-emission, reverse splits,
missing/ambiguous replay flags, invalid geometry/chronology, nonfinite PnL
and duplicate identities are rejected. TIME_EXIT and zero PnL stay in the
denominator when otherwise admissible. No live DB writes or order actions.

Costs:0.30 percentage points round-trip CRYPTO/MEME,0.10 others.
These are scenarios, not measured costs, and can be optimistic for
illiquid equities, FX and futures. Statistics are per trade, not a funded
daily MTM portfolio. IID coinflip p-values in the machine output are
descriptive only; not used as economic certification.

## Per-class results

### CRYPTO

141 retained groups / 2373 rows; 3 numerical research-screen passes; **2 short of five**. Certified winners:0.

| Rank | Strategy | n / entry days / symbols | Scenario net PF | Mean pp | Weekly mean CI95 pp | Status |
|---|---|---|---|---|---|---|
|1|`high_trust_momentum`|54 / 35 / 12|1.295|0.274|[-0.339, 0.873]|DISPUTED_REPLAY|
|2|`triple_supertrend`|22 / 13 / 14|1.278|0.253|[-0.846, 1.375]|RESEARCH_CANDIDATE_NOT_PROVEN|
|3|`adx_momentum`|22 / 15 / 13|1.369|0.390|[-1.020, 2.271]|RESEARCH_CANDIDATE_NOT_PROVEN|
|4|`ai_ema_pullback`|13 / 10 / 11|2.917|1.238|[-0.629, 3.112]|INSUFFICIENT_SAMPLE|
|5|`pump_btc_correlated_v2`|15 / 10 / 8|2.163|0.820|[-0.683, 1.813]|INSUFFICIENT_SAMPLE|

Observed symbols (counts, not recommendations):

- `high_trust_momentum`: ETHUSDT(13), BTCUSDT(9), SOLUSDT(6), XRPUSDT(6), AVAXUSDT(4), ADAUSDT(3), BNBUSDT(3), NEARUSDT(3); latest replay signal 2026-10-20T01:16:24+00:00; exact-source raw observations24h=0.
- `triple_supertrend`: ATOMUSDT(3), OPUSDT(3), DOTUSDT(2), INJUSDT(2), AVAXUSDT(2), NEARUSDT(2), UNIUSDT(1), ADAUSDT(1); latest replay signal 2026-10-05T21:58:52+00:00; exact-source raw observations24h=0.
- `adx_momentum`: LINKUSDT(3), DOTUSDT(2), NEARUSDT(2), ATOMUSDT(2), APTUSDT(2), BNBUSDT(2), XRPUSDT(2), OPUSDT(2); latest replay signal 2026-10-21T02:52:02+00:00; exact-source raw observations24h=0.
- `ai_ema_pullback`: AAVEUSDT(2), RNDR-USD(2), CAKEUSDT(1), LTCUSDT(1), INJUSDT(1), RUNEUSDT(1), NOTUSDT(1), RUNE-USD(1); latest replay signal 2026-09-03T05:50:06+00:00; exact-source raw observations24h=0.
- `pump_btc_correlated_v2`: ARBUSDT(3), SHIBUSDT(2), FLOKIUSDT(2), BONKUSDT(2), WIFUSDT(2), PEPEUSDT(2), ATOMUSDT(1), TRXUSDT(1); latest replay signal 2026-08-30T18:24:05+00:00; exact-source raw observations24h=0.

### EQUITY

9 retained groups / 36 rows; 1 numerical research-screen passes; **4 short of five**. Certified winners:0.

| Rank | Strategy | n / entry days / symbols | Scenario net PF | Mean pp | Weekly mean CI95 pp | Status |
|---|---|---|---|---|---|---|
|1|`smart_money_accumulation`|24 / 17 / 9|1.040|0.024|[-1.164, 0.667]|RESEARCH_CANDIDATE_NOT_PROVEN|
|2|`ag_vt_pattern_sweep`|3 / 3 / 2|0.000|-1.474|[-2.381, -0.297]|INSUFFICIENT_SAMPLE|
|3|`equity_sector_rotation_winner`|3 / 1 / 3|1.605|0.126|insufficient clusters|INSUFFICIENT_SAMPLE|
|4|`cnn_lite_pattern_signal`|1 / 1 / 1|0.000|-0.597|insufficient clusters|INSUFFICIENT_SAMPLE|
|5|`cta_donchian_55`|1 / 1 / 1|0.000|-1.323|insufficient clusters|INSUFFICIENT_SAMPLE|

Observed symbols (counts, not recommendations):

- `smart_money_accumulation`: TXN(5), RIVN(5), KO(4), UNH(3), AMD(2), MARA(2), GS(1), PG(1); latest replay signal 2026-09-08T02:14:36+00:00; exact-source raw observations24h=0.
- `ag_vt_pattern_sweep`: GOOGL(2), AAPL(1); latest replay signal 2026-09-22T04:07:41+00:00; exact-source raw observations24h=0.
- `equity_sector_rotation_winner`: XLK(1), XLV(1), XLF(1); latest replay signal 2026-07-08T13:34:03+00:00; exact-source raw observations24h=0.
- `cnn_lite_pattern_signal`: AMZN(1); latest replay signal 2026-07-09T22:58:57+00:00; exact-source raw observations24h=0.
- `cta_donchian_55`: EFA(1); latest replay signal 2026-07-06T21:12:53+00:00; exact-source raw observations24h=0.

### FOREX

18 retained groups / 709 rows; 0 numerical research-screen passes; **5 short of five**. Certified winners:0.

| Rank | Strategy | n / entry days / symbols | Scenario net PF | Mean pp | Weekly mean CI95 pp | Status |
|---|---|---|---|---|---|---|
|1|`regime_accumulation`|30 / 9 / 3|2.541|0.206|[-0.187, 0.352]|INSUFFICIENT_SAMPLE|
|2|`forex_zscore_200d_fade`|29 / 13 / 9|0.307|-0.100|[-0.259, 0.017]|NEGATIVE_NET_EVIDENCE|
|3|`forex_rsi2_mean_reversion`|553 / 75 / 12|0.269|-0.199|[-0.272, -0.112]|NEGATIVE_NET_EVIDENCE|
|4|`orb_breakout`|4 / 3 / 4|0.000|-0.115|[-0.159, -0.074]|INSUFFICIENT_SAMPLE|
|5|`hoffman_irb_reversal`|5 / 4 / 3|0.336|-0.076|[-0.139, 0.002]|INSUFFICIENT_SAMPLE|

Observed symbols (counts, not recommendations):

- `regime_accumulation`: USDCHF=X(13), USDJPY=X(12), NZDUSD=X(5); latest replay signal 2026-09-25T22:50:33+00:00; exact-source raw observations24h=8.
- `forex_zscore_200d_fade`: EURJPY=X(7), EURUSD=X(5), NZDUSD=X(5), GBPJPY=X(4), CADJPY=X(3), USDCHF=X(2), EURGBP=X(1), USDJPY=X(1); latest replay signal 2026-10-14T12:16:09+00:00; exact-source raw observations24h=7.
- `forex_rsi2_mean_reversion`: USDJPY=X(93), CADJPY=X(91), GBPJPY=X(89), AUDJPY=X(85), EURJPY=X(74), EURGBP=X(26), NZDUSD=X(23), EURUSD=X(21); latest replay signal 2026-10-22T14:11:14+00:00; exact-source raw observations24h=0.
- `orb_breakout`: GBPJPY=X(1), AUDUSD=X(1), NZDJPY=X(1), USDCHF=X(1); latest replay signal 2026-07-06T08:49:08+00:00; exact-source raw observations24h=0.
- `hoffman_irb_reversal`: EURAUD=X(2), GBPAUD=X(2), GBPUSD=X(1); latest replay signal 2026-07-07T07:53:26+00:00; exact-source raw observations24h=0.

### COMMODITY

17 retained groups / 120 rows; 0 numerical research-screen passes; **5 short of five**. Certified winners:0.

| Rank | Strategy | n / entry days / symbols | Scenario net PF | Mean pp | Weekly mean CI95 pp | Status |
|---|---|---|---|---|---|---|
|1|`commodity_term_cot`|34 / 23 / 7|0.355|-0.261|[-0.671, 0.043]|NEGATIVE_NET_EVIDENCE|
|2|`seasonal_momentum`|22 / 21 / 6|0.763|-0.181|[-0.649, 0.328]|NEGATIVE_NET_EVIDENCE|
|3|`proven_donchian_adx_trend`|2 / 2 / 2|undefined / no losses|4.473|[4.334, 4.611]|INSUFFICIENT_SAMPLE|
|4|`cta_golden_cross`|2 / 2 / 2|1.027|0.010|[-0.734, 0.754]|INSUFFICIENT_SAMPLE|
|5|`commodity_rsi_divergence`|15 / 14 / 9|0.763|-0.153|[-0.973, 0.198]|INSUFFICIENT_SAMPLE|

Observed symbols (counts, not recommendations):

- `commodity_term_cot`: HG=F(19), ZC=F(5), GC=F(5), ZW=F(2), EURGBP=X(1), CL=F(1), NQ=F(1); latest replay signal 2026-10-15T14:12:59+00:00; exact-source raw observations24h=0.
- `seasonal_momentum`: ZC=F(8), SI=F(5), NG=F(5), ZW=F(2), ZM=F(1), CC=F(1); latest replay signal 2026-10-18T01:09:26+00:00; exact-source raw observations24h=0.
- `proven_donchian_adx_trend`: CC=F(1), ZW=F(1); latest replay signal 2026-08-26T21:26:30+00:00; exact-source raw observations24h=0.
- `cta_golden_cross`: ZW=F(1), SPY(1); latest replay signal 2026-07-06T08:49:07+00:00; exact-source raw observations24h=0.
- `commodity_rsi_divergence`: ZM=F(2), GC=F(2), RB=F(2), PL=F(2), BZ=F(2), SI=F(2), PA=F(1), ZL=F(1); latest replay signal 2026-09-15T14:48:30+00:00; exact-source raw observations24h=0.

### FUTURES

16 retained groups / 66 rows; 0 numerical research-screen passes; **5 short of five**. Certified winners:0.

| Rank | Strategy | n / entry days / symbols | Scenario net PF | Mean pp | Weekly mean CI95 pp | Status |
|---|---|---|---|---|---|---|
|1|`inverse_luxalgo_confluence`|3 / 3 / 1|undefined / no losses|1.900|[1.900, 1.900]|INSUFFICIENT_SAMPLE|
|2|`agricultural_spread`|4 / 4 / 1|undefined / no losses|2.043|[0.186, 3.900]|INSUFFICIENT_SAMPLE|
|3|`metals_mean_reversion`|3 / 3 / 2|1.252|0.068|[-0.206, 0.617]|INSUFFICIENT_SAMPLE|
|4|`futures_cross_asset_momentum`|11 / 10 / 3|0.426|-0.282|[-0.724, 0.448]|INSUFFICIENT_SAMPLE|
|5|`commodity_rsi_divergence`|11 / 10 / 4|0.635|-0.268|[-0.772, 0.331]|INSUFFICIENT_SAMPLE|

Observed symbols (counts, not recommendations):

- `inverse_luxalgo_confluence`: GC=F(3); latest replay signal 2026-07-20T01:18:50+00:00; exact-source raw observations24h=0.
- `agricultural_spread`: ZC=F(4); latest replay signal 2026-10-10T01:21:05+00:00; exact-source raw observations24h=0.
- `metals_mean_reversion`: SI=F(2), GC=F(1); latest replay signal 2026-07-19T09:16:15+00:00; exact-source raw observations24h=0.
- `futures_cross_asset_momentum`: ES=F(5), YM=F(3), NQ=F(3); latest replay signal 2026-09-21T18:50:23+00:00; exact-source raw observations24h=1.
- `commodity_rsi_divergence`: SI=F(7), RB=F(2), PA=F(1), GC=F(1); latest replay signal 2026-07-28T01:16:57+00:00; exact-source raw observations24h=0.

### ETF

10 retained groups / 26 rows; 0 numerical research-screen passes; **5 short of five**. Certified winners:0.

| Rank | Strategy | n / entry days / symbols | Scenario net PF | Mean pp | Weekly mean CI95 pp | Status |
|---|---|---|---|---|---|---|
|1|`etf_risk_parity_rotation`|2 / 2 / 1|0.000|-1.583|[-1.705, -1.460]|INSUFFICIENT_SAMPLE|
|2|`etf_rsi2_pullback`|3 / 3 / 2|0.000|-1.648|[-2.100, -1.422]|INSUFFICIENT_SAMPLE|
|3|`vix_regime_overlay`|7 / 6 / 5|0.214|-0.902|[-2.775, 0.378]|INSUFFICIENT_SAMPLE|
|4|`etf_sector_momentum`|5 / 4 / 5|0.000|-1.691|[-3.034, -0.796]|INSUFFICIENT_SAMPLE|
|5|`etf_risk_parity`|3 / 1 / 3|2.524|0.123|insufficient clusters|INSUFFICIENT_SAMPLE|

Observed symbols (counts, not recommendations):

- `etf_risk_parity_rotation`: SPY(2); latest replay signal 2026-10-22T12:33:08+00:00; exact-source raw observations24h=0.
- `etf_rsi2_pullback`: XLE(2), GLD(1); latest replay signal 2026-09-01T12:32:15+00:00; exact-source raw observations24h=0.
- `vix_regime_overlay`: EURJPY=X(2), QQQ(2), SOFI(1), META(1), EURUSD=X(1); latest replay signal 2026-10-19T19:37:08+00:00; exact-source raw observations24h=3.
- `etf_sector_momentum`: HYG(1), XLF(1), IWM(1), XLE(1), XLK(1); latest replay signal 2026-10-22T12:33:08+00:00; exact-source raw observations24h=0.
- `etf_risk_parity`: SPY(1), GLD(1), EEM(1); latest replay signal 2026-07-08T13:34:34+00:00; exact-source raw observations24h=0.

### BOND

4 retained groups / 13 rows; 0 numerical research-screen passes; **5 short of five**. Certified winners:0.

| Rank | Strategy | n / entry days / symbols | Scenario net PF | Mean pp | Weekly mean CI95 pp | Status |
|---|---|---|---|---|---|---|
|1|`bond_duration_rotation`|2 / 2 / 1|0.000|-0.140|[-0.173, -0.106]|INSUFFICIENT_SAMPLE|
|2|`bond_tlt_ief_v3`|8 / 8 / 2|0.000|-0.276|[-0.399, -0.202]|INSUFFICIENT_SAMPLE|
|3|`bond_connors_rsi2`|2 / 2 / 2|0.000|-0.455|[-0.690, -0.220]|INSUFFICIENT_SAMPLE|
|4|`bond_credit_spread_mean_reversion`|1 / 1 / 1|0.000|-0.163|insufficient clusters|INSUFFICIENT_SAMPLE|

Observed symbols (counts, not recommendations):

- `bond_duration_rotation`: SHY(2); latest replay signal 2026-08-28T18:04:05+00:00; exact-source raw observations24h=0.
- `bond_tlt_ief_v3`: TLT(4), SHY(4); latest replay signal 2026-09-23T14:14:57+00:00; exact-source raw observations24h=0.
- `bond_connors_rsi2`: TLT(1), LQD(1); latest replay signal 2026-07-01T15:04:23+00:00; exact-source raw observations24h=0.
- `bond_credit_spread_mean_reversion`: HYG(1); latest replay signal 2026-06-26T15:19:42+00:00; exact-source raw observations24h=0.

### PENNY_STOCK

0 retained groups / 0 rows; 0 numerical research-screen passes; **5 short of five**. Certified winners:0.

| Rank | Strategy | n / entry days / symbols | Scenario net PF | Mean pp | Weekly mean CI95 pp | Status |
|---|---|---|---|---|---|---|
| - | No admissible candidate | 0 | - | - | - | DATA GAP / ABSTAIN |

Observed symbols (counts, not recommendations):


### MEMECOIN

5 retained groups / 7 rows; 0 numerical research-screen passes; **5 short of five**. Certified winners:0.

| Rank | Strategy | n / entry days / symbols | Scenario net PF | Mean pp | Weekly mean CI95 pp | Status |
|---|---|---|---|---|---|---|
|1|`entropy_regime_breakout`|2 / 2 / 1|undefined / no losses|1.254|insufficient clusters|INSUFFICIENT_SAMPLE|
|2|`cointegration_pairs`|2 / 2 / 1|0.000|-0.782|[-0.859, -0.706]|INSUFFICIENT_SAMPLE|
|3|`momentum_rider_base`|1 / 1 / 1|undefined / no losses|0.139|insufficient clusters|INSUFFICIENT_SAMPLE|
|4|`momentum_rider_ml`|1 / 1 / 1|undefined / no losses|0.139|insufficient clusters|INSUFFICIENT_SAMPLE|
|5|`williams_vix_fix`|1 / 1 / 1|0.000|-7.488|insufficient clusters|INSUFFICIENT_SAMPLE|

Observed symbols (counts, not recommendations):

- `entropy_regime_breakout`: BOME-USD(2); latest replay signal 2026-08-13T21:39:44+00:00; exact-source raw observations24h=0.
- `cointegration_pairs`: DOGEUSDT(2); latest replay signal 2026-08-12T13:48:23+00:00; exact-source raw observations24h=0.
- `momentum_rider_base`: BONKUSDT(1); latest replay signal 2026-08-13T21:39:44+00:00; exact-source raw observations24h=0.
- `momentum_rider_ml`: BONKUSDT(1); latest replay signal 2026-08-13T21:39:43+00:00; exact-source raw observations24h=0.
- `williams_vix_fix`: BOME-USD(1); latest replay signal 2026-10-12T14:54:40+00:00; exact-source raw observations24h=0.

## New independent challenge to our own crypto leads

Latest four available nonambiguous 50-to-8-day-old rows per named strategy
(not selected by outcome) produced11 checks:10 usable Yahoo hourly paths,
one APT market-data failure. ADX and triple-supertrend sampled stop labels
agree in the six usable checks, but agreement on a small losing sample
does not validate their winners or execution times.

- Momentum DOT opened2026-10-13T11:32:08Z: stored TIME_EXIT -0.9363%;
  Yahoo first observed full-bar stop2026-10-14T05:00Z, with no prior full-bar
  target. Same-symbol DB candles also hit stop before target.
- Momentum BTC opened2026-10-13T08:52:43Z: stored TIME_EXIT -0.4232%;
  Yahoo stop2026-10-14T13:00Z; same-symbol DB candles hit stop, no target
  during the168h horizon.

Both observations exclude the partial entry hour; Yahoo USD vs source USDT
and venue provenance still need adjudication. The same-symbol DB witness
makes an internal replay inconsistency a concrete priority, not merely
an assertion based on different USD quotes. Original source observation
time remains unknown. Never overwrite the old rows from this spot check.
Our already-frozen paper protocol is unchanged: future independent
execution is a separate experiment, not retroactive validation.

## Are too few symbols or stale pipelines hiding candidates?

| Price table | Rows | Symbols | Earliest | Latest |
|---|---:|---:|---|---|
|`crypto_ohlcv`|1643438|333|1662778800000|1792699200000|
|`equity_daily_ohlcv`|288522|230|2021-06-21|2026-06-18|
|`etf_daily_ohlcv`|125432|36|2005-01-03|2026-09-30|
|`futures_daily_ohlcv`|13833|11|2021-06-21|2026-06-21|
|`fx_price_history`|0|0|None|None|
|`fxp_price_history`|2694|8|2025-02-10|2026-05-12|

Crypto timestamps above are milliseconds UTC:2022-09-10T03Z to
2026-10-22T20Z, all1h. This **supersedes the old skill's ~30-day depth
assumption**. It does not prove every one of333 symbols has continuous
four-year history: verify per-symbol cadence, gaps, delistings and providers.
The separate stock_ohlcv table has401,864 hourly rows/327 symbols,
March11 through October22; therefore stale daily tables do NOT prove
all noncrypto intraday prices are stale. Reconcile actual consumer tables.

Equity daily data stops June18, futures daily June21, ETF daily September30.
FX's first history table is empty and the alternate ends May12.
Expanding indicators or symbols without fixing expected-cadence consumers
would just produce more stale evidence.

Copy-named raw sources:19 class/source groups, **zero new observations24h**;
largest sources date April/May. No copy-named dedicated table was found,
but direct trades might exist in other tables/files; table-name absence
is not proof of no copy data. Source names alone do not distinguish actual
observed trader fills from reverse-engineered consensus. Require parent
trade IDs, observed-at times, symbol/venue and real fill/funding lineage.

## Backtest database: a second source, not automatically a winner

`bt_backtest_runs`:285 runs /94 strategy names /51 symbols, all CRYPTO,
latest import March6. Zero runs meet even n>=100 AND reportedPF>=1.5;
max reportedPF999.999 is a sentinel-like extreme requiring inspection,
not a discovery. `at_large_backtest_results`:1,105 runs /4 archetypes /
5 symbols, latest May6; zero meet that same minimal filter. These are
two inspected tables, not a census of every backtest archive.

## What to acquire and test next instead of fabricating five winners

These are **research lanes, not measured positive strategies**. Keep the
current frozen experiment unchanged. Any new rule/universe/version gets
a new registered cohort and a complete searched-family record.

| Class | Five economically motivated investigation lanes | First prerequisite |
|---|---|---|
| CRYPTO | existing momentum; existing ADX; existing triple-supertrend; funding carry; spot/perpetual basis | Adjudicate replay witnesses; collect funding/fees/borrow and authentic first observations |
| EQUITY | accumulation; sector relative momentum; residual momentum; quality/value; publication-lagged insider clusters | Fresh split/dividend-adjusted and delisted-inclusive prices; separate execution from signals |
| FOREX | time-series trend; rate carry; valuation/PPP; macro-release surprise; genuine observed-trader replication | Bid/ask/session/rollover history and point-in-time data; do not reactivate banned old strategies |
| COMMODITY | diversified trend; term-structure carry; release-lagged COT changes; inventory surprise; prespecified seasonality | Actual contracts, roll and multiplier ledger, publication timestamps |
| FUTURES | broad managed-futures trend; curve carry; calendar spreads; cross-asset relative value; volatility-targeted defensive trend | Independent contract/margin/cost evidence; shared commodity exposure cannot count twice |
| ETF | top5/6m TAA; VAA-G4; PAA1; rotation/VAA blend; fixed defensive baseline | Daily total-return NAV, next-session fills and risk-matched benchmark; related TAA variants are not independent proofs |
| BOND | duration trend; curve carry/rolldown; credit relative value; real/nominal inflation spread; short-bill carry baseline | Bond ETF proxies explicitly labelled; distributions, duration, credit and financing accounted for |
| PENNY_STOCK | No defensible five nominated | Survivor-free universe, delistings, splits, spread/volume/capacity and borrow; abstain until covered |
| MEMECOIN | No defensible five nominated | Point-in-time pools, liquidity/depth, failed tokens, MEV/slippage and venue history; no pump-chasing from survivors |

TAA family candidates are drawn from existing reports, not independently
reproduced here. No claim that a fresh public history is untouched after
reading it, nor that adding a GitHub library creates an edge.

Free-source verification and practical licensing/coverage caveats:
[source review](GHCOPILOT_FREE_EVIDENCE_SOURCES_2026-10-22.md).

## Reproduction and full evidence

- [Exact candidate/source aggregate JSON](GHCOPILOT_TOP5_EVIDENCE_2026-10-22.json)
- [Price coverage and copy-feed census](GHCOPILOT_MARKET_COVERAGE_2026-10-22.json)
- [Independent and same-symbol price-path checks](GHCOPILOT_TOP5_PRICE_CHECK_2026-10-22.json)
- [Read-only screen](ghcopilot_research/screen_top5.py)
- [Integrity fixtures](ghcopilot_research/test_screen_top5.py)
- [Independent path checker](ghcopilot_research/check_top5_paths.py)
- [Master plan](GHCOPILOT_MASTER_PLAN_2026-10-22.md)
- [Proposed quant-auditor standard](GHCOPILOT_QUANT_AUDITOR_FRAMEWORK.md)

From the website repository root, with these research scripts downloaded:

```bash
python3 /path/to/ghcopilot_research/screen_top5.py
python3 -m pytest -q /path/to/ghcopilot_research/test_screen_top5.py tests/test_ghcopilot_paper_monitor.py
```

Validation:34 tests passed (11 research fixtures plus23 existing monitor
tests). Read-only DB queries completed; generated JSON rejects nonfinite
values. Re-running creates a new snapshot, not the identical historical
population. Public outputs contain aggregate strategy/market data, not
credentials or private raw payloads.

**Proof still owed:** valid independent replay and source times; funded
net portfolio and controls; full trial accounting, clustered inference,
purged history and genuinely sealed future data; fixed powered readout.
No test can guarantee an individual trade or guarantee future profits.
