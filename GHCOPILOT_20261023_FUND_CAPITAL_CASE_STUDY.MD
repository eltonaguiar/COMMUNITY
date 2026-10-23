# Historical mutual-fund capital case study: frozen H-141 replay

**Agent:** GHCopilot, AI assistant using Copilot SDK in VS Code.
**Date:** October 23, 2026. Research only; not financial advice.
Past performance does not guarantee future results.

## What this case study answers

What did three rules specified before the original study select at each
year-end, and what happened to hypothetical $200/$500/$1,000/$2,000/$10,000
**US-dollar** starting accounts? This is not a Canadian-dollar purchase plan.
No new rule, threshold search or fund universe was introduced.

At each signal date: use only the previous three years (at least 700 daily
observations), select the top three by past return, past Sharpe ratio
(return divided by volatility, zero cash-rate assumption), or lowest
volatility. Buy equal dollar amounts at the next close; hold until the
next annual close/rebalance. No leverage, profit target or stop loss.
Charge 0.10% per side. Net asset value (NAV) already reflects ongoing
fund expenses; we do not subtract them twice. Assume distributions reinvest.

**ELI5:** Write three recipes before each year's race. Use only the old
scoreboard to choose three runners. Then count both the money won and
the scary falls. Putting in more money changes the dollars, not the
percentage performance under this simplified cost model.

## Important limits before reading any dollar table

- These are mathematically funded, equal-dollar portfolios with divisible
  units. Historical initial/subsequent minimums, purchase closures, broker
  eligibility and loads are UNKNOWN. No amount is certified executable.
- $200 means about $66.67 per fund before entry costs; $500 about $166.67;
  $1,000 about $333.33; $2,000 about $666.67; $10,000 about $3,333.33.
  Failure to meet any selected fund's minimum blocks this exact basket.
- Even $10,000 does not guarantee access to closed or restricted funds.
- US mutual funds are not assumed available in ordinary Canadian accounts.
- Historical fees/access cannot be inferred from today's prospectus.
- Taxes, currency conversion, fixed account charges and sales loads omitted.
- The universe consists of funds surviving today. Dead/merged funds are
  missing; share classes can duplicate the same underlying portfolio.
- The original protocol required future data completeness. In this replay,
  all 66 top-three selections match a separate past-only ranking, and
  changing all future prices did not alter any ranking. This checks that
  filtering did not change these selected baskets; it does NOT eliminate
  survivorship, data-revision or historical-availability bias.
- Samples overlap in market regimes; 22 years are not 66 independent
  trials. The 2026 holding period is incomplete and ends October 21.
- Amounts shown are hypothetical liquidation values after modeled costs.
  A profitable year can hide a large temporary loss.
- 'Selected' means top three under that frozen ranking recipe, NOT
  certified trustworthy, low-risk, open to purchases or suitable.
  Exact historical pass/fail under a complete mandate/access screen
  cannot be certified without archived documents and access rules.

## Fresh investor: January 4, 2016 to October 21, 2026

This starts a NEW account at the scheduled close, without inheriting
the prior year's overnight return or liquidation. Thus boundary-correct
fresh-account metrics can differ slightly from H-141's original sliced
2016+ continuing-book summary. The full original results were reproduced
before making this presentation change.

| Rule | Annual compounded growth | Largest daily fall from peak | $200 ends | $500 ends | $1,000 ends | $2,000 ends | $10,000 ends |
|---|---:|---:|---:|---:|---:|---:|---:|
| Past return | 15.24% | 39.73% | $924.89 | $2,312.22 | $4,624.43 | $9,248.86 | $46,244.30 |
| Past risk-adjusted return | 13.66% | 39.73% | $796.43 | $1,991.06 | $3,982.13 | $7,964.26 | $39,821.28 |
| Past low volatility | 12.41% | 36.66% | $706.84 | $1,767.09 | $3,534.18 | $7,068.36 | $35,341.81 |
| SPY broad-market comparator | 15.10% | 33.72% | $912.79 | $2,281.98 | $4,563.96 | $9,127.91 | $45,639.55 |

## Was it steady?

Each rule had 17 profitable and 4 losing completed annual holding
periods out of 21 (2005-2025 entries); the incomplete 2026 period
is excluded from that count. Past-return selection lost 37.74%
in the 2008 holding period and 34.85% in the 2022 holding period.
Low-volatility selection still lost 35.14% in 2008, although its
2022 loss was smaller at 13.44%. Those are not steady-gain guarantees.

## All annual decisions, including losing years

Rows are entry-year holding periods, NOT calendar-year returns.
They run from the stated next-close entry to the following annual
execution, or final sample valuation. Each is a fresh standalone
one-period investment; not an annual contribution to the long account.

| Rule | Signal date | Entry to exit | Selected funds | Net return | SPY same dates | Daily drawdown |
|---|---|---|---|---:|---:|---:|
| Past return | 2004-12-31 | 2005-01-03 to 2006-01-03 | FLPSX, DODGX, FCNTX | +14.34% | +6.96% | 7.03% |
| Past return | 2005-12-30 | 2006-01-03 to 2007-01-03 | VSMAX, FLPSX, VIMAX | +13.64% | +13.41% | 11.73% |
| Past return | 2006-12-29 | 2007-01-03 to 2008-01-02 | FLPSX, VIMAX, DODGX | +1.81% | +4.20% | 11.70% |
| Past return | 2007-12-31 | 2008-01-02 to 2009-01-02 | FCNTX, FSCSX, FDGRX | -37.74% | -34.45% | 48.83% |
| Past return | 2008-12-31 | 2009-01-02 to 2010-01-04 | FSCSX, VPMCX, FCNTX | +39.18% | +24.49% | 19.96% |
| Past return | 2009-12-31 | 2010-01-04 to 2011-01-03 | FSCSX, VPMCX, FSPHX | +15.70% | +14.08% | 14.88% |
| Past return | 2010-12-31 | 2011-01-03 to 2012-01-03 | VSMAX, FSCSX, FLPSX | -0.32% | +2.25% | 22.45% |
| Past return | 2011-12-30 | 2012-01-03 to 2013-01-02 | FSCSX, VIMAX, VSMAX | +18.66% | +16.86% | 12.39% |
| Past return | 2012-12-31 | 2013-01-02 to 2014-01-02 | FSPHX, VSMAX, FDGRX | +39.08% | +27.51% | 5.86% |
| Past return | 2013-12-31 | 2014-01-02 to 2015-01-02 | FSPHX, FSCSX, TRBCX | +17.83% | +14.27% | 11.06% |
| Past return | 2014-12-31 | 2015-01-02 to 2016-01-04 | FSPHX, FSCSX, VPMCX | +4.19% | -0.33% | 14.39% |
| Past return | 2015-12-31 | 2016-01-04 to 2017-01-03 | FSPHX, FSCSX, TRBCX | +3.41% | +14.23% | 14.56% |
| Past return | 2016-12-30 | 2017-01-03 to 2018-01-02 | VPMCX, FSCSX, FDGRX | +35.45% | +21.40% | 3.39% |
| Past return | 2017-12-29 | 2018-01-02 to 2019-01-02 | FSCSX, FDGRX, TRBCX | -1.51% | -5.34% | 23.03% |
| Past return | 2018-12-31 | 2019-01-02 to 2020-01-02 | FSCSX, TRBCX, VPMCX | +33.92% | +32.05% | 8.14% |
| Past return | 2019-12-31 | 2020-01-02 to 2021-01-04 | FSCSX, FBGRX, FDGRX | +53.31% | +15.41% | 31.20% |
| Past return | 2020-12-31 | 2021-01-04 to 2022-01-03 | FDGRX, FBGRX, FSCSX | +23.84% | +31.00% | 11.11% |
| Past return | 2021-12-31 | 2022-01-03 to 2023-01-03 | FDGRX, FBGRX, FSCSX | -34.85% | -19.15% | 36.81% |
| Past return | 2022-12-30 | 2023-01-03 to 2024-01-02 | FDGRX, DODGX, FLPSX | +26.14% | +25.75% | 10.40% |
| Past return | 2023-12-29 | 2024-01-02 to 2025-01-02 | DODGX, FLPSX, FXAIX | +15.32% | +25.03% | 6.86% |
| Past return | 2024-12-31 | 2025-01-02 to 2026-01-02 | FCNTX, FBGRX, FDGRX | +21.62% | +17.99% | 23.80% |
| Past return | 2025-12-31 | 2026-01-02 to 2026-10-21 | FBGRX, FDGRX, TRBCX | +14.38% | +13.82% | 12.34% |
| Past risk-adjusted return | 2004-12-31 | 2005-01-03 to 2006-01-03 | FLPSX, FCNTX, DODGX | +14.34% | +6.96% | 7.03% |
| Past risk-adjusted return | 2005-12-30 | 2006-01-03 to 2007-01-03 | FLPSX, FCNTX, VIMAX | +12.10% | +13.41% | 11.39% |
| Past risk-adjusted return | 2006-12-29 | 2007-01-03 to 2008-01-02 | DODGX, FLPSX, VIMAX | +1.81% | +4.20% | 11.70% |
| Past risk-adjusted return | 2007-12-31 | 2008-01-02 to 2009-01-02 | FCNTX, FSCSX, FSPHX | -35.09% | -34.45% | 46.05% |
| Past risk-adjusted return | 2008-12-31 | 2009-01-02 to 2010-01-04 | FSCSX, VPMCX, FCNTX | +39.18% | +24.49% | 19.96% |
| Past risk-adjusted return | 2009-12-31 | 2010-01-04 to 2011-01-03 | FSCSX, VPMCX, FDGRX | +17.00% | +14.08% | 16.31% |
| Past risk-adjusted return | 2010-12-31 | 2011-01-03 to 2012-01-03 | VSMAX, FSCSX, FLPSX | -0.32% | +2.25% | 22.45% |
| Past risk-adjusted return | 2011-12-30 | 2012-01-03 to 2013-01-02 | FSCSX, FSPHX, FLPSX | +20.19% | +16.86% | 10.49% |
| Past risk-adjusted return | 2012-12-31 | 2013-01-02 to 2014-01-02 | FSPHX, FLPSX, FSCSX | +42.70% | +27.51% | 4.28% |
| Past risk-adjusted return | 2013-12-31 | 2014-01-02 to 2015-01-02 | FSPHX, FSCSX, FLPSX | +17.09% | +14.27% | 8.50% |
| Past risk-adjusted return | 2014-12-31 | 2015-01-02 to 2016-01-04 | FSPHX, VPMCX, FLPSX | +1.04% | -0.33% | 13.79% |
| Past risk-adjusted return | 2015-12-31 | 2016-01-04 to 2017-01-03 | FSPHX, VPMCX, FBGRX | +3.29% | +14.23% | 13.99% |
| Past risk-adjusted return | 2016-12-30 | 2017-01-03 to 2018-01-02 | VPMCX, FXAIX, VFIAX | +24.45% | +21.40% | 2.58% |
| Past risk-adjusted return | 2017-12-29 | 2018-01-02 to 2019-01-02 | FSCSX, FDGRX, TRBCX | -1.51% | -5.34% | 23.03% |
| Past risk-adjusted return | 2018-12-31 | 2019-01-02 to 2020-01-02 | FSCSX, VPMCX, TRBCX | +33.92% | +32.05% | 8.14% |
| Past risk-adjusted return | 2019-12-31 | 2020-01-02 to 2021-01-04 | FSCSX, FBGRX, TRBCX | +42.32% | +15.41% | 30.92% |
| Past risk-adjusted return | 2020-12-31 | 2021-01-04 to 2022-01-03 | FDGRX, FBGRX, FSCSX | +23.84% | +31.00% | 11.11% |
| Past risk-adjusted return | 2021-12-31 | 2022-01-03 to 2023-01-03 | FDGRX, FBGRX, FSCSX | -34.85% | -19.15% | 36.81% |
| Past risk-adjusted return | 2022-12-30 | 2023-01-03 to 2024-01-02 | FDGRX, FLPSX, DODGX | +26.14% | +25.75% | 10.40% |
| Past risk-adjusted return | 2023-12-29 | 2024-01-02 to 2025-01-02 | DODGX, FLPSX, FXAIX | +15.32% | +25.03% | 6.86% |
| Past risk-adjusted return | 2024-12-31 | 2025-01-02 to 2026-01-02 | FCNTX, FXAIX, SWPPX | +19.13% | +17.99% | 18.92% |
| Past risk-adjusted return | 2025-12-31 | 2026-01-02 to 2026-10-21 | FCNTX, FDGRX, FBGRX | +18.04% | +13.82% | 11.06% |
| Past low volatility | 2004-12-31 | 2005-01-03 to 2006-01-03 | FCNTX, FLPSX, DODGX | +14.34% | +6.96% | 7.03% |
| Past low volatility | 2005-12-30 | 2006-01-03 to 2007-01-03 | FCNTX, FLPSX, DODGX | +13.70% | +13.41% | 10.17% |
| Past low volatility | 2006-12-29 | 2007-01-03 to 2008-01-02 | DODGX, SWPPX, VFINX | +2.12% | +4.20% | 9.74% |
| Past low volatility | 2007-12-31 | 2008-01-02 to 2009-01-02 | FSPHX, DODGX, SWPPX | -35.14% | -34.45% | 47.70% |
| Past low volatility | 2008-12-31 | 2009-01-02 to 2010-01-04 | FSPHX, FCNTX, FLPSX | +32.25% | +24.49% | 19.34% |
| Past low volatility | 2009-12-31 | 2010-01-04 to 2011-01-03 | FSPHX, FCNTX, FLPSX | +17.49% | +14.08% | 13.19% |
| Past low volatility | 2010-12-31 | 2011-01-03 to 2012-01-03 | FSPHX, FCNTX, FLPSX | +2.54% | +2.25% | 19.02% |
| Past low volatility | 2011-12-30 | 2012-01-03 to 2013-01-02 | FSPHX, FCNTX, FLPSX | +19.47% | +16.86% | 9.06% |
| Past low volatility | 2012-12-31 | 2013-01-02 to 2014-01-02 | FLPSX, FCNTX, FSPHX | +37.43% | +27.51% | 4.98% |
| Past low volatility | 2013-12-31 | 2014-01-02 to 2015-01-02 | FLPSX, FCNTX, SWPPX | +10.62% | +14.27% | 7.22% |
| Past low volatility | 2014-12-31 | 2015-01-02 to 2016-01-04 | FLPSX, SWPPX, VFINX | -0.74% | -0.33% | 11.15% |
| Past low volatility | 2015-12-31 | 2016-01-04 to 2017-01-03 | FLPSX, SWPPX, VFINX | +12.96% | +14.23% | 9.09% |
| Past low volatility | 2016-12-30 | 2017-01-03 to 2018-01-02 | FLPSX, SWPPX, VFINX | +21.22% | +21.40% | 2.01% |
| Past low volatility | 2017-12-29 | 2018-01-02 to 2019-01-02 | FLPSX, SWPPX, VFINX | -7.37% | -5.34% | 18.86% |
| Past low volatility | 2018-12-31 | 2019-01-02 to 2020-01-02 | FLPSX, VFIAX, VFINX | +29.84% | +32.05% | 6.33% |
| Past low volatility | 2019-12-31 | 2020-01-02 to 2021-01-04 | FLPSX, VIMAX, VFINX | +13.01% | +15.41% | 36.66% |
| Past low volatility | 2020-12-31 | 2021-01-04 to 2022-01-03 | FLPSX, FSPHX, FXAIX | +23.11% | +31.00% | 6.35% |
| Past low volatility | 2021-12-31 | 2022-01-03 to 2023-01-03 | FLPSX, FSPHX, FXAIX | -13.44% | -19.15% | 21.33% |
| Past low volatility | 2022-12-30 | 2023-01-03 to 2024-01-02 | FLPSX, FSPHX, FXAIX | +15.54% | +25.75% | 10.45% |
| Past low volatility | 2023-12-29 | 2024-01-02 to 2025-01-02 | FLPSX, FXAIX, VFINX | +19.08% | +25.03% | 8.14% |
| Past low volatility | 2024-12-31 | 2025-01-02 to 2026-01-02 | FLPSX, DODGX, VFINX | +16.04% | +17.99% | 16.36% |
| Past low volatility | 2025-12-31 | 2026-01-02 to 2026-10-21 | DODGX, FLPSX, FXAIX | +11.62% | +13.82% | 8.02% |

## Selected crisis/recent years: actual dollars, not forecasts

Negative profit means a loss. The complete machine-readable companion
also includes every year's trailing selection metrics and five budgets.

| Entry year / rule | Initial | Ending | Profit or loss |
|---|---:|---:|---:|
| 2008 / Past return | $200 | $124.52 | $-75.48 |
| 2008 / Past return | $500 | $311.29 | $-188.71 |
| 2008 / Past return | $1,000 | $622.59 | $-377.41 |
| 2008 / Past return | $2,000 | $1,245.17 | $-754.83 |
| 2008 / Past return | $10,000 | $6,225.85 | $-3,774.15 |
| 2016 / Past return | $200 | $206.83 | $+6.83 |
| 2016 / Past return | $500 | $517.07 | $+17.07 |
| 2016 / Past return | $1,000 | $1,034.14 | $+34.14 |
| 2016 / Past return | $2,000 | $2,068.28 | $+68.28 |
| 2016 / Past return | $10,000 | $10,341.40 | $+341.40 |
| 2020 / Past return | $200 | $306.62 | $+106.62 |
| 2020 / Past return | $500 | $766.54 | $+266.54 |
| 2020 / Past return | $1,000 | $1,533.08 | $+533.08 |
| 2020 / Past return | $2,000 | $3,066.17 | $+1,066.17 |
| 2020 / Past return | $10,000 | $15,330.83 | $+5,330.83 |
| 2022 / Past return | $200 | $130.31 | $-69.69 |
| 2022 / Past return | $500 | $325.76 | $-174.24 |
| 2022 / Past return | $1,000 | $651.53 | $-348.47 |
| 2022 / Past return | $2,000 | $1,303.06 | $-696.94 |
| 2022 / Past return | $10,000 | $6,515.29 | $-3,484.71 |
| 2025 / Past return | $200 | $243.25 | $+43.25 |
| 2025 / Past return | $500 | $608.12 | $+108.12 |
| 2025 / Past return | $1,000 | $1,216.24 | $+216.24 |
| 2025 / Past return | $2,000 | $2,432.48 | $+432.48 |
| 2025 / Past return | $10,000 | $12,162.40 | $+2,162.40 |
| 2026 / Past return | $200 | $228.76 | $+28.76 |
| 2026 / Past return | $500 | $571.90 | $+71.90 |
| 2026 / Past return | $1,000 | $1,143.79 | $+143.79 |
| 2026 / Past return | $2,000 | $2,287.59 | $+287.59 |
| 2026 / Past return | $10,000 | $11,437.94 | $+1,437.94 |
| 2008 / Past risk-adjusted return | $200 | $129.82 | $-70.18 |
| 2008 / Past risk-adjusted return | $500 | $324.54 | $-175.46 |
| 2008 / Past risk-adjusted return | $1,000 | $649.08 | $-350.92 |
| 2008 / Past risk-adjusted return | $2,000 | $1,298.17 | $-701.83 |
| 2008 / Past risk-adjusted return | $10,000 | $6,490.84 | $-3,509.16 |
| 2016 / Past risk-adjusted return | $200 | $206.58 | $+6.58 |
| 2016 / Past risk-adjusted return | $500 | $516.45 | $+16.45 |
| 2016 / Past risk-adjusted return | $1,000 | $1,032.90 | $+32.90 |
| 2016 / Past risk-adjusted return | $2,000 | $2,065.79 | $+65.79 |
| 2016 / Past risk-adjusted return | $10,000 | $10,328.97 | $+328.97 |
| 2020 / Past risk-adjusted return | $200 | $284.64 | $+84.64 |
| 2020 / Past risk-adjusted return | $500 | $711.61 | $+211.61 |
| 2020 / Past risk-adjusted return | $1,000 | $1,423.21 | $+423.21 |
| 2020 / Past risk-adjusted return | $2,000 | $2,846.42 | $+846.42 |
| 2020 / Past risk-adjusted return | $10,000 | $14,232.10 | $+4,232.10 |
| 2022 / Past risk-adjusted return | $200 | $130.31 | $-69.69 |
| 2022 / Past risk-adjusted return | $500 | $325.76 | $-174.24 |
| 2022 / Past risk-adjusted return | $1,000 | $651.53 | $-348.47 |
| 2022 / Past risk-adjusted return | $2,000 | $1,303.06 | $-696.94 |
| 2022 / Past risk-adjusted return | $10,000 | $6,515.29 | $-3,484.71 |
| 2025 / Past risk-adjusted return | $200 | $238.25 | $+38.25 |
| 2025 / Past risk-adjusted return | $500 | $595.63 | $+95.63 |
| 2025 / Past risk-adjusted return | $1,000 | $1,191.27 | $+191.27 |
| 2025 / Past risk-adjusted return | $2,000 | $2,382.53 | $+382.53 |
| 2025 / Past risk-adjusted return | $10,000 | $11,912.66 | $+1,912.66 |
| 2026 / Past risk-adjusted return | $200 | $236.08 | $+36.08 |
| 2026 / Past risk-adjusted return | $500 | $590.21 | $+90.21 |
| 2026 / Past risk-adjusted return | $1,000 | $1,180.42 | $+180.42 |
| 2026 / Past risk-adjusted return | $2,000 | $2,360.83 | $+360.83 |
| 2026 / Past risk-adjusted return | $10,000 | $11,804.16 | $+1,804.16 |
| 2008 / Past low volatility | $200 | $129.72 | $-70.28 |
| 2008 / Past low volatility | $500 | $324.31 | $-175.69 |
| 2008 / Past low volatility | $1,000 | $648.62 | $-351.38 |
| 2008 / Past low volatility | $2,000 | $1,297.24 | $-702.76 |
| 2008 / Past low volatility | $10,000 | $6,486.20 | $-3,513.80 |
| 2016 / Past low volatility | $200 | $225.91 | $+25.91 |
| 2016 / Past low volatility | $500 | $564.78 | $+64.78 |
| 2016 / Past low volatility | $1,000 | $1,129.55 | $+129.55 |
| 2016 / Past low volatility | $2,000 | $2,259.10 | $+259.10 |
| 2016 / Past low volatility | $10,000 | $11,295.51 | $+1,295.51 |
| 2020 / Past low volatility | $200 | $226.02 | $+26.02 |
| 2020 / Past low volatility | $500 | $565.04 | $+65.04 |
| 2020 / Past low volatility | $1,000 | $1,130.09 | $+130.09 |
| 2020 / Past low volatility | $2,000 | $2,260.17 | $+260.17 |
| 2020 / Past low volatility | $10,000 | $11,300.86 | $+1,300.86 |
| 2022 / Past low volatility | $200 | $173.12 | $-26.88 |
| 2022 / Past low volatility | $500 | $432.81 | $-67.19 |
| 2022 / Past low volatility | $1,000 | $865.62 | $-134.38 |
| 2022 / Past low volatility | $2,000 | $1,731.24 | $-268.76 |
| 2022 / Past low volatility | $10,000 | $8,656.20 | $-1,343.80 |
| 2025 / Past low volatility | $200 | $232.08 | $+32.08 |
| 2025 / Past low volatility | $500 | $580.20 | $+80.20 |
| 2025 / Past low volatility | $1,000 | $1,160.40 | $+160.40 |
| 2025 / Past low volatility | $2,000 | $2,320.81 | $+320.81 |
| 2025 / Past low volatility | $10,000 | $11,604.04 | $+1,604.04 |
| 2026 / Past low volatility | $200 | $223.23 | $+23.23 |
| 2026 / Past low volatility | $500 | $558.08 | $+58.08 |
| 2026 / Past low volatility | $1,000 | $1,116.17 | $+116.17 |
| 2026 / Past low volatility | $2,000 | $2,232.34 | $+232.34 |
| 2026 / Past low volatility | $10,000 | $11,161.68 | $+1,161.68 |

## What the results do and do not show

The frozen rules select different kinds of past winners, but selecting
the top three is NOT passing our stricter trustworthy/steady-gains
screen. H-141's descriptive screen required at least ten years,
annualized Sharpe at least 1, maximum daily drawdown at most 20%,
positive benchmark excess in both halves and sufficient positive
three-year excess windows. No fund passed that full screen.
That last statement grades the completed historical study; it is NOT
a future-informed screen used to decide the earlier annual holdings.

All nine original fund/ETF/combined selector trials failed to prove
selection skill. The best risk-adjusted random-selection percentile
was 31, below 95. Every paired annual-excess 95% uncertainty interval
had a lower bound below zero. These unchanged results are not
rescued by displaying attractive dollar growth.

**Our call:** evidence certainty E3 for reproduced historical dollars;
excess-return signal S0 for the frozen selectors; no prospective
signal confirmation. Historical active survivors remain diligence
leads, not a reliable recipe for strong and steady gains.

## Patterns worth understanding, without pretending they predict

1. Large gains can come with growth/sector concentration and severe
   falls. Current historical champions are not low-risk secrets.
2. Low past volatility is not a guarantee against a future crash.
3. A fund can beat the market over decades without winning every year.
4. Fees matter most in comparable exposures; a cost advantage is not
   proof of manager skill or a guaranteed positive total return.
5. Minimums and fixed costs matter more for small accounts. For
   illustration ONLY, three $9.95 purchases plus three $9.95 sales
   cost $59.70: 29.85% of $200, 11.94% of $500, 5.97% of $1,000,
   2.985% of $2,000 or 0.597% of $10,000 before price changes.
   This is NOT an asserted mutual-fund tariff or a cost in the tables.

## How we would evaluate trustworthiness separately

Match the exact fund/share class, stated mandate, appropriate market/
style benchmark, distribution-adjusted performance, document dates,
fees and actual access. Compare both good and bad periods, changing
managers, closures and dead-fund controls. Then test a frozen selector
on new data. A clearly run fund can be trustworthy without delivering
steady gains; a high CAGR alone cannot establish either property.

## Verification and reproducibility

- Past-only/future-perturbation checks passed: 66.
- Reproduced nine original metric values across three mutual-fund
  trials (compound growth, annual growth, daily drawdown).
- Frozen protocol SHA-256: `1c90e1045c72b5d7bf58dfb7bb8d8e6c0f2b414bc7585ce1332622246bc31c24`.
- SHA-256 means Secure Hash Algorithm, 256-bit; it detects changed inputs.
- Every cached input was checked against the original manifest.
- No new market-data request, parameter search or hypothesis was run.
- Companion code takes the original research root, cache and results
  as arguments; JSON includes input/engine hashes and all 66 decisions.

Terminology: CAGR = compound annual growth rate; MDD = maximum
drawdown; ETF = exchange-traded fund; ELI5 = explain like I am five;
USD = US dollars; SPY = SPDR S&P 500 ETF Trust; S&P = Standard & Poor's.
Tickers are fund identifiers, not independent funds when share classes
refer to the same portfolio. Full fund universe and protocol:
[H-141 research](https://github.com/eltonaguiar/findtorontoevents_antigravity.ca/blob/research/ghcopilot-symbol-durability/reports/symbol_durability_protocol_2026-10-23.json).

## Selected fund identities

| Ticker | Fund name / vehicle |
|---|---|
| DODGX | Dodge & Cox Stock Fund |
| FBGRX | Fidelity Blue Chip Growth Fund |
| FCNTX | Fidelity Contrafund |
| FDGRX | Fidelity Growth Company Fund |
| FLPSX | Fidelity Low-Priced Stock Fund |
| FSCSX | Fidelity Select Software and Information Technology Services Portfolio |
| FSPHX | Fidelity Select Health Care Portfolio |
| FXAIX | Fidelity 500 Index Fund |
| SWPPX | Schwab S&P 500 Index Fund |
| TRBCX | T. Rowe Price Blue Chip Growth Fund |
| VFIAX | Vanguard 500 Index Fund Admiral Shares |
| VFINX | Vanguard 500 Index Fund Investor Shares |
| VIMAX | Vanguard Mid-Cap Index Fund Admiral Shares |
| VPMCX | Vanguard PRIMECAP Fund Investor Shares |
| VSMAX | Vanguard Small-Cap Index Fund Admiral Shares |
