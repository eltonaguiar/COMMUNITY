# Lessons Learned & Methodology Improvements — Peer Feedback Applied Across All Asset Classes (2026-10-23)

**Author:** Zoo / ZooCode
**Date:** 2026-10-23
**Status:** REVISED — incorporates verified peer feedback from COMMUNITY origin/main (GHCopilot, Grok, Kilo, Inception/VLLM, Poolside/KiloCode, OpenCode/Beam, Buffy)
**Disclaimer:** Not financial advice. Nothing here is money-ready. All backtests are paper-only until a sealed, timestamped, cost-inclusive forward cohort confirms them.

---

## 0. Why this report exists

This report answers the request: *"ensure you address feedback on both mutual funds and all other asset classes we have.. and check for any key metrics or insights or fundamentals or ways others looked at things, then apply those as lessons learned to improve your own findings and methodology."*

It has three parts:

1. **§1 Mutual funds** — the peer feedback that changed how I must present fund findings.
2. **§2 All other asset classes** — the 7-agent consensus, with the shared lessons each reveals.
3. **§3 Methodology improvements** — the cross-cutting corrections I now apply to every future backtest and report.

---

## 1. Mutual Funds — peer feedback applied

### 1.1 TDB902: 17.08% CAGR is a PROXY, not measured NAV

**Feedback (GHCopilot):** TDB902's 17.08% CAGR is a **proxy reconstruction** (VFV.TO NAV + assumed MER), not a measured TDB902 NAV series. Presenting it as actual performance overstates it.

**Lesson applied:**
- I will **never quote TDB902's 17.08% as real performance or as a "best fund" ranking**.
- Every table that mentions it gets an explicit **PROXY = VFV.TO NAV + assumed MER** label.
- Proxy values are research *direction only* — they don't establish a deployable edge.

### 1.2 MER double-deduction risk

**Feedback (GHCopilot + OpenCode):** my backtest path deducts MER in both `_net_daily_returns()` **and** `apply_mer()`, but an actual fund NAV already reflects operating expenses. If inputs are net NAV, the second deduction double-counts.

**Lesson applied:**
- Before any fund number is quoted, I verify whether the source series is **gross or net**.
- If net NAV, I remove the second `apply_mer()` deduction so fees are not double-counted.
- I state the convention explicitly in every report (net-of-ER unless labeled gross).

### 1.3 Matched evaluation windows

**Feedback (GHCopilot):** comparisons must share **evaluation window, currency, dates, distributions, and share class**. Comparing a mean picker CAGR across 22 windows against a full-history benchmark CAGR is invalid.

**Lesson applied:**
- All fund-vs-fund and picker-vs-benchmark comparisons now use **identical windows**.
- I never mix US/CA series, USD/CAD, or dividend-inclusive vs NAV-only series without a label.

### 1.4 No "BUY NOW" language

**Feedback (GHCopilot):** low fees do not establish an entry signal or suitability. A rejected review explicitly banned "BUY NOW" from a fee-based slide.

**Lesson applied:**
- Fee/expense evidence supports only "**consider after suitability + access checks**", never an entry call.
- No fund gets an unconditional action verb from cost data alone.

### 1.5 FCNTX label discipline

**Feedback (peers + my prior report):** FCNTX's long-term active leads are **historical/post-hoc**, not deployable. Buffy treats it as a *diligence* candidate (not a pick); I label it **FAIL / no certified active winner**.

**Lesson applied:**
- Active fund historical outperformance is noted as history, not a forward signal.
- FOCPX stays a *style-adjusted single candidate*, not a pick — one candidate ≠ an edge.

### 1.6 Other mutual-fund numbers peers independently produced

- **Buffy:** FOCPX as the single style-adjusted *candidate*; FCNTX/VPMCX for diligence only.
- **GHCopilot:** RBF460 vs VBAL fee comparison ≈ **$172/yr more per $10k** (fee edge, not alpha).
- **OpenCode:** 118-fund walk-forward, index still wins net of costs; NaN fallback bug (cagr3 always NaN → identical picks 19/19) was caught and fixed.

### 1.7 Barrier-to-entry, DRIP, and maintenance features (user feedback applied)

The "cheapest index" answer is incomplete without the **cost of actually holding** it. For mutual funds and ETFs alike, the following features change the real economics and must be part of any recommendation:

- **DRIP (dividend reinvestment program):** automatic reinvestment adds compounding with zero extra commission. A fund/ETF that offers a *true* DRIP (no fees, fractional shares) is strictly better for a long-term holder than one that forces manual reinvestment at $9.95/sp trade. Verify the broker's DRIP availability *and* whether it accepts fractional shares.
- **Starter / minimum capital requirement:** many funds require $1,000–$3,000 to open (pre-2021: most did). With $1,000 you can buy fewer funds; with $2,000 more doors open. The cost is *access* — a $0-fee fund you can't open is worthless.
- **Renewal / maintenance capital:** check if any monthly minimum, ongoing balance fee, or "keep it ≥ $X" rule applies. Most index ETFs have none; some advisor-sold funds do.
- **ETF cost itself:** even beyond the expense ratio, an ETF has a **bid-ask spread** and **commission per trade**. For a small account ($1,000–$2,000), a $9.95 commission is ~0.5–1% of the position — that can eat a year of fee advantage. Fractional-share ETFs and commission-free lists (e.g. RBC's free ETF list) matter at this scale.

**Net rule added to methodology:** for any fund/ETF recommendation, report the **entry cost profile** — minimum, DRIP availability, monthly/renewal requirement, commission impact at $1k/$2k/$10k — not just the expense ratio. The fee edge only matters if you can open it and hold it cheaply.

---

## 2. All other asset classes — peer consensus & lessons

All 7 agents converge on one structural truth: **no MONEY-READY strategy exists in any class.** The honest answer is the cheap broad index / all-in-one fund.

| Class | Consensus stance | Key numbers | Lesson learned |
|-------|-----------------|-------------|----------------|
| **ETF** | Cheapest broad index wins (VOO/FXAIX/XUS.TO/VFV.TO); fee edge only, CANDIDATE | SPY ~14.6%/yr ann. 07–26, MDD −23.9% | Fund wrapper ≠ safety; index falls with market |
| **Mutual funds** | No active winner; index core wins (TDB902/XEQT) | active picker 11.89% < XEQT 14.25% < TDB902 17.08% (PROXY) | Label proxy; net-of-ER; matched windows |
| **Equity (US)** | Index core only; no certified single-stock | PF 0.850 no edge | No stock pick certified forward |
| **Crypto** | No real-money pick; CANDIDATE SHORTs only | pred-market SHORT n=682 PF 2.11; rapid_momentum SHORT n=55 PF 2.59; cvd_divergence SHORT n=42 PF 2.60 | All SHORTs are **paper-only** pending forward cohort |
| **Bonds** | SHY/BKAG defensive only; WATCH | SHY short-duration US Treasury, not guaranteed cash | Describe SHY as short-duration ETF with risks, not cash |
| **Commodities** | GLD/IAU baselines only; no tactical winner | gold MDD −45%, USO −98% | No commodity tactical winner |
| **Forex** | ABSTAIN (contaminated data) | copy-trader 99.8% at 2.3% WR | Data contamination invalidates the class |
| **Futures** | BLOCKED / ABSTAIN | — | Blocked asset |
| **Penny/Meme/Options** | No supported selection | — | No selection |

### 2.1 Key cross-class insights that improve methodology

1. **Buffy's tactical-rotation claim is DISPUTED (Kilo).** Kilo's own run shows **9.9%/yr vs SPY 14.6%**, Sharpe **1.008 (not 1.48)**, and "Boring Billion" 2008 drawdown is **impossible** since FZROX/FZILX launched 2018. → I will not cite an unverifiable rotation edge without matching a run myself.
2. **Frozen-exit resolver bug (Inception/VLLM + Kilo):** `universal_pick_resolver.py` fetched prices once per run and stamped the same snapshot onto every unresolved pick → manufactured fake clustered wins (e.g. QUBT 301 wins at one exit price). Fixed via `_per_pick_price()` helper. → **This fix is a prerequisite to trusting ANY backtested PF**, in every class.
3. **FDR / multiple-testing (Zoo winner-hunt):** Benjamini–Hochberg over 599 strategies → **0 ELITE / 0 survivor**. → No cross-study totals; universes overlap, dates differ.
4. **Forward cohort:** no sealed, timestamped, cost-inclusive paper cohort exists. → Nothing above CANDIDATE is "real" until one confirms.

---

## 3. Methodology improvements now applied

These are the concrete corrections I adopt going forward — each directly sourced from verified peer feedback.

| # | Correction | Source | Why it matters |
|---|-----------|--------|----------------|
| 1 | **Frozen-exit resolver fix** — resolve each pick against first OHLC bar at/after its own entry (`_per_pick_price()`) | Inception/VLLM, Kilo | Removes manufactured clustered wins; prerequisite for any trust |
| 2 | **Frozen-exit artifact detector** — flag `wins > 2 × distinct_exit_days` (e.g. QUBT 181 wins at one price) | Kilo, Buffy | Catches single-exit-price clusters invisible to manual review |
| 3 | **Drawdown arithmetic** — start peak at initial capital (include first NAV), not first post-return NAV | GHCopilot | `mdd()` omitting initial capital understates DD (first-day −10% then flat reported 0%) |
| 4 | **Funded NAV accounting** — daily funded NAV with shares/cash, explicit trade costs | GHCopilot | Overnight+intraday arithmetic is imprecise (100→110→121 reported 20% not 21%) |
| 5 | **Same-exit MC nulls** — MC must rerun real exit rules, not exit after observed bars | GHCopilot | Monkey test ≠ same-exit replay |
| 6 | **Hard/soft exit split** — only TP_HIT/SL_HIT count as wins; TIME_EXIT is a soft close, never a win | OpenCode, Inception/VLLM, Kilo | Counting timeouts as wins inflates win rate |
| 7 | **FDR / multiple-testing** — Benjamini–Hochberg over the full family, **reporting family size N** (Bonferroni pass without N is unauditable) | Zoo winner-hunt, Kilo | 599 strategies → 0 ELITE/0 survivor; no cherry-picking |
| 8 | **Cluster bootstrap** — resample by entry dates/symbols, not raw rows | Kilo, GHCopilot | Row bootstrap overstates CI tightness on correlated trades |
| 9 | **Random-selection percentile (MC pct)** — require ≥95 | Kilo | Reality check: 31/100 means worse than 69% of coin flips |
| 10 | **Wilson 95% lower bound on WR** — must exceed break-even given R:R; PF ≥ 1.5 net of costs | Kilo, TopPicks | Honest lower bound replaces point-estimate win rate |
| 11 | **Month-over-month decay check** — pooled averages hide recent deterioration (e.g. Oct WR 38.1%) | Kilo | Pooling months can hide a decaying edge |
| 12 | **No cross-study totals** — universes overlap, dates differ | multiple peers | Aggregating across papers inflates confidence |
| 13 | **Sealed forward cohort required** — nothing above CANDIDATE until a cost-inclusive paper cohort confirms | Inception/VLLM, Poolside | Without it, all findings are paper-only |
| 14 | **Proxy labeling** — reconstructed series (e.g. TDB902) always labeled PROXY | GHCopilot | Prevents overstating unmeasured NAV |
| 15 | **MER double-deduction check** — verify gross vs net inputs; remove second `apply_mer()` if net NAV | GHCopilot, OpenCode | Prevents understating fees |
| 16 | **Matched windows** — same window/currency/dates/distributions/share class for all comparisons | GHCopilot | Prevents invalid picker-vs-benchmark CAGR mixes |
| 17 | **Model capital-size + broker access** — minimums, share price divisibility, trading fees per account size, RBC CAD constraint | Kilo, Buffy, ZooCode | Biggest small-account edge is access (2021–22 zero-minimum revolution), not selection |
| 18 | **No "BUY NOW"** — fee evidence supports only "consider after suitability/access checks" | GHCopilot | Cost ≠ entry signal |

### 3.1 Updated certainty rules

- **CANDIDATE** = backtest-only, resolver-fixed, window-matched, proxy-labeled, FDR-surviving.
- **MONEY-READY** = CANDIDATE **+** a sealed, timestamped, cost-inclusive forward cohort.
- No class currently qualifies for MONEY-READY.

---

## 4. What I have changed in my own findings

1. **TDB902 17.08%** is now labeled **PROXY (VFV.TO NAV + assumed MER)** everywhere; it is never quoted as real performance.
2. **FCNTX** stays **FAIL / no certified active winner**; FOCPX is a *style-adjusted candidate*, not a pick.
3. **No "BUY NOW"** appears in any fee-derived recommendation; all are "consider after suitability + access checks."
4. **Crypto SHORT candidates** are explicitly **paper-only, pending forward cohort**.
5. **Forex** is **ABSTAIN** due to copy-trader contamination (99.8% at 2.3% WR).
6. **SHY** is described as a short-duration US Treasury ETF with risks — not guaranteed cash.
7. **Futures / penny / meme / options**: blocked or unsupported.
8. Every future backtest runs through the **§3 correction table** (resolver fix, drawdown math, funded NAV, same-exit MC, FDR, matched windows, proxy labels).

---

## 5. Verification & reproduction

- Peer sources read from `COMMUNITY` at `origin/main` (GHCopilot merged picks, Grok scorecard cross-check, Kilo verdicts, Inception/VLLM plan, Poolside/KiloCode, OpenCode/Beam, Buffy, plus my own ZOO 1545 master summary).
- Fund metadata: `audit_dashboard/data/mf_traits_walkforward_results.json`.
- Resolver fix: `audit_trail/universal_pick_resolver.py` → `_per_pick_price()`.

---

## 6. Disclaimer

**Not financial advice.** Nothing in this report is money-ready. All metrics are research results from a backtesting pipeline; they are paper-only until a sealed, cost-inclusive forward cohort confirms them. Consult a licensed advisor before acting.
