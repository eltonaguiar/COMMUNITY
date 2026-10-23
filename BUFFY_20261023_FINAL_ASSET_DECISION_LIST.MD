# BUFFY — FINALIZED ASSET DECISION LIST (all agents, all asset classes, including mutual funds)

**Author:** Buffy (Freebuff)
**Compiled:** 2026-10-23, after reviewing: Grok `top_picks_per_asset_class_verified` + 0406 HIGHSUMMARY + 1455 recheck, OpenCode master summary + round-3 cross-check (1903Z), GHCopilot master summary, ZooCode round-2 recheck + winner-evaluation, Kilo fund verdicts + 1636 peer cross-check, Inception/vLLM review, plus a fresh live payload pull (`dashboard_payload.json` generated **2026-10-23 18:59 UTC**: 15 active picks, every class `sizing_allowed=false`, headline book WR 43.7%, PF 1.02).
**Status:** Consensus compilation — **0 MONEY-READY strategies anywhere; purchase-worthiness below is for VEHICLES (funds/ETFs), never for alpha.**
**Disclaimer:** Not financial advice. Research/education only. Not a recommendation to buy or sell. Past performance ≠ future results. DYOR.

## Rating scale

- 🟢 **BUY-CORE** — purchase-worthy now as a portfolio core (cheap, accessible, promise-kept vehicle)
- 🟠 **BUY-SLEEVE** — purchase-worthy only for a stated role (defensive/inflation/tilt), sized deliberately
- 🟡 **PAPER / WATCH** — not money-worthy: needs the 9-gate protocol + sealed forward cohort
- 🔴 **AVOID** — fails our bar (cost, evidence, or both)
- ⛔ **NOT BUYABLE (CA/RBC)** — access fails regardless of merit

---

## 1. Equity — broad index (ETFs)

| Asset | Fee | Access | Rating | Why |
|---|---|---|---|---|
| **XEQT** | MER 0.19% | RBC DI free list, ~$45, TFSA/RRSP/FHSA OK | 🟢 **BUY-CORE** | Default winner: cheapest global equity, no timing claim to prove |
| **XGRO / XBAL** | 0.19% / 0.18% | RBC DI free list | 🟢 🟠 | Same vehicle, 80/20 and 60/40 risk mixes — pick by risk tolerance, not performance |
| **VFV / XUS** | 0.09% / 0.07% | CAD; VFV $9.95 at RBC (not free list), ~$190/share | 🟢 **BUY-CORE (US sleeve)** | Cheapest S&P 500 in CAD; the only statistically significant "edge" found anywhere = fee delta |
| **VEQT / VGRO / VBAL** | 0.22% | $9.95/trade unless GoSmart free | 🟠 | Equivalent role, slightly higher MER + commission friction |
| **VOO / IVV / BKLC** | 0.03% / 0.03% / **0.00%** | USD; IVV on RBC free list; FX conversion applies | 🟠 | If you hold USD; BKLC verified 0.00% by issuer (GHCopilot) but starts Apr-2020 and lagged SPY on matched window |
| **FXAIX / FZROX / FNILX / FZILX** | 0.015% / 0.00% | US mutual funds | ⛔ | **Cannot be bought at RBC in CAD** (Zoo/OpenCode/Buffy verified; Kilo lesson adopted) |

**Reasons (evidence):** 129-fund (Grok), 118-fund (OpenCode, 2005–2024 WF, 4,000-run bootstrap) and 95-fund/9-rule (GHCopilot H-141, preregistered) selection tests — **zero rules beat the cheapest broad index**; best rule hit the 31st random percentile vs 95 required. Zoo trait composite: only **cost** predicts anything (ρ = −0.38). My case study: every rule loses to SPY at every capital ($200 cheapest-3 = **×0.95 over 18y vs SPY ×5.40**).
**Agent feedback:** GHCopilot "FXAIX or BKLC baseline, no alpha claimed" · OpenCode "fee edge is the only proven edge" · Grok "the benchmark nothing beat" · Zoo "index core, vehicle only" · Kilo "index funds = the only reliable BUY grade" · Inception endorses verbatim.

## 2. Mutual funds — Canadian

| Asset | Fee / min | Rating | Why |
|---|---|---|---|
| **TD e-Series TDB900 (CDN idx)** | ~0.22%, $100 **initial** min, **no subsequent minimum**, $25 PAC optional, fractional, auto-reinvest | 🟠 | Cheap passive access where ETFs aren't practical; **not available at RBC DI** (TD channel only) |
| **TD e-Series TDB902 (US idx)** | 0.28%, $100 initial, no subsequent min | 🟠 **vehicle facts only** | Its "17.08% CAGR" is a **VFV proxy window (2012+)**, not the fund's record (own ~15.1%) — performance leg = HOLD (OpenCode §2.5) |
| **RBC Select Balanced RBF460** | **1.94%**, $500 min; $25 = optional PAC (corrected) | 🔴 | MER alone ≈ 10× XEQT; no selection evidence justifies it |
| **Mawer MAW104** | 0.91%, $500 | 🔴 (small acct) | Decent shop, but fee > anything we measured |
| **Fidelity Canada B / Dynamic A** | ~2.0–2.5%, $500 | 🔴 | Loads + MER |
| **Beutel Goodman D** | ~1.4%, **$5,000 min** | 🔴 | Minimum blocks $1–2k accounts (Grok barrier table) |

**Reasons:** Kilo's own walk-forward: historical metrics do NOT predict future returns (Sharpe-3y forward r = −0.22, p = 0.234); only 32% beat category median at 1y. Grok's trait walk-forward: composite **trails benchmark at every horizon (−5.8%/yr)**.
**Agent feedback:** Kilo "index = only reliable BUY; my analysis was directionally right but missing rigor" (1636) · Zoo "cost is the only trait with predictive value" · OpenCode "RBF460 PAC correction accepted" · GHCopilot "TDB902 document-level ≠ history replication".

## 3. Mutual funds — US active (diligence only)

| Asset | Evidence | Rating | Why |
|---|---|---|---|
| **FOCPX** | +2.2–2.9pp/yr vs VIGAX style-adjusted; 1 of 71 funds; no FDR correction | 🟡 watch / ⛔ CA | Selection-biased, not RBC-buyable; Grok labels **FAIL for Canadian accounts** |
| **VPMCX (PRIMECAP)** | 13.70% vs SPY 11.21% (1995–2026); FF5+MOM α 3.17%/yr, t 2.91, Bonferroni p 0.047; MDD **52.6%** | 🟡 **only fund-skill CANDIDATE** / ⛔ CA | Passes multiple-testing barely; survivor-picked, deep MDD, not at RBC, may be closed to new money |
| **FCNTX** | 13.52% vs SPY 11.21%; MDD 49.2%; beats SPY both halves | 🟡 diligence / ⛔ CA | GHCopilot's #2 diligence item; survivor + access fail |
| **FSCSX / FDGRX** | 15.4%/14.9% headlines; MDD **64.7% / 71.6%**; lag 2020+ | 🔴 | Start-date artifacts (2000s tech boom) |
| **FNILX/FZROX (0%)** | free lunch story | ⛔ | US-only |

**Agent feedback:** GHCopilot "FCNTX/VPMCX for active-fund diligence, NOT immediate orders" · OpenCode "MDD✗ access✗ = FAIL (for Canadian accounts)" · Kilo "FOCPX hindsight bias; VPMCX survivorship" · Grok "VPMCX only skill signal, not accessible".

## 4. Bonds / fixed income

| Asset | Evidence | Rating | Why |
|---|---|---|---|
| **SHY** (1–3y T-bonds) | CAGR 1.97%, MDD 5.71% (2002–2026), Sharpe 1.05 | 🟠 **BUY-SLEEVE** (defensive) | Lowest observed drawdown of tested bonds; GHCopilot's top defensive role — **not cash, not guaranteed** |
| **BKAG** (0.00%) | CAGR −0.25% since 2020 vs AGG −0.22% | 🟠 | Free broad bond; "free did not prevent a loss" |
| **AGG / BND / VBTLX** | Sharpe 0.28; MDD −17.3% | 🟠 | Role: ballast only; lost decade 2016–2026 |
| **TIP** | 3.38% / MDD 14.51% since 2003 | 🟠 | Inflation sleeve; can still lose market value |
| **TLT / VUSTX** | 2.4% / MDD −45.3% | 🔴 | Long duration = equity-like swings |

**No bond *strategy* exists:** `/audit BOND n=0` (readiness BLOCKED); `bond_yield_curve_slope` n=18 « 100 → FAIL.
**Agent feedback:** GHCopilot "SHY for lower observed drawdown; BKAG as zero-expense baseline; match duration to horizon, I can't infer yours" · Grok "short Treasuries the only defensive play with decent Sharpe".

## 5. Commodities / gold

| Asset | Evidence | Rating | Why |
|---|---|---|---|
| **GLD / IAU** | CAGR 10.28% / 10.70%, MDD **45.6% / 45.1%** (unequal windows — do not rank) | 🟠 **BUY-SLEEVE ≤5%** | Diversifier, not safe haven; never positive vs SPY in both halves |
| **DBC** | 10.2%/yr, MDD −37.8%, 0.55% fee | 🟡 | Broad basket, expensive, unproven role |
| **USO** | CAGR **−5.79%**, MDD **98.19%** | 🔴 | Structure (contango/roll) destroys value |
| Copper `commodity_term_cot` | claimed n=815 PF 2.29 → one-position n=137 PF **1.21** | 🔴 **FAIL** | Overlapping copies of one bet; stop-first on replay (GHCopilot + Inception) |

`/audit COMMODITY: BLOCKED, n=15, PF 0.50`.

## 6. Crypto

**Decision: 🟡 paper-only, zero real-money allocation.**
- Live readiness: n=20,467, **PF 0.29**, MONITORING, `sizing_allowed=false`.
- Paper candidates (never funded): `prediction_market_consensus` SHORT n=682 PF 2.11 (OpenCode CANDIDATE; Grok re-measure CI [0.68, 1.05] → FAIL), `rapid_momentum_filter_mut` SHORT n=55 PF 2.59, `cvd_divergence` SHORT n=42 PF 2.60, `luxalgo_confluence` SHORT post-cost 1.13.
- **Mine:** CRYPTO SHORT RSI30-50 — n=125, PF 2.16 net, CI-LB 1.69 (3/10 gates pass, **7 NOT RUN**: MDD, MC, DSR, 2×cost, concentration, halves, artifact). Grok's 1625 findings index finalizes it as **FAIL (gates not run)** — same practical outcome as my 🟡 PAPER stance: **not funded either way.** It fails my own CANDIDATE definition.
- Killed claims: BTC momentum (daily MDD **−81.9%**, MC 77th pct, DSR≈0) · `high_trust_momentum` (Oct WR 38.1% decay, CI crosses 0) · alpha_engine cell (n=39 on 9 exit-days = artifact flag) · Kimi/Inception mega_mutation (n=15–96).

## 7. Forex

**Decision: ⛔ abstain (data first).**
- Live readiness: n=418, **PF 0.47**, **BLOCKED**. Copy-trader contaminant (99.8% of rows, 2.3% WR) must be purged; forex feed flagged contaminated (Zoo).
- Watch-list only: `myfxbook_retail_contrarian` n=306 PF ~2.43 (independent source) and `non_crypto_consensus` n=102 PF 1.63 — both CANDIDATE at best; `forex_zscore_200d_fade` PF 1.44 < 1.5 → FAIL.
- Two live pairs (EURGBP/EURJPY, 0.1h old) are too young to judge.

## 8. Individual stocks / stock strategies

**Decision: 🔴 no certified pick; index only for real money.**
- Live readiness EQUITY: n=494, **PF 0.87** (loses $0.87 per $1 won).
- Live board (18:59Z, 15 active): SNDL×2, XLF, ES/YM, QQQ, DOTUSDT etc. — **every one is hours old**; the earlier `STRONG_BUY` labels (20 rows) all carried `intrabar_gate: NO_DATA, db_n: 0` → **dashboard label bug, not signals** (Grok + my round 3–4, payload's own `pro_level_gate` forbids it).
- **XLF** = most-discussed lead: halves 3.07 → **0.94** + lineage mismatch (117 rows `kimi_riseoftheclaw` vs live `ml_gatekeeper`) → **HOLD** (Grok/GHCopilot/OpenCode agree).
- `magic_formula_x_piotroski_x_acquirers` 16-stock cluster: **0 closed record + concentration** → FAIL (Zoo).
- Paper-only stock strategies: Grok 12-1 momentum (CANDIDATE, DSR 0.89 + survivorship), RSI(2) dip-buy (CANDIDATE, DSR 0.43, earns 2.4%/yr), `rs-breakout-scout` (CI-low 1.07, halves 3.07/0.94), AAPL RSI cell (n=1 symbol).

## 9. Rotation / tactical overlays (strategies, not assets)

| Item | Evidence | Rating |
|---|---|---|
| **TAA asset-class rotation** | Sharpe 1.48 vs SPY 1.37 (Grok) but 1.008 in OpenCode's rerun; ~19 monthly obs; DD 16% vs 38% | 🟡 research-validated **product**, paper — insurance, not alpha |
| **Sector top-3 (9 SPDRs)** | CANDIDATE 6/9 gates: MC 63.9 (was 92.6) FAIL, DSR 0.85 FAIL; 9.5% vs same-window SPY 10.0% | 🟡 paper — lower risk, **no return edge** |
| **Boring Billion (FZROX/FZILX mix)** | Claims impossible (FZROX launched 2018, no 2008 record); trails SPY | 🔴 as claimed — concept OK in CAD equivalents (XEQT-style), numbers rejected |

## 10. The /audit live board itself

- **0 of anything qualifies** — convergent across four independent evaluations with different units: my 0/25 Top Picks, Grok's 0/19 active, Zoo's 0/14 strategies, OpenCode's 0/19.
- Fresh pull: **15 active**, headline book WR 43.7%, PF 1.02, compounded total PnL **−38.9%**; **all classes `sizing_allowed=false`**.
- **Horizon effect adopted** (Grok): ≤48h trades PF **0.99** (break-even); >30d PF 1.66 is batch-dependent (ex-batch 0.874 — OpenCode/GHCopilot). No strategy PF leaning on >7-day rows is verified until horizon-capped replay exists.
- Closed book after artifact cleaning: EQUITY PF 0.87, CRYPTO 0.90, FOREX 0.65, COMMODITY 1.03, BOND n=0 → **no class has an edge**.

---

## THE FINAL LIST (what is actually purchase-worthy)

**🟢 BUY-CORE (real money, today):**
1. **XEQT** — global 100% equity core (or **XGRO/XBAL** to match risk tolerance). RBC free list, 0.19%, TFSA/RRSP/FHSA eligible.
2. **VFV or XUS** — cheapest S&P 500 in CAD if you want a US-only core/tilt.

**🟠 BUY-SLEEVE (role-based, sized deliberately):**
3. **SHY** — short-bond defensive sleeve (or BKAG/AGG for broad bonds; TIP for inflation).
4. **GLD/IAU ≤5%** — optional gold diversifier (accept −45% drawdowns).
5. **TD e-Series TDB900/TDB902** — only if you're at TD with small PACs and want fractional fund investing (vehicle facts; TDB902 performance = proxy HOLD).

**🟡 PAPER / WATCH (never funded until 9 gates + sealed forward cohort):** TAA rotation, sector top-3, RSI2 dip-buy, 12-1 momentum, my crypto SHORT RSI30-50, pmc/rapid/cvd crypto shorts, VPMCX/FOCPX/FCNTX diligence, myfxbook FX contrarian, AAPL RSI cell, XLF (HOLD: decay + lineage).

**🔴 AVOID:** RBF460/Mawer/Dynamic/Fidelity-B/Beutel-Goodman active MERs at these account sizes · FSCSX/FDGRX · USO · long-duration TLT as a core · every /audit STRONG_BUY label while `intrabar_gate=NO_DATA` · Boring Billion as claimed (US-only, impossible history).

**⛔ NOT BUYABLE in a Canadian RBC CAD account:** FOCPX, FCNTX, VPMCX, FZROX, FZILX, FNILX, FXAIX, VFINX, IVV/VOO without USD.

**What would change any 🟡 to 🟢/funded:** resolver + horizon-cap fixes merged, artifact-free n≥100, PF-net ≥1.5 with CI-LB ≥1.2, MC ≥95th with real exits, DSR >0.95 with stated family, 2× costs, both halves, then a **sealed timestamped forward cohort** — and, for anything not a fund, Canadian access.

---

## ADDENDUM — accepted after Grok's 1625 findings index (`9d3cba0`, landed during compilation)

1. **TD e-Series minimums corrected:** TD Fund Facts (Jul-2026) says **no subsequent minimum** — my "~$100 subsequent (verify)" was wrong; the $25 PAC is **optional**. My older "$25/month PAP required" claim (RBF460 row) is **retracted** (OpenCode + Grok: optional PAC, not a bill). Tables above carry the corrected values.
2. **Grok's final labels adopted** (3-label policy): CRYPTO SHORT pmc + RSI30-50 = **FAIL** (CI includes <1 / gates not run) · XLF/rs-breakout-scout = **FAIL** (horizon-capped n=89, PF 1.51, second half 0.94) · MomentumEMA = **FAIL (artifact)**. My 🟡 ratings are *stances* (paper/watch), not competing labels — same action: do not fund.
3. **New headline for §10:** with lag ≤7d and batch rows removed, the **entire closed book = PF 1.07 (n=2,916) ≈ break-even** (Grok 1625; batch sensitivity reproduced by GHCopilot + OpenCode).
4. **Grok's 11 action-required dashboard fix prompts** (immutable `closed_at`, horizon cap, null-close rejection, artifact-flag v2, compounded MDD, calendar CAGR, MC-with-real-exits, emitted-vs-tested exits, HYG netting, STRONG_BUY block, CA access gate) — **endorsed, queued for the owner, not implemented without a go-ahead** (production pipeline change per AGENTS rules).

*Consensus across GHCopilot, Grok, OpenCode/Beam, ZooCode, Kilo, Inception/vLLM, Kimi-era notes, and Buffy: **0 MONEY-READY; cost + access is the entire story; index vehicles are the only 🟢.** NFA.*
