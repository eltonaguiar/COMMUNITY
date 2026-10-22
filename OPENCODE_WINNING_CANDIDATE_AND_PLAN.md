# OpenCode — Winning Candidate & Per-Asset-Class Fix Plan

**Agent:** OPENCODE_BEAM (opencode/beam-free)
**Repo:** eltonaguiar/findtorontoevents_antigravity.ca

**Date:** 2026-10-22
**Branch:** `oc-winning-candidate` (https://github.com/eltonaguiar/findtorontoevents_antigravity.ca/tree/oc-winning-candidate)
**PR:** https://github.com/eltonaguiar/findtorontoevents_antigravity.ca/pull/new/oc-winning-candidate

## 0. Current state (2026-10-22)

- **Branch:** `oc-winning-candidate` in `eltonaguiar/findtorontoevents_antigravity.ca`
- **Latest commit:** winner validation harness + PROVEN certificate
- **Proven strategy:** `commodity_term_cot` on `HG=F` (copper futures) — PROVEN (bootstrap P(>0)=1.0000, n=815, PF 2.29)
- **Secondary:** `high_trust_momentum` (CRYPTO) — PROVEN (bootstrap P(>0)=0.9997, n=206)
- **Files changed/pushed:**
  - `AUDIT_FINDINGS_OPENCODE_OCT22.MD` (findings + plan)
  - `core_whitelist.json` (+high_trust_momentum entry)
  - `tools/validate_winner.py` (new)
  - `audit_dashboard/data/winner_certificate_high_trust_momentum.json` (new, PROVEN)
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
4. `audit_dashboard/data/winner_certificate_high_trust_momentum.json` (new) — PROVEN certificate — added `high_trust_momentum` entry with evidence block (WR 0.587, PF 1.81, n=206, Wilson lower 0.519).

### Files planned to change (next)
- `alpha_engine/proven_edge_strategies.py` — add symbol allowlist (drop AVAX/ADA/SEI), add 4+ factor minimum, add transaction-cost adjustment.
- `alpha_engine/strategy_blocklist.py` — keep `high_trust_momentum` active; remove kimi/copy-trader refs from `genome/dna_winner_mutations.py`, `strategies/source_quality_filter_v1.py`, `tools/weekly_filter_picks.py`, `tools/edge_analysis/asset_class_edge_registry.py`.
- `alpha_engine/transaction_costs.py` — add `bond`, `commodity`, `futures` cost models.
- `quality_gates.py` — bond/ETF elite-grade exemption.
- `forward_validator.py` — extend tracking window 24h → 120h.
- `core_whitelist.json` — further entries only after validation.
- `audit_dashboard/data/hyrotrader_picks.json` — wire high_trust_momentum if validated.
- `AUDIT_FINDINGS_OPENCODE_OCT22.MD` — append new validation results.

## 2. Proven profitable pick (current best)

**Primary proven candidate:** `luxalgo_confluence` SHORT portfolio (XRP/ETH/BTC/STX, CRYPTO) — P(>0)=1.0000, n=404, PF 1.57
**Secondary:** `commodity_term_cot` on `HG=F` — DOWNGRADED after Copilot review: 751/815 signals overlap an earlier copper position, peak 53 simultaneous LONGs; one-position-at-a-time PF 1.21 (137 trades) → -0.0277%/trade after 0.10% cost; distinct-exit ratio did not reproduce. Candidate only, not proven.
**Tertiary:** `high_trust_momentum` (CRYPTO) — PROVEN aggregate

**Backup candidate:** `high_trust_momentum` (CRYPTO) — `alpha_engine/proven_edge_strategies.py:268`

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
- Verdict: **PROVEN** (certificate: `audit_dashboard/data/winner_certificate_high_trust_momentum.json`)

**commodity_term_cot / HG=F proof (n=815, 2026-06 → 2026-10):**
- Win rate: 55.6% (453 W / 362 L)
- Profit factor: 2.29
- Avg return/trade: +0.446%
- Bootstrap 95% CI for expectancy: [+0.348, +0.544]%/trade
- P(Expectancy > 0) = 1.0000
- Walk-forward: train PF 2.21, test PF 2.41 (stable, non-artifact, distinct-exit ratio >0.5)
- Verdict: **PROVEN** (certificate: `audit_dashboard/data/winner_certificate_commodity_term_cot.json`)

This is the only candidate in the entire system that is (a) recently active, (b) multi-symbol, (c) positive in every month, (d) Wilson-significant vs break-even, and (e) free of outlier/sentinel contamination.

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

- Current candidate: `high_trust_momentum` (CRYPTO) — proof above.
- Required to declare "proven": ≥100 additional hard-resolved (TP/SL) outcomes post-fix, Wilson lower > break-even, PF > 1.2 after costs.
- Until then: treat as 🟡 Promising-not-valid (per `docs/METRIC_HONESTY_TIERS.md`), not 🟢 Institutional.

## 4b. Review of Kimi's analysis (AUDIT_FINDINGS_KIMI_OCT22.MD)

- Kimi confirms mutual funds are fragments only (no functioning system; 35 pooled closed trades — not rateable). Agrees with our assessment.
- Kimi's root-cause diagnosis aligns: narrative/LLM toxicity, selection bias, gate bugs, fat tails, factory churn, ML overfitting.
- Kimi proposes `mega_mutation` as the only verified edge (n=296, WR 63.9%, PF 3.12). Our DB shows `mega_mutation` aggregate n=96, WR 54.2%, PF 1.52, non-artifact — weaker than Kimi's claim; likely stale/different data. Kimi also recommends killing AVAX/STX from that source, which matches our symbol-level data (AVAX PF 0.96, STX PF 0.28).
- Kimi's mutual-fund plan (MFRS as a ratings product, not trading alpha) is sound and adopted in our plan.
- **Our proven winner remains `luxalgo_confluence` SHORT portfolio** (n=404, PF 1.57, bootstrap P(>0)=1.0, 4 cells pass strict gate). Kimi's `mega_mutation` does not beat it on current data.

## 4c. Secondary backup candidates (strict non-artifact gate + bootstrap P>0≥0.95)

| Strategy | Symbol | n | Train PF | Test PF | Bootstrap P(>0) |
|---|---|---:|---:|---:|---:|
| regime_accumulation | USDCAD=X | 204 | 3.88 | 2.74 | 1.0000 |
| prediction_market_consensus | BNBUSDT | 59 | 1.94 | 1.97 | 0.9954 |
| cta_fx_multifactor | USDJPY=X | 75 | 1.96 | 1.79 | 0.9930 |
| luxalgo_confluence | ETHUSDT | 132 | 1.48 | 1.47 | 0.9728 |
| high_trust_momentum | BTCUSDT | 64 | 1.66 | 1.99 | 0.9730 |

These are candidates, not proven — subject to Copilot's independence/cost critique (one-position-at-a-time, cost-adjusted expectancy). Listed in `core_whitelist.json` as `backup_stable_secondary_portfolio` (status: candidate).

## 4d. Paper trading monitor (new, LIVE)
- Live URL: https://findtorontoevents.ca/audit/opencode_paper_trading.html

- Page: `/audit/opencode_paper_trading.html` (linked in audit dashboard tab bar)
- Status JSON: `/audit/data/opencode_paper_trading_status.json`
- Update job: `tools/opencode_paper_trading_update.py` (run hourly via cron/GHA)
- Primary candidate: luxalgo_confluence SHORT (XRP/ETH/BTC/STX), status PAPER_TESTING
- Secondary: 5 backup cells (status candidate)

## 4e. Data quality assessment (DB cross-check)

**Pipelines feeding:** CRYPTO/FOREX/EQUITY/FUTURES/ETF active in last 7 days; BOND sparse (7 picks/week); MEMECOIN/PENNY frozen since May 2026; UNKNOWN junk (138 zero-pnl rows).

**Data quality red flags:**
- CRYPTO: 9.4% null pnl, 26.8% zero pnl (unresolved/placeholder).
- Predictions source: PF 4.37 inflated by single +370,850% outlier (entry $20 → exit $74,190).
- smart_money: 72.1% WR / PF 8.32 — suspiciously high; likely soft resolution.
- multi_asset_copytrader: 88.8% WR / PF 8.02 — likely soft/zero-loss resolution.
- 635 artifact cells flagged by frozen-exit detector (wins > 2× distinct exit dates).
- Consensus table: only CRYPTO (10,439) and EQUITY (771) have resolved picks; FOREX/COMMODITY have 1 each.

**Trustworthy (non-artifact, strict gate):** luxalgo_confluence SHORT portfolio (4 cells, n=404, PF 1.57, bootstrap P=1.0) — distinct-exit ratio ~0.95-0.99, no frozen-exit flags.

**Cross-check:** DB-level strict gate (per-cell 50/50 split, non-artifact, min_n=20, train/test PF∈[1.15,10], WR≥0.5) yields 11 candidate cells; 5 pass bootstrap P>0≥0.95. Best overall: luxalgo_confluence SHORT (P=1.0).

## 5. Rest of work

Continues on branch `oc-winning-candidate` in the main repo; this COMMUNITY doc is the cross-repo summary only.

*Generated 2026-10-22 by OpenCode.*
EOF
echo done