# ZOOCODE — FINAL CHECK + RANKED TOP PICKS (2026-10-24, consensus-compiled)

**Author:** Zoo / ZooCode
**Date:** 2026-10-24 08:06 UTC
**Status:** One-last-check after reading final peer reports (Grok `GROK_FINAL_20261024_0045.MD` Top-10, Buffy `BUFFY_20261023_FINAL_ASSET_DECISION_LIST.MD`, OpenCode round-3 `OPENCODE_BEAM_20261023_1903Z_ROUND3_CROSSCHECK.MD`, Grok findings index). Reconciles against my round-2 report (`1abe662`).
**Disclaimer:** Not financial advice. Research/educational only. No strategy is MONEY-READY; rankings below are for VEHICLES (funds/ETFs), never alpha.

---

## 0. One-last-check verdict (convergent)

All agents now converge on the same three facts, so my findings hold:

1. **0 MONEY-READY strategies** in any class. Every strategy fails at least one gate (artifact, n<100, CI-LB<1.2, DSR<0.95, MDD>20%, survivorship, single-source).
2. **The only demonstrated "edge" is fee/cost** (Zoo trait composite: cost ρ = −0.38; OpenCode 118-fund / Grok 129-fund / GHCopilot H-141: zero selection rules beat the cheapest broad index).
3. **Only index vehicles earn a purchase-worthy (vehicle) rating** — as low-fee market exposure, not as a predictive edge.
4. The `/audit` live roster fails: MomentumEMA is an artifact (single `closed_at` batch; horizon-capped PF ≈ 1.07); XLF decays (later-half PF ≈ 0.94, source mismatch); 0/31 strategies with 20+ closes pass.

---

## 1. Ranked top picks (VEHICLES only — these are the highest-evidence options, not buy orders)

Ranking rule (consensus): gates passed → evidence grade → risk-adjusted return vs matched benchmark → cost → Canadian access.

### Core (broad index, buy-now-for-exposure)
| Rank | Option | Fee | Role | Key evidence |
|---|---|---|---|---|
| 1 | **XEQT** | 0.20% | Global equity, one ticker, CAD, RRSP/TFSA/FHSA | Cheapest broad global; no timing claim; 10y-window CAGR 14.8% (2019-08+). Default winner. |
| 2 | **VFV / XUS** | 0.09%/0.10% | Cheapest S&P 500 in CAD | Gap to index = fee (say-vs-do confirmed). Single-country (US) lowers rank below XEQT. |
| 3 | **XGRO / XBAL** | 0.20%/0.19% | 80/20 and 60/40 one-ticker mixes | Auto-rebalanced; lower MDD (−16.4%/−15.2%); pick by risk tolerance. |
| 4 | **VEQT / VGRO / VBAL** | 0.24% | Vanguard twins | Same role, slightly higher MER + more Canada weight. |
| 5 | **VOO / IVV / BKLC** | 0.03%/0.03%/0.00% | USD S&P 500 (BKLC 0.00% verified) | Only if you hold USD; FX cost; RRSP avoids US withholding. |

### Sleeves (buy for role, sized deliberately)
| Rank | Option | Fee | Role | Key evidence |
|---|---|---|---|---|
| 6 | **SHY** (1–3y Treasuries) | 0.15% | Lowest-drawdown parking spot | 10y SD 1.6%, MDD −5.4%; stability, not growth; USD/FX risk for CAD. |
| 7 | **ZAG / AGG** broad bonds | 0.09%/− | Defensive bond sleeve | CAD/USD; real 2022 bond drawdown risk; role tool, not tactical winner. |
| 8 | **GLD / IAU** | 0.40%/0.25% | Gold diversifier sleeve | CAGR 12.2% (2016-10+), MDD −23.8% monthly; unhedged, saturates fixed-income role. |

### Canadian index mutual funds (for no-broker / auto-buy access)
| Rank | Option | Fee | Role | Key evidence |
|---|---|---|---|---|
| 9 | **TDB902** TD US Index e-Series | 0.28% | US index, $100 start, no subsequent min, $25 PAC optional | Issuer-reported 10y 15.1% (to May 2026); 17.08% was a VFV proxy — HOLD on performance leg; TD channel only. |
| 10 | **TDB900** TD Canadian Index e-Series | ~0.20% | Canadian index | XIC proxy CAGR 12.2%, MDD −22.5%; home-country concentration. |

### NOT ranked / avoid (these are the reasons the "winner" hunt is empty)
- **Active mutual funds (RBF460, MAW104, Fidelity B, Dynamic A, Beutel, FCNTX/FOCPX/VPMCX):** all FAIL — MER 0.91–2.5% vs 0.19% for the same exposure; no selection edge; most not buyable/CA.
- **US zero-fee funds (FXAIX/FZROX/FNILX):** FAIL for Canadian accounts — not buyable at RBC/CAD.
- **Strategies (12-1 momentum, sector top-3, GEM dual momentum, BTC/ETH trend, forex, prediction markets):** all FAIL — DSR<0.95, survivorship, MDD>20%, or n<100/artifact. Best strategy (12-1 momentum, CAGR 14.5%) fails the DSR gate at N=65 and uses today's survivors.
- **/audit live picks:** 0 of 31 qualify; MomentumEMA = artifact; XLF decays.

---

## 2. What "ranked" means here (honest caveat)

These are the **highest-evidence vehicles we could find**, ranked by evidence grade + cost + access. None is MONEY-READY in the predictive sense. Buying XEQT is choosing a low-fee vehicle for market exposure — not a forecast. The 0-alpha conclusion is the core finding: **there is no certified winning strategy, only a winning cost structure.**

## 3. Verification & reproducibility

- `GROK_FINAL_20261024_0045.MD`, `BUFFY_20261023_FINAL_ASSET_DECISION_LIST.MD`, `OPENCODE_BEAM_20261023_1903Z_ROUND3_CROSSCHECK.MD`, `GROK_FINDINGS_INDEX_20261023_1625.MD` (COMMUNITY origin/main @ `17d02fb`).
- My round-2: `ZOOCODE_20261023_ROUND2_RECHECK_PEER_REVIEW.MD` (`1abe662`).
- Live payload: `dashboard_payload.json` (17:11:40 UTC, 10-23).

## 4. Disclaimer

Not financial advice. Nothing here is money-ready. Consult a licensed advisor. Past performance ≠ future results.
