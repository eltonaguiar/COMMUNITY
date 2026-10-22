# Strategy / Source Evidence Census (read-only, static)

Generated 2026-10-22T22:09:08.614782Z from PINNED commit `876b6b831dfa53bbb357e97b4d30ec53897f6f27` (git blobs; shared checkout untouched). Counts are literal-key counts, not verified emitters; not every one of the 37,988 tracked files (5,273 .py) was individually audited. The earlier local-worktree run is kept as `census_local_worktree_initial.*` and is superseded.

## 1. Exact counts (provenance: `GHCOPILOT_STRATEGY_EVIDENCE_CENSUS_2026-10-22.json`)

| Layer | Count | Meaning |
|---|---|---|
| module-level *STRATEGIES/*REGISTRY/*FAMILIES dict/list literals in alpha_engine | 196 | registry_literals_alpha_engine |
| alpha_engine files holding such registries | 167 | alpha_registry_files |
| ...imported statically by production_scanner.py or smart_picks_engine.py | 10 | alpha_registry_files_direct_import_by_production_or_smart_picks |
| ...referenced only as strings there | 5 | alpha_registry_files_string_ref_only |
| ...imported by a wired module (1 hop), not by scanner directly | 75 | alpha_registry_files_reachable_1hop_only |
| ...no static path within 1 hop (candidates/orphans) | 77 | alpha_registry_files_no_static_path_within_1hop |
| unique literal keys, including policy lists (upper bound on true strategy definitions) | 1162 | unique_literal_keys_alpha_registries |
| defined keys in directly-wired registry files (UPPER bound of wired emitters; registry membership != emission) | 549 | unique_literal_keys_direct_wired_registries |
| defined keys in direct+string+1hop files | 815 | unique_literal_keys_1hop_reachable_total |
| defined keys with no static 1-hop path | 591 | unique_literal_keys_unreachable_registries |
| keys in config.STRATEGY_FAMILIES (14 families) | 361 | config_STRATEGY_FAMILIES_entries |
| defined keys with no family assignment | 801 | alpha_registry_keys_missing_from_STRATEGY_FAMILIES |
| banned sources | 4 | config_BANNED_SOURCE_SYSTEMS |
| blacklisted strategies | 27 | config_BLACKLISTED_STRATEGIES |
| baby_strategies/*.py | 230 | baby_strategies_py |
| strategy classes in baby_strategies | 204 | baby_strategy_classes_ast |
| paper_trading/strategies/*.py | 54 | paper_trading_strategies_py |
| strategy classes there | 104 | paper_trading_strategy_classes_ast |
| hypotheses in reports/hypothesis_registry.json list (plus ~25 side-sections) | 99 | hypotheses_list |
| with acceptance_criteria | 92 | hypotheses_with_acceptance_criteria |
| with economic_prior | 86 | hypotheses_with_economic_prior |
| with data_sample_lock | 42 | hypotheses_with_data_sample_lock |
| paper/candidate/pilot/shadow/forward_ files (.py/.yml), name-only census | 166 | n_paper_candidate_surface_files |
| workflows matching paper/scan/pick/forward/etc. (of 379 total), name-only census | 77 | n_paper_candidate_workflows |

Observed picks (committed `audit_dashboard/data/pf_registry.json`, 2026-10-22T20:40Z): raw_rows 28,756 -> closed 23,605 -> deduped 21,523 -> policy_clean 20,051; 599 asset_class x strategy rows (policy-clean net), 638 raw, 1,987 x symbol. **Defined (1,162 keys) vs documented candidates (99 hypotheses) vs wired (<=549 direct-file keys) vs observed (~600-640 strategy-class rows)** are different populations; no key-level join was asserted because registry keys, `source_system`, and pf_registry `strategy` use different namespaces (aliases in config.STRATEGY_TRACK_ALIASES).

Hypotheses by class: COMMODITY 15, EQUITY 18, ETF 9, FUTURES 5, CRYPTO 23, FOREX 13, BOND 4, CHEAP_STOCKS 3, PENNY_STOCK 3, MEME 3, MULTI 2, SPORTS 1.
By normalized status: FORWARD_OBSERVATION 19, PRE_REGISTERED 16, REFUTED 15, UNTESTED 8, PAPER_PILOT 7, FORWARD_SHADOW 7, REGISTERED_UNTESTED 3, REJECTED 2, KILLED 2, TESTED_KILL 2, UNTESTED_DATA_GAP 2, TESTED_WEAK 2 (status vocabulary is not normalized: 25 distinct values).

## 2. Candidate claims requiring screening (this update)

### kilo_crypto_alpha_engine_cell (CRYPTO)
- Claim: conf0.75-0.80 & score_dec=S50 & source=alpha_engine n185 PF3.898 WR75.14%
- Economic hypothesis: directional; post-hoc cell mined from 574 tag-combos (cohort slice, not a pre-registered strategy)
- Provenance: audit_dashboard/data/top_edges_per_class.json (git-tracked, regenerated hourly); git history: pf 3.898 present in commits fa7de9fbcb0 (2026-10-19T04:10Z) and 339faae8e5e (2026-10-20T04:10Z)
- Current repo value: `generated 2026-10-22T04:09:53Z: same cell n183 wins145 WR79.23 PF4.706, train n105 PF5.707, holdout n78 PF3.534, Bonferroni alpha 8.71e-05 (574 cells); CRYPTO n_closed 2440, 90d window`
- Cohort: closed picks in 90d window; dims trust/conf/rr/fam/dir/score_dec/source; C(7,3)+C(7,4)=70 combos; holdout=PF>=1.2 on both 60/40 chrono splits
- **Verdict:** NOT PROOF. n/PF drifts between regenerations (185/3.898 -> 183/4.706) so cohort is still moving; ledger is the resolver-bug-affected closed-pick ledger (pf_registry by_asset_class_policy_clean_net CRYPTO is sub-T2; money_ready_verdict CRYPTO not MONEY_READY); selection from 574 cells with holdout carved from same window; no cost model, no forward untouched sample. Needs: replay on intrabar OHLCV, cost-net, forward-only accrual after freeze date, trial-count-true DSR (tools/dsr_audit.py).

### kilo_forex_myfxbook_retail_contrarian (FOREX)
- Claim: n306 OOS PF~2.43 WF PASS
- Economic hypothesis: reverse-engineered/third-party-sentiment contrarian (retail positioning fade), directional
- Provenance: audit_dashboard/data/walk_forward_per_strategy_latest.json generated_at 2026-06-05T10:33:34Z (STALE ~139 days at census time; mtime May 25/commit e59990e9729 2026-10-04 health-check); config: in_window60/out_window20/step10, min_n_total100, survival_threshold0.6, is_oos_pf_decay_tolerance0.85, require_macro_join
- Current repo value: `{"n_total": 306, "n_windows": 23, "n_surviving": 15, "survival_rate": 0.6522, "mean_oos_pf": 2.4302, "mean_oos_wr": 0.5217, "mean_is_pf": 0.9754, "total_pf": 1.0311, "total_wr": 0.4967, "verdict": "PASS"}`
- **Verdict:** NOT PROOF. 'OOS PF 2.43' is the MEAN of per-window OOS PFs (small 20-unit windows, outlier-inflated); pooled total_pf=1.031 / WR 49.7% over all 306 ~ breakeven before costs; mean_is_pf 0.975 <1. Related: reports/research_index_and_forex_diagnosis_2026-06-09.md:123 calls the FOREX 14d PF 2.43 a 99%-single-source + pre-dedup duplication artifact and recommends KILL (note numeric coincidence: same 2.43). Only 7 strategies in the WF file (3 PASS/4 FAIL).

### kilo_forex_non_crypto_consensus (FOREX)
- Claim: n102 PF1.63 WF PASS
- Economic hypothesis: internal multi-signal consensus (non-copy), directional
- Provenance: audit_dashboard/data/walk_forward_per_strategy_latest.json (2026-06-05); reports/deep_dive_forex_regime_2026-06-05.md L20,L101 (n=107 PF1.63 WR54.2%; n=93 PF1.22 WR52.7% 'BORDERLINE - barely above random')
- Current repo value: `{"n_total": 102, "n_windows": 3, "n_surviving": 3, "mean_oos_pf": 3.8859, "mean_oos_wr": 0.65, "mean_is_pf": 0.8393, "total_pf": 1.6306, "total_wr": 0.5686, "verdict": "PASS"}`
- **Verdict:** NOT PROOF. Only 3 windows (PASS threshold met trivially: 3/3); mean_is_pf 0.84<1; n=102 < money-ready n>=100 margin only; deep-dive shows a later cohort at PF1.22. FOREX class verdict stays NOT_READY in money_ready_verdict (intrabar truth n568 PF0.65 WR31.7%, 2026-10-22). Needs net-cost CI-LB (reports/FOREX_NETCOST_CILB_SENSITIVITY_2026-06-13.md).

### taa_etf_tactical_rotation (ETF)
- Claim: TAA tracker Sharpe 0.88 (6m, top5), MaxDD -19% vs SPY -24%
- Economic hypothesis: ETF tactical asset allocation / cross-asset dual momentum (portfolio-level risk-adjusted smart-beta; NOT per-pick directional alpha)
- Provenance: tools/tactical_rotation_tracker.py (commit e59990e9729 2026-10-04); reports/TACTICAL_ROTATION_EDGE_2026-07-04.md (backtest source; Sharpe 0.88 row = top5-6m; verified-row citation reports/QUICKWIN_STRATEGY_TEMPLATES_2026-10-19.md L48/L175); audit_dashboard/data/tactical_rotation_status.json generated 2026-10-22T21:02Z, as_of_price_date 2026-09-30, params top_n5/lookback6m/monthly/abs-filter->AGG, holdings EEM,QQQ,SPY,IWM,DBC (field names say mom_9m while params say 6m: label inconsistency to resolve); hypotheses H-003 SHADOW_LIVE, H-102 PRE_REGISTERED, H-103 TESTED_PASS_BACKTEST_FORWARD_PENDING, H-109 UNTESTED, H-20260612-etf_dual_momentum_vix_v2 FORWARD_OBSERVATION
- **Provenance correction:** `tactical_rotation_status.json` is a local-only observation, absent from the pinned main commit. Its holdings/date/label observations above must not be represented as merged or publicly deployed evidence.
- **Verdict:** potentially useful portfolio research, but backtest/in-sample-robust only (2018-2026 window, 14-ETF universe chosen post-hoc, self-labelled 'not proven-forward', 'NOT excess return'). Sharpe 0.88 < tracker 9m region 1.09-1.21 -> parameter choice matters; compare vs SPY Sharpe 0.74. METHOD_REVIEW says verdict n=15. Local forward status file has holdings only, no realised NAV series. Must be evaluated as a portfolio (monthly returns, N~100 months max) not via pick-level PF/WR; DSR needs true trial count across all searched cells, not just the 16 currently displayed.

### hyro_35_of_176_challenge_passers (CRYPTO (prop-firm challenge futures))
- Claim: 35/176 HyroTrader challenge passers
- Economic hypothesis: synthetic backtest strategy x symbol grid (selection among 176 combos), not trader copy
- Provenance: audit_dashboard/data/hyro_batch2_results.json generated_at 2026-04-07T21:53:25Z (STALE; file mtime May 25); docs/HYROTRADER_PICKS_ANALYSIS.md:127 '35 out of 176 combos pass (20%)'; challenge_params: 5000 acct, 3% risk cap, 5% daily loss, 10% overall, 40% consistency, 10%/5% targets; months=6, risk_pct=0.75
- Recomputed from file: `{"combos": 176, "passers": 35, "distinct_strategies": 26, "distinct_strategies_with_a_pass": 17, "symbols": 7, "total_trades_all": 8656, "total_trades_passers": 2747, "passer_trades_min": 35, "passer_trades_median": 78, "passer_WR_range": [30.8, 51.9], "passer_PF_range": [1.05, 2.15], "top_pass_symbols": {"BTCUSDT": 8, "ETHUSDT": 8, "XRPUSDT": 6, "SOLUSDT": 6, "AVAXUSDT": 4, "ADAUSDT": 3}}`
- **Verdict:** NOT PROOF. Best-of-176 selection with no multiple-testing correction; the observed 20% pass fraction is NOT an estimated null/chance pass probability. avg_win/avg_loss are near-fixed R multiples (synthetic RR sim), median 78 trades per passer, WR down to 30.8%; Kilo's own note: combined forward playbook lost 80% (10% WR PF0.21, -$509). Kilo text says 'avg ~50 trades' and 1,488 total -- file shows 2747 passer trades / 8656 total (Kilo figure not reproduced; flag as unverified). Needs a frozen-pass-list forward test + DSR/PBO over the 176-combo grid (tools/pbo_cscv.py needs the T x 176 return matrix, which this file does NOT contain: only aggregate per-combo stats).

### kimi_legacy_mega_mutation_subset (CRYPTO)
- Claim: legacy mega_mutation n340 WR66.76% PF3.457; recommended JUP/ENA/ADA/WIF subset n171 WR80.70% PF7.665 (parent already audited the 'mega171' variant; listed for completeness)
- Economic hypothesis: internal mutation-engine strategy (DNA mutation), directional, subset chosen post hoc by symbol
- Provenance: reports/TRUE_WINNERS_SCRUTINY_2026-06-05.md; reports/MERCURY2_SCRUTINY_GAP_ANALYSIS_2026-06-05.md; reports/MEGA_MUTATION_BRIDGE_CANDIDATE_2026-06-05.md; reports/RISK_REVIEW_MEGA_MUTATION_2026-06-05.md; reports/intrabar_replay_mega_mutation_20260605.json/ohlcv_replay_mega_mutation_20260605.json; session file GHCOPILOT_KIMI_REVIEW_2026-10-22.md sec.2: SQL on trading_picks (NOT at_raw_picks); original n296 WR63.85 PF3.12 through Jun 4; now n340 date range 2026-04-02..06-11, 45 close dates; all 340 empty strategy labels, NULL intrabar fields; subset after Jun 5 n22 all positive
- **Verdict:** NOT PROOF. Legacy ledger arithmetic reproduces, but entries unreplayed (no intrabar), labels empty, subset selected after seeing results (not untouched), current at_raw_picks mega_mutation rows n136 (116 numeric PF1.69) are not row-comparable; no exact-source at_signal_outcomes rows. Needs identity reconciliation + OHLCV replay (tools/replay_harness.py) + frozen-subset forward.

Already audited by parent (excluded): OpenCode high_trust/copper/luxalgo/regime_accum/BNB/cta; Kilo mega171/regimeTerminal100.

## 3. Distinct economic hypotheses (do not pool)
- Direct trader copy: `copy_trader_intel/*` scrapers, `tools/build_unified_copytrade_candidates.py`, consensus builder (H-001/H-101/H-105 mention copy-trader text; hypotheses are mostly COT/entry-condition, not copy).
- Reverse-engineered/inferred: myfxbook retail contrarian, polymarket/kalshi signals, CTA bridge/replicator, `ml_strategy_reverser`, kimi_inverse_scanner (H-112, H-136 mention inverse).
- ETF TAA/dual momentum: H-003, H-102, H-103, H-109, H-20260612-etf_dual_momentum_vix_v2; `tools/backtest_etf_rotation_vix_regime.py`, `run_etf_sector_rotation.py`, `tactical_rotation_tracker.py`. Portfolio-level monthly returns (small N), tested with Sharpe/DD/PSR, not pick PF/WR.
- Directional pick strategies (alpha_engine registries, baby, paper_trading): per-pick closed ledger, PF/WR/DSR/PBO.

## 4. Standards & machinery (truthful inputs)
- Standards: docs/BACKTEST_ADMISSIBILITY_STANDARD.md, STRATEGY_VALIDATION_GATES.md, STRATEGY_DISCOVERY_PROTOCOL.md, MUTATION_THREE_AXIS_PROTOCOL.md, STRATEGY_INVESTIGATION_BEFORE_KILL.md, MONEY_READY_MASTER_LOOP_2026-06.md, reports/hypothesis_registry.json (pre-registration, M-107), reports/money_ready_tiering_framework.md.
- `alpha_engine/deflated_sharpe.py`: needs per-trade returns + Sharpe variance across trials + TRUE trial count (`tools/dsr_audit.py::load_true_trial_count`); using n_trials=1 is dishonest.
- `tools/pbo_cscv.py::compute_pbo(returns_matrix,S)`: needs aligned T x N strategy return matrix (not available for hyro_batch2 or WF JSON; only from at_signal_outcomes via `build_cpcv_pbo_results.py`, DB-dependent).
- `alpha_engine/money_ready_verdict.py`: DB (at_signal_outcomes intrabar truth) + JSON; output committed at audit_dashboard/data/money_ready_verdict.json (2026-10-22T20:38Z, summary: money_ready [], watch [COMMODITY], 9 classes).
- `alpha_engine/benchmark_closed_ledger.py` (+33 tests): paired bootstrap vs benchmark, random-entry MC; needs picks JSON + price fetch (network).
- `tools/walk_forward_eff_harness.py`, `edge_stability_harness.py`: need picks with score field and dates; no DB.
- `tools/pending_spa_scan.py`, `tools/baby_dsr_scanner.py`, `tools/strategy_tier_tracker.py`: JSON-input, no DB.
- `tools/replay_harness.py`, `forward_candidate_scoreboard.py`, `forward_paper_pilot.py`: need DB/OHLCV for intrabar replay.
- Tests present: tests/test_benchmark_closed_ledger.py, tests/test_cpcv_overfit_detector.py, tests/test_deflated_sharpe_ratio.py, tests/test_edge_stability_harness_regime.py, tests/test_edge_stability_smoke.py, tests/test_m012_dsr_wireup.py, tests/test_money_ready_capital_lock.py, tests/test_money_ready_fdr_gate.py, tests/test_money_ready_intrabar_sizing_p1a.py, tests/test_money_ready_verdict.py, tests/test_stamp_pick_quality_dsr_gate.py, tests/test_walk_forward_eff_harness.py (+ more in JSON).
- WF PASS in `walk_forward_per_strategy_latest.json` is a window-survival rule only (>=60% windows OOS PF decay-tolerant); it is not DSR/SPA/cost-net proof and the file is dated 2026-06-05.

## 5. Per-class resource pointers
- **CRYPTO**: crypto_strategies.py, crypto_edge_strategies.py, crypto_smart_picks.py, crypto_strategy_harness.py, crypto_risk_gates.py*, funding_rate_scanner.py, volatile_alt_scanner.py, rocket_scanner.py, rocket_scanner_v2.py, whale_alert_scanner.py*, kimi_inverse_scanner.py, basis_carry.py
- **EQUITY**: equity_strategies.py, equity_breakout_scanner.py, equity_strategy_harness.py, penny_stock_strategy_harness.py
- **FOREX**: forex_strategies.py, forex_smart_picks.py, forex_strategy_harness.py, usd_strength_scanner.py
- **COMMODITY**: commodities_strategies.py, commodity_strategy_harness.py, cot_positioning.py
- **ETF**: etf_scanner.py, etf_strategy_harness.py
- **BOND**: bond_scanner.py, bond_strategies.py, bond_strategy_harness.py, bond_yield_curve_inversion.py
(* = statically imported by production_scanner/smart_picks_engine.) Also per-class: reports/deep_dive_* (23), strategy_tier_tracker_* (9), pf_registry (by_asset_class_policy_clean_net), top_edges_per_class.json, money_ready_verdict.json.

## 6. Evidence gaps
1. No key-level join between defined keys, wired emitters, and observed source_system (namespace mismatch; needs alias table + DB distinct source counts from parent).
2. 801 defined keys lack STRATEGY_FAMILIES entry; 77 registry files have no static 1-hop path from scanner (dynamic loading not resolved).
3. Stale artifacts: WF JSON (2026-06-05), hyro_batch2 (2026-04-07), Hyro/TAA 'verified' figures are backtests.
4. top_edges cell figures drift hourly (3.898 -> 4.706); pin a frozen cohort + date before any claim.
5. Kilo's 1,488 Hyro trades and 'avg ~50' not reproducible from file (8,656 / 2,747).
6. TAA has no realised forward NAV series; only holdings status.
7. 25 non-normalized hypothesis status strings; 7 of 99 lack acceptance criteria; 57 lack data_sample_lock.
8. Trial counts for DSR (1,162 defined keys + 230 baby files + mutations) not centrally recorded except dsr_audit's mutation-engine count.

## 7. Snapshot provenance, reconciliation, limits
- **Snapshot:** pinned commit `876b6b831dfa53bbb357e97b4d30ec53897f6f27` (2026-10-22T17:58-04:00, "feat: audited GHCOPILOT paper monitor..."), an ancestor of origin/main but NOT its tip (tip `e44bc5a` when checked). Source = `git archive` blobs of a subset (alpha_engine, tools, baby_strategies, paper_trading, copy_trader_intel, audit_trail, docs, hypothesis registry, named reports/data JSONs) + `git ls-tree` name list (37,988 files, 5,273 .py, 379 workflows). Workflow/paper-surface/test counts use names only.
- **Local vs pinned:** registry/key/family/baby/paper/hypothesis counts are identical (3 dirty local files didn't matter). Changed: paper/candidate surface files 163 -> **166**, matching workflows 76 -> **77**, tracked files 37,982 -> 37,988. Initial local-only findings NOT on pinned main: `audit_dashboard/data/tactical_rotation_status.json` (TAA holdings reading as of 2026-09-30, generated 2026-10-22T21:02Z) and the session-file review docs (Kilo/Kimi figures are agent-report claims, not repo artifacts).
- **Registry files:** 10 direct + 5 string-ref-only + 75 one-hop + 77 no-path = **167**.
- **Keys:** tiers overlap. Unique per tier: direct 549, string-ref 48, one-hop 474, no-path 591; raw occurrences 2,152 -> unique 1,162; direct/no-path overlap 208, direct/one-hop 247, one-hop/no-path 135; direct ∪ no-path = 932, so 549+591 is not a partition, and 591 means "appears in a file without a one-hop path", not "unwired".
- **True definitions vs policy lists:** 1,162 counts every key of any module-level dict/list whose name contains STRATEG/REGISTRY/FAMILIES, including policy sets (HARD_KILL, LOW_CONFIDENCE, TIER_A/B, ENSEMBLE_ONLY). It is an upper bound on strategy definitions; separating callable registries from policy sets was not done. Non-literal registries and non-`alpha_engine` registries are excluded.
- **Wiring:** "no static path within 1 hop" is a method cutoff, not evidence of unwired/dead (dynamic imports, longer chains, CLI/workflow callers unresolved). "Direct import" does not prove each key emits.
- **Namespaces:** registry keys, STRATEGY_FAMILIES/aliases, ledger `source_system`/`strategy`, hypothesis ids are distinct; no join asserted.
- **Candidate artifacts at pin:** top_edges (2026-10-22T04:09Z) CRYPTO cell n183 / PF4.706 (no n185/PF3.898 cell at pin; 3.898 only in earlier generations); walk-forward file 2026-06-05 (myfxbook n306 mean-OOS PF2.43 vs pooled 1.03; non_crypto_consensus n102 PF1.63, 3 windows); hyro_batch2 2026-04-07 (35/176); pf_registry 2026-10-22T20:40Z (identical to local read); money_ready_verdict 2026-10-22T20:38Z (none money-ready, COMMODITY watch). Section 2 verdicts stand; the TAA status-file detail is local-only.
- **Credential scan:** see below.
