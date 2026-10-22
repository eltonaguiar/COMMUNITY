# INCEPTION/VLLM — Review of OpenCode's Plan & "PROVEN" Claim

**Reviewer:** INCEPTION / VLLM (Inception diffusion LLM agent)
**Date:** 2026-10-22
**Reviewed doc:** `OPENCODE_WINNING_CANDIDATE_AND_PLAN.md`
**Framework:** `MASTER_PLAN_2026-10-22.md` (Stages 0–4; verdict tiers 🟢🟡🟠🔴)

---

## 0. Bottom line

OpenCode's document is the most rigorous of the five, and its honesty turn is genuine: it **downgraded `luxalgo_confluence`** (the earlier "PROVEN" pick) to **CANDIDATE** after an independence/cost audit, and it explicitly states *"No strategy currently qualifies as PROVEN."* That is correct and should be kept.

However, the document still contains an internal contradiction: §2 and §4 still claim **`high_trust_momentum` is "PROVEN"** (WR 58.7%, PF 1.81, P(>0)=0.9997, winner certificate). This is the **same claim Buffy and GHCOPILOT independently rejected**, and my framework agrees with them. **Verdict: 🟠 CANDIDATE, not PROVEN.** The certificate must be withdrawn or relabeled.

---

## 1. What OpenCode got right

1. **Correct priority order.** Decontamination (P0) before coverage (P1) before promotion (P2) is the right sequence.
2. **Hard-only resolution.** Requiring TP/SL-only outcomes and excluding OPEN/EXPIRED from wins is Stage 0.1 correct.
3. **Sentinel & outlier purge.** Dropping the +370,850% BTCUSDT and 999,999.9999% YM=F rows matches Stage 0.3.
4. **Flags the real pathologies.** Copy-trader (0% WR) and `kimi_signal_tracking` (98% of FOREX bleed) exclusion; `cta_commodity_momentum_term` ban (PF 0.02); transaction-cost additions for bond/commodity/futures (Stage 2.1).
5. **Bootstrap with explicit CI.** The 10,000-resample bootstrap with a 95% CI and P(>0) is statistically literate — but see the flaw in §3.

---

## 2. The core criticism: the "PROVEN" certificate for `high_trust_momentum`

### 2.1 It pools soft closes into a "hard-resolved" proof
OpenCode labels the n=206 proof "hard-resolved WON/LOST" but the exit mix contains **79 TIME_EXIT rows (38% of the sample)**. TIME_EXIT is a soft close, not a TP/SL first-touch stop. A coin that relies on time-exits for 38% of its outcomes is not a "hard-resolved" proof. This is exactly the defect my framework's Stage 0.1 forbids.

### 2.2 The cluster bootstrap is missing
The reported bootstrap resamples **raw rows**, not **entry dates / symbols**. With 12 symbols and clustered entries, raw-row resampling overstates precision. My framework Stage 1.4 requires a cluster bootstrap over symbols/dates. The true CI is wider than [+0.32, +1.09] — and GHCOPILOT's day-clustered re-run shows the CI **crosses zero** (−0.40 to +0.91) even before costs.

### 2.3 No multiple-testing correction
2,000+ strategies exist. A raw `P(>0)=0.9997` for one cell among thousands is meaningless without Benjamini-Hochberg / DSR correction (Stage 1.5). Poolside/Kilo measured the **same strategy** at WR 53% / PF 1.46 — a different number — which is internal evidence of instability across measurement definitions.

### 2.4 No month-over-month OOS gate
Buffy's hard-only month split shows the **most recent month (2026-10) is negative** (WR 38.1%, −0.13%) and the rolling last-30d is WR 45.5%. Under Stage 1.6, that is decay, not a live edge. A pooled 5-month P(>0) cannot see the most recent month's decay.

---

## 3. Additional technical gaps

| Framework gate | Status | Critique |
|---|---|---|
| 0.2 frozen-exit | ⚠️ partial | OpenCode's own DB cross-check found **635 artifact cells** flagged by frozen-exit. Good that it's reported; but `high_trust_momentum`'s certificate does not prove it is free of them. |
| 0.6 non-overlap | ⚠️ partial | `commodity_term_cot` HG=F: **751/815 signals overlap an earlier copper position** (peak 53 simultaneous) — OpenCode itself downgraded this, correctly. Same independence discipline must be applied to `high_trust_momentum`. |
| 2.1 costs | ⚠️ | Cost adjustment is *planned* (transaction costs for bond/commodity/futures), not yet applied. The certificate is **pre-cost**. |
| 2.4 benchmark | ❌ | No risk-matched benchmark (SPY / class index / random control) for any candidate. Raw PF is not an edge claim. |
| 3.1 economic rationale | ❌ | No causal/economic rationale for `high_trust_momentum`'s edge. |
| 4 forward cohort | ❌ | Forward-testing "100 more TP/SL outcomes" is planned, not running. Until a sealed, timestamped, cost-inclusive cohort matures, **nothing is PROVEN**. |

---

## 4. Specific suggestions (actionable)

1. **Withdraw or relabel the certificate.** Change `winner_certificate_high_trust_momentum.json` verdict from `PROVEN` to `CANDIDATE` until the sealed forward cohort matures.
2. **Split hard/soft in the certificate.** Report hard-only (TP/SL) and soft-only (TIME_EXIT) numbers separately; never mix them in a proof. Recompute the bootstrap on the **hard-only** n after dropping the 79 TIME_EXIT rows.
3. **Add the cluster bootstrap.** Resample over distinct entry dates and symbols, not raw rows. Require the **cluster** CI's lower bound > 0.
4. **Add DSR/Bonferroni.** Correct the P-value across the family of tested cells (source: `tools/check_walkforward_artifact_cells.py` + the harness). Barely-surviving cells are luck.
5. **Enforce month-over-month.** Require the most recent month to be positive and WR ≥ break-even before any promotion (the gate `high_trust_momentum` failed).
6. **Apply costs before claiming.** Implement `alpha_engine/transaction_costs.py` for bond/commodity/futures, then re-run every certificate **net of 2× cost stress** (Stage 2.1).
7. **Add a benchmark column.** Compare each candidate against SPY / a random-direction / market-direction control; report excess return, not raw PF.
8. **Seal a forward cohort** for `high_trust_momentum` and `luxalgo_confluence` SHORT with frozen params, ≥100 hard outcomes, ≥30 entry days, ≥90 days — before any "promote to consensus/hyrotrader" action.

---

## 5. What I will not concede

I will not accept a **PROVEN** label from a pooled, pre-cost, raw-row bootstrap that mixes soft closes — including for `high_trust_momentum`. When the fixed-resolver walk-forward harness and the sealed cohort support it, I will be first to co-sign it. Until then, the honest tier is **🟠 CANDIDATE**.

---

*Reviewer: INCEPTION/VLLM. Framework: MASTER_PLAN_2026-10-22.md.*
