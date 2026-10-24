# OPENCODE_OPENROUTER-FLINT — Case Study: "After ML & Copy-Trading, Why Index Funds?" (2026-10-24)

**Author:** OPENCODE_OPENROUTER-FLINT (opencode/beam-free, fleet identity confirmed)
**Date:** 2026-10-24, 08:17 UTC
**Status:** Case study write-up of this session's responses + findings; cross-referenced against the peer case study; THIRD-AGENT (OpenRouter Flint) confirmation + verification caveat added.
**Disclaimer:** Not financial advice. Research/education only. No pick below is money-ready.

---

## 0. Context / TL;DR

User arc this session (compounded over the last several days of peer rounds):

1. "Winning traders / competitions exist (crypto/stock trading comps) — can we replicate that for consistent gains?"
2. (Given my findings) Re-add my findings in terms of the MF vs stocks vs index-funds/crypto discussion, and my final verdict: are the picks index funds, $0-entry mutual funds, or what — and why?
3. Explain why, despite ML and copy trading, we still have no true winner for anything, so index funds win — cross-reference the other agent's case study if I see it.
4. "Go go go" / "go" — proceed.

My answers: (a) winners exist but are not replicably so via our gates; (b) the verdict is broad index ETFs / low-fee index mutual funds as **vehicles**, not alpha — with TD e-Series low-MER index MFs ($100 start, no subsequent min, fractional auto-reinvest, $25 PAC optional) as the $0-entry-class MF option; (c) ML/copy-trading edges unraveled → the only surviving repeatable edge is cost → index funds win; (d) cross-referenced with the peer case study (INCEPTION/ZOOCODE `INCEPTION_ZOOCODE_20261024_CASESTUDY_ML_VS_INDEX_FUNDS.MD`, addendum by GHCopilot) — **fully consistent**.

---

## 1. User Q1: Successful traders / competition winners — can we replicate for consistent gains?

**Answer:** Yes, real winners exist. But replicating them ≠ having a replicable edge.

- Tournament success ≠ strategy skill (selection bias; top finishers can be lucky).
- Published winners rarely have complete timestamped trade records → can't reconstruct honestly.
- Competition conditions ≠ real conditions (no slippage/spreads/fees/risk limits; risk tolerance is a gate, not a parameter; capacity effects).
- Our gates exist precisely to kill such winners: MC ≥95th pct, DSR >0.95, MDD ≤20%, 2× cost stress, sealed forward cohorts.

**Conclusion:** No certified replicable winner from competition copying. Index funds (cost edge) are the answer, not competition winners.

---

## 2. User Q2: MF vs stocks vs index funds / crypto — findings + final verdict

- Stocks / single-stock picks: **FAIL** (equity intrabar honest PF 0.87, n=234).
- Crypto strategies: **FAIL** (trend MDD −55% to −70%, MC low; shorts artifacts / n<100).
- MF selection: **FAIL** across ~450 fund studies (Grok 129, OpenCode 118, GHCopilot 95/H-141) — zero rules beat cheapest broad index; cost ρ ≈ −0.38 is the only predictive trait.
- ETFs / low-fee index MFs: **CANDIDATE as vehicles** (XEQT #1, VFV/XUS #2, XGRO/XBAL, VEQT/VGRO/VBAL, TDB902/TDB900).

**Final verdict:** The picks are **broad index ETFs / low-fee index mutual funds** — market exposure (vehicles), not alpha. The $0-entry mutual-fund angle = low-MER index MFs via TD e-Series (TDB902 US idx MER 0.28% 10y 15.1%; TDB900 CDN idx MER ~0.2%). (Not RBC Select Balanced — RBF460 MER 1.94%, FAIL.)

---

## 3. User Q3: Why, despite ML + copy trading, no true winner → index funds win?

- Markets near-efficient; most return = beta.
- 599-strategy winner hunt → post FDR/DSR → noise.
- ML/copy-trading edges unraveled (artifacts, batches, n<100, overfitting). ML did build the measurement infra to prove negatives.
- Only surviving edge = cost → cheapest broad index wins.
- Index = no timing claim → passes gates.

**Cross-ref:** Other agent (Zoo/ZooCode via INCEPTION) published the ML-vs-index case study; GHCopilot addendum confirmed pillars. My round-3 findings fully consistent. **No conflict.**

---

## 4. Third-agent (OpenRouter Flint) confirmation + verification caveat (2026-10-24, appended)

**Third agent: OpenRouter Flint.** Confirmed — **fully consistent on every pillar** with ZooCode and OpenCode (and GHCopilot):
- 0 money-ready; cost-only edge; index vehicles as exposure not alpha; active MFs fail; competition winners not replicable; cross-ref correct.

**Independent check on Flint's one genuinely new claim:** "horizon-capped PF ≈1.07 kills the long-hold edge."

Agent ran independent cut on stored PnL by hold/lag (`age_hours` buckets) from `/home/eaguiar2015/findtorontoevents_antigravity.ca/audit_dashboard/data/dashboard_data.json` (`picks.recent_closed`, rows with `pnl_pct` + `age_hours` not None):
- 6–24h: n=38, WR 39.5%, mean −0.45%, PF 0.71
- 24–72h: n=76, WR 44.7%, mean +1.59%, PF 2.26
- 72–168h: n=310, WR 42.6%, mean −0.06%, PF 0.97
- 168–720h: n=932, WR 44.3%, mean +0.48%, PF 1.25
- 720h+: n=2136, WR 46.2%, mean +0.42%, PF 1.29
- **Overall: n=3500, WR 45.3%, mean +0.41%, PF 1.26**

**Verdict:** On stored PnL, longer holds don't degrade — PF ≈1.29 (long-hold) / ≈1.26 (overall). Could NOT confirm "1.07" from naive stored cut. The `1.07` almost certainly comes from a different method (honest intrabar-replayed, fixed-horizon cap). **Direction right (honest measurement beats stored); number not yet reproduced as fact.**

**Minor precision notes (not behavior changes):**
- `cost p ≈ 0.38` → should be **ρ ≈ −0.38** (correlation, negative sign).
- "shorts artifacts n<1,100" → almost certainly typo for **n<100** (RSI30-50 short n=125).
- "~$0 entry MF (TDB902)" → in-practice right ($100 initial, no subsequent min, DRIP); qualifying reason is low MER + broad index, not entry fee.

**Bottom line:** Nothing changes on pillars; **3-agent convergent** (GHCopilot + ZooCode + Flint); only unendorsed item: PF≈1.07 needs honest-method reproduction before entering canonical record.

---

## 5. Consolidated write-up of this session's responses (save-out).

- Round-3 cross-check note: `OPENCODE_BEAM_20261023_1903Z_ROUND3_CROSSCHECK.MD` (self-corrections: MomentumEMA batch artifact → HOLD; XLF downgrade → PAPER-ONLY×LOW/HOLD; lag≠holding; fee wording tempered; TDB902 scope).

---

## 6. Verification / reproducibility.

- Live payload: `/tmp/dd_final.json` — generated 2026-10-24T07:07Z; 14 actives; 3,500 closed; smart_picks=0; money_ready verdicts present (all classes FAIL/not ok).
- Community: origin/main at 17d02fb (incl. `INCEPTION_ZOOCODE_20261024_CASESTUDY_ML_VS_INDEX_FUNDS.MD`).

---

## 7. Disclaimer.

Not financial advice. Research/education only. Nothing money-ready.

---

## 8. Money-ready ASAP recommendation (2026-10-24, appended per user instruction).

If we had to get money ready ASAP in a few asset classes, the only honest way is to lock in the index vehicles as the actionable money-ready positions.

- Equity: XEQT (MER 0.20%, CAD, RRSP/TFSA/FHSA) — BUY-CORE. US sleeve: VFV/XUS (MER 0.09/0.10). Risk mix: XGRO/XBAL.
- Fixed income: SHY — BUY-SLEEVE.
- Gold: GLD/IAU — BUY-SLEEVE ≤5%.
- MF vehicles (TD channel): TDB902 (US idx, MER 0.28%, 10y 15.1%, $100 start/no subsequent min, DRIP; perf leg HOLD/proxy) / TDB900 (CDN idx, MER ~0.2%).

Not worth trying to find a new strategy edge ASAP: edge hunt effectively closed (599 → noise post FDR/DSR); remaining candidates fail gates (12-1 DSR 0.89; sector-top-3 MDD −20.8% > 20%; GEM n=44). New edge now = sealed forward cohorts + honest intrabar fixed-horizon re-cuts — months of work, likely noise.

**Verdict:** Stick to index funds for actual money-ready positioning; strategy-level money-ready deferred/blocked.

Not financial advice. Research/education only. Nothing money-ready.
