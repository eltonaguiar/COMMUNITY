# INCEPTION/VLLM — Approach (high-level)

**Agent:** INCEPTION/VLLM · **Date:** 2026-10-22 · **Repo:** eltonaguiar/COMMUNITY (branch `m0vies`)

> This is the high-level plan. For the granular task list, code changes, verification,
> and current state, see
> [`INCEPTION_VLLM_PLAN_PROFIT_PICK.md`](INCEPTION_VLLM_PLAN_PROFIT_PICK.md).
> For the open questions and the data-access plan, see
> [`KEY_QUESTIONS.md`](KEY_QUESTIONS.md).

## Goal

Produce **at least one statistically proven, forward-validated winning sleeve**
per asset class — proven the same way our own strict harness will accept it, not
by hand-waving or by backtests that overfit.

## The core diagnosis (what we found first)

We did **not** start by tuning strategies. We started by asking *is the scoreboard
honest?* Across all concurrent agent investigations, the one thing that converged
was that **the measurement layer is corrupting the results**:

- The resolver fetched **one price snapshot per run** and stamped it onto every
  unresolved pick of a symbol (`universal_pick_resolver.py`) → **manufactured
  fake clustered wins** (frozen-exit artifact).
- The copy-trader emitted stale/closed historical rows as if they were fresh
  active picks (lifecycle break).
- No asset class currently clears a strict, honest gate.

So the sequence is **fix the scoreboard first, then measure, then forward-test,
then promote.**

## Plan at a glance

### Step 0 — Fix the measurement layer (DONE)
- **P0-1** Frozen-exit resolver fix: each pick resolved against its **own** price
  (`_per_pick_price`), not a run-wide snapshot. ✅ committed on `fix/frozen-exit-resolver`.
- **P1-1** Standing **artifact detector** CI gate (`wins > 2× distinct exit dates`)
  so fake clusters can never silently poison a report again. ✅ committed on
  `feat/artifact-detector-ci`.

### Step 1 — Force an honest re-run
- **P0-2** Deploy the resolver fix so production regenerates resolved picks.
- **P1-2** Re-run the 90-day walk-forward harness on the **fixed-resolver** data;
  confirm whether any sleeve clears the strict gate (test n≥10, PF≥1.15, WR≥0.50,
  train PF>1.0, non-artifact).

### Step 2 — Forward-proof the strongest sleeve
- **P1-3** Open a **sealed, timestamped, cost-inclusive forward paper cohort** for
  the single best sleeve. No claim before the cohort resolves (≥100 observations).

### Step 3 — Productize only what's proven
- **P2** Keep the mutual-fund ranker as the stable product; promote a sleeve to
  tactical rotation **only** after it passes the fixed-resolver harness AND a
  sealed forward cohort.

## Guardrails

- We do **not** claim a winner until it passes (a) the strict fixed-resolver
  harness and (b) a sealed forward cohort with costs.
- We **do not** loosen gates or change sizing to make something "win".
- Every code fix ships with a regression test, a `.MD` in `updates/`, and
  verification, per the workspace rules.

## Where the detail lives

| Topic | File |
|---|---|
| Full plan, task table, current state, verification | `INCEPTION_VLLM_PLAN_PROFIT_PICK.md` |
| Open questions + data-access/DB plan | `KEY_QUESTIONS.md` |
| Audit findings (6 mission questions, root causes) | `AUDIT_FINDINGS_GCOPILOT_OCt22.MD` (in main repo) |
