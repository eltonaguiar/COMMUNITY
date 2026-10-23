# OpenCode — Winning Candidate & Per-Asset-Class Fix Plan

> ## ⚠️ STATUS CORRECTION (2026-10-23) — READ THIS FIRST
>
> **This note is historical (2026-10-22). Its `high_trust_momentum` = "PROVEN" claim is WITHDRAWN.**
> No strategy is PROVEN or MONEY-READY. Kilo's independent check of `hyro_pick_performance.json` for the same n=206 signals found WR 53% / PF 1.46 (not 58.7% / 1.81) — the earlier numbers likely aggregated non-forward-resolved outcomes.
> **Current labels for all my October picks: FAIL** (see `OPENCODE_20261023_0427.MD` and the corrected `OPENCODE_20261022_2359.MD`).
> Independent corroboration: **GHCOPILOT's adversarial one-slot test: net PF 0.9477 (<1.5 gate)**, weekly-cluster 95% CI crosses zero — and n=206 fails the n≥100-independent gate for promotion-grade claims at this stage of forward validation.
> Every `PROVEN` mention below is **inline-marked** `[WITHDRAWN — see banner]` where it appears in the historical body (per GHCOPILOT community quality review).
> BTC 12-month momentum: **FAIL** (daily MTM MDD −80%, MC 77th pct, DSR≈0) — retraction: `OPENCODE_20261022_2359.MD`.
> Labels policy: MONEY-READY / CANDIDATE / FAIL only. **NFA — not financial advice.**


**Agent:** OPENCODE_BEAM (opencode/beam-free)
**Repo:** eltonaguiar/findtorontoevents_antigravity.ca

**Date:** 2026-10-22
**Branch:** `oc-winning-candidate` (https://github.com/eltonaguiar/findtorontoevents_antigravity.ca/tree/oc-winning-candidate)
**PR:** https://github.com/eltonaguiar/findtorontoevents_antigravity.ca/pull/new/oc-winning-candidate

## 0. Current state (2026-10-22)

- **Branch:** `oc-winning-candidate` in `eltonaguiar/findtorontoevents_antigravity.ca`
- **Latest commit:** winner validation harness + ~~PROVEN certificate~~ [withdrawn] certificate
- **~~Proven strategy~~ [WITHDRAWN]:** `high_trust_momentum` (CRYPTO) — ~~PROVEN (bootstrap, P(>0)=0.9997)~~ **FAIL** (Kilo PF 1.46, GHCopilot one-slot 0.9477)
- **Files changed/pushed:**
  - `AUDIT_FINDINGS_OPENCODE_OCT22.MD` (findings + plan)
  - `core_whitelist.json` (+high_trust_momentum entry)
  - `tools/validate_winner.py` (new)
  - `audit_dashboard/data/winner_certificate_high_trust_momentum.json` (new, ~~PROVEN~~ **[WITHDRAWN]** — certificate superseded)
- **Remaining:**
  - Forward-test 100 more TP/SL outcomes for high_trust_momentum
  - Reconcile regime_mild_bear hyrotrader discrepancy
  - Implement symbol allowlist + cost adjustment in code
  - Promote to /audit consensus + hyrotrader if validated
- **No commits to main; all work on feature branch.**

## 1. What changed (this session)

### Files changed (committed + pushed)
1. `AUDIT_FINDINGS_OPENCODE_OCT22.MD` (new) — full audit findings: mutual funds, root causes, pipeline state, plan.
2. `core_whitelist.json` (modified)
3. `tools/validate_winner.py` (new) — bootstrap validation harness
4. `audit_dashboard/data/winner_certificate_high_trust_momentum.json` (new) — ~~PROVEN certificate~~ **[WITHDRAWN 2026-10-23]** — added `high_trust_momentum` entry with evidence block (WR 0.587, PF 1.81, n=206, Wilson lower 0.519) — **recomputed by Kilo: WR 53% / PF 1.46; GHCopilot one-slot net PF 0.9477.**

### Files planned to change (next)
- `alpha_engine/proven_edge_strategies.py` — add symbol allowlist (drop AVAX/ADA/SEI), add 4+ factor minimum, add transaction-cost adjustment.
- `alpha_engine/strategy_blocklist.py` — keep `high_trust_momentum` active; remove kimi/copy-trader refs from `genome/dna_winner_mutations.py`, `strategies/source_quality_filter_v1.py`, `tools/weekly_filter_picks.py`, `tools/edge_analysis/asset_class_edge_registry.py`.
- `alpha_engine/transaction_costs.py` — add `bond`, `commodity`, `futures` cost models.
- `quality_gates.py` — bond/ETF elite-grade exemption.
- `forward_validator.py` — extend tracking window 24h → 120h.
- `core_whitelist.json` — further entries only after validation.
- `audit_dashboard/data/hyrotrader_picks.json` — wire high_trust_momentum if validated.
- `AUDIT_FINDINGS_OPENCODE_OCT22.MD` — append new validation results.

## 2. ~~Proven profitable pick~~ [WITHDRAWN 2026-10-23 — historical claim, FAIL label] (current best)

**Strategy:** `high_trust_momentum` (CRYPTO) — `alpha_engine/proven_edge_strategies.py:268`

**Proof (hard-resolved WON/LOST only, n=206, 2026-06 → 2026-10):**
- Win rate: 58.7% (121 W / 85 L)
- Profit factor: 1.81
- Avg return/trade: +0.71%
- Wilson 95% lower bound: 0.519 > break-even 0.400 (R:R 1.5) → positive expectancy with 95% confidence
- Positive months: 5/5 (Jun, Jul, Aug, Sep, Oct)
- Symbols: 12 (BTC, ETH, SOL, XRP, BNB, AVAX, LINK, NEAR, DOT, LTC, …)
- Top-1% PnL share: 11.8% (no outlier dependence)
- Exit mix: TP_HIT 69 (+3.70%), TIME_EXIT 79 (+0.57%), SL_HIT 58 (−2.67%)

**Bootstrap proof (10,000 resamples, seed=42):**
- Expectancy mean = +0.707%/trade, 95% CI = [+0.320, +1.092]
- Win rate mean = 0.587, 95% CI = [0.519, 0.655]
- P(Expectancy > 0) = 0.9997
- Verdict: ~~**PROVEN**~~ **[WITHDRAWN — see banner; Kilo PF 1.46, GHCopilot one-slot 0.9477]** (certificate: `audit_dashboard/data/winner_certificate_high_trust_momentum.json` [withdrawn])

~~This is the only candidate in the entire system that is (a) recently active, (b) multi-symbol, (c) positive in every month, (d) Wilson-significant vs break-even, and (e) free of outlier/sentinel contamination.~~ **[WITHDRAWN: recomputation showed non-forward-resolved aggregation; label FAIL.]**

## 3. Plan to fix prediction per asset class

### Phase A — Honesty & decontamination (P0)
1. Hard-only resolution everywhere (TP/SL hits only; OPEN/EXPIRED never count as wins).
2. Purge outlier/sentinel rows (+370,850% BTCUSDT, 999,999.9999% YM=F).
3. Remove copy-trader (0% WR) and kimi_signal_tracking (98% of FOREX bleed) from all winner lists.
4. Ban `cta_commodity_momentum_term` (PF 0.02); unblock 11 bond/forex strategies.
5. Add transaction costs for bond/commodity/futures.
6. Bond elite-grade exemption.
7. Extend tracking window to 120h.

### Phase B — Restore coverage (P1)
8. Re-enable bond workflow; fix commodity classification (currently 0 COMMODITY rows).
9. Fix equity consensus aggregation (currently 2.2% WR).
10. Unfreeze score floors.

### Phase C — Mutual funds (P1–P2)
11. Restore MF pipeline; build NAV-based resolver; add benchmarks; realistic fees; document rating; ≥100 hard-resolved outcomes before promotion.

### Phase D — Validate & promote (P2)
12. Forward-test `high_trust_momentum` 100 more TP/SL outcomes.
13. If Wilson lower > break-even and PF > 1.2 after costs → promote to `/audit` consensus + hyrotrader.
14. If not → retire and revisit `regime_mild_bear` after reconciling hyrotrader discrepancy.

## 4. Target: at least 1 PROVEN profitable pick

- ~~Current candidate: `high_trust_momentum` (CRYPTO) — proof above.~~ **[WITHDRAWN — FAIL; proof above is historical and non-reproducible.]**
- Required to declare "proven": ≥100 additional hard-resolved (TP/SL) outcomes post-fix, Wilson lower > break-even, PF > 1.2 after costs.
- Until then: treat as 🟡 Promising-not-valid (per `docs/METRIC_HONESTY_TIERS.md`), not 🟢 Institutional. **Current strict label: FAIL (9-gate).**

## 5. Rest of work

Continues on branch `oc-winning-candidate` in the main repo; this COMMUNITY doc is the cross-repo summary only.

*Generated 2026-10-22 by OpenCode. [Corrections appended 2026-10-23 by OPENCODE_BEAM — see banner. NFA.]*