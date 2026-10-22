# INCEPTION / VLLM — Plan to Get ≥1 Proven Profitable Pick

**Agent:** INCEPTION / VLLM
**Date:** 2026-10-22
**Repo context:** `eltonaguiar/findtorontoevents_antigravity.ca` (audit + prediction system)

---

## 1. Executive summary

We now have a **strict, read-only, out-of-sample evaluation harness** (walk-forward, chronological 50/50 split) over the live resolved-pick history. It delivers an honest, reproducible answer to "do we have a winning asset class / symbol / strategy yet?"

**Honest answer: not yet.** On the test (out-of-sample) half of 3,446 cleaned resolved picks, **zero cells passed the strict winner gate**. No asset class is statistically proven profitable. We are not going to pretend otherwise — we are going to fix the pipeline so the *next* evaluation can reveal a real edge.

What we *have* proven:

| Class | n (test) | WR | PF | Verdict |
|-------|-----------|-----|-----|---------|
| FOREX | 26 | 53.8% | **3.15** | interesting but n too small |
| CRYPTO | 1,430 | 44.4% | 1.27 | positive PF but WR < 50% |
| EQUITY | 120 | 43.3% | 0.98 | no edge |
| ETF | 82 | 35.4% | 0.72 | no edge |
| COMMODITY | 8 | 50% | 1.03 | n too small |
| BOND / FUTURES | ~0–2 | — | ~0 | degenerate |

---

## 2. What I already changed (completed work)

These files are new/updated from this investigation (branch `feat/walkforward-strategy-eval`):

| File | What it does |
|------|--------------|
| `tools/walkforward_strategy_eval.py` | **New.** Read-only OOS harness: clean picks (drop sentinel/flat/missing-pnl/duplicate), detect artifact cells, chronological 50/50 walk-forward split, per-cell metrics (n, wins, WR, PF with `INF_PF_CAP`, avg pnl%), strict winner gate (test n ≥ 10, test PF ≥ 1.15, test WR ≥ 0.50, train PF > 1.0, not artifact), ranking by `stable_pf = min(train PF, test PF)`. |
| `tests/test_walkforward_strategy_eval.py` | **New.** 8 tests (all green), incl. OOS-stability test (AAA stable wins; BBB early-only must NOT rank as winner). |
| `reports/walkforward_strategy_eval_2026-10-22.json` | **New.** Harness output: 3,446 cleaned (1,669 train / 1,669 test), 19 artifact cells flagged, 0 strict winners, class-level test-half metrics. |
| `updates/2026-10-22-walkforward-strategy-eval.md` | **New.** Method, gate, results, honest interpretation. |
| `AUDIT_FINDINGS_GCOPILOT_OCt22.MD` | **Modified.** Appended §G (cross-agent synthesis) and §H (closest-to-forward evidence + literature mapping + verdict). |

---

## 3. Root causes — why we don't have winners yet (verified)

1. **Frozen-exit resolver bug** (`audit_trail/universal_pick_resolver.py`): live prices are fetched **once per run** (line ~1117) and stamped onto **every** unresolved pick of that symbol (line ~1265). This manufactures fake clustered "wins" (e.g. QUBT 301 wins at one exit price), corrupting any naive evaluation. → This is why our *real* evidence must come from the harness above, which flags these as **artifact cells** (19 flagged).
2. **Scorekeeping problem, not strategy-generation problem** — consensus of Copilot / Freebuff / Kilo / OpenCode: we have hundreds of strategies but no trustworthy scorekeeper to say which sleeve is real.
3. **No forward cohort**: every pick so far is resolved by the buggy resolver, so we cannot trust backfilled results; we need a sealed forward paper cohort.

---

## 4. The plan to get ≥1 PROVEN profitable pick

### Phase P0 — Fix the scorekeeper (highest priority)

| # | Task | Files to change | Status |
|---|------|-----------------|--------|
| P0-1 | Fix frozen-exit resolver: resolve **per symbol + per pick** using that symbol's actual price series at the pick's own exit (or dedup so one price resolves at most one pick per symbol-day). Add regression test. | `audit_trail/universal_pick_resolver.py`, `tests/test_universal_pick_resolver.py` | **STARTING NOW** |
| P0-2 | Merge + deploy copy-trader lifecycle repair (branch `fix/copytrader-active-lifecycle-20261022`) so picks actually enter/exit active lifecycle correctly. | copy-trader modules | pending review |
| P1-1 | Add **artifact detector** (`wins > 2× distinct exit dates`) as a standing CI check so fake clusters never silently poison reports. | `.github/workflows/`, harness module | after P0-1 |

### Phase P1 — Measure honestly

| # | Task | Files to change | Status |
|---|------|-----------------|--------|
| P1-2 | **Re-run** the 90-day harness with the fixed resolver. Confirm whether any sleeve clears the strict gate (PF ≥ 1.15, WR ≥ 50%, n ≥ 10, train PF > 1, no artifact). | `tools/walkforward_strategy_eval.py` (re-run) | after P0-1 |
| P1-3 | **Open a sealed, timestamped, cost-inclusive forward paper cohort** for the single best candidate sleeve (likely FOREX or a specific CRYPTO cell). No prediction made before it is timestamped. | `paper_trading/` cohort files | after P1-2 |

### Phase P2 — Productize only what's proven

| # | Task | Files to change | Status |
|---|------|-----------------|--------|
| P2-1 | Keep the **mutual-fund ranker** as the stable, low-risk product (it is a ranker, not a per-pick bet). | existing ranker | stable |
| P2-2 | **Only after** P1-3 validation, promote the proven sleeve to tactical rotation. | strategy-registry / allowlist | gated on proof |

**Decision gate:** a sleeve is promoted only when it clears the strict gate on the **fixed-resolver** data AND then confirms on a sealed forward cohort with costs included. Everything else stays paper.

---

## 5. What I will commit to

- I will **not** claim a winner until both (a) the fixed-resolver harness **and** (b) a sealed forward cohort confirm it.
- The harness, the artifact detector, and the resolver fix ship together as a single reviewable unit.
- Every code fix will get a `.MD` in `updates/` + a regression test + verification, per the workspace rules.

**Closest candidates today** (not yet proven — need P0-1 re-run + forward confirmation): `JUPUSDT|mega_mutation_macd_rsi_m048|LONG` (PF ~3.99, but train n < 10), plus `drawdown_recovery_rsi_eth/sol` and `multi_period_rsi_confluence_eth` cells (high train PF, need test-half confirmation), and FOREX as a class (PF 3.15, n too small).

---

## 6. Current State — 2026-10-22 21:26 UTC (INCEPTION/VLLM)

### ✅ P1-1 COMPLETED — standing artifact-detector CI gate (branch `feat/artifact-detector-ci`, pushed)

New `tools/check_walkforward_artifact_cells.py` + `tests/test_check_walkforward_artifact_cells.py` (5 tests) + `.github/workflows/artifact-detector.yml` (daily 06:30 UTC + on-push). The gate fails whenever the latest walk-forward report contains any frozen-exit artifact cells; it correctly exits **1** on the current 19-cell report and will go green once P0-1's fixed resolver yields a clean re-run. Verified: 5/5 new tests, 26/26 existing harness tests pass.

### ✅ P0-1 COMPLETED — frozen-exit resolver fix (branch `fix/frozen-exit-resolver`, pushed)

**Root cause fixed:** `audit_trail/universal_pick_resolver.py` fetched prices **once per run** and stamped one snapshot onto every unresolved pick of a symbol → manufactured fake clustered wins. Fixed by a new `_per_pick_price()` helper that resolves each pick against the **first OHLC bar at/after its own entry timestamp**, falling back to the run-wide snapshot only when no bars exist (byte-identical legacy behavior).

- Files changed: `audit_trail/universal_pick_resolver.py` (+helper, wired into `close_approx` + `TIME_EXIT` fallbacks), `tests/test_resolver_frozen_exit_fix.py` (new, 5 tests), `updates/2026-10-22-frozen-exit-resolver-fix.md` (new).
- Verification: 10/10 resolver tests pass (5 new + 5 existing); broader run `pytest tests/ -k "resolver or outcome or orphan"` → 227 passed, 14 skipped (pre-existing skips).
- Backward-compatible: when no bar data for a symbol, falls back to the exact legacy snapshot path.

### ⏭️ Remaining (next)

| # | Task | Status |
|---|------|--------|
| P0-2 | Merge + deploy copy-trader lifecycle repair (`fix/copytrader-active-lifecycle-20261022`) | pending |
| P1-1 | Add artifact detector (`wins > 2× distinct exit dates`) as standing CI check | after P0-1 |
| P1-2 | Re-run 90-day harness on fixed-resolver data; confirm edge (PF, CI, DSR) | after P1-1 |
| P1-3 | Open sealed, timestamped, cost-inclusive forward paper cohort for strongest sleeve | after P1-2 |
| P2 | Mutual-fund ranker as stable product; tactical rotation only post-validation | gated on proof |

### 🤝 Cross-agent note
OpenCode has claimed `high_trust_momentum` (CRYPTO) is statistically proven (bootstrap 95% CI expectancy +0.320 / +1.092% per trade, P(>0)=0.9997, n=206). INCEPTION/VLLM will **verify this claim against our strict fixed-resolver harness** (gate: test n≥10, PF≥1.15, WR≥0.50, train PF>1.0, non-artifact) before endorsing any winner — consistent with our "no winner until harness + forward cohort confirm" commitment.

---

## 7. P1-2 status — 2026-10-22 21:28 UTC (INCEPTION/VLLM)

### 🚧 P1-2 BLOCKED on deploy (cannot claim a re-run winner yet)
P1-2 is "re-run the harness on **fixed-resolver** data." The frozen-exit resolver fix (P0-1) is committed on `fix/frozen-exit-resolver` but is **not yet deployed to production**, so the current `dashboard_data.json` (2026-10-19) still carries the legacy buggy resolved picks. Re-running the harness against that data reproduces the same 19 artifact cells — not a valid re-run. A true fixed-resolver re-run requires P0-2 (merge + deploy) so the resolver regenerates resolved picks, then the harness re-runs. **Thus P1-2's "confirm edge" is gated on P0-2, not on more harness work.**

- Current gate state: `tools/check_walkforward_artifact_cells.py` exits **1** on the 19-cell report (correctly red). It goes green only after the fixed resolver regenerates the data.

### ✅ Cross-agent claim verified against strict harness — `high_trust_momentum` does NOT clear the gate
I directly checked every `high_trust_momentum` cell in the latest harness report:
- `CRYPTO|ADAUSDT|high_trust_momentum|LONG` → test n=1, PF=0.0, WR=0.0; train metrics absent → **fails** min_n=10
- `CRYPTO|BTCUSDT|high_trust_momentum|LONG` → test n=1, PF=0.0, WR=0.0 → **fails**
- `CRYPTO|DOTUSDT|high_trust_momentum|LONG` → test n=2, PF=inf, WR=1.0 → **fails** min_n=10
- `CRYPTO|AVAXUSDT|high_trust_momentum|LONG` → test n=1, PF=inf, WR=1.0 → **fails**
- Overall harness winners on current data: **0**.

Verdict: OpenCode's n=206 bootstrap claim does **not** map onto our strict walk-forward cells (each cell has test n of 1–2, far below the n≥10 gate, and split-dependent). We therefore do **not** endorse `high_trust_momentum` as a winner. This is consistent with our commitment: a winner is only claimed when it clears the strict gate on fixed-resolver data AND then confirms on a sealed forward cohort.

### ⏭️ Next
- P0-2 (merge + deploy resolver fix) is the upstream unlock for a clean P1-2 re-run.
- P1-3 (sealed forward cohort) cannot be responsibly opened until P1-2 shows a gate-clearing sleeve.
