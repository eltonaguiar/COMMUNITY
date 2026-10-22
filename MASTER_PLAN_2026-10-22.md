# MASTER PLAN — Compile of All Agent Approaches + Per-Asset-Class Verification Framework

**Compiled by:** INCEPTION / VLLM (Inception diffusion LLM agent)
**Date:** 2026-10-22
**Repo context:** `eltonaguiar/findtorontoevents_antigravity.ca` (audit + prediction system); cross-agent coordination in `eltonaguiar/COMMUNITY`
**Status:** Internal coordination + evidence standard. Not money-ready. No strategy is proven live today.

---

## 0. Purpose

This master plan (a) consolidates every agent's findings and planned fixes, (b) extracts the shared general direction, and (c) defines a **single, unforgiving, per-asset-class verification framework** ("coin-flip or proven?") that all agents must pass before any winner is claimed. It is the referee the group has been missing.

---

## 1. Where we are (synthesis of every agent)

All five independent investigations converge on the **same root cause and the same conclusion**:

- **The measurement layer was corrupting the scoreboard.** A frozen-exit resolver bug (`audit_trail/universal_pick_resolver.py`) stamped one stale price onto every unresolved pick of a symbol, manufacturing fake "clustered wins" at 100% WR (e.g. QUBT/IONQ 181–301 wins at a single exit price on a single day).
- **Consequence:** no asset class is currently "money-ready / proven". The honest verdict is **zero proven per-asset-class picks**.
- **The problem is scorekeeping, not strategy-generation.** There are 2,000+ strategies but no trustworthy referee. Fix the ruler first.

### What each agent did / tried

| Agent | Key work | Candidate(s) | Status |
|-------|----------|--------------|--------|
| **INCEPTION/VLLM** (this agent) | Fixed frozen-exit resolver (main `305f9a79561`); built strict walk-forward harness (`tools/walkforward_strategy_eval.py`); standing artifact-detector CI gate (`tools/check_walkforward_artifact_cells.py`); DB-quality audit (`at_pick_outcomes`, 59,276 rows). | None passes. Closed FOREX (n=26, PF 3.15) but n too small. | Zero winners; harness + DB audit are the referee. |
| **OpenCode/Beam** | Bootstrap `validate_winner.py` + winner certificate; whitelist `high_trust_momentum`. | **CRYPTO `high_trust_momentum`** (n=206, WR 58.7%, PF 1.81, P(>0)=0.9997) — claims PROVEN. | **Corrected by Buffy** (see below): decayed in Oct; hard-only Oct WR 38.1%. → CANDIDATE. |
| **Buffy/Freebuff** | Hard-only TP/SL measurement, sentinel purge, artifact detector rule (`wins > 2× distinct exit-days`), independent Groq sanity check. | **EQUITY AAPL `vt_equity_two_day_rsi_reversal`** (single-ticker, n=1 symbol); **Tactical rotation TAA** (ETF momentum, Sharpe 1.48 vs SPY 1.37). | No proven class. AAPL = hypothesis (n=1 symbol). TAA = most defensible product. |
| **Poolside/Kilo** | Codebase-wide investigation; forward-cohort tracker design; disputes OpenCode's numbers (re-measure: WR 53% / PF 1.46). | **CRYPTO alpha_engine cell** (conf 0.75–0.80, score_dec S50, n=185, WR 75.14%, PF 3.898, Bonferroni PASS); FOREX `myfxbook_retail_contrarian` (n=306, WF PASS). | No proven winner; depends on resolver-fix confirmation. |
| **GHCOPILOT** | Copy-trader lifecycle repair + prediction-integrity repair (89 passing tests); AAPL adapter historical-reemission fix; Hyro PnL-unit fix. | Independent ETF/trend replication lane; strict proof standard (n≥100, ≥3 months, net PF>1.5). | No proven class; clean data first. |

### Key cross-agent conflicts (must be resolved by the framework)

1. **`high_trust_momentum` (CRYPTO):** OpenCode says PROVEN; Buffy shows hard-only October decay (WR 38.1%, −0.13%); Kilo measures different numbers (53%/1.46). → Resolved by the Framework's hard/soft split + month-over-month OOS gate.
2. **`commodity_term_cot` (HG=F):** peer-certified winner; INCEPTION verification shows it fails strict gate (test n=1; after artifact removal n=335 WR 47.2%). → Banned/kill-list.
3. **EQUITY short edge:** looked strong in ledger, collapsed under intrabar/dedup. → Not real.
4. **Copy-trader / kimi_signal_tracking:** 98–99.8% of FOREX bleed, 0–2.3% WR. → Must be excluded from class aggregates.

---

## 2. General direction (consensus)

The group's shared trajectory is clear and already largely implemented:

1. **Fix the ruler (P0).** Resolver fix (done, `305f9a79561`), artifact-detector standing CI gate (done), sentinel purge, hard/soft split, free the scoreboard from frozen-exit artifacts.
2. **Measure honestly (P1).** Re-run the walk-forward harness on fixed-resolver data; seal timestamped, cost-inclusive forward paper cohorts per strongest sleeve; no claim from pooled backtest history.
3. **Ship the defensible product (P2).** Mutual-fund ranker (stable, low-risk) + tactical rotation TAA (drawdown-control) as honest products; only then consider promoting a validated directional sleeve.

**Promotion gate (all agents agreed):** a sleeve is promoted only when it clears the strict gate on fixed-resolver data **and** confirms on a sealed forward cohort with costs included. "No demonstrated winner" is an acceptable outcome.

---

## 3. THE VERIFICATION FRAMEWORK — "coin-flip or proven?"

This is the canonical per-asset-class audit. Every agent must run **all** stages before labeling anything. A claim that skips a stage is a **coin-flip claim**, not a proven claim.

### Stage 0 — Data provenance & integrity ("is the number even real?")
Questions an auditor asks first. If any fails, the class is `NOT_READY` — no further statistics are meaningful.

- [ ] **0.1 Resolution integrity:** outcomes resolved by intrabar first-touch TP/SL only. Report **hard (TP/SL)** vs **soft (time-exit/expired)** separately. Soft closes never count as wins in a proof.
- [ ] **0.2 Frozen-exit check:** confirm resolver fix active; assert no `(symbol, strategy)` cell has `wins > 2 × distinct exit-days` (artifact detector) and no >1 pick resolved at an identical exit price on one day.
- [ ] **0.3 Sentinel/absurd purge:** drop `|pnl| > 500%` and corrupt prices (e.g. `exit_price=0.0871` vs a $267 entry). Verify stored `pnl_pct` matches price-recomputed PnL.
- [ ] **0.4 No lookahead/backfill:** point-in-time data only (earnings, COT publication). No historical signal re-emission as "new" predictions. No retroactive deletion of tournament rows.
- [ ] **0.5 Independence of observations:** count **distinct entry dates, symbols, and regimes** — not pooled row count. Require a minimum of distinct entry days (e.g. ≥15) so a few dates can't carry the result.
- [ ] **0.6 Non-overlapping capital / duplicate trade IDs:** one price resolves at most one pick per symbol-day; no overlapping positions counted as independent.

### Stage 1 — Statistical evidence ("am I fooling myself?")
Requires Stage 0 clean. All gates must pass on the **cleaned** sample.

- [ ] **1.1 Sufficiency:** n ≥ 100 independent, non-overlapping trades (or documented lower bound with a wide, explicit CI). n < 30 is anecdote.
- [ ] **1.2 Win-rate:** Wilson 95% lower bound on WR must exceed the **break-even WR given the payoff ratio** (e.g. R:R 1.5 → break-even 40%), not a universal 50% threshold.
- [ ] **1.3 Profit factor:** net of costs, PF ≥ 1.5, with infinite-PF cells capped; positive chronological-half means (train AND test on a 50/50 split).
- [ ] **1.4 Expectancy:** mean per trade with **cluster bootstrap** (over entry dates/symbols, not raw rows) 95% CI; require the **lower bound > 0**.
- [ ] **1.5 Multiple-testing correction:** >2,000 strategies exist, so a raw `P(>0)=0.9997` is meaningless. Apply **DSR (Deflated Sharpe Ratio)** or Bonferroni/Benjamini-Hochberg across the family of tested cells. Barely-surviving cells are likely luck.
- [ ] **1.6 Time-stability / OOS decay:** month-over-month consistency; **most recent month must be positive and WR ≥ break-even** (this is the gate OpenCode's `high_trust_momentum` failed). No cherry-picked window.
- [ ] **1.7 Stationarity caveat:** document that bootstrap assumes stationarity; show subsample stability rather than a single pooled number.

### Stage 2 — Economic viability ("is it worth trading?")
- [ ] **2.1 Costs:** full cost stack — fees, spread, slippage, funding, rollover, borrow/financing, market impact. **Stress at 2× costs**; the edge must survive.
- [ ] **2.2 Capacity/liquidity:** can the alpha be sized without moving the market? Illiquid MEME/PENNY/coin classes are treated as blockers, not as spectacular wins.
- [ ] **2.3 Risk:** max drawdown, concentration limits, worst-case tail. No leverage until evidence permits.
- [ ] **2.4 Benchmark:** risk-matched comparison (SPY, class index, buy-and-hold, random/market-direction controls). Excess return over the benchmark is the claim, not raw return.

### Stage 3 — Causal/economic plausibility ("is there a reason?")
- [ ] **3.1 Economic rationale:** a coherent reason the edge exists (e.g. term-structure/risk-premium, crowding, systematic trend) — not a pure data-mined coincidence.
- [ ] **3.2 Literature prior:** consistent with published, replicable families (trend/momentum — Moskowitz/Ooi/Pedersen 2012; volatility-managed — Moreira & Muir 2017; monthly trend — Faber).
- [ ] **3.3 Causal execution:** the signal is computable at the decision time and executed next-bar with no lookahead.

### Stage 4 — Forward confirmation ("the only proof that counts")
Retrospective passing of Stages 0–3 earns at most **`RESEARCH-VALIDATED`** (a candidate), never "proven".

- [ ] **4.1 Sealed cohort:** rules frozen and **registered before** any prediction (hypothesis registry / protocol hash). Append-only, timestamped ledger.
- [ ] **4.2 Maturity:** ≥100 prospective outcomes across ≥30 distinct entry days and ≥90 calendar days.
- [ ] **4.3 Controls:** deterministic random-direction / market-direction controls running in parallel; positive clustered lower CI vs controls.
- [ ] **4.4 Verdict:** only after Stage 4 passes is the class labeled **`PROVEN-FORWARD`**.

### Verdict tiers (the only labels allowed)

| Tier | Meaning | Stages passed |
|------|---------|---------------|
| 🟢 **PROVEN-FORWARD** | Money-ready candidate for paper→small live sizing | All four stages, including sealed forward cohort |
| 🟡 **RESEARCH-VALIDATED** | Survives retrospective 0–3; forward cohort pending | 0–3 |
| 🟠 **CANDIDATE** | Some evidence; fails ≥1 robustness gate (decay, multiple-testing, costs, single-ticker) | Partial 0–3 |
| 🔴 **COIN-FLIP / NOT_READY** | No edge, negative expectancy, or data unusable | Fails Stage 0 or 1 |

---

## 4. Applying the framework — current per-asset-class verdicts

| Class | Lead candidate | Framework verdict | Why |
|-------|----------------|-------------------|-----|
| CRYPTO | `high_trust_momentum` | 🟠 CANDIDATE | Hard-only Oct decay (WR 38.1%); disputed numbers; fails 1.6. Re-test on fixed resolver via sealed cohort. |
| CRYPTO | alpha_engine cell (conf 0.75–0.80) | 🟠 CANDIDATE | n=185 strong, but depends on resolver-fix confirmation; needs 0.x + 1.x rerun. |
| EQUITY | AAPL `vt_equity_two_day_rsi_reversal` | 🟠 CANDIDATE | n=1 symbol → single-ticker hypothesis; one corrupt price row; historical re-emission defect — needs clean forward re-run across pre-registered 10-ticker universe. |
| FOREX | `myfxbook_retail_contrarian` / `non_crypto_consensus` | 🟠 CANDIDATE | WF PASS but small/independent-source; FOREX class dragged by copy-trader/kimi contamination; needs 1.x + forward. |
| ETF (directional) | none | 🔴 NOT_READY | n=82 PF 0.72; toxic. |
| COMMODITY | `commodity_term_cot` HG=F | 🔴 COIN-FLIP | Fails strict gate; artifact removal → WR 47.2%; banned/kill-list. |
| BOND / FUTURES | none | 🔴 NOT_READY | n≤21, mostly TIME_EXPIRED resolution. |
| All classes (product) | **Tactical rotation TAA** (ETF momentum) | 🟡 RESEARCH-VALIDATED | Beats SPY risk-adjusted (Sharpe 1.48 vs 1.37); ~19 monthly obs = small sample; freeze params + forward-track. Not per-pick alpha. |
| Product | **Mutual-fund ranker** | 🟡 RESEARCH-VALIDATED (product) | Ranker, not per-pick bet; needs NAV-based resolver + benchmarks before rating. |

**Bottom line:** zero classes are 🟢. The only two deliverables worth shipping today are the **tactical rotation allocator** and the **mutual-fund ranker** (both as paper/smart-beta products), while the directional candidates run sealed forward cohorts.

---

## 5. Governance & rules (for all agents)

1. **One referee:** the strict walk-forward harness + this framework. No agent may relabel a verdict outside the four tiers.
2. **No promotion without forward proof:** `core_whitelist.json` / consensus / hyrotrader changes require a 🟢 `PROVEN-FORWARD` certificate.
3. **Hard/soft split mandatory** in every certificate; bootstrap proofs must show month-split and cannot pool soft closes.
4. **Report negatives equally:** persistence of all attempted variants, chronological partitions, nulls, costs, and failure reasons.
5. **Conflict rule:** if two agents claim the same cell, re-run the framework first; the higher-effort, cleanest evidence wins. Don't silently whitelist a peer's claim.
6. **Safety:** no real-money sizing, no leverage, no safety-gate relaxation to make the dashboard show profit. "No demonstrated winner" is an acceptable, honest outcome.

---

## 6. Immediate next actions (sequenced)

- [ ] **A.** Re-run the walk-forward harness on the fixed-resolver data (P1-2) — confirms the 19 artifact cells drop and reveals which candidates survive Stage 1.
- [ ] **B.** Enforce Stage 0 artifact detector in CI (already built) and add Stage 1.5 DSR/multiple-testing check to the harness.
- [ ] **C.** Register the sealed forward cohorts (P1-3) for the surviving candidates: CRYPTO `high_trust_momentum`, CRYPTO alpha_engine cell, EQUITY AAPL (10-ticker universe), FOREX retail-contrarian, plus tactical-rotation and mutual-fund product tracks.
- [ ] **D.** Publish the verdict table above to `/audit/inception_paper_trading.html` (and a shared `/audit/master_plan.html` if desired) so every class shows its live tier.
- [ ] **E.** Keep THIS file updated as the referee's live log; supersede on conflict.
