# ZOOCODE — Live /audit Site & Data Audit (2026-10-23)

> **Not financial advice. This is a data-quality / readiness audit, not a recommendation to buy or sell anything.**
> Author: Zoo (ZooCode) · Compiled 2026-10-23 ~15:56Z.

---

## 0. What I checked (scope)

| Check | Result |
|-------|--------|
| Live page `findtorontoevents.ca/audit/` | 200 OK (title: "Unified Audit Dashboard - Antigravity") |
| Live payload `audit/data/dashboard_data.json` | **Fresh** — generated 2026-10-23T15:43:20Z (~9 min before my check), payload lag 77 min, repo_sha `b497ccaf` |
| `audit/real_money.html` | **STALE (static)** — "Generated 2026-05-12 by Claude Opus 4.7" (5+ months old doc page) |
| `audit/mutual-funds.html` | Live page; renders `generated_at` from the fresh payload |
| US-equity / predictions / stocks / equity pages | 404 — no separate pages exist; equity content lives in the dashboard + `real_money.html` |
| `analyst_active_calls` block | **STALE** — `updated_at` 2026-03-26 (≈7 months old), `total_active: 0` |
| `smart_picks_feed` | **Fresh-but-EMPTY** — generated 13:58Z but `total_scored: 0`, `picks: []` |
| `money_ready_2026-10-23.json` on live | **404 — Object not found** (file exists in repo but is not deployed) |

**Headline:** the *payload* is fresh, but the page has structural staleness (analyst calls 7 months old, empty smart-picks feed, missing money_ready archive) and the underlying books do **not** survive the money-readiness gates.

---

## 1. Overall dashboard book (all closed picks, n=7160 valid)

| Metric | Value | Gate? (≤/≥) | Verdict |
|--------|-------|--------------|---------|
| Overall win rate | 44.0% | n/a | weak |
| Plain PnL sum | **−42.31%** | n/a | negative |
| Compounded equal-weight | **−97.71%** | n/a | catastrophic |
| Profit factor | 1.03 | ≥1.5 | **FAIL** |
| Net Sharpe (annual) | 0.23 | high | low |
| Expectancy | +0.04% | >0 | marginal |
| Rolling 30d max drawdown | 26.91% | ≤20% | **FAIL** |
| Signal→trade rate | 36.3% | n/a | — |

**ELI5:** imagine a coin that lands heads (win) 44% of the time. The average win is only slightly bigger than the average loss, so after thousands of trades the account is down 42% — and if you reinvested side-by-side in every trade, you would have lost **97.7%**. The system is not self-funding yet.

---

## 2. Per-asset-class evaluation (from live `hf_stats.by_asset_class`)

### 2.1 US EQUITY — **CANDIDATE / WATCH (no MONEY-READY stock)**
| Metric | Value | Gate? | Verdict |
|--------|-------|-------|---------|
| n | 287 | ≥100 | pass |
| Sharpe / net | 3.15 / 3.15 | ≥1 | pass |
| Profit factor | 1.68 | ≥1.5 | pass |
| Win rate | 52.6% | n/a | ok |
| Max drawdown | **62.5%** | ≤20% | **FAIL** |

- Active pick: **AAPL LONG** (regime_terminal, entry $348.22). Single-name momentum is a **CANDIDATE** — profitable per trade, but a 62% drawdown is not investable.
- **ELI5:** buying US stocks has been net-positive here, but the rides are so bumpy you'd have sat through a 62% dip. That is not a "safe" signal.
- **Call:** WATCH. Index core (broad low-fee ETF) only; no individual stock gets a certified call from this data.

### 2.2 ETF — **CANDIDATE (not MONEY-READY)**
| Metric | Value | Gate? | Verdict |
|--------|-------|-------|---------|
| n | 164 | ≥100 | pass |
| Sharpe / net | 2.49 / 2.48 | ≥1 | pass |
| Profit factor | 1.45 | ≥1.5 | **FAIL (close)** |
| Win rate | 54.9% | n/a | ok |
| Max drawdown | **77.6%** | ≤20% | **FAIL** |

- Active picks: XLE/EWY/VLUE/XLK/EFA/XLV/XLF LONG, KWEB/KBE/IYR SHORT (sector rotation / dual-momentum family).
- **ELI5:** sector-rotation ETFs win more than they lose, but a 77% drawdown shows the strategy is highly concentrated and volatile — not a dependable edge.
- **Call:** CANDIDATE. The tactical rotation *family* is the only validated edge in the space (per prior reports), but it is **not yet** money-ready.

### 2.3 CRYPTO — **FAIL / WATCH (no real-money pick)**
| Metric | Value | Gate? | Verdict |
|--------|-------|-------|---------|
| n | 1153 | ≥100 | pass |
| Sharpe / net | 1.74 / 1.73 | ≥1 | pass |
| Profit factor | 1.34 | ≥1.5 | **FAIL** |
| Win rate | 51.3% | n/a | ok |
| Max drawdown | **208.3%** | ≤20% | **FAIL (extreme)** |

- Active picks: **ETHUSDT SHORT** (kalshi_mtf_consensus, entry $2400), **HYPEUSDT SHORT** (quan_engine).
- **ELI5:** crypto trades win about half the time, but the swings are so wild the drawdown meter exceeds 200% (worse than starting from zero). You cannot size this safely with real money.
- **Call:** FAIL. Even SHORT candidates fail the gates (confirmed by the Grok-verified scorecard: prediction_market_consensus / forex_zscore_200d_fade / luxalgo_confluence / bond_yield_curve_slope all FAIL). Buffy's CRYPTO SHORT RSI30–50 remains the only **CANDIDATE\*** to watch.

### 2.4 FOREX — **FAIL**
| Metric | Value | Gate? | Verdict |
|--------|-------|-------|---------|
| n | 107 | ≥100 | pass |
| Sharpe / net | −1.35 / −1.39 | ≥1 | **FAIL** |
| Profit factor | 0.73 | ≥1.5 | **FAIL** |
| Win rate | 23.4% | n/a | **FAIL** |
| Max drawdown | 13.7% | ≤20% | pass (only gate that passes) |

- Active picks: **AUDUSD=X SHORT** (combined_confidence), **EURGBP=X LONG** (non_crypto_consensus).
- **ELI5:** forex here is a coin that comes up heads only 23% of the time — you lose money over the long run.
- **Call:** FAIL. Abstain.

### 2.5 BOND — **FAIL**
| Metric | Value | Gate? | Verdict |
|--------|-------|-------|---------|
| n | 14 | ≥100 | **FAIL (tiny)** |
| Sharpe / net | −6.79 / −6.83 | ≥1 | **FAIL** |
| Profit factor | 0.37 | ≥1.5 | **FAIL** |
| Win rate | 35.7% | n/a | **FAIL** |

- Active picks: **IEF / TLT LONG** (non_crypto_consensus).
- **ELI5:** only 14 bond trades — far too few to trust, and what little exists is a net loser.
- **Call:** FAIL. No bond signal is actionable.

### 2.6 COMMODITY — **FAIL**
| Metric | Value | Gate? | Verdict |
|--------|-------|-------|---------|
| n | 18 | ≥100 | **FAIL (tiny)** |
| Sharpe / net | −17.05 / −17.07 | ≥1 | **FAIL (extreme)** |
| Profit factor | 0.13 | ≥1.5 | **FAIL** |
| Win rate | 11.1% | n/a | **FAIL** |

- Active picks: **SI=F LONG** (silver), **PA=F SHORT** (palladium, commodity_carry_momo_double_sort).
- **ELI5:** for every 9 commodity trades, ~8 lose. This is the worst book on the dashboard.
- **Call:** FAIL. No commodity tactical pick.

### 2.7 FUTURES — **INSUFFICIENT_DATA / FAIL**
| Metric | Value | Gate? | Verdict |
|--------|-------|-------|---------|
| n | 3 | ≥100 | **FAIL (n=3 meaningless)** |
| Sharpe | 10.78 | ≥1 | pass (but n=3) |
| Profit factor | 5.41 | ≥1.5 | pass (but n=3) |

- Active picks: **ES=F / YM=F LONG** (futures_connors_rsi2).
- **ELI5:** only 3 futures trades ever — that's like flipping a coin 3 times and declaring you're a genius. Statistically meaningless.
- **Call:** FAIL / INSUFFICIENT_DATA. Do not trade.

---

## 3. Stale vs fresh — what I found

1. **`active_raw` = 4,271 vs `active` = 22.** The payload carries **4,271 "active" raw picks**, but only **22** are the real current roster. The raw pool includes legacy unresolved entries dating back to **March 2026** (e.g., BTCUSDT LONG marked active at entry **$70,000**). These are stale ghosts still served to the page — a **data-quality defect**, not a live signal.
2. **`analyst_active_calls` is 7 months stale** (updated 2026-03-26, 0 active calls). A section of the dashboard claims zero analyst calls and hasn't refreshed since March.
3. **`smart_picks_feed` is empty** (0 scored, 0 picks) despite a fresh `generated_at` — the generator runs but emits nothing.
4. **Live `money_ready_2026-10-23.json` → 404** — the file is in the repo but not deployed to the live site, so the "money-ready" stamp is not actually visible/auditable live.
5. **Recent closes ARE fresh**: `recent_closed` n=3500, with 1,180 closes in 2026-10 and 1,085 in 2026-09 (marginally more than any earlier month). The book is receiving new trades; the problem is the *quality*, not the freshness, of those trades.
6. `real_money.html` is a **static May 12, 2026** page — documentation, not live data.

---

## 4. What is healthy

- The **main payload is genuinely fresh** (77-min lag, matching repo SHA). The pipeline is alive.
- The **close ledger is being updated daily** (fresh closes through 2026-10-23).
- The **measurement-hygiene / NFA framing** is present on the live dashboard (banner), consistent with the codebase's invariant.

---

## 5. Bottom-line rating ("calls")

| Asset class | Call | One-line reason |
|-------------|------|-----------------|
| US Equity | **WATCH** | Positive per-trade but 62% drawdown; index-only, no certified stock |
| ETF | **CANDIDATE** | Rotation family is the only edge, but PF 1.45 & MDD 78% keep it un-certified |
| Crypto | **FAIL / WATCH** | MDD 208%; only SHORT RSI30–50 is a CANDIDATE\* |
| Forex | **FAIL** | 23% win rate, PF 0.73 — net loser |
| Bonds | **FAIL** | n=14, PF 0.37 |
| Commodities | **FAIL** | n=18, PF 0.13, worst book on the page |
| Futures | **FAIL / INSUFFICIENT_DATA** | n=3 — statistically meaningless |
| **Whole dashboard** | **NOT money-ready** | overall PF 1.03, compounded EW −97.7%, 30d MDD 26.9% |

**Nothing on the live /audit page currently earns a MONEY-READY call.** The strongest single asset classes (Equity, ETF) are at best **CANDIDATE** because their drawdowns blow the 20% gate. The rest are FAIL.

---

## 6. Reproduce

- Live payload: `curl -s https://findtorontoevents.ca/audit/data/dashboard_data.json`
- Per-class stats: `hf_stats.by_asset_class` in that payload.
- Active roster: `picks.active` (22). Stale backlog: `picks.active_raw` (4,271).
- Analyst calls: `analyst_active_calls` (updated 2026-03-26).
- Smart picks: `smart_picks_feed` (scored 0).

---

*Zoo (ZooCode), 2026-10-23. Not financial advice. Data as served by the live /audit payload; gate thresholds per the 9-gate protocol.*
