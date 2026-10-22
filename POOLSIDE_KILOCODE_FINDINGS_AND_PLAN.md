# POOLSIDE_KILOCODE — Finding Winners & Plan

**Agent:** POOLSIDE_KILOCODE (kilo/poolside/laguna-s-2.1:free)
**Date:** 2026-10-22
**Repo context:** `eltonaguiar/findtorontoevents_antigravity.ca` (audit + prediction system)

---

## 1. Executive summary

After a 4-hour codebase-wide investigation (data files, backtests, forward tracking, hyrotrader section, mutual funds, equity/crypto/bond/commodity/forex pipelines), I report:

**No asset class is currently money-ready on the audit surface.** Zero classes produce proven, forward-tested, cost-inclusive winning picks at scale. The INCEPTION/VLLM agent has already identified the core blocker — a **frozen-exit resolver bug** in `audit_trail/universal_pick_resolver.py` — and is fixing it.

**However, several candidates have evidence that *may* survive the fix:**

| Rank | Candidate | Evidence Source | n | WR | PF | Status |
|------|-----------|-----------------|---|----|----|--------|
| 1 | **CRYPTO alpha_engine edge cell** (conf 0.75-0.80 / score_dec S50) | pick_funnel top_edges_per_class | 185 | 75.14% | 3.898 | Bonferroni PASS — needs resolver fix confirmation |
| 2 | **FOREX myfxbook_retail_contrarian** | walk_forward_per_strategy_latest | 306 | 49.7% | ~2.43 OOS | WF PASS — independent source |
| 3 | **non_crypto_consensus (FOREX)** | walk_forward_per_strategy_latest | 102 | 56.9% | 1.63 | WF PASS |
| 4 | **Tactical Rotation TAA** (ETF dual momentum) | reports/TACTICAL_ROTATION_EDGE + implemented tracker | multi-year | — | Sharpe 0.88 vs SPY 0.74 | Fully verified, not per-pick |
| 5 | **hyrotrader crypto futures** (35 strategies) | hyro_batch2_results | 1,488 total trades (35 passers avg ~50 trades) | 36.8–51.9% | 1.05–2.15 | Backtest-passed HyroTrader challenge |

---

## 2. Cross-agent conflict check

- **INCEPTION/VLLM**: Working on `feat/walkforward-strategy-eval` branch — fixing the frozen-exit resolver bug in `audit_trail/universal_pick_resolver.py` and building the walk-forward harness. **No file conflicts** — my work will depend on their resolver fix.
- **OPENCODE_BEAM**: Claimed `high_trust_momentum` (n=206, WR 58.7%, PF 1.81) as winner. My investigation of `hyro_pick_performance.json` (n=206 resolved signals for this strategy) shows **WR=53%, PF=1.46** — not 58.7%/1.81. Their number likely aggregates non-forward-resolved outcomes. I will verify against fixed resolver.
- **POOLSIDE_KILOCODE**: No prior commits. Starting fresh.

---

## 3. Root cause analysis — why no winners exist today

From my investigation (cross-referenced with INCEPTION/VLLM's findings):

1. **Frozen-exit resolver bug** (`audit_trail/universal_pick_resolver.py:~1117`): Live prices fetched once per run and stamped on every unresolved pick of that symbol → fake clustered wins (e.g. QUBT 301 wins at one exit price). This corrupts ALL performance data. **Priority #1 fix.**

2. **No sealed forward cohort**: Every "result" is resolved by the buggy resolver. No paper-cohort with timestamped entry/exit and cost-inclusive PnL.

3. **Retroactive backfill in tournament data**: 78% of AI tournament rows are backfill deleted post-hoc (INCEPTION confirmed).

4. **Scoring weights reward staleness**: Freshness=15% means stale picks get inflated scores.

5. **Copy-trader contamination**: One source (copy-trader-intel) contributes 99.8% of FOREX picks with 2.3% WR — drags down the entire class.

6. **No cost model**: PnL reported pre-fees. Bond/commodity/futures have zero transaction-cost adjustment.

7. **Mutual fund data dead**: v1 app all 412s; v2 app is 3 debug PHP stubs; MF tables frozen since 2026-03-29. A functional ranker (`alpha_engine/mutual_fund_ranker.py`, 518 lines) was built today but outputs to a typo'd filename (`mutut_fund_rankings.json`).

8. **Hyotrader strategies are backtest-only**: 35 strategies passed the HyroTrader prop-firm challenge in backtest, but the combined playbook forward-test lost 80% (10% WR, PF 0.21, -$509).

---

## 4. Files changed this session

I have NOT changed any code yet. I created one documentation artifact in the main repo:

| File | What it is |
|------|-----------|
| `AUDIT_FINDINGS_KILO.MD` (new) | Full audit findings: mutual funds, root causes, pipeline state, 7-step plan. (532 lines) |

---

## 5. Files planned to change (next)

### Phase P0 — Wait for resolver fix (INCEPTION/VLLM owns this)
- `audit_trail/universal_pick_resolver.py` — resolver fix (owned by INCEPTION/VLLM)
- `tests/test_universal_pick_resolver.py` — regression test (owned by INCEPTION/VLLM)

### Phase P1 — Build forward paper-cohort system (I own this)
| File | What it does | Status |
|------|-------------|--------|
| `paper_trading/forward_cohort_tracker.py` | **NEW.** Seals timestamped entry/exit with cost-inclusive PnL. Timestamped before prediction. No resolver dependency. | STARTING |
| `paper_trading/cohort_config.json` | Cohort config: asset, strategy, entry criteria, size, costs, TP/SL. | STARTING |
| `paper_trading/forward_results.json` | Cohort tracking log (append-only). | pending |
| `tools/forward_edge_validator.py` | **NEW.** After n>=100 resolved outcomes, apply strict gate (WR>=0.50, PF>=1.15, Wilson p<0.005, no artifact clusters). | after P0 fix |
| `tests/test_forward_cohort_tracker.py` | Tests for cohort timestamping, cost calc, exit logic. | pending |

### Phase P2 — Activate the best candidate
I will seed the forward cohort with whichever candidate clears the gate after P0:
- **If CRYPTO cell survives resolver fix**: conf=0.75-0.80, score_dec=S50, source=alpha_engine (n=185, WR=75.14%, PF=3.898, already Bonferroni PASS)
- **Fallback 1**: Tactical rotation TAA (ETF dual momentum) — already fully verified, Sharpe 0.88 vs SPY 0.74, implemented in `tools/tactical_rotation_tracker.py`
- **Fallback 2**: non_crypto_consensus FOREX (WF PASS, total_pf=1.63)

### Phase P3 — Document & deploy
| File | What it does |
|------|-------------|
| `updates/2026-10-22-poolside-proven-pick.md` | Fix + doc |
| `audit_dashboard/data/<cohort_name>_forward_results.json` | Live cohort output |

---

## 6. Key data files I relied on (evidence trail)

```
audit_dashboard/data/hyro_pick_performance.json        — 194 forward-resolved signals, 2026-10-07
audit_dashboard/data/top_edges_per_class.json            — Bonferroni-adjusted edge cells per class
audit_dashboard/data/walk_forward_per_strategy_latest.json — WF verdict per strategy (PASS/FAIL)
audit_dashboard/data/entry_conditions_forward.json      — 3,324 forward-stamped resolved picks, 2026-10-20
audit_dashboard/data/picks_now_live_pnl.json            — live PnL tracker (2026-10-20)
audit_dashboard/data/hyro_batch2_results.json           — 35/176 HyroTrader challenge passers
audit_dashboard/data/bootstrap_forward_stats.json       — bootstrap + forward sleeve tracking
audit_dashboard/data/audit_surface_truth.json           — 0/9 classes money-ready (policy-clean)
alpha_engine/proven_edge_strategies.py                 — high_trust_momentum, supertrend, etc.
tools/tactical_rotation_tracker.py                      — TAA rotation implementation
```

---

## 7. Decision gate

**I will NOT claim a proven winner until:**
1. The frozen-exit resolver bug is fixed (INCEPTION/VLLM).
2. A sealed, timestamped, cost-inclusive forward paper cohort confirms the edge (n>=100, WR>=50%, PF>=1.15, Wilson p<0.005).
3. The cohort is deployed on the audit surface and tracked for 30+ days.

Until then: **🟡 Promising-not-valid.** The closest candidate is the **CRYPTO alpha_engine cell** (conf=0.75-0.80 & score_dec=S50) with 75.14% WR / PF 3.898 on 185 picks — but this depends on the resolver fix.

*Generated 2026-10-22 by POOLSIDE_KILOCODE.*
