# Buffy: top picks per asset class, justification, and how the logic works

**Published October 23, 2026. Goal #1: trustworthy performance evidence on /audit.**
Companion to [GHCopilot's master summary](GHCOPILOT_20261023_MASTER_SUMMARY_PICKS_AND_PLAN.MD) — this note adds the Buffy-side per-class picks and the fee-split ETF analysis, and cross-references Zoo's winner-hunt.

## High-level answer

**Three independent agents ran three independent studies. All three reached the same verdict: no selection rule reliably beats a cheap, broadly diversified index fund.** No strategy reviewed here is MONEY-READY. What follows is the best-*supported* option per role, not a global ranking, and not a buy list.

| Study | Universe | Method | Verdict |
|---|---|---|---|
| Buffy walk-forward | 71 funds, 1994–2024 | Annual point-in-time, net of ER, vs SPY/XEQT | No rule beats index; cheapest ties |
| Copilot H-141 ([PR #759](https://github.com/eltonaguiar/findtorontoevents_antigravity.ca/pull/759)) | 95 funds | 9 *preregistered* rules, block bootstrap, random control | 0 survivors; best rule 31st pctile vs 95th required |
| Zoo Track 13/14 | 599 strategies + CAD funds | 4-gate + Benjamini–Hochberg FDR; CAD walk-forward 2004–2025 | 0 ELITE / 0 SURVIVOR; picker 11.89% < XEQT 14.25% < TDB902 17.08% |

## Top picks per asset class (Buffy side)

### US EQUITY — SWPPX / FXAIX / VOO (core), FZROX/FNILX (zero-fee variants)

**Justification:** SWPPX is the only T1 Proven fund in our composite rating (score 87.1, ER 0.02%). The walk-forward test shows the cheapest-3 rule is the only rule that *ties* SPY rather than losing to it (−0.9%/−1.0%/−1.0% at 1/3/5y, CI includes 0). Split-half proof: cheapest tercile returned **+9.2%/yr forward vs +5.0%/yr** for the dearest tercile (ρ = −0.38 between ER and future returns).

**Fee-vs-non-fee split (matched window 2018-09-28 → 2026-10-21, our NAV cache):**

| Fee tier | Examples | Mean net CAGR | Mean MaxDD |
|---|---|---|---|
| Zero (0.00%) | FZROX 14.05%, FNILX 14.72%, FZILX 9.23% | 12.67% | −34.4% |
| Near-zero (0.015–0.035%) | FXAIX 14.66%, VOO/IVV 14.63%, SWPPX 14.63%, SWLGX 16.30% | 14.65% | −34.0% |
| Low (0.04%) | VFIAX 14.60%, VTSAX 13.87%, VV 14.62% | 14.36% | −34.4% |

Same-index comparisons isolate the fee effect: **FZROX 14.05% vs VTSAX 13.91% (both total-US-market) — the zero-fee clone wins by ~0.14%/yr, which is exactly the fee difference.** FNILX vs FXAIX differences are index-sampling differences, not fee alpha. Below ~0.05% ER, fees stop separating funds; index construction does. Zero-fee means zero *expense ratio*, not zero risk — every tier shows ~−34% drawdowns (2020, 2022).

**ELI5:** a free ticket to the same show gives you the same seats, not a better show.

### MUTUAL FUNDS (active) — FOCPX as the single style-adjusted candidate; FCNTX/VPMCX for diligence

**Justification:** Raw winners FSPGX/SWLGX beat SPY by +5.6%/+5.1%/yr — but against a style-matched benchmark (VIGAX) the edge vanishes (+0.2%/−0.1%): growth beta, not skill. **FOCPX (Fidelity OTC, 0.78% ER) is the only fund whose edge survives style adjustment: +2.2%/yr vs VIGAX over 25 non-overlapping years, win 56%, stable in both 1994–2009 and 2010–2024.** Caveats: worst relative years −23.5%/−22.2%; concentrated growth; one manager-era result. CANDIDATE, not a proven winner.

Copilot independently prioritizes FCNTX (13.52% CAGR vs SPY 11.21% since 1995, MDD −49.2%) and VPMCX (13.70%, MDD −52.6%) for active-fund diligence. Both orderings are disclosed post-hoc research judgments, not preregistered selections.

**ELI5:** we checked whether the star runners were actually faster runners or just drawn a lucky lane (growth style). Only FOCPX still looked fast after fixing the lane — once. That's a candidate for more testing, not a trophy.

### CANADA — XEQT.TO (all-equity role) / VBAL.TO (60/40 role)

**Justification:** No rule beat the all-in-one in our test (cheap rule −3.0%/yr). Zoo's independent CAD walk-forward: picker 11.89% < XEQT 14.25% < TDB902 US Index 17.08% (net of MER). Copilot's matched-date comparison: XEQT 14.41% CAGR / −29.7% MDD vs VBAL 8.68% / −21.2% (2019-08 → 2026-10). These serve different risk roles, not a contest.

**ELI5:** one pre-mixed recipe beat every attempt to bake a better cake from separate ingredients — in three kitchens.

### BONDS — FXNAX/AGG as the defensive sleeve; SHY for lower drawdown; BKAG as the free baseline

**Justification:** Bonds are not a pick source (all `bond_*` classes NO_EDGE in the money-ready framework). They are the defensive sleeve in the rotation. Copilot: SHY 1.97% CAGR / −5.7% MDD (2002→2026) = lowest observed drawdown; BKAG 0.00% ER but −0.25%/yr — free did not prevent losses; TIP 3.38%/−14.5% since 2003.

**ELI5:** short bonds are a small boat, not dry land — and a zero fee doesn't stop waves.

### COMMODITY — no pick; GLD/IAU as research baselines only

**Justification:** Honest PF 1.03 but policy-clean 0.46, concentration NG=F 33%. Copilot: GLD 10.28%/−45.6%, IAU 10.70%/−45.1% (unequal windows — do not rank); USO −5.79%/−98.2% is why oil-futures ETFs are not buy-and-hold. CT=F is Zoo's sleeve-unblock candidate for the rotation universe, not a standalone pick.

**ELI5:** gold does a different job than stocks but can still lose half its value en route; an oil-futures ETF is not a warehouse of barrels.

### CRYPTO — abstain; CRYPTO SHORT RSI30-50 remains the single forward-monitored candidate

**Justification:** Aggregate long-side negative (intrabar PF 0.89, MDD ~100%). Only forward-valid cell: SHORT RSI30-50 (n=125, net PF 2.16, boot CI-LB 1.69, ex-top3 1.54). Copilot's independent BTC replay: OpenCode's claim refuted — 81.74% daily MTM drawdown despite high terminal growth.

**ELI5:** a ride can finish high after falling through most of the floor. Only the short-side cell has enough independent evidence to keep watching — watching, not funding.

### FOREX / FUTURES — abstain

Intrabar truth negative (forex); all `futures_*` NO_EDGE, and copper HG=F hit its stored stop first on independent replay. Session/gap/roll accounting must be fixed before any promotion.

**ELI5:** if the scoreboard's clock is wrong, it can award points for plays nobody could make.

### ETF / MULTI-ASSET — the tactical rotation family is the only validated edge; sleeve map from the T1/T2 list

**Justification:** The rotation/VAA/PAA family (Sharpe 0.88–1.21, MaxDD cut ~2.5x vs SPY, 2007–2026, three corroborating variants) is the only robustly-validated edge in the repo. The T1/T2 rated funds map directly onto its sleeves: SWPPX/FSKAX→VOO/VTI, FIPDX→TIP, VVIAX→VTV, FXNAX→AGG, SFENX→EEM, VGSLX→VNQ. Productize the wrapper (Zoo's P0), don't scale the pick engine.

**ELI5:** we already built the winning machine — it's a rotation of boring index funds. We were trying to win by picking stars; the data says win by rotating cheap whole teams and paying almost no fees.

## How the justification logic works (ELI5 of the method)

1. **Hide the future first.** Every December, the score uses only data that existed that day (unit-tested against leakage). You can't grade a race by letting the judge watch the finish.
2. **Subtract the fees before comparing.** Fund NAVs already include expenses; we charge them once, correctly (a unit bug that charged 100× fees was found and fixed — that discipline is why the numbers are trusted).
3. **Make the years independent.** Non-overlapping windows so one lucky decade can't be counted three times.
4. **Compare against the boring option.** Every rule is measured against just buying the index (SPY/XEQT), plus a matched random-selection control (Copilot) and FDR correction across all trials (Zoo).
5. **Adjust for style before crediting skill.** If a growth fund beats the market, it must beat *other growth funds*, not just the average.
6. **Demand stability, not averages.** Split-half and bootstrap CI: if the edge lives in one half or one symbol cluster, it's an artifact.
7. **Historical winners ≠ future winners.** Survivor databases exclude dead funds; picking champions afterward is not a hiring rule. A rule must pick winners *before* the race, or it isn't a rule.

**One analogy:** hiring a driver. Check the logbook is real, watch the whole journey including crashes, subtract fuel and tolls, compare against an ordinary driver on the same road — then test whether your hiring rule picks good drivers on *new* trips. A beautiful old arrival photo is not a driver's license.

## Plan (prioritized, with completion criteria)

1. **[P0] Productize the tactical balanced fund wrapper** (Zoo's P0) — core T1/T2 sleeves + rotation overlay; done when a public forward-tracked record exists and a sealed cohort resolves.
2. **[P1] Monitor FOCPX style-adjusted residual** — promote only if a fresh out-of-sample window keeps positive excess vs VIGAX with CI excluding 0.
3. **[P1] Forward-monitor CRYPTO SHORT RSI30-50** — the single funded-candidate pipeline; promote only after a sealed forward cohort clears the promotion bar.
4. **[P2] Extend rotation universe** (TIP/VTV/VNQ/SCHD, unblock CT=F as sleeve) and re-run the rotation backtest with the enlarged universe.
5. **Never:** scale the per-symbol pick engine, fund crypto-long/forex, or call any historical winner \"proven\" without forward data.

## Verification

- Buffy walk-forward: `python3 tools/mf_walkforward_backtest.py --fetch && python3 tools/mf_walkforward_backtest.py --universe all`; 5/5 unit tests; page `/audit/mutual-funds.html` HTTP 200, balanced DOM, disclaimers present.
- Fee-split table: computed from `audit_dashboard/data/mf_backtest_cache/` (72 cached funds, matched 2018-09-28→2026-10-21 window).
- Copilot: H-141, 12/12 tests, protocol SHA256 locked pre-data, [PR #759](https://github.com/eltonaguiar/findtorontoevents_antigravity.ca/pull/759).
- Zoo: [winner-hunt report](https://github.com/eltonaguiar/findtorontoevents_antigravity.ca/blob/main/updates/2026-10-23-winner-hunt-report.md), commits `504050d5e80` / `897bf6d4766c`.

**⚠ NOT FINANCIAL ADVICE — research and education only. Every fund named is an analysis subject, not a recommendation. Past performance does not predict future results. No choice here is MONEY-READY.**
