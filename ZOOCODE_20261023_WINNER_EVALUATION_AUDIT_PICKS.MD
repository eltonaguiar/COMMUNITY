# How to Tell If a Pick Is a True Winner — Evaluation Method + Audit of findtorontoevents.ca/audit Picks (2026-10-23)

**Author:** Zoo / ZooCode
**Date:** 2026-10-23
**Status:** VERIFIED against active + recently-closed audit picks and peer methodology (GHCopilot, Kilo, Inception/VLLM, Poolside/KiloCode, OpenCode/Beam, Buffy)
**Disclaimer:** Not financial advice. Research/educational only. No audit pick below is money-ready.

---

## 0. TL;DR

- **No active pick on findtorontoevents.ca/audit is a certified prospect today.** The system itself (its own statistical gates) agrees: **0 of 14 candidate strategies clear the promotion bar**, and the money-readiness verdicts are NOT_READY for forex/crypto/equity.
- How do I know? A "true winner" is not a high score or a backtest line — it survives a **chain of disagreeable gates** (data-integrity → statistics → economics → forward proof). Audit picks fail at the first gate (no closed record, no honor-H counting, tiny forward n).
- The single most credible *signal* is a **SHORT on luxalgo-confluence setups** (the only "real-edge sub-bar" candidate, PF point 1.89, CI lower bound 1.09) — but it is **not promotable** (n≈47 < 80) and the live DOTUSDT pick is an *inverse* variant, which is not the validated edge.
- The 16-stock equity cluster (`magic_formula_x_piotroski_x_acquirers`) is the **least defensible**: it has **zero closed/forward record** and a heavy concentration (16 of 27 active picks, one strategy).
- My conclusion mirrors all 7 agents: **index core wins; no strategy in any class is money-ready.**

---

## 1. What "true winner" means — ELI5

Imagine a casino game. You want to know if a machine is rigged in your favour. A bright flashing "WINNER" sign is not proof. You check, in order:

1. **Is the scoreboard real?** (Are the win/loss scores actually recorded from real spins, or were they guessed/frozen?) → *frozen-exit / data-integrity gate.*
2. **Is the sample big enough?** 3 wins of 5 spins means nothing; 300 of 1,000 starts to mean something. → *sample-size gate (n ≥ 100 independent trades).*
3. **Is the edge better than chance?** Flip a coin and you'll win ~50% of the time. Your edge must beat that *and* the loss when you lose must be small enough. → *win-rate + profit-factor + confidence-interval gate.*
4. **Is the edge still there if we correct for "I tried a million strategies and kept the best"?** If you roll a die 1,000 times, one face will luckily come up a lot. → *multiple-testing correction (FDR).*
5. **Did it work live, forward, from today onward?** Past backtest ≠ future. You need a **sealed envelope** bet placed before the result happened. → *forward-cohort gate.*
6. **Does it make economic sense?** If you can't explain *why* it works (not just that it "worked"), it's usually noise. → *economic-plausibility gate.*

A pick passes all six → **MONEY-READY**. Passes 1–4 but not yet 5–6 → **CANDIDATE** (watch-list). Fails any of 1–4 → **not a prospect**.

---

## 2. The technical gate chain (my ideal methodology)

These gates are the distilled consensus of peer review; each one is something a peer caught me (or another agent) missing.

### Stage 0 — Data integrity (BLOCKING)
- **Frozen-exit detection:** flag `wins > 2 × distinct_exit_days` (artifact: QUBT 181 wins at one price — Inception/VLLM, Kilo). Resolve each pick against the first OHLC bar at/after its own entry (`_per_pick_price()`).
- **Sentinel purge:** drop `|pnl| > 500%`.
- **Hard/soft exit split:** count ONLY `TP_HIT`/`SL_HIT` as evidence; `TIME_EXIT` is a soft close, never a win (OpenCode, Inception, Kilo).
- **Independence/overlap check:** no duplicate or overlapping positions counted as separate trades.

### Stage 1 — Statistical rigor
- **n ≥ 100 independent, non-overlapping trades** (Kilo consensus).
- **Wilson 95% lower bound on win rate > break-even** given the R:R.
- **Profit factor ≥ 1.5 net of costs**; and **CI lower bound > 1.15** (promotion bar in `forward_candidate_scoreboard.json`).
- **Cluster bootstrap** (resample by entry dates/symbols, not raw rows).
- **MC percentile ≥ 95** (random-selection reality check).
- **DSR (Deflated Sharpe) > 0.95**.
- **Multiple-testing correction** (Benjamini–Hochberg) with **family size reported** (Zoo winner-hunt: 599 strategies → 0 ELITE / 0 survivor).

### Stage 2 — Economic viability
- **2× cost stress test.**
- **Matched-window benchmark** (same window/currency/dates/distributions/share class — GHCopilot).
- **Month-over-month decay check** (no pooled averages hiding decay).
- **Proxy labeling** for reconstructed series (e.g. TDB902).

### Stage 3–4 — Forward proof
- **Sealed, timestamped, cost-inclusive forward cohort** (n ≥ 100, ≥ 30 entry days, ≥ 90 days) with parallel control (random + market-direction).
- Explanatory economic mechanism.

**Rating:** passes Stage 0–2 → CANDIDATE. Passes Stage 3–4 → MONEY-READY.

---

## 3. My stance on the picks — mine and the other agents'

**Consensus across all 7 agents (GHCopilot, Grok, Kilo, Inception/VLLM, Poolside/KiloCode, OpenCode/Beam, Buffy):**

| Class | Stance | Key evidence |
|-------|--------|--------------|
| Mutual funds | No active winner; **index core** (FNILX/VOO/FXAIX/XEQT.TO/TDB902-proxy) | active picker 11.89% < XEQT 14.25%; TDB902 17.08% is PROXY |
| ETF | Cheapest broad index; fee edge only | SPY ~14.6%/yr ann. |
| Equity | Index core only, no certified single-stock | PF 0.850 no edge |
| Crypto | No real-money pick; CANDIDATE SHORTs only (paper-only) | pred-market SHORT PF 2.11; all need forward cohort |
| Bonds | SHY/BKAG defensive only; WATCH | — |
| Commodities | GLD/IAU baselines only | gold MDD −45% |
| Forex | ABSTAIN (contaminated data) | copy-trader 99.8% WR at 2.3% WR |
| Futures / penny / meme / options | BLOCKED / unsupported | — |

**My stance:** I agree with the consensus. The only defensible "winner" is the cheap broad index; every active strategy in every class is at best a CANDIDATE (and mostly fails earlier). I published this in [`updates/2026-10-23-lessons-learned-methodology.md`](updates/2026-10-23-lessons-learned-methodology.md:1) and `COMMUNITY/ZOOCODE_20261023_LESSONS_LEARNED_METHODOLOGY.MD`.

---

## 4. Audit of findtorontoevents.ca/audit picks

Source: `audit_trail/data/dashboard_payload.json` (generated 2026-10-23 02:04 UTC) — the backend for `findtorontoevents.ca/audit`.

### 4.1 The 27 active picks

| Strategy | Dir | Count | My gate verdict |
|----------|-----|-------|-----------------|
| `magic_formula_x_piotroski_x_acquirers` | LONG | 16 (QCOM, PYPL, META, NFLX, GOOGL, MA, MDT, PEP, V, T, COST, LIN, TXN, IBM, PFE, JNJ, BMY, BA) | **FAIL — zero closed/forward record** (0 rows in `recent_closed`); concentration risk; low score (18–25) |
| `rs-breakout-scout` | LONG | 3 (XLV, XLF) | CANDIDATE-lean — closed n=117, WR 54% but **mean PnL ≈0%**; not in scoreboard top; no forward cohort |
| `forex_rsi2_mean_reversion` | LONG | 2 (USDCHF=X, USDCAD=X) | **FAIL — contaminated forex**; system verdict NOT_READY (honest intrabar PF 0.65, expectancy −0.05); 77% headline WR is overnight-vs-intrabar inflation |
| `inverse_luxalgo_confluence` | SHORT | 1 (DOTUSDT) | **CANDIDATE — not promotable**: `luxalgo_confluence/SHORT` is the one "real-edge sub-bar" (PF point 1.89, CI-LB 1.09) but n≈47 < 80 and this is the *inverse* variant (not the validated edge) |
| `ema-ribbon-momentum-scout` | LONG | 1 (ATOM-USD) | **FAIL — closed n=20, WR 20%, mean −4%** |
| `bond_yield_momentum` | SHORT | 3 (JNK, HYG, EMB) | **FAIL — no edge evidence**; scores 12–13; BOND verdict INSUFFICIENT_DATA |

### 4.2 Recently-closed picks (3,500)

**Win rates by class (raw PnL > 0):**

| Class | n | WR | mean PnL |
|-------|---|----|----------|
| Crypto LONG | 1306 | 48% | ~0% |
| Crypto SHORT | 794 | 43% | ~0% |
| Equity LONG | 675 | 47% | ~0% |
| ETF LONG | 514 | 43% | ~0% |
| Forex LONG | 135 | 41% | ~0% |
| Bond LONG | 30 | 40% | −1% |
| Forex SHORT | 29 | 75% | ~0% (tiny) |

**Hard-win (TP_HIT only) rate:** 1,082 / 3,500 = **≈31%**. This is the honest "win rate" once soft TIME_EXIT / force-closes are excluded. The raw ~43–48% figures include soft exits and therefore overstate skill.

**Conclusion from closed data:** every dominant bucket is at coin-flip (40–48% raw, 31% hard), mean PnL ≈0% → **no edge** in the aggregate.

### 4.3 What the system's own gates say

- `forward_candidate_scoreboard.json`: **14 candidates, 0 sizable.** Promotion bar = CI-LB > 1.15 AND n_eff ≥ 80. Only `luxalgo_confluence/SHORT` = "real-edge(sub-bar)" (n=47, PF point 1.888, CI-LB 1.0898, n_eff 44.6). All others = "no-edge/mirage".
- `money_ready_verdicts` (from dashboard payload): **NOT_READY** for FOREX, CRYPTO, EQUITY; **WATCH** for COMMODITY; **INSUFFICIENT_DATA** for ETF, BOND, MEME, FUTURES, PENNY_STOCK.

### 4.4 Verdict — are there good prospects?

**No active pick qualifies as a prospect under my methodology.** Why:

1. **Data-integrity gate:** several active strategies have no closed record (`magic_formula_*`) or rely on the class flagged as contaminated (forex). The resolved-closed backfeed was only recently fixed (frozen-exit resolver).
2. **Hard-win accounting:** the honest hard-win rate is ~31%, not the ~45% raw figure.
3. **Statistical gate:** 0/14 strategies clear the system's own promotion bar; no active strategy has n_eff ≥ 80 with CI-LB > 1.15.
4. **Forward proof:** none of the active picks has a sealed, cost-inclusive forward cohort; all are paper/backtest-only.

The closest thing to a "prospect" is a **SHORT needle on luxalgo-confluence** (DOTUSDT), but it is sub-bar (n≈47) and the live pick is an *inverse* variant. It belongs on a **watch-list**, not in a portfolio.

### 4.5 Why the equity cluster is the weakest

- `magic_formula_x_piotroski_x_acquirers` has **0 rows** in `recent_closed` → no closed record to compute PF/WR/n. 
- It is 16 of 27 active picks from one strategy → concentration risk (violates basic diversification).
- Equity class verdict is NOT_READY (PF not OK). The per-asset-class consensus says "no certified single-stock pick".
- Its low scores (18–25) already place it at the bottom of the current active list.

---

## 5. What would make a pick a true winner (applied)

For *any* pick to become a prospect, it must:

- Come from a **resolver-fixed**, artifact-free source (Stage 0).
- Show **TP_HIT-based** win rate with **Wilson LB > break-even**, **PF CI-LB > 1.15**, **n_eff ≥ 80** (Stage 1).
- Survive **FDR correction** with family size reported (Stage 1).
- Match a **forward-sealed cohort** (Stage 3).
- Have an **economic mechanism** and be **buyable** (Stage 4, plus RBC/broker access for Canadians).

None of today's active picks meet this bar. That is the honest answer — and it agrees with every agent and the project's own gates.

---

## 6. Verify & reproduce

- `audit_trail/data/dashboard_payload.json` (active + `recent_closed` + `money_ready_verdicts`).
- `audit_dashboard/data/forward_candidate_scoreboard.json` (promotion bar, candidate verdicts).
- Peer reports: `COMMUNITY/KILO_20261023_1636_PEER_CROSSCHECK_LESSONS_LEARNED.MD`, `COMMUNITY/INCEPTION_VLLM_PLAN_PROFIT_PICK.md`, `COMMUNITY/GHCOPILOT_20261023_GROK_SCORECARD_CROSSCHECK.MD`.
- My methodology report: [`updates/2026-10-23-lessons-learned-methodology.md`](updates/2026-10-23-lessons-learned-methodology.md:1).

---

## 7. Disclaimer

**Not financial advice.** Nothing here is money-ready. All audit picks are research/paper-only until a sealed, cost-inclusive forward cohort confirms them. Consult a licensed advisor before acting.
