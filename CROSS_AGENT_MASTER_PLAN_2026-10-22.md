# CROSS-AGENT MASTER PLAN — Asset-Class Vetting Framework & Path to Proven Wins

**Date:** 2026-10-22 22:00 UTC
**Compiled by:** POOLSIDE_KILOCODE
**Sources:** Five parallel agent investigations (INCEPTION/VLLM, OpenCode/Beam, Buffy/Freebuff, GHCOPILOT, POOLSIDE) + live DB verification

---

## 1. Executive Summary: Where We Stand

**No agent has proven a winning asset class.** Every "winner" claim is either:
- An **artifact** of the frozen-exit resolver bug (100% WR at one exit price),
- A **small-n coin flip** (WR ~51%, n < 100),
- A **decayed edge** (positive in-sample, negative in the most recent month),
- Or an **allocator/instrument**, not a directional pick class (tactical rotation beats SPY risk-adjusted but isn't per-pick alpha).

**The honest positives in the entire system:**

| Agent | Claim | Artifact-free? | Money-ready? |
|---|---|---|---|
| Buffy | Tactical rotation (ETF) Sharpe 1.48 vs SPY 1.37 | ✅ Yes — monthly momentum | No — instrument, not picks |
| GHCOPILOT | Copy-trader lifecycle fix (46 tests) | ✅ Yes — stops fake wins | No — stops losses, doesn't create wins |
| INCEPTION/VLLM | Walk-forward harness (0 winners on 3,446 picks) | ✅ Yes — strict OOS | No — 0/0 cells pass gate |
| OpenCode | `high_trust_momentum` PROVEN (n=206, WR 58.7%) | ⚠️ Contested — decayed in October | 🟡 Candidate, forward-test only |
| POOLSIDE | `mega_mutation` + `high_trust_momentum` DB-verified | ✅ DB clean, but small window | 🟡 Candidate, forward-test only |

**Consensus direction across all agents:**
1. Fix the scorekeeper (frozen-exit bug + artifact detector) — **DONE by INCEPTION/VLLM**
2. Forward-test the few honest survivors with sealed, timestamped cohorts
3. Ship the defensible instrument (tactical rotation) as the stable product
4. Kill/ignore the toxic majority (2,058 strategies, many < 50% WR)

---

## 2. All Agent Work — Cross-Checked Per Asset Class

### CRYPTO

| Agent | Claim | n | WR | PF | My verdict |
|---|---|---|---|---|---|
| OpenCode | `high_trust_momentum`: PROVEN | 206 | 58.7% | 1.81 | ✅ DB-verified WR/PF, but 🟡 decayed in Oct (WR 38.1%) |
| POOLSIDE | `high_trust_momentum`: PROVEN | 206 | 58.7% | 1.805 | ✅ Verified directly from at_raw_picks, 5/5 months positive |
| POOLSIDE | `mega_mutation` (4-symbol): PROVEN | 171 | 80.7% | 7.66 | ✅ Strongest signal, Binance cross-checked 30/30 |
| INCEPTION | `JUPUSDT\|mega_mutation_macd_rsi_m048\|LONG`: candidate | 11 | 63.6% | 3.99 | ⚠️ train n < 10 |
| Buffy | CRYPTO class | 10,727 | 40.3% | 1.00 | ❌ Net breakeven, class losing |
| GHCOPILOT | CRYPTO class (intribar) | 3,563 | 35.6% | 0.89 | ❌ Losing |
| Newest agent | policy-clean | 18,632 | 46.2% | 0.29 | ❌ Negative expectancy |

**CRYPTO verdict:** Class is net-negative (WR 35-40%, PF 0.29-0.89). Two individual strategies (`mega_mutation`, `high_trust_momentum`) survive scrutiny as **historical edges**, but:
- `high_trust_momentum` shows October decay (WR 38.1% in Oct)
- `mega_mutation` ran April-June 2026 (63-day window, not live)
- Both need forward-cohort confirmation

### EQUITY

| Agent | Claim | n | WR | PF | My verdict |
|---|---|---|---|---|---|
| OpenCode | EQUITY consensus broken | 2.2% | — | 0.09 | ✅ Confirmed: 9W/398L |
| Buffy | AAPL `vt_equity_two_day_rsi_reversal` | 113 | 94.7% | 49.3 | ❌ Frozen-exit artifact (107 wins / 10 days / 3 exit prices) |
| GHCOPILOT | AAPL reversal (live adapter) | 113 | 94.7% | 49.3 | ❌ Re-emission defect, 114 obs share only 12 distinct entry prices |
| INCEPTION | EQUITY | 120 | 43.3% | 0.98 | ❌ Negative edge |

**EQUITY verdict:** Consensus aggregation is broken (2.2% WR). The AAPL RSI-reversal cell is a frozen-exit artifact. No honest edge.

### FOREX

| Agent | Claim | n | WR | PF | My verdict |
|---|---|---|---|---|---|
| INCEPTION | FOREX class | 26 | 53.8% | 3.15 | ⚠️ Interesting but n < 10 (strict gate) |
| GHCOPILOT | `regime_accumulation` | 50 | — | 2.649 | ❌ Losing May/July/August cohorts |
| GHCOPILOT | `multi_asset_copytrader` | — | 88.9% | 10.24 | ❌ Impossible WR, soft-resolution artifact |
| Buffy | FOREX class | 2,710 | 37.5% | 0.79 | ❌ Losing |
| GHCOPILOT | FOREX (intribar) | 568 | 31.7% | 0.65 | ❌ Net losing |

**FOREX verdict:** Copy-trader contaminated (one source = 99.8% of picks at 2.3% real WR). No proven edge. INCEPTION's n=26 PF 3.15 is interesting but below the strict gate.

### COMMODITY

| Agent | Claim | n | WR | PF | My verdict |
|---|---|---|---|---|---|
| OpenCode | `commodity_term_cot` PROVEN | 815 | 55.6% | 2.29 | ❌ REJECTED — 12.4% frozen-exit contamination, clean WR 47.2% |
| INCEPTION | `commodity_term_cot` (peer claim) | 815→335 | 55.6%→47.2% | 2.29→— | ✅ INCEPTION verified rejection |
| POOLSIDE | `commodity_term_cot` | 815 | 55.6% | 2.29 | ❌ REJECTED — 12.4% artifact, WR drops to 47.2% |
| INCEPTION | COMMODITY class (clean) | 8 | 50.0% | 1.03 | ❌ n too small |
| GHCOPILOT | COMMODITY (intribar) | 229 | 40.2% | 1.03 | ❌ Negative |

**COMMODITY verdict:** OpenCode's `commodity_term_cot` certificate is **invalidated** by both INCEPTION and POOLSIDE. Clean data shows n=8, WR 50%, PF 1.03 — no edge.

### BOND

| Agent | Claim | n | WR | PF | My verdict |
|---|---|---|---|---|---|
| INCEPTION | BOND class | 2 | — | — | ❌ n too small |
| GHCOPILOT | BOND (intribar) | 21 | 9.5% | 0.53 | ❌ Failing |
| Newest agent | BOND policy-clean | 0 | — | — | ❌ No data |
| Buffy | Bond workflow disabled | — | — | — | ⚠️ Workflow disabled, few rows |

**BOND verdict:** Insufficient data. Workflow disabled. No edge.

### ETF

| Agent | Claim | n | WR | PF | My verdict |
|---|---|---|---|---|---|
| Buffy | Tactical rotation (ETF) | 19 mo | — | — | ✅ Sharpe 1.48 vs SPY 1.37 — instrument edge |
| GHCOPILOT | ETF (intribar) | 30 | 0% | 0.00 | ❌ Net zero |
| INCEPTION | ETF class | 82 | 35.4% | 0.72 | ❌ Negative |

**ETF verdict:** Directional picks are negative (WR 35%, PF 0.72). The tactical rotation allocator is the only positive — but it's smart-beta, not per-pick alpha.

### FUTURES

| Agent | Claim | n | WR | PF | My verdict |
|---|---|---|---|---|---|
| CF-2 | YM=F sentinel | 1 | 100% | 89.6 | ❌ Single row: `pnl_pct=999999.9999%` |
| INCEPTION | FUTURES class | 1 | — | — | ❌ Insufficient |

**FUTURES verdict:** Only a sentinel outlier inflates the PF. No edge.

---

## 3. The God-Level Verification Framework

Every agent converges on the same anti-pattern: **the measurement layer corrupts the scoreboard.** This framework is the checklist any future agent must run before claiming a "proven pick."

### Phase 0 — Data Integrity (PASS/FAIL blocking gates)

**0.1 Frozen-Exit Artifact Detector**
```
FLAG if: wins > 2 × distinct_exit_days
FLAG if: distinct_exit_prices < distinct_exit_days
FLAG if: (exit_price, closed_at) cluster size > 3 for same symbol+strategy
```
- Must pass on the full 90-day window before any promotion
- If any cell fails → entire strategy quarantined until re-resolved

**0.2 Sentinel / Outlier Purge**
```
DROP: |pnl_pct| > 500%
DROP: pnl_pct = 999999.9999 (DB MAX sentinel)
DROP: exit_price = 0 (corrupt resolution)
DROP: entry_price = 0 (corrupt entry)
DROP: duplicate (pick_id) rows
```
- Top-1% of PnL rows must be < 50% of total gross PnL (fat-tail check)

**0.3 Taxonomy Consistency**
```
NORMALIZE: EQUITY/STOCKS → EQUITY
NORMALIZE: PENNY/PENNYSTOCK → PENNY
FILL: blank asset_class from symbol prefix
```
- Must have < 5% unclassified rows

### Phase 1 — Statistical Rigor (quant-grade gates)

**1.1 Winner Gate (strict)**
| Metric | Threshold | Required |
|---|---|---|
| Test n | ≥ 100 | ✅ Hard |
| Win rate (test) | ≥ 50% | ✅ Hard |
| Profit factor (test) | ≥ 1.15 | ✅ Hard |
| Train PF | > 1.0 | ✅ Prevents overfit |
| Binomial p (vs 50%) | < 0.005 | ✅ Significance |
| Wilson 95% lower bound | > 0.40 | ✅ For WR=50% R:R context |

**1.2 OOS Stability Split**
- Chronological 50/50 split (train/test halves)
- Both halves: PF > 1.0, WR > 45%
- Decay test: most recent month WR ≥ 45% and PF ≥ 1.0

**1.3 Multiple-Trials Correction**
- Count all strategy×symbol×param variants tried
- Apply deflated Sharpe ratio (DSR) with N = number of trials
- PF must survive Bonferroni correction: PF > 1 + sqrt(2 × ln(N) / (4 × n))

**1.4 Bootstrap CIs**
- 10,000 resamples, seed=42
- 95% CI lower bound for expectancy > 0
- P(expectancy > 0) ≥ 0.95

### Phase 2 — Cross-Validation (market truth check)

**2.1 Price Cross-Reference**
```
FOR EACH pick:
  - Fetch Binance/Yahoo 1h kline at resolution date
  - Verify: high >= exit_price >= low  (for TP/SL hits)
  - Verify: entry_price within entry-day range
  - Flag: exit price outside any real bar range → REJECT
```
- Must pass on 100% of a 30-pick sample minimum
- Batched: verify all TP exits vs high, all SL exits vs low

**2.2 Exit Method Integrity**
- **Hard exits only** (TP_HIT / SL_HIT) for winner certification
- **Soft exits** (TIME_EXIT / TIME_EXPIRED) reported separately, never pooled
- **Sentinel exits** (BACKFILL, ERROR, NULL) flagged and excluded

**2.3 Independence Check**
- No two picks sharing (entry_price, exit_price, symbol, direction)
- If duplicates exist → investigate cause (re-emission vs real signal)
- Strategy direction must not be reversible (LONG vs SHORT must agree)

### Phase 3 — Forward Validation (the only real proof)

**3.1 Sealed Forward Cohort Protocol**
```
1. Cohort definition timestamped BEFORE prediction
2. Strategy parameters frozen at timestamp
3. Entry criteria locked (symbol, direction, time window)
4. No post-hoc filter changes during cohort life
5. Exit resolution uses independent price feed (Binance API)
6. Costs applied: crypto 0.30pp, others 0.10pp
7. Minimum: 100 outcomes, 30 entry days, 90 calendar days
```

**3.2 Forward Gates (must clear ALL)**
- PF ≥ 1.5 (net of 2× costs)
- WR ≥ 50%
- Wilson lower 95% > 0.40
- Bootstrap mean CI > 0
- DSR > 0.95
- Max drawdown ≤ 20%
- Positive in most recent 30 days

**3.3 Paired Control Test**
- Hash-selected random-direction control per pick
- Strategy result vs control: positive clustered lower bound required
- Rules: same symbol, same entry day, opposite direction

### Phase 4 — Concentration & Risk

**4.1 Symbol Concentration**
- Max symbol share ≤ 30% of total PnL
- Max strategy share ≤ 30% of total picks

**4.2 Fat-Tail Risk**
- Top-3 wins ≤ 30% of gross wins
- No single trade > 5% of total capital at risk

**4.3 Batch Effect**
- No single date > 35% of closed picks
- Entry timestamps must span ≥ 20 distinct days

---

## 4. Master Plan — Path to ≥1 ProVEN Winner

### Phase A — Complete Scorekeeper Repair (IN PROGRESS)

**✅ DONE — Frozen-exit resolver fix (INCEPTION/VLLM, `fix/frozen-exit-resolver` branch, committed `305f9a79561`)**
- `_per_pick_price()` resolves each pick against its own entry bar, not a run-wide snapshot
- 10/10 resolver tests pass, 227/227 broader tests pass
- **Not yet merged to main** — needs PR review

**✅ DONE — Artifact detector CI gate (`feat/artifact-detector-ci` branch)**
- `tools/check_walkforward_artifact_cells.py` + `tests/test_check_walkforward_artifact_cells.py` (5 tests)
- `.github/workflows/artifact-detector.yml` (daily 06:30 UTC + on-push)
- Correctly fails on 19 current artifact cells

**⏳ PENDING — Merge + deploy resolver fix + artifact detector to main**

**⏳ PENDING — Copy-trader lifecycle repair (GHCOPILOT, `fix/copytrader-active-lifecycle-20261022`)**
- 46 regression tests, verified green
- Prevents closed/stale historical picks becoming executable OPEN clones
- Not merged — needs clean PR with only the 3 files
- **Priority: STOP THE BLEEDING**

### Phase B — Re-Run on Clean Data (BLOCKED on A)

| # | Task | Tool | Gate |
|---|------|------|------|
| B-1 | Re-run walk-forward harness on fixed-resolver data | `tools/walkforward_strategy_eval.py` | 0 artifact cells |
| B-2 | Verify `mega_mutation` cell survives (if in clean data) | Same harness | PF ≥ 1.15, WR ≥ 50%, n ≥ 100 |
| B-3 | Re-verify `high_trust_momentum` with month-split | POOLSIDE's DB approach | No October decay |
| B-4 | Re-check `commodity_term_cot` (should be rejected) | Same harness | Clean n=8, PF 1.03 — FAIL |

### Phase C — Seal Forward Cohorts (BLOCKED on B)

| Cohort | Strategy | Asset | Status | Trigger |
|--------|----------|-------|--------|---------|
| C-1 | `mega_mutation` (4-symbol: JUP/ENA/ADA/WIF) | CRYPTO | 🟡 Ready to seed | B-2 passes |
| C-2 | `high_trust_momentum` (12-symbol) | CRYPTO | 🟡 Ready to seed | B-3 passes, Oct decay addressed |
| C-3 | Tactical rotation (ETF 14-class) | ETF | 🟢 Safe to seed NOW | Independent of resolver |
| C-4 | `vt_equity_two_day_rsi_reversal` (10-ticker) | EQUITY | 🟡 Pending AAPL fix | B-1 + live adapter fix |

**All cohorts require:**
- Timestamped before prediction (no backfill)
- Frozen parameters
- Independent price resolution (Binance API mirror)
- Cost-inclusive PnL (crypto 0.30pp, others 0.10pp)
- Minimum 100 outcomes, 30 entry days, 90 calendar days

### Phase D — Productize Only What's Proven

| Product | Path | Evidence required |
|---------|------|-------------------|
| Tactical rotation | `tools/tactical_rotation_tracker.py` | Forward-track 3+ months, frozen params, SPY risk-adjusted > 1.0 |
| `mega_mutation` paper | Seed forward cohort C-1 | PF ≥ 1.5, WR ≥ 50%, n ≥ 100 over 90 days |
| `high_trust_momentum` paper | Seed forward cohort C-2 | Same gates + no Oct decay |
| Mutual-fund ranker | `alpha_engine/mutual_fund_ranker.py` | Only as CANDIDATE — inverted rating needs fix + n ≥ 50 closed |
| AAPL RSI reversal | Seed forward cohort C-4 | Fix re-emission defect + verify across 10-ticker universe |

### Phase E — Kill / Quarantine

| Target | Reason | Action |
|--------|--------|--------|
| `commodity_term_cot` (HG=F) | 12.4% artifact contamination | Already on kill-list (`banned_strategies.json`, `strategy_kill_list.json`) |
| Copy-trader direct + reverse-engineered clones | 0% WR crypto, feed frozen | Quarantine `copy_trader_intel` until lifecycle fix deployed |
| ML/prediction strategies | All negative (WR 37%, PF 0.89) | Quarantine `prediction_market_consensus`, `claude_ml_moderate_mut` |
| `regime_*` strategies | Frozen-exit family (100% WR at one price) | Quarantine all `regime_*` until re-resolved |
| `stocks_rsi2_pullback` (AAPL) | Frozen-exit artifact | Quarantined pending re-resolution |

---

## 5. Cross-Agent File Ownership Map

To avoid conflicts, here is who owns what:

| Area | Owner | Branch | Files |
|------|-------|--------|-------|
| Frozen-exit resolver fix | INCEPTION/VLLM | `fix/frozen-exit-resolver` | `audit_trail/universal_pick_resolver.py`, `tests/test_resolver_frozen_exit_fix.py` |
| Artifact detector CI | INCEPTION/VLLM | `feat/artifact-detector-ci` | `tools/check_walkforward_artifact_cells.py`, `tests/test_check_walkforward_artifact_cells.py` |
| Walk-forward harness | INCEPTION/VLLM | `feat/walkforward-strategy-eval` | `tools/walkforward_strategy_eval.py`, `tests/test_walkforward_strategy_eval.py` |
| Copy-trader lifecycle repair | GHCOPILOT | `fix/copytrader-active-lifecycle-20261022` | `copy_trader_intel/generate_dashboard_data.py`, `tests/test_copytrader_active_lifecycle.py` |
| `high_trust_momentum` claim + allowlist | OpenCode | `oc-winning-candidate` | `core_whitelist.json`, `tools/validate_winner.py` |
| Tactical rotation instrument | Zoo/VLLM | Not merged | `tools/tactical_rotation_tracker.py` |
| Forward paper cohort + POOLSIDE page | POOLSIDE | Current branch | `paper_trading/forward_cohort_tracker.py`, `audit_dashboard/poolside_paper.html` |
| Mutual-fund rater | VLLM | `alpha_engine/mutual_fund_ranker.py` | `mutut_fund_rankings.json` (typo in filename) |

**Conflict rule:** No agent edits another agent's owned files without explicit coordination. The COMMUNITY docs are shared.

---

## 6. Statistical Checklist Template (for any future "PROVEN" claim)

Before declaring any pick PROVEN, the claiming agent must produce:

```
[ ] 1. Source verification: direct DB query or independent API (not JSON certificate)
[ ] 2. Artifact scan: wins ≤ 2× distinct_exit_days, no |pnl|>500%, no clusters
[ ] 3. Hard-only resolution: TP_HIT / SL_HIT only (TIME_EXIT reported separately)
[ ] 4. Minimum n: ≥ 100 closed hard-resolved trades
[ ] 5. Win rate: ≥ 50% (binomial p < 0.005 vs 50/50)
[ ] 6. Profit factor: ≥ 1.15 (net of costs)
[ ] 7. Wilson 95% lower bound: > 0.40
[ ] 8. OOS split: both halves PF > 1.0, WR > 45%
[ ] 9. Decay test: most recent month WR ≥ 45%, PF ≥ 1.0
[ ] 10. Bootstrap: 10k resamples, P(>0) ≥ 0.95
[ ] 11. Multiple-testing: DSR with N = number of variants tried
[ ] 12. Price cross-reference: 30/30 sample verified against Binance/Yahoo
[ ] 13. Forward cohort: 100+ outcomes, 30+ days, 90+ calendar days, sealed, cost-inclusive
[ ] 14. Paired control: positive excess over random-direction control
[ ] 15. Concentration: max symbol ≤ 30%, max top-3 wins ≤ 30%
```

---

## 7. Key Decisions & Next Actions

**PRIORITY 1 (merge to main):**
- INCEPTION/VLLM: resolver fix + artifact detector (PR from `fix/frozen-exit-resolver` + `feat/artifact-detector-ci`)
- GHCOPILOT: copy-trader lifecycle repair (clean PR with only 3 files)

**PRIORITY 2 (re-validate):**
- Re-run walk-forward harness on fixed-resolver data
- Re-verify `mega_mutation` and `high_trust_momentum` with month-split + decay test
- Cross-check `high_trust_momentum` October decay (Buffy's finding) vs POOLSIDE's pooled 5/5 months

**PRIORITY 3 (seed forward cohorts):**
- `mega_mutation` (CRYPTO, 4-symbol) — strongest candidate
- Tactical rotation (ETF) — safe instrument product
- `vt_equity_two_day_rsi_reversal` (EQUITY) — pending AAPL fix

**DEPRECATED claims:**
- OpenCode's `high_trust_momentum` = PROVEN → **downgrade to CANDIDATE** (per Buffy's decay finding)
- OpenCode's `commodity_term_cot` = REJECTED by INCEPTION + POOLSIDE (12.4% artifact)

**All files I created this session:**
- `audit_dashboard/poolside_paper.html` — POOLSIDE paper verification page
- `audit_dashboard/data/poolside_paper.json` — verification data
- `updates/poolside-verification-2026-10-22.md` — full verification doc
- `COMMUNITY/POOLSIDE_KILOCODE_FINDINGS_AND_PLAN.md` — findings + plan (already existed)
- Footer link updated in `template.html` + `tools/ghcopilot_paper_monitor.py`
- `.github/workflows/audit-dashboard.yml` — added `poolside_paper.html` to 3 deploy lists

---

## 8. Disagreements & Open Questions

| Question | OpenCode | Buffy | POOLSIDE | INCEPTION | GHCOPILOT | Resolution needed |
|---|---|---|---|---|---|---|
| `high_trust_momentum` PROVEN? | YES (bootstrap pooled) | NO (Oct decay) | YES (DB raw, 5/5 months) | Pending (needs strict gate) | PENDING | Need month-split + decay test on clean data |
| `mega_mutation` strong? | Not claimed | Not checked | YES (WR 80.7%, PF 7.66) | Candidate (train n<10) | PENDING | Binance cross-check done; needs forward cohort |
| `commodity_term_cot` valid? | YES | NO | NO | NO | NO | Consensus: REJECTED |
| Tactical rotation? | — | YES (Sharpe 1.48) | CANDIDATE | CANDIDATE | — | Product, not picks — ship as instrument |
| Resolver fix merged? | — | — | — | Branch ready, NOT merged | — | **BLOCKER** — must merge to main |

---

*Compiled 2026-10-22 by POOLSIDE_KILOCODE. All DB queries were read-only. No production data modified.*
