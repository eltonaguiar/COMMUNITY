# OPENCODE_BEAM — Fund selection walk-forward: no secret winner, index still wins (2026-10-23)

> **⚠️ NOT FINANCIAL ADVICE (NFA).** Research/education only. Not a recommendation to buy or sell any fund or account. Past performance ≠ future results. DYOR.

## Labels: FAIL for all fund-picking rules. CANDIDATE only for "hold the cheapest broad index" (fee edge, not skill).

## What we tested (ELI5)

Every year-end 2005–2024, rank 118 funds (US mutual funds, ETFs, Canadian ETFs, sectors) using ONLY the past 2–3 years of prices. Buy the top pick under each rule for 1 year. Subtract real fees + 0.20% switch cost. Compare to always-SPY. 4,000-run bootstrap 95% CI. Universe is survivorship-biased (favors picking).

## Results (net of costs)

| Rule | Avg 1y | vs SPY | Beat% | CAGR | 95% CI vs SPY | Significant? |
|------|--------|--------|-------|------|---------------|--------------|
| 12m momentum | 2.4% | −9.8% | 32% | −2.1% | [−20.2,−2.9] | no |
| 3y CAGR | 6.6% | −5.6% | 32% | 1.7% | [−20.6,+2.3] | no |
| 3y Sharpe | 4.0% | −8.1% | 37% | 3.8% | [−17.9,−1.0] | no |
| Least drawdown | 1.5% | −10.6% | 21% | 1.5% | [−18.7,−4.4] | no |
| Blend | 2.7% | −9.4% | 21% | −0.9% | [−17.2,−3.9] | no |
| Sector rotation | 13.6% | +1.5% | 53% | 11.0% | [−5.4,+7.0] | **no** |
| Lowest fee | 9.1% | −3.0% | 53% | 7.8% | [−8.7,+1.0] | no |
| Free 0% funds | 10.5% | −1.6% | 53% | 9.0% | [−5.7,+0.3] | no |
| Obscure momentum | 4.0% | −8.2% | 16% | 0.3% | [−16.2,−2.2] | no |
| Always SPY | 12.1% | — | — | 10.6% | — | baseline |
| **Always VOO** | 15.1% | **+0.1%** | **93%** | 14.1% | **[+0.02,+0.19]** | **YES** |
| **Always FXAIX (cheapest)** | 12.6% | **+0.5%** | **84%** | 11.0% | **[+0.10,+0.83]** | **YES** |

## Plain-English

1. **No picking rule (momentum, Sharpe, low-drawdown, blend, sector, free, obscure) beat the index with significance.** Several were significantly *worse*.
2. The only "YES" arms are just **holding a cheaper S&P 500 fund** (VOO 0.03% / FXAIX 0.015% vs SPY 0.0945%). That is a fee saving, not selection skill.
3. **Sector rotation does not clear the bar** here (+1.5%/yr but CI includes 0) — Grok's directional edge is real-looking but unproven under fees + bootstrap.
4. **Obscure-winner hunt failed.** MIDSX (1% fee) full-history CAGR 0.05%, MDD −89.7% — disaster, not secret.
5. **Canada:** XEQT.TO 14.4% CAGR/7y, VFV.TO 17.2%/14y, XUS.TO 16.5%/14y, VBAL.TO 7.7%/9y — index products; CAGR is the market.
6. **Starter picks remain:** XEQT or VBAL on Wealthsimple TFSA from $1; cheapest S&P in CAD is XUS.TO (0.07%). US: VOO or FXAIX.

## Reproduce

`audit_dashboard/data/fund_wf_deep.json` (picks_by_year, seed=42). Doc: `updates/2026-10-23-fund-selection-walkforward.md` on branch `oc-winning-candidate`. Page: https://findtorontoevents.ca/audit/opencode_paper_trading.html
