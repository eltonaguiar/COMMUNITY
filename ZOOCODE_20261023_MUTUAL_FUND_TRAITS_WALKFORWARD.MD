# Mutual-Fund "What Actually Wins?" Trait Walk-Forward + Capital Case Study (2026-10-23)

**Agent:** Zoo / ZooCode — **Scope:** point-in-time (no lookahead) fund trait backtest + $200/$500/$1,000/$2,000/$10,000 affordability case study with RBC trading fees.
**Status:** Backtest ran clean, 7 unit tests pass, results in [`audit_dashboard/data/mf_traits_walkforward_results.json`](audit_dashboard/data/mf_traits_walkforward_results.json).

---

## 0. The honest bottom line (read this first)

- **Skill traits do NOT reliably beat a cheap index.** When we pick funds using alpha-after-market, downside capture, benchmark consistency, and manager tenure — **only data known at each year-end** — the picks *underperform* the S&P 500 / XEQT benchmark at every horizon tested. At 5 years the underperformance is statistically significant (US 5y excess **−5.78%/yr**, bootstrapped 95% CI −10.6% to −1.0%).
- **But you WOULD have made money in absolute terms at every capital size** — because the funds are diversified and markets generally rose. The catch is *how much* you made depends almost entirely on **how big your account is**:
  - US: $200 → **+2.5%/yr** average vs $10,000 → **+8.9%/yr**.
  - Canada: $200 → **+5.5%/yr** vs $10,000 → **+12.5%/yr**.
- **That gap is fees, not skill.** A $9.95 flat RBC commission is ~5% of a $200 purchase and ~0.1% of a $10,000 purchase. Small accounts also can't spread across enough funds, so one bad year is undiversified.
- **Survivorship bias is real but small here** (~−0.3pp) and does NOT change the conclusion: even *before* the haircut, the active funds in our data already lose to the benchmark.
- **Rating: NO MONEY-READY active-fund pick.** What "wins" after traits + fees is still the **cheap index core** (cost is the only proven, reliable edge). This matches SPIVA and prior agent reports (OpenCode, Buffy, GHCopilot).

**NOT FINANCIAL ADVICE. Research/education only. Past performance does not guarantee future results.**

---

## 1. Why we ran this (the question)

Your agents kept saying "mutual funds match the market, there's no edge." That's the *average* story. You asked: **go beyond fees** — is there a *consistent* winning pattern in manager tenure, benchmark-consistency, how much a fund falls in down markets, skill after adjusting for market exposure, and style tilts (quality / low-vol / value)? And run it as a per-size case study: **if I only had $200 / $500 / $1,000 / $2,000 / $10,000**, which funds pass at that size (minimum + share price + RBC fee), and would I have made or lost money?

---

## 2. Methodology

### 2.1 Point-in-time walk-forward (no future data — ELI5)
Every **December 31st** we "forget the future." We line up funds using **only data known that day**, rank them, pick the top ones, then roll the clock forward 1 / 3 / 5 years and look at what *actually* happened. Nothing from the future leaks into the ranking. Windows are non-overlapping (1y, 3y, 5y).

### 2.2 The trait score (beyond fees)
Each fund gets a 0–1 composite score from **5 traits**, weighted:

| Trait | Weight | What it measures | Technical |
|---|---|---|---|
| **Alpha after market** | 30% | Skill left over after removing market movement | Jensen's α = intercept of regression of fund-excess returns on market-excess returns (36m trailing) |
| **Benchmark consistency** | 25% | How often the fund *beat* its benchmark in past years | Fraction of trailing calendar years fund CAGR > benchmark CAGR |
| **Low downside capture** | 20% | Does it fall *less* than the market in down months | Down-market beta: Cov(fund,mkt \| mkt<0) / Var(mkt \| mkt<0) |
| **Manager tenure** | 15% | Is the same person managing it? | Years at helm ($ metadata) |
| **Cost** | 10% | Expense ratio (lower better) | ER (percentile-ranked) |

Two selection rules compared: **alpha_only** (pure past alpha) and **trait_composite** (full weighted score). Top 3 funds per rule per year.

### 2.3 Affordability + RBC fees
For each capital size we only allow funds where **capital ≥ minimum initial investment** and where at least **1 whole share** fits after the **$9.95 RBC commission** (`units = floor((capital − 9.95) / NAV)`). The commission is charged per fund opened. Forward value uses the fund's **net-of-expense-ratio** CAGR. We report the *average 1-year return* over all rebalance windows and the fraction of windows that made money.

### 2.4 Survivorship-bias estimate (the honest limit)
Free data mostly keeps funds that survived and drops funds that closed down. So past winners look better than reality. We estimate the effect by re-mixing a negative return for a delisted fraction (`delist_rate = 4%`, lost fund return −10%) into the active-fund excess distribution.

---

## 3. Results

### 3.1 Did skill traits beat the benchmark? (excess vs benchmark, net of ER)

**US (benchmark SPY, 59 funds universe):**

| Horizon | Rule | Mean excess/yr | Win rate | t-stat | 95% CI |
|---|---|---|---|---|---|
| 1y (32 windows) | alpha_only | −3.98% | 44% | −1.74 | [−8.6, +0.2] |
| 1y | trait_composite | −3.12% | 41% | −1.74 | [−6.9, +0.1] |
| 3y (11) | alpha_only | −4.67% | 18% | −1.88 | [−9.2, +0.0] |
| 3y | trait_composite | −3.50% | 18% | −1.63 | [−7.6, +0.4] |
| 5y (6) | alpha_only | −7.15% | 0% | −3.48 | [−10.8, −3.6] |
| 5y | trait_composite | **−5.78%** | 33% | −2.13 | **[−10.6, −1.0]** |

**Canada (benchmark XEQT.TO, 12 funds universe):**

| Horizon | Rule | Mean excess/yr | Win rate | t-stat |
|---|---|---|---|---|
| 1y (6) | alpha_only | −0.78% | 50% | −0.37 |
| 1y | trait_composite | −2.01% | 33% | −1.15 |
| 3y (2) | alpha_only | +1.74% | 100% | +6.84 |
| 3y | trait_composite | −0.01% | 50% | −0.00 |

> **Read:** Trait-selected funds *underperform* the index on average. The few positive cells (CA 3y alpha_only, n=2) are small-sample noise, not a reliable edge.

### 3.2 The capital case study — did you make or lose money?

**US — average 1-year return (net of ER, after RBC $9.95 + affordability):**

| Capital | n windows | Mean 1y return | Win rate | Distinct funds ever affordable |
|---|---:|---:|---:|---:|
| $200 | 31 | **+2.51%** | 65% | 19 |
| $500 | 32 | +6.56% | 69% | 20 |
| $1,000 | 32 | +7.69% | 72% | 20 |
| $2,000 | 32 | +8.28% | 72% | 20 |
| $10,000 | 32 | +8.85% | 72% | 27 |

**Canada — average 1-year return:**

| Capital | n windows | Mean 1y return | Win rate | Distinct funds ever affordable |
|---|---:|---:|---:|---:|
| $200 | 6 | **+5.50%** | 83% | 6 |
| $500 | 6 | +10.16% | 83% | 6 |
| $1,000 | 6 | +11.45% | 83% | 6 |
| $2,000 | 6 | +12.05% | 83% | 6 |
| $10,000 | 6 | +12.51% | 83% | 6 |

> **The key finding:** You made money at every size — but **the return scales up with account size almost entirely because of fees**. The US benchmark (S&P 500) averaged ~**12%**/yr net over the same windows; even the $10,000 trait portfolio made only 8.9%, and the $200 portfolio made 2.5%. The $200→$10,000 gap (~6.3pp US, ~7.0pp CA) is the $9.95×N commission and affordability dilution — **not** skill.

### 3.3 Which funds "passed" at each size (trait screen + affordable)

The union of funds that could be opened (after min + whole-share + RBC fee) **and** were ever a top-3 trait pick:

- **$200 (US):** FNILX, FXAIX, VOO, IVV, SCHB, SPTM, VV, SWISX, SWLGX, SWRSX, FCNTX, DODGX, TRBCX, AGTHX, FLPSX, FRESX, FSPGX, FSRNX, BND, AGG
- **$10,000 adds:** VFIAX (min $3,000), VTSAX, FZROX, VIMAX, VSMAX, VTMGX, VEMAX, VBTLX, FXNAX, VGSLX, VGSIX, FIPDX, VAIPX, SWPPX, etc.

> **Notice what keeps passing:** most of the "winners" are **cheap index funds** (FNILX/FXAIX/VOO/IVV/SCHB…) — they score high on cost + tenure + low downside. The expensive active funds (FCNTX, DODGX, TRBCX, AGTHX, FLPSX) only occasionally make the screen and then *underperform* the index after fees. This is the honest takeaway: **a skill-trait screen keeps surfacing the index, not the star manager.**

### 3.4 Survivorship-bias estimate

| Region | Active obs | Observed mean excess | Adjusted mean excess | Haircut |
|---|---:|---:|---:|---:|
| US | 566 | −1.58% | −1.92% | −0.34pp |
| Canada | — | −3.20% | −3.53% | −0.32pp |

> We already see active funds *losing* to the benchmark; the survivorship haircut (−0.3pp) makes them slightly worse but does not flip any conclusion. **Honest caveat:** free data almost certainly drops more than 4% of funds (losers), so the true effect is likely larger than this estimate — meaning the "active funds lose" result is if anything understated.

---

## 4. What actually makes a "consistently winning" fund? (patterns found)

1. **Cost is the only trait that reliably predicts winning.** The funds that kept passing and kept paying were the near-zero-ER ones (FNILX, FXAIX, SWPPX, VOO). High-ER active funds (FCNTX 0.74%, FOCPX 0.78%) could not overcome their fee drag.
2. **Alpha and consistency did NOT transfer into future outperformance.** Funds with high trailing alpha/consistency underperformed the benchmark over the next 1/3/5 years. This is the classic "hot hand" illusion — past skill metrics do not forecast future skill.
3. **Downside capture / low-vol tilt mostly just picked bonds and value funds** (VBTLX, BND, AGG, DODGX). Those feel "steady" but structurally underperform an equity benchmark in a bull market — which is why the composite score lost so badly vs SPY/XEQT.
4. **Manager tenure is a coin flip** in our data — no reliable edge.
5. **The affordability/fee effect is decisive at small sizes.** At $200 the $9.95 commission plus inability to diversify dominates everything; you're basically paying ~5%+ up front.

---

## 5. Calls / ratings

| Instrument / approach | Rating | Reasoning |
|---|---|---|
| **Active mutual fund picking (traits)** | **FAIL / WATCH** | Statistically significant underperformance vs index at 5y; no reliable skill signal found |
| **Cheap index core (FNILX/FXAIX/VOO/SWPPX)** | **CANDIDATE** | Cost edge is the only *proven* reliable edge; lowest fees, lowest survivorship risk |
| **$200 / $500 starter accounts** | **WATCH** | You make money (market beta) but fees eat ~5%+ up front; diversify is nearly impossible with one $9.95 flat commission |
| **$2,000+ accounts** | **CANDIDATE** (index core) | Fees become tolerable; still prefer index over active funds |
| **Survivorship-adjusted active edge** | **None found** | Observed active excess is negative before and after haircut |

---

## 6. Acronym glossary

- **α (alpha)** — return not explained by market movement; skill after beta.
- **β (beta)** — sensitivity to the market (1.0 = moves with market).
- **Downside capture** — how much a fund falls vs the market in down months (<1 = falls less).
- **ER (expense ratio)** — annual % fee the fund charges.
- **RBC** — Royal Bank of Canada; $9.95 flat online commission modeled.
- **NAV** — net asset value per share (price per unit).
- **CAGR** — compound annual growth rate.
- **SPIVA** — S&P Indices vs Active (industry study: majority of active funds lag indices).
- **t-stat / CI** — statistical significance measures (|t| > ~2 ≈ unlikely by chance; 95% CI = range containing the true mean 95% of the time).

---

## 7. How to reproduce

```bash
# regenerate results JSON
python3 tools/mf_traits_walkforward_runner.py --universe all

# unit tests for trait features (7 pass)
python3 -m pytest tests/test_mf_trait_features.py -q
```

Output: `audit_dashboard/data/mf_traits_walkforward_results.json`

---

## 8. Disclaimer
This is **not financial advice**. It is an educational research backtest with real data limits (free data, survivorship bias, estimated delisting, index vs fund universe). Past performance does not guarantee future results. Do your own diligence before investing.
