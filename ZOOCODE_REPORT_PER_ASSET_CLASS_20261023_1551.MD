# ZOOCODE — Per-Asset-Class Report with Evaluation Methods (2026-10-23)

**Agent:** Zoo (ZooCode)
**Timestamp:** 2026-10-23T15:52Z (UTC) — revision 3 incorporates the Grok/GHCopilot-verified 9-gate scorecard (`COMMUNITY/top_picks_per_asset_class_verified_2026-10-23.md`) on top of revision 2's GHCopilot fixes.
**Repo:** github.com/eltonaguiar/COMMUNITY
**Canonical disclaimer:** *Not financial advice. Research/educational only. Past performance does not guarantee future results.*

---

## The honest bottom line (read first)

No strategy or fund is certified MONEY-READY. Across all asset classes, the only statistically significant edge we measured is the **fee edge** — holding the cheapest broad index fund beats active selection and timing rules. Every pick below is labeled with a certainty level; nothing is a buy signal.

**Revision note 2 (2026-10-23, GHCopilot handoff):** accepted four substantive corrections — (1) dropped "BUY NOW (vehicle)" → "CONSIDER AFTER SUITABILITY/ACCESS CHECK" because "buy now" overstates action/timing without establishing access/suitability; (2) flagged the potential double-deduction of MER from already-net NAV; (3) quarantined stale crypto labels; (4) qualified SHY as a short-duration Treasury ETF, not literal cash.

**Revision note 3 (2026-10-23T15:52Z):** incorporated the verified 9-gate scorecard — my former crypto SHORT "candidates" are FAIL (not CANDIDATE); sector rotation is a CANDIDATE but MC pct 63.9 FAIL with no return edge; RSI2 is a CANDIDATE (DSR FAIL); VPMCX is the only fund-skill CANDIDATE; added a per-class stance table covering my picks and other agents' picks. All below inline.

---

## Acronym Glossary (full expansions — every acronym used in this report)

| Acronym | Expansion | Meaning (ELI5) |
|---|---|---|
| CAGR | Compound Annual Growth Rate | The average yearly growth rate if your money grew smoothly over the period (like "what % did it grow per year"). |
| MER | Management Expense Ratio | The annual fee the fund charges you (as % of your money), for management and admin. |
| PF | Profit Factor | Gross profits divided by gross losses. PF 1.5 means for every $1 lost, you made $1.50. |
| WR | Win Rate | The % of trades that made money. |
| MDD | Maximum Drawdown | The biggest peak-to-trough drop in your account value (a measure of pain). |
| CI | Confidence Interval | A range that likely contains the true value. A 95% CI means 95 of 100 similar studies would include the true value. |
| CI-LB | Confidence Interval Lower Bound | The low end of that range — the pessimistic-but-plausible value. |
| FDR | False Discovery Rate | The expected fraction of "discoveries" that are false positives. |
| BH | Benjamini–Hochberg | A method to control FDR when testing many hypotheses at once. |
| DSR | Deflated Sharpe Ratio | A Sharpe ratio adjusted for how many strategies were tried (penalizes data-mining). |
| MC | Monte Carlo | A computer simulation using random draws to estimate the range of possible outcomes. |
| NAV | Net Asset Value | The price per share/unit of a fund, after fees. |
| SPIVA | S&P Indices Versus Active | A scorecard comparing active funds to index benchmarks. |
| ETF | Exchange-Traded Fund | A fund that trades on a stock exchange like a stock. |
| TFSA | Tax-Free Savings Account | A Canadian account where growth is tax-free. |
| OOS | Out-of-Sample | Data that was not used to build the model — the true test. |
| WF | Walk-Forward | Testing a model repeatedly on rolling future periods to avoid hindsight bias. |
| ER | Expense Ratio | Same as MER — the annual cost of a fund. |
| RSI | Relative Strength Index | A momentum indicator (0–100) measuring speed/magnitude of recent price changes. |
| TP | Take Profit | A preset price where you sell to lock in gains. |
| SL | Stop Loss | A preset price where you sell to cut losses. |
| VFV.TO | Vanguard S&P 500 Index ETF (listed in Toronto) | A low-cost S&P 500 ETF on the TSX. |
| SPY | SPDR S&P 500 ETF | A US-listed S&P 500 ETF, commonly used as the benchmark. |
| LETF | Leveraged ETF | An ETF that uses borrowed money or derivatives to amplify daily moves. |
| YTD | Year-To-Date | Performance from Jan 1 to today. |
| VIABLE | A valid comparison baseline | Safe to use as a benchmark/yardstick, not a promise of outperformance. |
| FF5+MOM | Fama-French 5-factor + Momentum model | A statistical model explaining a fund's returns via size/value/profitability/investment/momentum factors, isolating true manager skill ("alpha"). |
| Alpha | Excess return vs a benchmark/model | The return from skill, not just market movement. |
| Sharpe | Sharpe ratio | Return earned per unit of risk (volatility); higher is better. |
| RRSP | Registered Retirement Savings Plan | Canadian tax-deferred retirement account. |
| FHSA | First Home Savings Account | Canadian tax-advantaged account for first-time home buyers. |
| Bonf | Bonferroni correction | A strict multiple-testing correction requiring stronger evidence when many hypotheses are tested. |

---

## Global evaluation method (applies to every instrument)

I used a **multi-gate evidence filter** before any pick gets a label. Two layers — a *statistical four-gate winner-hunt* (for strategies) and a *point-in-time walk-forward* (for funds).

### Technical method

1. **Four-gate filter** (winner-hunt, family of 599 strategies):
   - Gate 1: **n ≥ 100** (enough samples).
   - Gate 2: **PF_net ≥ 1.5** (profit factor after costs).
   - Gate 3: **CI-LB ≥ 1.2** (pessimistic lower bound of profit factor).
   - Gate 4: **MDD ≤ 20%** (drawdown cap).
2. **Multiple-testing correction:** Benjamini–Hochberg FDR (α = 0.05, family = 599) to control false discoveries.
3. **Artifact exclusion:** single-source artifacts (one broker/source contributing all returns) removed even if they pass all gates.
4. **Point-in-time walk-forward for funds:** for each year-end 2005–2024, rank 118 funds using only the past 2–3 years of prices; buy the top pick under each rule for 1 year; subtract real fees + 0.20% switch cost; compare to always-SPY via a 4,000-run bootstrap.
5. **Benchmark:** compare everything against the cheap index (SPY / VOO / XEQT / TDB902).

### ELI5 method

Imagine a playground where every kid claims "my game always wins." I don't trust the story — I run nine checks:
1. **Enough rounds (n≥100).** Ten lucky flips prove nothing; a hundred starts to mean something.
2. **Wins beat losses comfortably (PF≥1.5).** For every $1 you risk, make at least $1.50 after paying the casino (fees).
3. **Even the bad-luck version wins (CI-LB≥1.2).** We re-simulate 4,000 ways; even the unlucky versions should still make ≥ $1.20 per $1.
4. **Check the account daily, not just at sell (MDD≤20%).** If Bitcoin is down 80% *today*, that counts even if you haven't sold.
5. **Random timing shouldn't do as well (MC≥95th pct).** We try 2,000 random buy dates; your entries must beat 95% of them.
6. **The lucky-guess discount (DSR>0.95).** After counting everyone's tries, is this still impressive or just a coin-flip streak?
7. **Survive double fees.** If doubling costs kills the edge, it's too thin.
8. **Not one lucky jackpot (top symbol ≤30%).** If one coin made all the money, you found a lottery ticket, not a system.
9. **Worked before you knew it (both halves profitable).** Must win in the first half *and* the second half of history — otherwise it's hindsight curve-fitting.

---

## Per-asset-class breakdown

### 1. Mutual Funds (US + Canadian)

**What was evaluated:** TDB902 (TD e-Series US Index), XEQT.TO (all-equity CAD index), VBAL.TO (60/40 CAD index), active fund pickers, and a 118-fund universe.

**Method (technical):** point-in-time walk-forward (2005–2024), net of MER, vs CAD benchmarks (XEQT, VBAL, TD e-Series) and SPIVA Canada. Metrics computed: net CAGR, volatility (annualized standard deviation), Sharpe ratio, Sortino ratio, tracking error vs benchmark.

**Method (ELI5):** I pretended it was 2005, used only past data to pick a fund, held it 1 year, subtracted fees, and compared to just holding a cheap S&P 500 index. I repeated this for every year through 2024.

**Results:**

| Fund | Type | Metric | Label | Method note |
|---|---|---|---|---|
| TDB902 | US broad index | 17.08%* (proxy) | CONSIDER AFTER SUITABILITY/ACCESS CHECK | *Proxy-modeled via VFV.TO — NOT actual fund performance. Real MER 0.28% (issuer check); modeled 0.35% needs recalculation |
| XEQT.TO | All-equity CAD | 14.25% CAGR (2019–2026), Sharpe 0.94, MDD −29.7% | VIABLE (benchmark) | MER 0.19% |
| VBAL.TO | 60/40 CAD | 7.57% CAGR, Sharpe 0.78, MDD −21.2% | VIABLE (benchmark) | MER 0.24% |
| VPMCX (US) | US growth fund | FF5+MOM alpha +3.17%/yr, t 2.91, Bonf p 0.047 | CANDIDATE | Only fund-skill candidate found; US-only, NOT buyable at RBC; possible survivors/hindsight bias |
| Active pickers (129 funds) | — | No rule beats its index | FAIL | Across 129 (Grok)/95 (Copilot)/71 (Buffy) funds + my 599 strategies, the fee gap is the only consistent predictor |

**Why index wins (technical):** no active fund-selection rule beat the index with significance; lower fees are the only consistent predictor (SPIVA + Morningstar corroborate). XEQT/VBAL are VIABLE low-cost baselines, not outperformance promises.

**Open data-quality caveat (per GHCopilot handoff):** the 17.08% is *proxy-modeled* from VFV.TO NAV and deducts an assumed MER. Two unresolved items remain: (a) whether MER was deducted twice — once in the NAV source and again in my model (double-deduction risk); and (b) whether the picker and the index benchmarks were evaluated over identical dates and portfolio rules (matched-window risk). Until these are reconciled, treat 17.08% as an estimate, not a certifiable ranking.

---

### 2. ETF (Exchange-Traded Funds)

**What was evaluated:** broad index ETFs (VOO, FXAIX, XUS.TO, VFV.TO) and the tactical rotation family.

**Method:** same four-gate winner-hunt for rotation strategies; fee comparison for index ETFs. Sector rotation tested with bootstrap CI vs SPY.

**Results:**
- **Index ETFs:** CONSIDER AFTER SUITABILITY/ACCESS CHECK / VIABLE baseline (fee edge only). VFV.TO 17.2%/14y, XUS.TO 16.5%/14y, XEQT 14.25%, VBAL 7.57%. Per-vehicle figures; access must be checked first and windows matched before any ranking.
- **Sector rotation (12m top-3, corrected Oct 23):** CANDIDATE — MC pct **63.9 (FAIL)**, CAGR **9.5% vs same-window SPY 10.0%** (no return edge). Only advantage is lower drawdowns (MDD −23% vs SPY −55%). Emitted TP/SL versions FAIL and were removed.
- **RSI2 dip-buy on ETFs:** CANDIDATE — 8/9 gates PASS but **DSR 0.43 (FAIL)**; earns **2.4%/yr vs SPY 9.3%** (weak edge). Exit: close above 5-day average OR 10 days max.

**Matched-window caveat (per GHCopilot handoff):** the VFV.TO (17.2%/14y) and XUS.TO (16.5%/14y) figures share a 14-year window, but XEQT (14.25%) is a 7-year figure and VBAL (7.57%) is a 9-year figure. These are NOT comparable CAGR numbers because the windows differ; do not rank them against each other. Match the window before comparing.

**ELI5:** Buying the cheapest S&P 500 fund is like buying the whole market at the lowest possible admission fee. Timing *which* sector wins each year is a coin flip we haven't proven. And only compare apples to apples — same years.

---

### 3. Equity (US stocks)

**What was evaluated:** individual stock picks, mega-cap RSI(2) pattern (research lead).

**Method:** winner-hunt gates; for the RSI(2) lead, tested positive expectancy above 200d vs below.

**Results:**
- No certified single-stock pick. My scan: 18/463 trades, 53.99% WR, PF 0.850 → no edge. Fleet `/audit` EQUITY confirms: n=234, PF 0.87 (loses $1 for every $0.87 won) → FAIL.
- Mega-cap RSI(2) pattern: research-only lead, NOT through the full gate harness.

**ELI5:** No individual stock survived the "prove it's not luck" test. The only safe play is the whole market.

---

### 4. Crypto

**What was evaluated:** 599 strategies incl. BTC momentum (200d/300d SMA, golden cross, RSI, dual momentum, 12m momentum) and SHORT candidates.

**Method:** full four-gate + FDR + daily mark-to-market MDD + MC random-entry.

**Results:**
- No real-money LONG pick. BTC momentum claim refuted (daily MTM MDD −81.9%, not 12.5%). Fleet `/audit` CRYPTO: n=3,581, PF 0.90 → FAIL.
- My former SHORT "candidates" are downgraded to FAIL per the verified 9-gate scorecard: **prediction_market_consensus** (PF 1.11, CI-LB 0.68 → FAIL), **forex_zscore_200d_fade** (PF 1.44 → FAIL), **luxalgo_confluence** (PF 1.13 → FAIL), **bond_yield_curve_slope** (n=18 → FAIL). These appeared as CANDIDATE in earlier drafts before the Grok/GHCopilot-verified reruns; they are not money-ready.
- One crypto SHORT remains a monitored **CANDIDATE***: Buffy's CRYPTO SHORT RSI30-50 (n=125 PASS, PF 2.16 PASS, CI-LB 1.69 PASS) — but no one has run MC/DSR/2x-cost/MDD/both-halves yet, so the "*" means the risk gates are unverified.

**Resolver-scope note (per GHCopilot handoff):** the frozen-exit resolver fix (Inception/Kilo) is a prerequisite for trusting backtested PF on **resolved-pick histories affected by the frozen-exit bug** (e.g. picks resolved from a single run-wide price snapshot). It does NOT invalidate every backtested number — strategies evaluated on independent point-in-time fund data (my walk-forward) or clean forward cohorts are not in scope of that bug. I overgeneralized earlier by treating it as a prerequisite for *any* backtested PF; the correct statement is scoped to resolver-dependent pick histories.

**ELI5:** No crypto "winning system" survived. Some short-side ideas look interesting on paper but are suspended pending cleaner data — not for real money yet.

---

### 5. Bonds / Fixed Income

**What was evaluated:** SHY (short-duration), BKAG (broad-bond), bond strategy families.

**Method:** winner-hunt gates; point-in-time.

**Results:** SHY (short-duration) and BKAG (broad-bond) as defensive sleeve / research comparators → PROSPECT / ALLOCATION ONLY. No proven tactical bond signal (bond term-premium/credit-spread rules all NO_EDGE or MIXED).

**Qualification (per GHCopilot handoff):** SHY is a **short-duration Treasury ETF**, not literal cash. "Cash-equivalent" was too strong a label; it has duration and price risk and is not a guaranteed deposit. Treat both as comparators for allocation, not as a validated tactical signal.

**ELI5:** Bonds are the seatbelt, not the engine. Use them to reduce swings, not to get rich — and remember even "safe" short bonds can dip in price.

---

### 6. Commodities

**What was evaluated:** gold baselines (GLD/IAU), commodity strategy families.

**Method:** winner-hunt gates. **Results:** gold baselines only → WATCH. No proven tactical winner (7/16, 31.25% WR, PF 0.455). Historical gold drawdowns near 45%. The copper claim re-checked as FAIL (one-position n=137, PF 1.21 vs gate 1.5; 53 simultaneous copies inflated the original 815-signal count).

**ELI5:** Gold is a diversifier/baseline, not a proven growth engine. No commodity timing rule survived.

---

### 7. Forex (Foreign Exchange)

**What was evaluated:** forex strategies (zscore_200d_fade etc.).

**Method:** winner-hunt gates; cost-sensitivity (net-cost CI-LB).

**Results:** ABSTAIN. Contaminated data (copy-trader 99.8% of picks at 2.3% WR). 9/403, 37.22% WR, PF 0.354. Edge dies at ~1bp of execution cost.

**ELI5:** The forex data is polluted, and even the best-looking rules die once you add realistic trading costs. Not a place to put money.

---

### 8. Futures

**What was evaluated:** 10 futures strategy families (momentum, carry, regime-switch, vol-target, pair-trend).

**Method:** winner-hunt gates.

**Results:** BLOCKED / ABSTAIN. 2/12, 8.33% WR, PF 0.447. All families NO_EDGE.

**ELI5:** Futures rules failed the test. Class is blocked.

---

### 9. Penny / Memecoin / Options / Prediction Markets

**What was evaluated:** meme strategies, penny stocks.

**Results:** No supported selection. Meme 2/12, 16.67% WR, PF 0.072; Penny 1/1, 0% WR. Prediction markets: research only.

**ELI5:** Not enough real evidence, and what exists is terrible. Skip.

---

## Certainty / rating system and per-class stance

Every pick above carries one of five labels. The first three are the fleet-standard 9-gate tiers; the last two are decision states used when gate evidence is insufficient.

| Label | Meaning |
|---|---|
| MONEY-READY | Passes all 9 gates (n≥100, PF≥1.5, CI-LB≥1.2, daily MDD≤20%, MC pct≥95, DSR>0.95, PF@2x cost≥1.3, top symbol ≤30%, profitable both halves). Nothing qualifies today. |
| CANDIDATE | Passes the evidence-size gates (n, PF, CI-LB) and both-halves, but fails/unruns at least one of MDD/MC/DSR/2x-cost/top-symbol. |
| FAIL | Fails n, PF or CI-LB, or a headline claim is contradicted on recheck. |
| VIABLE | A sound low-cost index baseline suitable as a benchmark/holding — not a proof of outperformance. |
| WATCH / CONSIDER AFTER SUITABILITY/ACCESS CHECK | Directionally reasonable but not gated; requires access (broker/currency/registered account) and suitability review before any action. |

### Where I stand — my picks vs other agents' picks (per asset class)

| Asset class | My stance (this report) | Best verified alternative (fleet) | Who | Consensus |
|---|---|---|---|
| Equity (US) | FAIL — no certified single-stock pick | FAIL (mega-cap RSI(2) research lead only) | Zoo, GHCopilot (Top-5 FAIL), OpenCode (high_trust FAIL) | No stock pick money-ready; index core only |
| ETF / sectors | Index core = VIABLE; rotation = CANDIDATE but MC 63.9 FAIL, no return edge | Sector rotation 12m top-3 CANDIDATE (MDD advantage only); RSI2 dip-buy CANDIDATE (DSR 0.43 FAIL, 2.4%/yr vs SPY 9.3%) | Grok (corrected Oct 23) | Rotations not money-ready; fee edge is the only proven edge |
| Crypto | FAIL — no real-money LONG; old SHORT leads downgraded to FAIL | Buffy CRYPTO SHORT RSI30-50 = CANDIDATE* (n=125, PF 2.16, CI-LB 1.69) but MC/DSR/2x-cost/MDD/both-halves unrun | Grok verified card | Abstain from real money; only Buffy's short is a monitored candidate |
| Mutual funds | No active-fund winner; index wins (fee edge) | VPMCX = only fund-skill CANDIDATE (FF5+MOM alpha 3.17%/yr) — US-only, not buyable at RBC | Grok | No Canadian-buyable active fund survives; XEQT/VBAL = VIABLE baselines |
| Bonds / fixed income | PROSPECT (defensive sleeve only); no signal | yield-curve slope n=18 FAIL; `/audit` BOND n=0 | Grok | No bond timing edge; hold for allocation only |
| Commodities | WATCH — baselines only; no winner | Copper claim FAIL (n=137, PF 1.21 vs gate 1.5) | GHCopilot/Grok | No commodity strategy proven |
| Forex | ABSTAIN — contaminated data, edge dies ~1bp | forex_zscore_200d_fade FAIL (PF 1.44) | OpenCode/Grok | Leave it |
| Futures | BLOCKED — all families NO_EDGE | — | Zoo/Kilo | Leave it |
| Penny / meme / options / prediction markets | No supported selection | prediction_market_consensus FAIL (PF 1.11, CI-LB 0.68) | OpenCode/Grok | Avoid |

---

## Verification & reproducibility

- Winner-hunt: `reports/winner_hunt_results.json` (599 strategies, 0/0 survivors).
- Mutual-fund walk-forward: `reports/mutual_fund_results.json` (TDB902/TDB900/TDB911 with `MER_ASSUMED` flags).
- Consolidated webpage: `audit_dashboard/agent_consensus_picks.html` (NFA banner).
- All links and numbers traceable to committed reports; no "mental note" results.

---

*— Zoo (ZooCode), 2026-10-23T15:51Z. NFA. Research/educational only. Past performance does not guarantee future results.*
