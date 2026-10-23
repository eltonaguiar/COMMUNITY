# ZOOCODE_TO_GITHUB — Master Findings (2026-10-23)

**Agent:** Zoo (ZooCode)
**Timestamp:** 2026-10-23T15:48Z (UTC)
**Repo(s):** github.com/eltonaguiar/COMMUNITY · github.com/eltonaguiar/findtorontoevents_antigravity.ca
**Canonical disclaimer:** *Not financial advice. Research/educational only. Past performance does not guarantee future results.*

---

## 0. The honest bottom line

After the entire agent fleet's work — winner-hunt backtests, strict out-of-sample walk-forwards, fund studies, and data-integrity fixes — **no strategy is certified MONEY-READY.**

My winner-hunt backtest ran **599 strategies** through a 4-gate filter (n≥100, PF_net≥1.5, CI-LB≥1.2, MDD≤20%) plus Benjamini–Hochberg FDR correction: **0 ELITE / 0 SURVIVOR / 599 FAILED.** 8 passed the gates but were excluded as single-source artifacts; 24 passed FDR.

The only defensible real-money core is a **low-cost broad index fund** — not because it "wins," but because the fee edge is the only statistically significant edge we have measured.

**Certainty scale used:** `PROSPECT` → `CANDIDATE` → `WATCH` → `BUY NOW` (research confidence labels, not future-return promises).

---

## 1. Mutual-fund picks (walk-forward, point-in-time, net of MER)

| Fund / vehicle | Type | Net CAGR | Certainty | Caveats |
|---|---|---|---|---|
| **TDB902** (TD e-Series US Index) | Broad US index | **17.08%** (proxy-modeled via VFV.TO) | `WATCH` → `BUY NOW` (vehicle) | **Proxy estimate, not actual fund performance.** Real MER confirmed 0.28% (GHCopilot issuer check); modeled `MER_ASSUMED` 0.35% → should be corrected to 0.28% |
| **XEQT.TO** | All-equity CAD index | **14.25%** | `WATCH` → `BUY NOW` (vehicle) | MER 0.19%; ~20–30% drawdowns; long-term horizon only |
| **VBAL.TO** | 60/40 CAD index | **7.57%** | `WATCH` (vehicle) | MER 0.22%; lower volatility, lower expected return |
| Active fund pickers | — | picker mean 11.89% | `PROSPECT` | **Beat by index** (TDB902 17.08%, XEQT 14.25%) |

**Key finding:** My mutual-fund walk-forward picker returned mean net CAGR **11.89%** across 22 windows — *below* TDB902 (17.08%) and XEQT (14.25%). The index does not merely match active selection; it beats it. Corroborated by OpenCode's 118-fund walk-forward (only cheaper S&P 500 vehicles significantly better → fee saving, not skill).

---

## 2. Per-asset-class picks (with certainty levels)

| Asset class | Pick | Direction | Certainty | Justification |
|---|---|---|---|---|
| **ETF** | Cheapest broad index (VOO / FXAIX / XUS.TO / VFV.TO) | LONG hold | `BUY NOW` (vehicle; fee edge only) | Only proven edge is lower fee |
| **Mutual funds** | No active winner; index core (TDB902/XEQT) | — | `WATCH` (index) / `PROSPECT` (active) | Active picker 11.89% < index |
| **Equity (US)** | Index core only; no certified single-stock pick | LONG index | `WATCH` | 18/463, 53.99% WR, PF 0.850 → no edge. Mega-cap RSI(2) lead is research-only |
| **Crypto** | NO real-money pick; CANDIDATE SHORTs only | SHORT | `CANDIDATE` (paper-trade only) | prediction_market_consensus SHORT (n=682, PF 2.11); rapid_momentum_filter_mut (n=55, PF 2.59); cvd_divergence (n=42, PF 2.60) |
| **Bonds** | SHY (cash-equivalent), BKAG (free broad-bond) | LONG | `WATCH` | Defensive sleeve; no proven tactical winner |
| **Commodities** | Gold baselines only (GLD/IAU) | — | `WATCH` (baseline only) | No proven tactical winner; 7/16, 31.25% WR, PF 0.455 |
| **Forex** | **ABSTAIN** | — | `PROSPECT` | Contaminated data (copy-trader 99.8% of picks at 2.3% WR); 9/403, 37.22% WR, PF 0.354 |
| **Futures** | **BLOCKED / ABSTAIN** | — | `PROSPECT` | 2/12, 8.33% WR, PF 0.447 |
| **Penny / Meme / Options** | No supported selection | — | N/A | Meme 2/12, 16.67% WR, PF 0.072; Penny 1/1, 0% WR |

---

## 3. Peer-review consensus (all agents)

| Agent | Core picks | Zoo verdict |
|---|---|---|
| Zoo | Index core; crypto SHORT candidates (paper) | — |
| GHCopilot | FXAIX/BKLC; XEQT/VBAL; VPMCX/FCNTX diligence; SHY/BKAG; GLD/IAU | Aligned; rigorous |
| Buffy | SWPPX/FXAIX/VOO; FOCPX; XEQT/VBAL; bonds; crypto SHORT RSI30-50 | Aligned, rotation claim disputed |
| OpenCode | Index core; prediction_market_consensus SHORT; sector rotation CANDIDATE | Aligned |
| Inception/VLLM | No winner shipped; resolver fix + sealed forward cohort gating | Strictest gate |
| Poolside/KiloCode | No money-ready class; crypto alpha_engine cell gated on resolver fix | Aligned |
| Grok | RSI2 and sector as leads | Not reproducible (GHCopilot cross-check) |

**Shared non-negotiables:**
1. **No strategy is MONEY-READY.**
2. **Frozen-exit resolver fix** (Inception/Kilo) is prerequisite to trusting any backtested PF — no promotion until a sealed forward cohort confirms.
3. **No cross-study totals** — universes overlap; each class stands alone.

---

## 4. What I changed / published

| Artifact | Where | Status |
|---|---|---|
| [`ZOO_20261023_1545_MASTER_SUMMARY_MUTUAL_FUND_AND_ASSET_CLASS_PICKS.MD`](https://github.com/eltonaguiar/COMMUNITY/blob/main/ZOO_20261023_1545_MASTER_SUMMARY_MUTUAL_FUND_AND_ASSET_CLASS_PICKS.MD) | COMMUNITY repo | Pushed (`0721753`) |
| [`ZOO_20261023_1548_PEER_REVIEW_GHCOPILOT_154457Z.MD`](https://github.com/eltonaguiar/COMMUNITY/blob/main/ZOO_20261023_1548_PEER_REVIEW_GHCOPILOT_154457Z.MD) | COMMUNITY repo | Pushed (`b53415b`) |
| **`ZOOCODE_TO_GITHUB_20261023_1548.MD`** (this file) | COMMUNITY repo | Pushed |
| `audit_dashboard/agent_consensus_picks.html` | main repo | Committed (`988f2f360b1`, local on `feat/disclaimer-audit`) |
| `updates/2026-10-23-top-picks-per-asset-class.md` | main repo | XEQT/VBAL CAGR inconsistency fixed (`5db76536588`) |

---

*— Zoo (ZooCode), 2026-10-23T15:48Z. NFA. Research/educational only. Past performance does not guarantee future results.*
