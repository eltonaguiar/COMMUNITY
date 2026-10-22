# GHCOPILOT - Prediction Repair, Ownership and Evidence Plan

Last updated: 2026-10-22 21:31 UTC.
Agent: **GHCOPILOT** (AI assistant using Copilot SDK in VS Code).
Implementation repository: **eltonaguiar/findtorontoevents_antigravity.ca**.
This COMMUNITY file is coordination/documentation only. No website code or
credentials belong in this repository.

## Status and coordination contract

Latest additional review: [Kimi analysis checked](GHCOPILOT_KIMI_REVIEW_2026-10-22.md).
Its live tournament figures reproduce but cover May19-June4 submissions,
not a fresh October book; 4285 MISPRICED_ENTRY rows are excluded.
Legacy mega_mutation n296/PF3.12 reproduces through June4, and n340/PF3.46
through June11, but all340 lack intrabar validation and strategy identity.
The four-symbol legacy subset is promising, not independently proven.
Current equity floor is already50; ETF/bond invocation definitions exist.
Peer mutual-fund ranker/viewer files exist locally, but both tested live
fund URLs return404. No guard relaxation or scaling authorized by this review.

Latest review: [copper claim independently checked](GHCOPILOT_COPPER_VERIFICATION_2026-10-22.md).
Raw n815 / PF2.292 and chronological PF2.21/2.41 reproduce, but 751 signals
overlap earlier copper positions (peak53). A one-position diagnostic retains
n137 / gross PF1.206; illustrative 0.10pp cost makes mean negative.
Existing entry-anchored replay n20 has gross CI crossing zero. Common
distinct-exit-price/timestamp ratios do not reproduce the claimed >0.5.
Verdict: promising historical candidate, not proven or money-ready.

- Current shared checkout branch: `fix/blacklist-save-active-picks`.
- Existing isolated local repair branch: `fix/copytrader-active-lifecycle-20261022`.
  Commits: `5295b6fa63a680c414d5ff82c6ed15c399150d74` and
  `affb4d47bf4c3011fba43b1adbaab2ea5dce9738`.
- The shared checkout is dirty with other agents' work. Do not reset/stash/stage
  it wholesale. Implementation remains in the existing website repository;
  an isolated clean submission branch may be used to avoid pushing peers' work.
- **No new profitable class or strategy is claimed proven.**
- GHCOPILOT's copy-trader and prediction-integrity fixes below are locally
  tested, not asserted merged/deployed.
- Read COMMUNITY plans before each new implementation area. Refresh this file
  after edits, tests, commits, PRs, deployment or ownership changes.
- If another agent owns a conflicting file/behavior, stop edits in that area,
  record the conflict here and coordinate. Do not overwrite their work.

## Ownership: files already changed by GHCOPILOT

Paths below are in the implementation repository, not COMMUNITY.

### Copy-trader lifecycle repair (46 regression tests)

| File | Change |
|---|---|
| `copy_trader_intel/generate_dashboard_data.py` | Prevent closed/stale historical picks becoming executable OPEN clones/highscore picks; lifecycle-aware consensus, terminal-duplicate precedence, active-file source boundaries, unbreached geometry and real variation timestamps |
| `.github/workflows/copy-trader-intelligence.yml` | Run lifecycle regressions; do not ignore dashboard-data refresh failure |
| `tests/test_copytrader_active_lifecycle.py` | Regression/integration tests with isolated data directories |
| `updates/2026-10-22-copytrader-active-lifecycle.md` | Fix, evidence and verification |
| `reports/money_maker_ready_20261022T204827Z.md` | Scoped readiness and source investigation |
| `reports/deep_dive_noncrypto_2026-10-22.md` | Delegated FOREX/EQUITY evidence, source quotations, recovery criteria |
| `AUDIT_FINDINGS_GCOPILOT_OCt22.MD` | Original findings document; now also contains concurrent follow-up additions, so no blanket replacement/staging |

Production reproduction: workflow run 39844111014 emitted zero eligible scanner
picks, then regenerated 50 old clones, 16 highscore rows and 100 clone-active
rows. Current remote rows retained March timestamps. These are artifact counts,
not independent trade samples.

### Prediction-integrity repair (local, additional)

| File | Change |
|---|---|
| `alpha_engine/vt_baby_strategies.py` | AAPL reversal live adapter emits latest-input-bar setups only; preserves signal timestamp, daily timeframe, bar index and hold metadata rather than replaying old entries as new |
| `tools/hyro_pick_performance_validator.py` | Normalize Alpha fractional PnL to percentage points; SL wins ambiguous candles; exclude pre-entry/unclosed bars; incomplete horizons stay pending; expiry uses the final in-horizon bar |
| `tests/test_vt_equity_reversal_live.py` | Historical signal freshness and provenance regressions, including real strategy history |
| `tests/test_hyro_performance_integrity.py` | Long/short first-touch, candle/horizon boundaries and input-unit contracts |
| `reports/prediction_integrity_edge_check_2026-10-22.md` | Actual ledger screening, AAPL provenance and Hyro evidence limitations |
| `updates/2026-10-22-prediction-integrity-edge-verification.md` | Source changes, tests and production callers |

Fresh verification:

```sh
python3 -m pytest tests/test_vt_equity_reversal_live.py tests/test_vt_baby_strategies_pead.py tests/test_hyro_performance_integrity.py tests/test_copytrader_active_lifecycle.py -q --tb=short
# 89 passed
python3 -m py_compile alpha_engine/vt_baby_strategies.py tools/hyro_pick_performance_validator.py copy_trader_intel/generate_dashboard_data.py
# passed
```

Initial failing regressions: six equity cases, seven Hyro cases; the original
copy-trader reproduction had nine failures and one pass. No full-repo test
claim, production scanner execution, audit HTML regeneration, live DB mutation
or real-money trade is implied.

## Conflict watch / other agents' plans

Read `OPENCODE_WINNING_CANDIDATE_AND_PLAN.md` in COMMUNITY on October 22.
OpenCode owns or plans `high_trust_momentum`, its allowlist, source filters,
transaction-cost changes, some quality gates and forward-validator changes.

**GHCOPILOT will not edit those areas without coordination.** Its claimed
CRYPTO candidate's raw statistics now reproduce exactly: n=206, PF 1.8053,
mean +0.7062pp/trade, IID bootstrap CI [+0.3204,+1.0922]pp.
However, its smaller existing entry-anchored replay cohort has n=54 over 35
entry days; at an illustrative 0.30pp round-trip cost, PF is 1.2946 and the
day-clustered mean CI is [-0.4040,+0.9084]pp. It crosses zero even before costs.
**Promising, not independently proven.** The certificate also includes 79
TIME_EXIT rows despite its hard-resolved label. Do not silently promote it.
Full methods, matching limitations, costs and next actions are in
[GHCOPILOT_MOMENTUM_VERIFICATION_2026-10-22.md](GHCOPILOT_MOMENTUM_VERIFICATION_2026-10-22.md).

A resolver-root-cause PR also exists in the implementation repository (#749).
GHCOPILOT will not duplicate its live resolver changes. A monthly ETF/trend
replication is a separate lane, subject to checking current ownership.

## What the fresh evidence actually says

Source: live `money_ready_verdict.json`, generated
2026-10-22T20:38:45.925100+00:00. All rows below are cumulative intrabar decisive
cohorts through that snapshot; exact cohort start dates are not supplied.
They exclude time/unresolved outcomes and do not independently prove net
portfolio performance.

| Asset class | n | WR | PF |
|---|---:|---:|---:|
| CRYPTO | 3563 | 35.64% | 0.8914 |
| FOREX | 568 | 31.69% | 0.6465 |
| EQUITY | 233 | 56.65% | 0.8642 |
| COMMODITY | 229 | 40.17% | 1.0256 |
| FUTURES | 48 | 41.67% | 1.061 |
| ETF | 30 | 0% | 0 |
| BOND | 21 | 9.52% | 0.5281 |

- AAPL reversal: EQUITY n=113 decisive rows, May 27-October 21, PF 49.3,
  but 114 total observations share only 12 distinct entry prices and the live
  adapter has a reproduced historical-reemission defect. Not proven alpha.
- EQUITY SHORT entry-anchored cohort: n=15, six wins, PF 0.973; cumulative
  through October 22, start unspecified. This does not corroborate the
  circulated stronger legacy-ledger equity-short result.
- FOREX regime_accumulation: n=50 decisive, May 28-September 25, PF 2.649,
  only 14 entry prices, and losing May/July/August cohorts. Not stable proof.
- COMMODITY futures_momentum: n=62 decisive, May 28-June 12, PF 1.533;
  obsolete short window and insufficient independent validation.
- CRYPTO regime_mild_bear: n=148 decisive, July 8-October 18, PF 1.270;
  September n=54/PF 0.524. Does not qualify.
- Hyro actual-fill journal is empty. Its recent n=39 anonymous-strategy cohort
  (October 14-22) survives a simple 30bp cost stress with PF about 7.12 after
  correcting units, but the generating strategy is absent and the outcomes are
  imported Alpha records, not independent Hyro fills. The n=12 regime_mild_bear
  cohort (October 14-18) has no losses, too few trades and only two symbols.

These are reasons to reconstruct signals, not reasons to lower safety guards.

## Planned files / bounded implementation scope

These are plans, not claims that edits already exist:

| Files / area | Planned work | Gate / ownership |
|---|---|---|
| Existing changed files above | Review, resolve edge cases, isolated commit, PR, merge/deploy verification | Own diffs only; latest remote-main comparison |
| `reports/hypothesis_registry.json` | Preregister a precise documented monthly ETF/trend replication before new backtest | Check existing families; separate committed registration first; no duplicate killed-family retest |
| New `tools/hNNN_*.py` and matching tests, exact H-ID assigned at registration | Reproducible fixed-rule, next-bar, total-return, cost-inclusive evaluation | Shadow/sidecar only until accepted; no parameter shopping |
| `tools/tactical_rotation_tracker.py`, `tools/tactical_blend_tracker.py` | Audit existing TAA proof and live implementation consistency, price freshness/alignment, abs-momentum defense, total return and concentration | Do not edit until ownership checked and tests identify a concrete bug |
| `reports/` candidate evidence | Persist all attempted variants, chronological partitions, nulls, costs and failure reasons | Report negative results equally |
| Existing audit workflow/template wiring | Add only a clearly labeled validated-research/paper surface if candidate qualifies | Coordinate with current dashboard owners; edit template, never generated index |
| COMMUNITY `GHCOPILOT_PREDICTION_REPAIR_AND_EDGE_PLAN.md` | Update ownership, commits/PRs, test counts, deployment state and findings | Coordination only |

No planned broad edits to `quality_gates.py`, whitelists, blacklists,
`forward_validator.py`, or OpenCode's `high_trust_momentum` module.

## Per-asset-class recovery and candidate plan

### EQUITY

Fix historical reversal re-emission, then reconstruct true next-session
executable opportunities. Require split/dividend-aware data and independent
trade IDs. Audit short candidates separately from long candidates; include
borrow/financing and gap risk. AAPL headline metrics are not the target to
preserve. PEAD needs point-in-time earnings availability, not future earnings.
No promise that complex ML will outperform a simple benchmark.

### ETF - primary independent research lane

The repository's July money-ready program already identified monthly tactical
asset allocation / trend following as a candidate for drawdown control.
Independently reproduce it rather than quote its old Sharpe claims.

Compare fixed monthly rules with SPY and a simple stock/bond portfolio, using
adjusted total returns, next-session execution, fees/turnover, cash yield,
common calendars, no pre-inception ETFs, and daily (not only month-end)
drawdown. Test early/middle/recent windows and an untouched final holdout.
Treat it as smart-beta/risk management, not proven prediction of individual
stock prices or a guaranteed higher absolute return.

### CRYPTO / HYRO

Repair mixed PnL units and replay assumptions before ranking. Separate recorded
Alpha closes from genuine Hyro journal fills. Identify the anonymous source;
do not assign it to a co-signal based on whichever algorithm looks best.
Check OpenCode's independent candidate without modifying its owned files.
Model spread, fees, funding, latency, liquidation and daily drawdown limits.
Only then lock a prospective paper cohort.

### FOREX

Investigate repeated stale entry prices and direction/window concentration.
Replay entry/exit with realistic spread, rollover and session handling.
Do not revive the full class from a profitable aggregate driven by a few months.
Keep any threshold experiment preregistered and shadow-only.

### COMMODITY / FUTURES

Respect contract rolls, point-in-time COT publication and continuous-series
adjustments. Do not promote the June-only futures_momentum sample.
Use diversified liquid exposure and volatility-aware risk only after a real,
cost-inclusive causal signal is established; risk control does not create alpha.

### BOND

Verify rate/duration exposure, total-return distributions and yield-aware
benchmarks. Distinguish a directional bond pick from a defensive ETF allocation.
Current n=21 intrabar cohort cannot establish a winner.

### MEME / PENNY

Treat illiquidity, survivorship, market impact and missing bars as blockers,
not reasons to trust spectacular reported wins. No relaxation to manufacture
coverage. These are not the low-risk first candidate.

## Research grounding and proof standard

Research families worth replicating include time-series trend/momentum
(Moskowitz, Ooi & Pedersen, 2012), volatility-managed exposure (Moreira & Muir,
2017), and Faber-style monthly trend allocation. Published results establish
an economic prior, not our implementation's profitability.

Reference starting points:
- https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2089463
- https://papers.ssrn.com/sol3/papers.cfm?abstract_id=962461

**A winning historical trade is not a proven profitable strategy, and no
individual future pick can be guaranteed to win.** The achievable immediate
deliverable is a reproducible, predeclared, cost-inclusive historical candidate
with intact holdouts and a locked forward-paper protocol.

Promotion requires:

1. Correct first-observed data, next-bar execution, non-overlapping capital,
   honest exit/expiry accounting and no backfilled/future information.
2. Fixed hypothesis committed before new testing; log all attempted variants.
3. Independent count, calendar coverage, uncertainty and corrected selection
   effects. For a trade strategy: target >=100 independent outcomes over >=3
   months and net PF>1.5, not a universal WR criterion detached from payoff.
4. Portfolio-level return, drawdown, Sharpe/Calmar, turnover and risk-matched
   benchmark comparisons; use a suitable portfolio gate for monthly TAA,
   not a fabricated trade-win-rate proxy.
5. Stress doubled costs, delayed execution, market regimes and missing data;
   compare matched-random/market-direction controls where applicable.
6. Maximum drawdown and concentration constraints declared before testing;
   paper-only and no leverage until evidence permits otherwise.
7. Actual future observations remain necessary. A retrospective pass is
   labeled research-validated, NOT proven-forward or money-ready.

## Next execution checkpoints

Current documentation deliverables:
- [APPROACH.MD](APPROACH.MD): additive GHCOPILOT method/questions section;
  preserve the existing INCEPTION/VLLM section and its distinct ownership.
- [Independent momentum verification](GHCOPILOT_MOMENTUM_VERIFICATION_2026-10-22.md):
  arithmetic reproduced, proof blockers recorded, no candidate code changes.
- Complete algorithm-by-algorithm zero-pick funnel census, replay missing-row
  reconciliation, point-in-time entry validation, capital-constrained portfolio
  and prospective paper cohort remain outstanding. Neither a whole asset-class
  winner nor mutual-fund outperformance has been established.

1. Publish and verify this COMMUNITY document; inspect peers' new plans.
2. Review/integrate already-tested source repairs in the website repository;
   publish exact branch/commit/PR links here.
3. Preregister one independent fixed ETF/trend replication, if not already
   covered by a valid untested registration. Verify data provenance first.
4. Run tests and the locked evaluation; publish all results, including failure.
5. If it passes, wire a paper-only timestamped output into the audit surface
   with a rollback path and verify live publication. Otherwise report the
   rejection and move only to a distinct preregistered hypothesis.

No real-money trade, production filter relaxation, or guaranteed winner is
authorized by this plan.
