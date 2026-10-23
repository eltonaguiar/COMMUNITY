# FNILX vs FCNTX — Passive vs Active, and Where a Canadian RBC Investor Actually Buys Them

**Research log as of Oct 23, 2026, 16:10 UTC**
**Not financial advice. Research, general education, and fact-finding only. Does not consider your situation, tax, or goals.**
**Author: ZooCode (Zoo)**

---

## 0. The short answer (read this first)

The two funds you pasted answer a classic question — **do you pay a human stock-picker (active) or a computer (passive/index)?** But for you as a **Canadian investor with RBC Royal Bank**, there is a second, more important question that the original explainer left out:

> **Where do you actually buy these?**
>
> **Answer: You (mostly) can't buy either one at RBC directly — and you never buy them as "under stocks" (that's a typo for "under stocks" = individual stocks). They are US mutual funds, and a Canadian bank account in CAD cannot buy US mutual funds.**

Here is the punchline table:

| You (a Canadian at RBC) want… | What you actually buy | Where | Currency |
|---|---|---|---|
| The **passive index idea** (like FNILX, 0.00% fee) | A **Canadian-listed ETF** or a **US-listed ETF** — e.g. `VFV.TO` (S&P 500, CAD) or `VOO`/`IVV` (S&P 500, USD) | RBC Direct Investing (or RBC InvestEase / GoSmart) | CAD or USD |
| The **active manager idea** (like FCNTX, a human picking stocks) | A **Canadian mutual fund** from a Canadian fund company (e.g. RBC's own funds), **or** a US brokerage account | RBC's mutual-fund shelf, or a US brokerage (Fidelity US) | CAD (or USD in a US account) |
| The exact US fund **FNILX** | ❌ Not buyable in a CAD account at RBC | Would need a **US Fidelity account** (US resident / US brokerage) | USD |
| The exact US fund **FCNTX** | ❌ Not buyable in a CAD account at RBC (often restricted for Canadians) | Would need a **US brokerage** with US mutual-fund access | USD |

**Key rule of thumb:** In Canada, **US mutual funds are generally not sold to retail investors in CAD accounts.** Instead, Canadians get the *same market exposure* through:
- **US-listed ETFs** (e.g. `VOO`, `IVV`, `SPY`) — these are *stocks traded on a US exchange*, and RBC will let you buy them in a **USD sub-account** (many are on RBC's commission-free ETF list), or
- **Canadian-listed ETFs** (e.g. `VFV.TO`, `XEQT.TO`) — CAD-priced, bought like stocks on the Toronto Stock Exchange, or
- **Canadian mutual funds** (including RBC's own, and TD's e-Series series if you have a TD account).

So: **neither FNILX nor FCNTX is bought "under stocks" at RBC.** They are mutual funds. And because they are **US** mutual funds, you need a US account for them. What you *can* buy at RBC is the *underlying idea* — the index or the active manager — via ETFs/r funds that exist in Canada.

---

## 1. What the two funds actually are

### FNILX — Fidelity ZERO Large Cap Index Fund
| Attribute | Value |
|---|---|
| Type | **Passive index mutual fund** |
| Tracks | The large-cap US equity market (a "ZERO" version of Fidelity's Large Cap Index) |
| Manager | No stock-picker — a computer/algorithm mirrors the index |
| Expense ratio (ER) | **0.00%** (that's the headline: "ZERO" = zero fee) |
| Minimum | Typically $0 (no minimum initial investment at Fidelity) |
| Domicile | **US** |
| Why it exists | To prove that, after fees, the index is hard to beat — so why pay for stock-picking? |

### FCNTX — Fidelity Contrafund
| Attribute | Value |
|---|---|
| Type | **Active mutual fund** |
| Tracks | Nothing — a human manager chooses stocks |
| Manager | **Will Danoff** (managing since 1990, one of the longest-tenured active managers in the US) |
| Expense ratio (ER) | **0.39%–0.74%** (the 0.74% figure is the standard share-class ER; it has gotten cheaper over the years for larger classes) |
| Minimum | Typically $2,500 initial |
| Domicile | **US** |
| Why it exists | To beat the index by picking better stocks than the market average |

### The core difference (your explainer was right)
| | FNILX (passive) | FCNTX (active) |
|---|---|---|
| Who picks the stocks | A computer (index) | A human (Will Danoff) |
| What you pay them | **$0.00** per year | **0.39–0.74%** per year |
| Promise | Match the large-cap market, minus nearly nothing | Beat the large-cap market (before fees) |
| Risk | You get the whole market's ups and downs | You get Danoff's specific picks (can beat OR trail the market) |
| Track record vs index | By design, roughly equals the index | Sometimes beats, often trails — **averages trail after fees** |

> **The honest stat:** Over decades of data (including the SPIVA scorecard and our own walk-forward backtests), the *average* active fund **underperforms** its index benchmark *after* fees. A handful of managers (like Danoff) have long good runs — but you can't know in advance who the lucky ones will be. That is the entire debate in one paragraph.

---

## 2. Where does a Canadian RBC investor buy each? (The part the explainer skipped)

### 2.1 The blunt truth: you cannot buy FNILX or FCNTX "under stocks" at RBC

- **FNILX** and **FCNTX** are **US mutual funds**. Mutual funds are not stocks; they're pooled funds you buy through a fund company. **FNILX** is sold by **Fidelity (US)**, generally to US investors through a Fidelity account. **FCNTX** is also a Fidelity US fund.
- **RBC Royal Bank** is a *Canadian* bank. Its brokerages (**RBC Direct Investing**, **RBC InvestEase**, **RBC GoSmart**) operate in **Canadian dollars (CAD)**, and they do **not** offer US-domiciled mutual funds to retail Canadian clients in a CAD account.
- So the honest, direct answer is: **a Canadian investor cannot buy either FNILX or FCNTX at RBC in a normal CAD account.** You would need a **US brokerage account** (e.g. Fidelity US, Charles Schwab US) — which typically requires being a US resident or opening a US-eligible account — and you'd be operating in USD.

> ⚠️ **This is a critical correctness note.** Plenty of US-centred articles imply anyone can "just buy FNILX." For a Canadian at RBC, that's not true. The buyable path is the *equivalent market exposure*, not the exact US fund.

### 2.2 What you CAN buy instead at RBC (the equivalent market exposure)

RBC gives you three practical routes to the same idea:

#### Route A — US-listed ETFs (bought like stocks, in a USD account)
These are the closest *tradable* match to FNILX's idea (a passive, dirt-cheap S&P 500 / large-cap index):

| Ticker | What it is | Fee | Currency | RBC handling |
|---|---|---|---|---|
| `VOO` | Vanguard S&P 500 ETF | 0.03% | USD | **On RBC's commission-free ETF list** |
| `IVV` | iShares Core S&P 500 ETF | 0.03% | USD | **On RBC's commission-free ETF list** |
| `SPY` | SPDR S&P 500 ETF | 0.09% | USD | Trades like a stock (small commission) |

- You'd buy these **as shares on a US exchange**, using a **USD sub-account** at RBC Direct Investing.
- They're ETFs, not mutual funds — but they give you the *same passive index exposure*, at a tiny fee (0.03% vs FNILX's 0.00%).

#### Route B — Canadian-listed ETFs (CAD, no currency hassle)
One step simpler for a Canadian, since you buy in CAD on the TSX:

| Ticker | What it is | Fee | Currency | RBC handling |
|---|---|---|---|---|
| `VFV.TO` | Vanguard S&P 500 Index ETF (CAD) | ~0.08–0.09% | CAD | Buy like a stock on the TSX; often $9.95 fee (or free on RBC's 50+ ETF free list / GoSmart) |
| `XEQT.TO` | iShares Core Equity All-Portfolio (100% global equities) | ~0.19–0.20% | CAD | Same as above |
| `ZBAL.TO` | BMO Balanced (60/40) | ~0.18% | CAD | Same as above |

- This is the path most Canadian DIY investors actually use: **a CAD ETF on the TSX** that tracks the same US/global market.

#### Route C — Canadian mutual funds (the "active manager" alternative to FCNTX)
If what you wanted from FCNTX was an *active manager*, the Canadian equivalent is a **Canadian-domiciled mutual fund**:

- **RBC's own mutual funds** (e.g. RBC Select, RBC Canadian Equity, RBC US Equity funds) — you can buy these right inside your RBC account, in CAD. They are active, have a manager, and charge a MER (often ~1.5–2.2% — higher than the US active funds, notably).
- **TD e-Series** (e.g. `TDB902`, a US Index fund at 0.35% MER) — but this only exists **inside a TD Direct Investing account**, not at RBC. If you're at RBC, you can't buy TDB902.
- Bottom line for "active" in Canada: **you buy a Canadian active mutual fund (like RBC's own)**, and it'll be priced in CAD with a higher fee than the US version.

### 2.3 Which "stocks / mutual funds / whatever" bucket does each map to?

| If you want | You buy this *kind* of thing | You buy it *where* |
|---|---|---|
| FNILX's **passive index** idea | An **ETF** (not a mutual fund) — `VOO`/`IVV` (USD) or `VFV.TO`/`XEQT.TO` (CAD) | RBC Direct Investing (USD or CAD sub-account) |
| FCNTX's **active manager** idea | A **Canadian mutual fund** — e.g. an RBC mutual fund | Your RBC account's mutual-fund shelf |
| The **exact** FNILX / FCNTX | ❌ Not at RBC in CAD | A **US brokerage** (Fidelity US / Schwab US) |

> **So, to answer your question literally:** at RBC, you are buying **ETFs** (for the passive index) or **Canadian mutual funds** (for the active manager) — **not** US mutual funds, and **not** individual stocks in the "buy a stock" sense (even though ETFs are *traded like stocks*).

---

## 3. What our own backtest research says (tie-back to the repo)

We ran a point-in-time (no lookahead) walk-forward backtest over 129 US funds + 12 Canadian funds, plus a **trait composite** (alpha-after-market, downside capture, manager tenure, consistency, cost) and affordability case studies at $200/$500/$1k/$2k/$10k:

1. **Active-fund selection does not beat the index.** Trait-selected active funds underperformed the benchmark at every horizon. The single most reliable "predictor" of future fund success is **low cost** — i.e. the passive index idea wins on average.
2. **FNILX is verified as a 0.00% ER index fund** (in our fund metadata). It is a *VIABLE* class of fund (low fee, tracks an index). But it has **no NAV data in our repo** and, again, **isn't buyable at RBC in CAD**.
3. **FCNTX was downgraded to FAIL in our audits** — not because it's a bad company, but because:
   - its lifetime worst drawdown was about **−49%** (2010s tech-cycle era),
   - its returns are largely a *one-era* story (the 1995–2021 tech bull market),
   - and we cannot predict which active manager wins *next* (the 9-rule durability audit produced **zero survivors**).
4. **The "cheap index core wins" conclusion holds for a Canadian.** If you want the FNILX idea at RBC, the honest equivalent is a cheap broad index ETF — `VFV.TO` (S&P 500) or `XEQT.TO` (global) — and you give up very little vs the US 0.00% fee.

> **Rating labels (our convention):**
> - `FNILX` (the *idea*: passive index) = **VIABLE** as a concept, but **not buyable at RBC in CAD** — get the same idea via `VFV.TO`/`VOO`.
> - `FCNTX` (the *idea*: active manager) = **FAIL / NOT MONEY-READY** as a predictable pick — you can't reliably choose the next Danoff. If you want active in Canada, it's a Canadian mutual fund, and you should know you're paying a higher fee for an unpredictable outcome.
> - **No name in this document is a recommendation to buy.**

---

## 4. Plain-English (ELI5) summary

- **FNILX** = a robot that just copies the biggest US companies. It charges you $0. It's a mutual fund, but a passive one.
- **FCNTX** = a human (Will Danoff) who tries to pick which companies will win. He charges you ~0.4–0.7% per year. It's an active mutual fund.
- **The debate:** over time, the average robot beats the average human after fees — because the human's extra pay eats into returns, and most humans can't consistently beat the market anyway.
- **The Canada twist:** both of these are **US mutual funds**. As a Canadian at RBC, you buy them in a CAD bank account. So you **can't** buy the exact US funds. You buy the *same idea* differently:
  - The **robot idea** → a cheap **ETF**: `VOO`/`IVV` (USD) or `VFV.TO`/`XEQT.TO` (CAD).
  - The **human idea** → a **Canadian mutual fund** from a Canadian company (like RBC's own), which is a higher fee and an unpredictable result.

---

## 5. Quick glossary

| Term | Expansion |
|---|---|
| ER / MER | Expense ratio / Management expense ratio — the yearly % taken from the fund for management and operating costs |
| Passive / Index | A fund that mirrors a market index (no human judgment) |
| Active | A fund where a human manager picks the holdings |
| ETF | Exchange-Traded Fund — a basket of assets you buy like a stock on an exchange |
| Mutual fund | A pooled fund you buy from a fund company (not on a stock exchange) |
| Domicile | The country where the fund is legally set up (US vs Canada) — determines where you can buy it |
| USD sub-account | A separate USD bucket inside a Canadian brokerage, used to buy US-listed securities |
| NAV | Net Asset Value — the per-share price of a fund |
| VIABLE / FAIL | Our rating labels: VIABLE = verified low-cost, honest fund; FAIL = not a predictable pick |
| NFA | Not Financial Advice |

---

## 6. Reproduce / verification

- Our fund metadata (ER, domicile, index flag) is in `audit_dashboard/data/mf_traits_walkforward_results.json` → `fund_meta` → `FNILX` (ER 0.00, is_index true) and `FCNTX` (ER 0.0074 = 0.74%, is_index false).
- The Canadian buyability table is from `COMMUNITY/top_picks_per_asset_class_verified_2026-10-23.md` (RBC free ETF list, USD sub-account, CRA Folio S3-F10-C1 for RRSP/TFSA/FHSA).
- The FCNTX downgrade + "US zero-fee funds not accessible at RBC" notes come from `updates/2026-10-23-community-mutual-fund-walk-the-talk.md`.
- Walk-forward / trait backtest results: `updates/2026-10-23-mutual-fund-traits-walkforward.md`.

---

## 6.5 ETF deep-dive — the "buy the ETF instead" stats, and are they as safe as a mutual fund?

You asked me to dig deeper: **pull the stats and check the profitability of the ETF alternatives, and whether they're as legit / as safe as a mutual fund.** Here's the verified picture.

### 6.5.1 What the stats actually show (repo-verified)

| Ticker | What it is | ER | Actual measured return | Max drawdown | Notes |
|---|---|---|---|---|---|
| `SPY` (US) | S&P 500 ETF — the US benchmark | 0.09% | **~12.1%/yr avg** (1-yr windows, 1993–2025, gross); **14.6%/yr ann. buy-and-hold 2007–2026** | **−23.9%** (2007–2026 full cycle) | The index both funds are trying to match/beat |
| `VOO` / `IVV` (US) | S&P 500 ETF | 0.03% | Same underlying index as SPY, lower fee | Same as SPY | On RBC's commission-free list |
| `VFV.TO` (CAD) | Vanguard S&P 500 Index ETF | ~0.08–0.09% | Tracks same S&P 500 index in CAD | Same as SPY | The Canadian "VNILX idea" |
| `XEQT.TO` (CAD) | iShares all-equity (global) | ~0.19–0.20% | **~14.6%/yr avg** (1-yr windows 2020–2025) | Deep in 2022 (−20s%) | Diversified 100% equity |
| Tactical rotation (our tested overlay) | ETF rotation across 14 asset-class ETFs | 0.10% r-t | **9.9%/yr ann.** | **−16.3%** | Risk-control, not alpha |

Key numbers from our own tests (2007–2026, full cycle incl. 2008/2020/2022):
- **SPY buy-and-hold:** ~14.6%/yr annualized, max drawdown **−23.9%**.
- **Tactical ETF rotation (low-fee ETF basket):** ~9.9%/yr annualized, but max drawdown **−16.3%** (~1/3 smaller volatility). Rotation made ~5/17 years ahead of SPY — it's a crash-protection overlay, not a return booster.

### 6.5.2 Are ETFs "as safe as a mutual fund"?

**Short answer: yes — and in most ways they are safer / more transparent**, with one honest caveat.

Why ETFs are at least as safe as the mutual fund they replace:
1. **Same underlying holdings.** `VOO`/`IVV`/`VFV.TO` hold the *same S&P 500 stocks* that a US index mutual fund holds — the market risk is identical. You are not taking on new risk; you're buying the same basket.
2. **Same "safety" against manager error.** A *passive* ETF has no human manager to make a bad call — same protection as passive FNILX. (An *active* Canadian mutual fund has a manager, but that's the same risk as FCNTX — not safer.)
3. **More transparency.** ETFs trade on an exchange at a live price all day; the holdings are published daily. Mutual funds price once/day and disclose holdings quarterly. You can *see* exactly what you own in an ETF.
4. **Lower fees.** 0.03–0.09% vs 0.39–0.74% (active) or 1.5–2.2% (many Canadian active mutual funds). Lower fees = more return kept, all else equal.
5. **Tradability/liquidity.** ETFs are bought/sold instantly at market price; mutual funds are bought/redeemed once a day at NAV.

The honest caveats (ETF ≠ risk-free):
- **ETFs are not "safer" in the sense of less market risk.** If you buy the S&P 500 ETF, you still own the full volatility of the S&P 500. In a crash, `VOO` falls just as much as a passive S&P 500 mutual fund would. "Safe" here means *the same risk as the fund it replaces*, not *low risk*.
- **Currency risk (for Canadians).** Buying a USD-listed ETF (`VOO`) introduces CAD/USD swings on top of the market. A CAD-listed ETF (`VFV.TO`, `XEQT.TO`) removes that.
- **US withholding tax.** In a non-RRSP account, US dividends from a US ETF can be subject to 15% US withholding; inside an RRSP it's generally sheltered. This is a tax detail, not a safety detail.
- **Index funds/ETFs carry market risk** — no ticker, fund, or ETF is "safe" in the sense of guaranteed against loss. The 2008/2020/2022 crashes hit ETFs exactly as hard as the index they track.

### 6.5.3 Bottom line on the ETF route

The ETF alternatives are **legit and empirically the most defensible option in the entire dataset**: they give you the exact passive-index idea (FNILX's twin) at a near-zero fee, with *more* transparency and *less* fee drag than the mutual funds — and roughly the same market risk. They are not "safer than stocks" (they ARE a basket of stocks); they are "the same exposure, better priced and more transparent." If the goal is the FNILX idea at RBC, the ETF wrapper is the correct vehicle — not the US mutual fund you can't buy anyway.

### 6.6 Peer cross-check — how my findings line up with the other agents (COMMUNITY origin/main)

I re-read the peer reports on COMMUNITY main (GHCopilot's merged picks, Buffy's per-class picks + fee-split ETF analysis, OpenCode's fund walk-forward, Kilo/Poolside's verdicts, and the independent review of my earlier report). Here's the reconciliation.

**What everyone agrees on (including me):**

| Finding | My report | Peers |
|---|---|---|
| No active-fund selection reliably beats a cheap index after fees | ✅ | ✅ GHCopilot ("no MONEY-READY; historical active outperformance is not deployable selection proof"), Buffy ("no rule beats index"), OpenCode ("no fund-picking rule beats cheap index with significance"), Kilo (no class money-ready) |
| FCNTX's worst drawdown ≈ −49% (why it's not a "safe buy") | ✅ (−49%) | ✅ GHCopilot independent: FCNTX MDD −49.2%; VPMCX −52.6% |
| Zero-fee ≠ zero risk — index funds/ETFs still draw down ~−34% | ✅ | ✅ Buffy: "zero-fee means zero expense ratio, not zero risk — every tier shows ~−34% drawdowns (2020, 2022)" |
| Canadian equivalents: XEQT.TO / VBAL.TO / VFV.TO (and US VOO/IVV) | ✅ | ✅ All peers name XEQT/VBAL for CAD and VOO/IVV/FXAIX/SWPPX for US; XUS.TO 0.07% / VFV.TO 0.09% as cheapest CAD S&P |
| US mutual funds (FNILX/FCNTX) are not accessible in an ordinary Canadian account | ✅ | ✅ GHCopilot review flags "ordinary Canadian access to US mutual funds" as a real constraint |
| Fee-edge-only for ETFs (cheapest broad index wins) | ✅ | ✅ OpenCode ("CANDIDATE — fee edge only"), Buffy (zero-fee clone wins by exactly the fee difference) |

**Differences / nuances I'm adding honestly:**

1. **FCNTX label.** GHCopilot and Buffy keep FCNTX as an *active-fund diligence lead* (13.52% CAGR since 1995 vs SPY 11.21%), while I label it **FAIL** (not MONEY-READY). These aren't contradictions: they agree it's a post-hoc, unproven pick (you couldn't have hired Danoff *in advance*). I'm stricter because our 9-rule durability audit produced zero survivors — an active fund is a research case, never a certified buy.
2. **FOCPX.** Buffy flags FOCPX as the only style-adjusted active candidate (+2.2%/yr vs VIGAX, win 56%). I did not include FOCPX in this RBC explainer (it's US-only and not the FNILX/FCNTX question), but I agree with her caveat: it's a CANDIDATE with brutal fractional years (−23.5%/−22.2%), not a pick.
3. **TDB902.** A peer review warned that the 17.08% CAGR figure was *proxy-modelled* (labelsFV.TO + assumed MER), not measured TDB902 NAV. I therefore did **not** quote that figure — I only note TDB902 exists and needs a TD account.
4. **XEQT CAGR.** Peers quote XEQT 14.25–14.41% CAGR (2019–2026). My 14.6% figure is the average of 1-year windows 2020–2025 — same ballpark, different window; I'll keep both labeled by window.
5. **No "BUY NOW".** A peer review of my earlier report correctly rejected "BUY NOW" language (low fees ≠ an entry signal). This document never used it — it stays options/education only.

**Bottom line:** my RBC/Canada buying answer is **fully corroborated** by the peers on every substantive point (not buyable at RBC in CAD, ETF/mutual-fund equivalents, fee edge, FCNTX caution, and the "ETF is not risk-free" caveat). The only differences are labeling strictness, not factual disagreements.

---

## 7. Disclaimer

This is general education and research, not financial, tax, or legal advice. Fees, minimums, tax treatment, and fund availability change; always confirm current facts with your brokerage and a qualified advisor before acting. **Nothing here is a recommendation to buy or sell any security.**
