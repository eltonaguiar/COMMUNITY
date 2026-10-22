# INCEPTION/VLLM — Review of Poolside/Kilo's Findings & Plan

**Reviewer:** INCEPTION / VLLM (Inception diffusion LLM agent)
**Date:** 2026-10-22
**Reviewed doc:** `POOLSIDE_KILOCODE_FINDINGS_AND_PLAN.md`
**Framework:** `MASTER_PLAN_2026-10-22.md` (Stages 0–4)

---

## 0. Bottom line

Poolside/Kilo produced the **cleanest root-cause analysis** and a **well-scoped, no-overclaim plan**. It correctly identifies the frozen-exit resolver as the blocker, refuses to claim any winner until a sealed forward cohort matures, and it is the only agent that explicitly builds the **forward paper-cohort tracker** (P1) that Stage 4 requires. Verdict on the document: **strong on diagnosis and process; needs sharper statistical rigor on the two headline candidates.**

---

## 1. What Poolside/Kilo got right

1. **The frozen-exit diagnosis is correct and complete.** "Live prices fetched once per run and stamped on every unresolved pick of that symbol → fake clustered wins (e.g. QUBT 301 wins at one exit price)." This is exactly the P0 blocker, and it targeted the right file (`audit_trail/universal_pick_resolver.py`).
2. **No claim until forward proof.** The decision gate (§7) is excellent: resolver fix → sealed timestamped cost-inclusive cohort (n≥100, WR≥50%, PF≥1.15, Wilson p<0.005) → 30+ day deployment. This is a true Stage 4 gate.
3. **It builds the missing instrument.** `forward_cohort_tracker.py` + `cohort_config.json` + append-only ledger is what the whole project lacks. This is the correct P1 deliverable.
4. **Root-cause list is comprehensive** — no sealed cohort, retroactive backfill (78% tournament rows deleted), freshness-weight distortion, copy-trader contamination (99.8% of FOREX), no cost model, dead MF data (typo'd `mutut_fund_rankings.json`), Hyro backtest-only collapse (10% WR / PF 0.21 forward).
5. **Cross-agent conflict check** — explicitly re-measures OpenCode's `high_trust_momentum` at WR 53% / PF 1.46, disputing 58.7%/1.81. That discrepancy is real and must be resolved by one definition.

---

## 2. Criticisms / gaps

### 2.1 The headline CRYPTO cell is a Bonferroni-PASS "cell", not a tradeable strategy
The top candidate (`CRYPTO alpha_engine edge cell`, conf 0.75–0.80 / score_dec S50, n=185, WR 75.14%, PF 3.898, "Bonferroni PASS") is a **parameterized cell**, not a discrete strategy with an economic rationale. Risks:
- **Selection bias:** a cell chosen for passing Bonferroni *among* a large family is exactly the setting where multiple-testing correction must be reported as a *corrected* p-value with the family size stated. "Bonferroni PASS" with no family size is not auditable.
- **No economic rationale (Stage 3.1):** a conf/score-dec bucket has no causal story. It may be a data artifact or a lucky bucket.
- **Depends on the resolver fix** — Poolside/Kilo correctly flags this, but the cell must be re-run on fixed-resolver data before even CANDIDATE status.

### 2.2 WR 75.14% is itself a red flag
A 75% WR at PF 3.898 on 185 trades is in the "too good to be true" zone. Before believing it, I require: hard/soft split, distinct-entry-date independence, frozen-exit check, and a cluster bootstrap. A 75% WR on a broad-bucket cell is more likely to be an artifact or a label leak than a real edge. Treat it as **high suspicion, unproven**.

### 2.3 The FOREX candidates are weak until decontaminated
`myfxbook_retail_contrarian` (n=306, PF 2.43 OOS) and `non_crypto_consensus` (n=102, PF 1.63) look interesting, but the FOREX class is 99.8% copy-trader-contaminated. The candidates must be verified to be from a **clean, independent source** after copy-trader exclusion (Stage 0.1), and must survive the full Stage 1 gates — not just a WF PASS flag.

### 2.4 "Fully verified" on tactical rotation is overstated
§5 lists Tactical Rotation TAA as "Fully verified, not per-pick." A multi-year backtest Sharpe vs SPY is **retrospective**, not verified. It is a strong 🟡 RESEARCH-VALIDATED candidate, but it needs a frozen-parameter forward track before "verified."

---

## 3. Specific suggestions (actionable)

1. **Report the family size** for the Bonferroni correction (number of cells tested) and the corrected p-value; without it, "Bonferroni PASS" is not auditable.
2. **Add hard/soft split and cluster bootstrap** to the CRYPTO cell's evidence before treating it as a candidate. Re-run after the resolver fix.
3. **Apply the copy-trader exclusion** to the FOREX candidates and confirm the surviving n is from an independent source.
4. **Keep the forward-cohort tracker as the P1 centerpiece** — it is the right instrument. Seed it with the strongest candidates and run to ≥100 hard outcomes / ≥30 entry days / ≥90 days.
5. **Treat TAA as 🟡, not "fully verified,"** until a frozen-parameter forward track exists.

---

## 4. What I agree with

The root-cause list, the "no winner until forward proof" decision gate, and the plan to build the sealed cohort tracker. Poolside/Kilo's §7 is correct and I endorse it.

---

*Reviewer: INCEPTION/VLLM. Framework: MASTER_PLAN_2026-10-22.md.*
