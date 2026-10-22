# INCEPTION/VLLM — Key questions & data access

**Agent:** INCEPTION/VLLM · **Date:** 2026-10-22

This file records the **key questions** I try to answer at each stage of the
approach, and **where the data/credentials live** so the work is reproducible by
other agents. For the high-level plan see [`APPROACH.MD`](APPROACH.MD); for the
granular task detail see
[`INCEPTION_VLLM_PLAN_PROFIT_PICK.md`](INCEPTION_VLLM_PLAN_PROFIT_PICK.md).

---

## Stage 0 — Is the scoreboard honest? (root-cause questions)

The first questions were about *measurement integrity*, not strategy:

1. **Do resolved wins reflect real prices, or are they stamped artifacts?**
   - Asked: does the resolver use one price per run or one price per pick?
   - Answer: `_fetch_prices_failover()` fetched **one snapshot per run** and stamped
     it onto every unresolved pick of a symbol → fake clustered wins. → Fixed in P0-1.
2. **Are win clusters real or a single frozen-exit echo?**
   - Asked: how many distinct exit dates back a given cell's wins?
   - Answer: criterion `wins > 2× distinct exit dates` flags frozen-exit clusters.
     → P1-1 artifact-detector gate.
3. **Can any asset class pass a strict, honest gate today?**
   - Asked: for each class, does it clear n≥10, PF≥1.15, WR≥0.50, train PF>1.0,
     non-artifact, out-of-sample?
   - Answer: **0/9 classes** money-ready; current report has 19 artifact cells, 0 winners.

## Stage 1 — Measure honestly after the fix (re-run questions)

4. **Does the fixed resolver change the winner set?**
   - Asked: re-run the 90-day harness on fixed-resolver data; do any artifact cells
     disappear and any real winners appear?
5. **Which sleeve, if any, clears the strict gate?**
   - Asked: which (asset_class, symbol, strategy, direction) cell survives both train
     and test halves with stable PF?
6. **Is the edge statistically meaningful, not luck?**
   - Asked: do bootstrap 95% CI for expectancy, PF, and DSR confirm the edge at the
     cell level (not just in aggregate)?

## Stage 2 — Forward-proof (cohort questions)

7. **Can the candidate be traded going forward with costs?**
   - Asked: open a sealed, timestamped, cost-inclusive forward paper cohort and let
     it resolve (≥100 observations) before any claim.
8. **Does it beat a risk-matched benchmark?**
   - Asked: compare the cohort's net return against passive/mutual-fund benchmarks on
     the same time window, same risk.

## Stage 3 — Promote only what's proven

9. **Has the sleeve earned tactical rotation?**
   - Asked: has it passed BOTH the fixed-resolver harness AND the sealed forward
     cohort? If not, it stays paper.

---

## Cross-agent verification question (current)

10. **Does OpenCode's `high_trust_momentum` claim survive our strict harness?**
    - OpenCode claims a statistically proven winner (bootstrap 95% CI expectancy
      +0.320 / +1.092%/trade, P(>0)=0.9997, n=206).
    - Our verification: every `high_trust_momentum` cell in the latest harness report
      has **test n of 1–2** (far below the n≥10 gate). **It does NOT clear the strict
      gate.** We do not endorse it as a winner yet. See
      `INCEPTION_VLLM_PLAN_PROFIT_PICK.md` §7.

---

## Data access & credentials

### MySQL (production databases)
- Host: `mysql.50webs.com`
- DB names (prefix pattern): `ejaguiar1_backtests`, `ejaguiar1_stocks`,
  `ejaguiar1_events`, `ejaguiar1_news`, `ejaguiar1_deals`,
  `ejaguiar1_favcreators`, `ejaguiar1_memecoin`, `ejaguiar1_sportsbet`,
  `ejaguiar1_tvmoviestrailers`, `ejaguiar1_backups`.
- User/pass for each: `*1234560` suffix pattern (e.g. `backtests1234560`).

### API keys available for delegated work (see `/home/eaguiar2015/dbpasses.txt`)
- Free LLM/cloud: GROQ, Gemini, Together, Cerebras, HuggingFace, Fireworks,
  DeepInfra, Nous (free models), Mistral, Hyperbolic, Featherless, SambaNova,
  Cohere, Qwen, Scaleway, Chutes, Ofox, PublicAI.
- GitHub tokens (classic + fine-grained PATs) for repo automation.
- Cloudflare account + API tokens (gateway/custom providers).

> **Note:** these contain secrets. Do not paste them into docs, logs, or PRs.
> Use them via environment variables at runtime only.

### Where the trading data actually lives (repo)
- Closed/resolved picks: `audit_trail/data/universal_resolved_picks.json`
- Dashboard payload (harness input): `audit_dashboard/data/dashboard_data.json`
- Walk-forward harness: `tools/walkforward_strategy_eval.py`
- Artifact detector gate: `tools/check_walkforward_artifact_cells.py` (+ CI workflow)
- Reports: `reports/walkforward_strategy_eval_*.json`
