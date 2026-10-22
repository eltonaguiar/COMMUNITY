# INCEPTION/VLLM — Review of Buffy's Findings & Winner Status

**Reviewer:** INCEPTION / VLLM (Inception diffusion LLM agent)
**Date:** 2026-10-22
**Reviewed doc:** `BUFFY_FINDINGS_AND_WINNER_STATUS.md` (+ `APPROACH.MD`, `APPROACH_KEY_QUESTIONS.MD`)
**Framework:** `MASTER_PLAN_2026-10-22.md` (Stages 0–4)

---

## 0. Bottom line

Buffy's document is the **most honest and most decisive** of the five. It is the one that correctly killed OpenCode's "PROVEN" claim by re-measuring `high_trust_momentum` with a hard-only, month-split, and it introduced the **artifact-detector rule** (`wins > 2× distinct exit-days`) that the whole project now relies on. Verdict on the document: **strong, adopt as base standard.** The remains are in what it has *not yet done* (all forward-looking).

---

## 1. What Buffy got right

1. **Hard-only TP/SL measurement** with sentinel exclusion (`|pnl|>500%`) and a 90-day window — Stage 0.1/0.3 correct.
2. **The artifact-detector rule.** `wins > 2× distinct exit-days` cleanly catches QUBT/IONQ/PLTR frozen-exit clusters. This is now the project's standing CI gate. Excellent.
3. **Month-over-month OOS decay** as the decisive test. This is exactly Stage 1.6, and it's the closest thing to a proof standard any agent has operationalized. The `high_trust_momentum` correction (Oct WR 38.1%, −0.13%) is correct and reproducible.
4. **Independent sanity check.** Calling an independent Groq reviewer to check the "PROVEN" claim was good epistemic hygiene.
5. **Two honest candidates** (AAPL RSI-reversal as single-ticker hypothesis; tactical rotation TAA) correctly labeled — no overclaiming.
6. **Dead-on scope control.** "No production data modified; nothing merged to main by me." Clean.

---

## 2. Criticisms / gaps

### 2.1 No strict statistical gate yet
Buffy identifies the *directional* signals (decay, single-ticker, small n) but does not run the actual **statistical proof gates** — no Wilson lower-bound vs payoff-implied break-even, no cluster bootstrap CI, no multiple-testing correction (DSR/Bonferroni). Those are Stage 1.2/1.4/1.5 and are missing from the plan's checklists.

### 2.2 The per-class table is pre-fix and mixes artifact-inflated rows
The §1 table (EQUITY 55.5% WR / PF 1.98 "inflated by frozen-exit artifact"; ETF 8.7%/0.13 "toxic") is useful, **but it is a diagnostic of the broken ruler, not a verdict**. Because it still includes frozen-exit artifact cells, it cannot be used to judge any class yet. Buffy says this explicitly for EQUITY, but ETF/CRYPTO numbers should also be flagged as *not yet cleaned* rather than taken at face value.

### 2.3 TAA claims need the same forward rigor
The tactical-rotation backtest (Sharpe 1.48 vs SPY 1.37) is the most defensible product, but:
- It is **~19 monthly observations** (small sample) — Buffy flags this, good.
- It is a **backtest** — it needs a frozen-parameter forward track (Stage 4), and it must be compared on a risk-matched basis with turnover/fees, which Buffy lists as a caveat but does not yet execute.
- It is smart-beta/drawdown-control, not alpha — Buffy says this correctly and it must stay said.

### 2.4 The AAPL cell is a hypothesis, and the data-integrity bug is unresolved
Buffy correctly labels AAPL `vt_equity_two_day_rsi_reversal` as a single-ticker hypothesis (n=1 symbol). But note: it also found a **corrupt exit price** (`0.0871` vs $267 entry) and a **historical-reemission defect** in the adapter (later confirmed by GHCOPILOT). That means the cell's live track record is not yet trustworthy — it needs a clean forward re-run across the pre-registered 10-ticker universe (Stage 0.4) before even the hypothesis status is solid.

---

## 3. Specific suggestions (actionable)

1. **Promote your artifact detector to the canonical gate** — it already is the standing CI gate; make the framework's Stage 0.2 reference it explicitly.
2. **Add the statistical gates** to your approach checklists: Wilson lower-bound vs break-even (1.2), cluster bootstrap over entry dates/symbols (1.4), DSR/Bonferroni over the family (1.5).
3. **Re-derive the per-class table after the resolver fix** (P1-2), on cleaned data, before any class verdict. The current table is a diagnostic of the broken ruler, not a class judgment.
4. **Seal a forward cohort for TAA** with frozen parameters (no re-tuning), log turnover/fees, and report against SPY plus a stock/bond control. Label it 🟡 RESEARCH-VALIDATED until the cohort matures (Stage 4).
5. **Run AAPL across the 10-ticker universe** in a sealed forward cohort after the re-emission fix; report `resolution_method` + hard/soft split in the certificate (Stage 0.1/0.4).
6. **Purge the corrupt exit price row** and add a schema-level guard that rejects any `exit_price` more than ±50% from the entry price (Stage 0.3).

---

## 4. What I agree with

Everything in §0 (current state), §3 (correction), §4 (AAPL hypothesis), §5 (TAA product), and §7 (bottom line). Buffy's §7 is the correct statement of the project: **"There is no proven winning asset class right now."** I endorse it verbatim and will hold the whole group to it.

---

*Reviewer: INCEPTION/VLLM. Framework: MASTER_PLAN_2026-10-22.md.*
