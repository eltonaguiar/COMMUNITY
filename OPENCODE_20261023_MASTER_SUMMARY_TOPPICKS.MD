# OPENCODE_BEAM — Master Summary: Work, Plan, Top Picks per Asset Class, and How the Justification Works

> **⚠️ NOT FINANCIAL ADVICE (NFA).** Research and education only. Not a recommendation to buy or sell any security, fund, or account. Past performance does not guarantee future results. Do your own research (DYOR).

**Labels policy (Grok 9-gate protocol):** only `MONEY-READY` / `CANDIDATE` / `FAIL` are allowed. **Nothing is MONEY-READY** — no strategy has passed all 9 gates.

---

## 1. What we did (work explanation)

Since 2026-10-22, OPENCODE_BEAM:

1. **Found 3 real P/L bugs** in the /audit scoreboard (numbers from DB audit):
   - **Duplicate trades** — same trade under different UUIDs (IONQ: 64 rows / 7 distinct) inflates n up to 5.2×; regime_mild_bear SHORT EQUITY win-rate drops 54.1% → 38.5% after dedup.
   - **Batch-closes** — 13,682 picks closed within seconds (2026-05-10: 11,381 at 03:16:00, `RESOLUTION_TIMEOUT_NULL_TS`; 2026-04-11: 2,301 in 15s) = 21.2% of all closed picks.
   - **Lookahead closes** — 1,239 picks closed <2 minutes after entry (impossible real fills).
   - Tests written: `tests/test_artifact_exclusion.py` (10/10 pass).
2. **Refuted my own earlier BTC momentum claim** after Grok + GHCOPILOT independent rebuilds: daily mark-to-market MDD is **−80%**, not 12.5%; MC 77th pct (gate ≥95); DSR≈0 at N=65; does **not** beat holding BTC. Label: **FAIL**. Retraction note: `OPENCODE_20261022_2359.MD`.
3. **Tested 6 published BTC strategies** (200d/300d SMA, golden cross, RSI, dual momentum, 12m momentum) — all failed multiple gates.
4. **Ran a 118-fund walk-forward** (2005–2024, 19 year-ends, fees + 0.20% switch, 4,000-run bootstrap): **no fund-picking rule beats the cheap index with significance**. Only "YES" arms are holding cheaper S&P 500 vehicles (VOO/FXAIX vs SPY) = fee saving, not skill. Obscure-winner hunt found MIDSX (CAGR 0.05%, MDD −89.7%) = disaster. See `OPENCODE_20261023_FUND_WALKFORWARD.MD`.
5. **Documented everything** with NFA on pages/docs: https://findtorontoevents.ca/audit/opencode_paper_trading.html · `updates/2026-10-22-beat-index-plan.md` · `updates/2026-10-23-fund-selection-walkforward.md`.

---

## 2. Top picks per asset class (deduped + artifact-excluded October 2026 DB picks)

All are **CANDIDATE** (or FAIL), never MONEY-READY. Per-pick stats are post-dedup, post-batch-close-removal.

| Asset class | Top pick(s) | Direction | n | PF (net) | Label | Why this one (justification) |
|---|---|---|---|---|---|---|
| **CRYPTO** | prediction_market_consensus | SHORT | 682 | 2.11 | CANDIDATE | Largest clean sample in crypto; PF>1.5 with room above 1.3×-costs buffer; short side aligns with mean-reversion edge (bears fade faster than bulls) |
| CRYPTO (alt) | rapid_momentum_filter_mut | SHORT | 55 | 2.59 | CANDIDATE | Highest PF of liquid crypto shorts; small n is the limiter |
| CRYPTO (alt) | cvd_divergence | SHORT | 42 | 2.60 | CANDIDATE | Flow-based (order-book) logic ≠ price momentum → less correlated with other crypto picks; n small |
| CRYPTO (alt) | luxalgo_confluence | SHORT | 206 | 1.65 | CANDIDATE | Decent n; PF comfortably >1.5; MDD 85.6% (closed-trade) needs daily-MTM re-check before any upgrade |
| **BOND** | bond_yield_curve_slope | LONG | 18 | 9.44 | CANDIDATE | Massive PF; fundamental logic (curve steepening ≠ noise); **limiter: n=18 < 100** — most likely a regime-specific fluke until n grows |
| **FOREX** | forex_zscore_200d_fade | SHORT | 207 | 1.44 | CANDIDATE | Mean-reversion vs 200d fair value; PF 1.44 < 1.5 → needs fee-sensitivity proof; n is good |
| **EQUITY** | *(none yet)* — mega-cap above-200d / RSI(2)<10 pattern | LONG bias | 7 names | not gated | research lead | All 7 mega-caps show positive expectancy above 200d vs negative below; **not yet through 9-gate harness** — no label |
| **ETF** | hold-cheapest broad index (VOO / FXAIX / VFV.TO / XUS.TO) | BUY-AND-HOLD | — | vs SPY: CI [+0.02,+0.19] / [+0.10,+0.83] | CANDIDATE (fee edge only) | The only statistically significant "edge" we found = lower fee, not timing skill |
| **COMMODITY** | HG=F term-structure COT | LONG/SHORT rotate | — | — | **FAIL** (overlap) / class REHAB | Overlapping-window violation found; class status REHAB per dashboard |
| **FUTURES** | — | — | — | — | **BLOCKED** | PF 0.29 / WR 46.1% on Forex PR#6 gate context; futures remain blocked |
| **INDEX_STOCK** | — | — | — | — | thin n | Sample-size thin, no label |

**Sector rotation (equity basket, 9 SPDRs):** +1.5%/yr avg vs SPY, beat 53% of years, but 95% CI [−5.4, +7.0] includes zero → **CANDIDATE at best, not proven**. Runs on paper alongside the fund.

**Overall standing answer to "can we beat S&P 500?":** After ~150 strategies across asset classes, **no proven yes**. The evidence-backed answer for real money remains a low-fee all-in-one index fund (Canada starter: XEQT or VBAL on Wealthsimple TFSA from $1; cheapest S&P in CAD: XUS.TO 0.07% / VFV.TO 0.09%).

---

## 3. How the justification logic works (ELI5 of the 9 gates)

Imagine kids on a playground claiming "my coin-call game always wins." We don't trust the story — we run nine checks:

1. **Enough rounds (n≥100).** Ten flips that go your way is luck. A hundred starts to mean something. Bond pick n=18? It's a kid who won 10 tosses once.
2. **Big enough wins vs losses (PF≥1.5 net).** For every $1 you risk, you should make at least $1.50 after paying the casino (fees). Less than that, the house eats you alive.
3. **Even the pessimistic view wins (PF CI-low≥1.2).** We re-simulate the results 4,000 ways. Even in bad versions of the past, you're still making ≥$1.20 per $1 risked. If the "bad luck" version loses, it's not a real edge.
4. **Check the account every day, not just when you sell (daily MTM MDD≤20%).** If you hold Bitcoin and it's down 80% *right now*, that counts — even if you haven't sold. (This is exactly where my BTC claim died: closed-trade view said 12.5%, daily view said −80%.)
5. **Would random timing do as well? (Random-entry MC ≥95th pct).** We try 2,000 random buy dates with the same hold length. Your real entry dates must beat 95% of them. Otherwise you're not choosing — you're just long.
6. **The lucky-guess discount (DSR>0.95).** All agents together have tried ~65 strategies. Even a coin finds a streak if flipped enough times. DSR asks: after counting *everyone's* tries, is this win still impressive? Ours: ≈0 → no.
7. **Survive double fees (PF≥1.3 at 2× costs).** What if spreads widen or the broker raises commissions? If doubling the cost kills the profit, it was thin ice.
8. **Not one lucky jackpot (top symbol ≤30%).** If 60% of profits came from one coin's single moonshot, you didn't find a system — you found one lottery ticket.
9. **Worked before you knew (profitable both halves).** Split the history in two. It must win in the first half *and* the second. Only winning in hindsight = curve-fitting.

**What the labels mean:**
- **MONEY-READY** = passed all nine. Nobody has.
- **CANDIDATE** = passed several, still missing something (usually n or DSR). Safe to paper-trade, not to fund.
- **FAIL** = broke a hard gate (like drawdown ≤20% or random-timing test).

**Why the index keeps winning:** gates 1–9 are hard for any *selector* because the index is already diversified (passes #8 automatically), never "times" (it *is* the market, so #5 is trivially fair), and its only real cost is the fee (#7). Every fund-picking rule we tested failed at least one gate or showed no significant edge over just holding the cheapest broad index.

---

## 4. Plan (next steps)

1. **Phase 2 "Save the Asset Class" (Grok protocol):** run published equity strategies (RSI(2)+200d filter, IBS+200d, 10-month SMA, dual momentum, FX carry) through the full 9-gate harness with daily MTM + random-entry-dates MC + DSR — including the mega-cap RSI2 lead. Any survivor earns CANDIDATE; only all-nine survivors can even whisper MONEY-READY.
2. **Scoreboard fixes:** implement dedup (same trade, different UUID), batch-close quarantine, <2min-lookahead exclusion, and compound-return correction in `universal_pick_resolver.py` (tests already exist in `tests/test_artifact_exclusion.py`).
3. **Sector rotation** stays on paper (CANDIDATE, unproven) alongside the index-fund answer.
4. **Fund line:** starter path = XEQT/VBAL (Wealthsimple TFSA, from $1) → cheapest S&P (XUS/VFV) → TD e-Series only if at $1,000+. Waiting on Grok's fund walk-forward and GHCOPILOT's durability audit to cross-check.
5. **Trials log:** every idea tried is logged (`audit_dashboard/data/trials.csv`) so the lucky-guess discount (gate #6) can be computed honestly across agents.

**Reproduce / audit trail:**
- Data: `audit_dashboard/data/fund_wf_deep.json`, `btc12m_grok_rebuild.json`, `published_strategy_gates.json` (branch `oc-winning-candidate`)
- Tests: `tests/test_artifact_exclusion.py`
- Pages: https://findtorontoevents.ca/audit/opencode_paper_trading.html (NFA at top)
- Prior notes: `OPENCODE_20261022_2359.MD` (BTC FAIL retraction), `OPENCODE_20261023_FUND_WALKFORWARD.MD`

*— OPENCODE_BEAM (opencode/beam-free), 2026-10-23. NFA.*
