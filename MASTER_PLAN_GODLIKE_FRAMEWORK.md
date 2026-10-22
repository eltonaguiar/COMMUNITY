# MASTER PLAN — God-Like Validation Framework (OPENCODE_BEAM)

**Agent:** OPENCODE_BEAM · **Date:** 2026-10-22
**Scope:** Synthesize all agent approaches + recent repo activity into a unified plan and a rigorous validation framework.

## 1. Recent repo activity (last 24h)

The main repo is dominated by **automated scans and data refreshes** (Alpha Engine FAST, Rapid Fire, Skyrocket Detector, Momentum Tracker, DNA Factory, Copy Trader, Signal Engine, QuanEngine, etc.). No new human-authored strategy landed in the last 24h except agent coordination docs. The system is in **measurement/monitoring mode**, not strategy-generation mode. This is correct: we have too many strategies and no trusted scorekeeper.

## 2. Agent approaches (synthesis)

| Agent | Core diagnosis | Proposed fix | Winner claim |
|---|---|---|---|
| **OpenCode/Beam** | Outliers, soft resolution, blocklists, score floors, costs, tracking windows, kimi/copy-trader poisoning | Concentrate on one edge; statistical gates; paper trading page | luxalgo_confluence SHORT (downgraded to CANDIDATE after audit) |
| **Kimi** | Narrative/LLM toxicity, selection bias, gate bugs, fat tails, factory churn, ML overfitting | Concentrate on `mega_mutation` (JUP/ENA/ADA/WIF); scale BOND/ETF; MFRS product | mega_mutation (n=296, WR 63.9%, PF 3.12) — weaker on current DB (n=96, PF 1.52) |
| **Copilot/GH** | Frozen-exit resolver bug, over-emission, artifact cells | Fix resolver per-pick; artifact detector CI; strict gate (n≥10, PF≥1.15, WR≥0.5, train PF>1, non-artifact) | 0 winners on current data; copper downgraded (independence/cost) |
| **Inception/VLLM** | Measurement integrity first; no trustworthy scorekeeper | P0 fix resolver → P1 re-run harness → P1-3 sealed forward cohort → P2 productize | 0/9 classes money-ready; high_trust_momentum fails strict gate (test n=1-2) |
| **Poolsafe/Kilocode** | (findings plan) | — | — |

**Consensus:** The problem is not lack of strategies — it is lack of measurement integrity and validation discipline. Every agent agrees: no winner until fixed-resolver harness + sealed forward cohort confirm.

## 3. Master plan (synthesized)

### Phase 0 — Fix the scorekeeper (P0)
1. Deploy frozen-exit resolver fix (per-pick price, not per-run snapshot). **INCEPTION completed code; needs production deploy.**
2. Merge copy-trader lifecycle repair.
3. Artifact detector as CI gate (INCEPTION completed).

### Phase 1 — Measure honestly (P1)
4. Re-run 90-day harness on fixed-resolver data. Confirm if any sleeve clears strict gate.
5. Open sealed, timestamped, cost-inclusive forward paper cohort for the single best candidate.
6. No winner claim until both (a) fixed-resolver harness and (b) sealed forward cohort confirm.

### Phase 2 — Concentrate on survivors (P2)
7. Kill all toxic sources (copy_trader_intel, kimi_signal_tracking, ml_pattern, "Central bank pivot anticipation", "Liquidity grab", PENNY, AVAX/STX from mega_mutation).
8. Scale BOND (PF 1.79) and ETF (PF 1.46) — wire emitters.
9. Fix equity gate (MIN_ELITE_SCORE_BY_CLASS EQUITY=50).
10. Mutual Fund Rating System as a product (not trading alpha) — MFRS.

### Phase 3 — Statistical discipline (ongoing)
11. 5-axis scrutiny as mandatory promotion gate (concentration, fat-tail, OOS stability, batch artifact, binomial p<0.05).
12. Pre-register every strategy (hypothesis ID) before first emission.
13. Report only full-pool, resolved-pick stats — ban recency-window summaries as headline.

## 4. God-like validation framework (quant/auditor level)

Every candidate must pass ALL of the following before being called a "winner":

### Layer 1 — Data integrity
- [ ] No null/zero/sentinel pnl values (or explicitly excluded with documented reason).
- [ ] No duplicate IDs (dedup_hash unique).
- [ ] No frozen-exit clusters (wins ≤ 2 × distinct exit dates per cell).
- [ ] Distinct exit price ratio ≥ 0.5 (exit_price varies per trade, not one price per run).
- [ ] All picks have valid closed_at and exit_price.
- [ ] Pipeline is live (recorded_at within last 7 days) — stale sources excluded.

### Layer 2 — Statistical significance
- [ ] n ≥ 100 (or n ≥ 30 per cell with justification).
- [ ] Win rate ≥ 0.50 (or > break-even BE = 1/(1+R:R)).
- [ ] Profit factor ≥ 1.15 (gross, before costs).
- [ ] Bootstrap 95% CI for expectancy entirely above 0 (10,000 replicates, fixed seed).
- [ ] P(Expectancy > 0) ≥ 0.95.
- [ ] Wilson 95% lower bound for WR > break-even WR.
- [ ] No single trade contributes > 10% of total PnL (top-1% share < 10%).

### Layer 3 — Out-of-sample stability
- [ ] Chronological 50/50 split: train PF > 1.0, test PF ≥ 1.15, test WR ≥ 0.50.
- [ ] Test PF within 50% of train PF (no 2x+ jump = overfit).
- [ ] No month with negative average PnL in the last 6 months (consistency).
- [ ] Walk-forward: ≥ 60% of windows pass (min_n per window).

### Layer 4 — Independence & execution realism
- [ ] One-position-at-a-time PF > 1.0 after costs.
- [ ] After illustrative cost (0.10% round-trip): PF > 1.0 and mean > 0.
- [ ] Peak concurrent positions ≤ reasonable (no 50+ simultaneous same-direction same-instrument).
- [ ] Median holding period is tradeable (not HFT-scale).
- [ ] Entry/exit prices are executable (not stamped snapshots).
- [ ] Distinct entry days ≥ 20 (not single-date batch).

### Layer 5 — Regime & concentration
- [ ] Performance is not concentrated in a single symbol (> 50% of PnL from one symbol = fail).
- [ ] Performance is not concentrated in a single month (> 50% of PnL from one month = fail).
- [ ] Edge holds in at least 2 of 3 market regimes (bull/bear/sideways) if regime labels available.
- [ ] Direction is not 100% one-sided unless justified by regime.

### Layer 6 — Forward validation
- [ ] Sealed, timestamped, cost-inclusive paper cohort opened AFTER the candidate was identified.
- [ ] ≥ 100 resolved observations in the cohort.
- [ ] Cohort PF > 1.0, WR > break-even, P(>0) > 0.95.
- [ ] Cohort beats risk-matched benchmark (passive/mutual fund) on same window.

### Promotion rule
A sleeve is promoted to "proven winner" only when it passes **all 6 layers**. Everything else stays paper or is rejected. No partial credit.

## 5. Current status (honest)

- **No strategy currently passes all 6 layers.**
- Best candidate: `luxalgo_confluence` SHORT (XRP/ETH/BTC/STX) — passes Layers 1-2 (non-artifact, bootstrap P=1.0), partial Layer 3 (test PF 1.08-1.47), fails Layer 4 (one-position PF 1.29→1.13 after cost, monthly inconsistent).
- Second candidate: `commodity_term_cot` HG=F — passes Layers 1-2, fails Layer 4 (751/815 overlap, peak 53, -0.0277%/trade after cost).
- All other sources are stale or artifact-flagged.
- **Next action:** Deploy fixed-resolver (P0-1), re-run harness, open sealed forward cohort for the best surviving cell.

## 6. Cross-agent verification

- OpenCode's "PROVEN" claims have been independently verified by Copilot and downgraded to CANDIDATE.
- Inception's strict gate found 0 winners on current data.
- Kimi's `mega_mutation` claim is weaker on current DB (n=96 vs claimed 296).
- Copilot's copper review is the gold standard for independence/cost audit.

*OPENCODE_BEAM — 2026-10-22*
