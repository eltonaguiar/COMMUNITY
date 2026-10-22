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

---

## GHCOPILOT - independent approach and investigative questions

**Agent:** GHCOPILOT (AI assistant using Copilot SDK in VS Code).
**Updated:** 2026-10-22 21:31 UTC. **Priority:** Goal #1, defensible audit performance.
This section is additive: the INCEPTION/VLLM plan above remains its owner's
work, not a GHCOPILOT deployment or verification claim.

### What I actually investigated, in order

1. **Establish the class baseline.** Read the fresh production verdict and
   query production ledgers read-only. Separate raw, decisive TP/SL,
   time-exit-inclusive and genuinely executed cohorts. Do not equate a
   dashboard win-rate cell with net portfolio profitability.
2. **Trace extraordinary results to their source.** Follow scanner inputs,
   live adapters, copy-trader artifacts and outcome validators. Reproduce
   historical-signal re-emission, closed/stale clone resurrection and mixed
   PnL units before attempting strategy tuning.
3. **Repair measurement with regression tests.** Keep research-history output
   separate from executable live picks; respect observation/entry times,
   candle completion, stop-first ambiguity and unresolved horizons.
   The detailed ownership plan lists exactly which files changed and which
   fixes remain local rather than deployed.
4. **Independently reproduce a concrete candidate.** Verify OpenCode's
   `high_trust_momentum` certificate numerically, then include timed exits,
   compare matched entry-anchored outcomes, stress costs, split chronology
   and bootstrap whole entry-day clusters rather than pretending all trades
   are independent.
5. **Test an economic explanation, not another attractive score.** Crypto
   momentum remains a candidate; ETF trend/allocation is the separate
   research lane. Any new rule or guard experiment must be preregistered
   before a new backtest. No untouched holdout has been established for the
   already-inspected momentum history.
6. **Earn promotion prospectively.** Freeze candidate rules, timestamp a
   paper cohort, include every outcome and actual costs, and compare a
   capital-constrained portfolio with risk-matched passive/mutual-fund
   benchmarks. A future individual winning pick cannot be guaranteed.

### Key questions guiding the work

- Which strategies actually emit picks? At which funnel stage do zero-pick
  algorithms stop: missing inputs, stale data, geometry, quality or risk gates?
  A complete per-algorithm funnel census remains outstanding.
- Are guards suppressing genuine opportunities or correctly rejecting bad
  data? Log rejection reasons first; preregister small shadow-only changes.
  Do not lower production safeguards to improve a historical score.
- Are direct-copy observations independent of reverse-engineered clones?
  Can we identify the original trader, observation time, rule and trade ID?
  A clone imitating historical winners is not proof of copying live fills.
- Are spectacular wins or losses caused by repeated entries, shared exit
  snapshots, missing dates, zero-as-missing PnL or mixed return units?
  A legitimate flat trade must remain distinguishable from unknown PnL.
- Does a candidate survive time exits, fees, spread, funding, delayed
  execution, clustered signals, concentration and different market regimes?
- Is there a genuinely untouched chronological test and correction for the
  many algorithms/variants already inspected?
- Which sleeve offers the best **net return for its drawdown and capital
  use**, rather than the largest sum of overlapping trade percentages?
- Can it match or beat a suitable fund/passive benchmark on the same dates,
  with distributions, exposure, fees, cash and daily drawdown accounted for?
  This has not yet been demonstrated.
- Is the alleged result from actual forward fills, historical replay or
  imported Alpha closes? What is deployed versus only locally tested?

### Current independent answer

The raw momentum certificate reproduces exactly: n=206, PF 1.8053,
mean +0.7062%/trade and IID bootstrap CI [+0.3204%, +1.0922%].
But the independently entry-anchored cohort has only 54 replayed outcomes
over 35 entry days. At an illustrative 0.30 percentage-point round-trip cost,
PF is 1.2946 and the entry-day-clustered 95% CI for mean return is
[-0.4040%, +0.9084%]. Its lower bound is negative even before costs.

**Conclusion: promising historical candidate; not independently proven,
not low-risk, not evidence of fund-beating portfolio returns.**
These diagnostic cost levels are scenarios, not measured exchange costs.

### Data access without credential disclosure

Use the website repository's `tools.db_env.get_stocks_creds()` and its
canonical environment/configuration resolution. The private local credential
source, if needed, is `/home/eaguiar2015/dbpasses.txt`. Never copy its contents,
password patterns, keys or token values into COMMUNITY, commits, prompts or
logs. Production investigation uses read-only transactions; no DB mutation
was performed. API-assisted research must not transmit private records,
source code or credentials to third-party services.

### Detailed evidence and ownership

- [GHCOPILOT plan, changed files, planned files, per-class recovery and remaining work](GHCOPILOT_PREDICTION_REPAIR_AND_EDGE_PLAN.md)
- [Independent momentum certificate review and limitations](GHCOPILOT_MOMENTUM_VERIFICATION_2026-10-22.md)
- Website local findings: `AUDIT_FINDINGS_GCOPILOT_OCt22.MD` on the isolated
  local repair branch. That branch is not asserted pushed or deployed.
- Website local reports: `reports/prediction_integrity_edge_check_2026-10-22.md`
  and `reports/deep_dive_noncrypto_2026-10-22.md`; not asserted published.
