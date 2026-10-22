# Free-source acquisition plan: data before more parameter searches

GHCOPILOT, 2026-10-22. This is a source map, not a winning strategy or a
representation that every endpoint/dataset has been integration-tested.
Library licenses and data redistribution/venue terms are separate.
Nothing is installed or wired into production by this report.

## Reuse before adding dependencies

The database already contains1,643,438 hourly crypto rows across333 symbols
and401,864 hourly stock rows across327 symbols in the inspected snapshot.
Aggregate minimum/maximum dates do not imply continuous history per symbol.
Several daily and FX datasets are stale or empty; class-specific freshness,
missingness and point-in-time instrument membership must be checked.
See [market coverage](GHCOPILOT_MARKET_COVERAGE_2026-10-22.json) and
[lifecycle audit](GHCOPILOT_CLASS_LIFECYCLE_AUDIT_2026-10-22.md).

| Class | Candidate free/public source or library | Evidence still required |
|---|---|---|
| CRYPTO | [CCXT](https://github.com/ccxt/ccxt), [official Binance archives](https://github.com/binance/binance-public-data) and venue APIs | Spot/perpetual identity, outages, delistings, funding, realistic spread/depth. Do not use one exchange endpoint without fallbacks. |
| EQUITY | [yfinance](https://github.com/ranaroussi/yfinance) for bounded independent research witnesses; [LEAN](https://github.com/QuantConnect/Lean) as an engine candidate | Point-in-time universe, delistings, corporate actions, total returns, borrow and venue execution. Free software does not supply every historical dataset. |
| FOREX | [pandas-datareader](https://github.com/pydata/pandas-datareader) where supported, official central-bank reference series | Daily reference rates do not establish intraday bid/ask fills, rollover or feasible weekend prices. Current internal FX history needs repair/refresh. |
| COMMODITY / FUTURES | [CFTC public reports](https://www.cftc.gov/MarketReports/CommitmentsofTraders/index.htm), [FRED](https://fred.stlouisfed.org/) / [ALFRED vintages](https://alfred.stlouisfed.org/) and exchange specifications | Respect actual release times, revisions, contract rolls, multipliers, margin, financing and executable tradable proxies. Macro series are not futures fills. |
| ETF | Issuer distributions/holdings and independently checked price/total-return series; LEAN engine candidate | Distributions, fees, inception/delisting, reconstitution and point-in-time selection; test timing versus passive exposure. |
| BOND | Treasury/FRED yield curves, ALFRED vintages and investable ETF proxies where appropriate | Yield change is not bond total return. Duration, credit, coupons, currency and distributions must match the hypothesis and benchmark. |
| PENNY_STOCK | Exchange/company disclosures and SEC data; a broker/vendor feed with acceptable rights | Free current snapshots rarely solve delisted-universe survivorship, spreads, halts and borrow. No verified adequate free dataset established here: abstain until available. |
| MEMECOIN | Official venue/on-chain feeds and CCXT where supported | Token/contract identity, pool liquidity, fees, gas/MEV, delisted failures and point-in-time universe. A survivor leaderboard is not an investable strategy. |

## Actual copying versus observing historical leaderboards

[Hyperliquid's public Info API](https://hyperliquid.gitbook.io/hyperliquid-docs/for-developers/api/info-endpoint)
and its [official Python SDK](https://github.com/hyperliquid-dex/hyperliquid-python-sdk)
are concrete read-only research options for fills and positions.
Endpoint history limits, query availability and permissible use still require
an implementation check. Public address observations need privacy review
before any publication; do not publish trader identities unnecessarily.

Archive first observation, source fill time/price and the follower's feasible
post-observation fill separately. Include trader selection/survivor failures,
fees, funding, liquidity and delay. A public PnL card is not an independently
replicated follower ledger. The inspected copy-named database source groups
have no fresh24h observations; broader absence was not established.

## Candidate validation tools, not sources of automatic alpha

[Freqtrade](https://github.com/freqtrade/freqtrade),
[Jesse](https://github.com/jesse-ai/jesse) and
[TA-Lib Python](https://github.com/TA-Lib/ta-lib-python) may help implement
reproducible signals, lookahead checks and independent simulation.
LEAN may help cross-asset accounting. Verify applicable licenses, maintenance,
supported execution assumptions and data rights before choosing a dependency.
More libraries or a faster parameter sweep do not prove more edge.

## Next bounded acquisition experiment

1. Freeze one mechanism and minimum instrument/liquidity universe per class.
2. Audit internal coverage before downloading duplicates.
3. Fetch a small independent witness sample; reconcile UTC/bar semantics,
   splits/rolls and first-touch outcomes before scaling.
4. Version raw data hashes, missing observations, provider lineage and costs.
5. Preregister any new backtest/filter; retain the untouched future cohort.

No new data feed is claimed operational, no third-party strategy is promoted,
and no private credentials or raw trader payloads accompany this source map.
