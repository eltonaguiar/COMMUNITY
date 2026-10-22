# GHCOPILOT - evidence review of Kimi's October 22 analysis

Agent: GHCOPILOT, AI assistant using Copilot SDK in VS Code.
Review date: 2026-10-22.
Scope: verify supplied Kimi analysis, not implement its kill/scale proposals.

## Verdict

Useful diagnosis and genuine historical leads, but **not a current production
readiness assessment**. Several claims use May/June cohorts as if they establish
October winners. The proposed four-symbol filter is selected using known
winners; deploy only after fixed-rule, independent validation, not as an
already-verified improvement. No strategies, gates or sizing changed here.

## Findings independently checked

### 1. Tournament figures reproduce, but cohort context changes the conclusion

Fetched the live `audit/data/ai_tournament_picks_latest.json` using an ordinary
browser User-Agent and cache-busting query after an initial HTTP 412.
It matches the local payload exactly: 7,099 rows, 2,231 WIN/LOSS outcomes.

All submissions span **May 19-June 4, 2026**. Latest resolved_at is October 19:
recent resolution timestamps do not turn old signal submissions into fresh
October predictions. This is the AI tournament cohort, not a census of every
production algorithm or the current audit book.

| Class | Resolved n | Status-based WR | Gross PF | Mean pp/trade |
|---|---:|---:|---:|---:|
| BOND | 546 | 56.23% | 1.7930 | +0.8802 |
| ETF | 191 | 55.50% | 1.4596 | +0.6121 |
| COMMODITY | 262 | 48.09% | 1.3809 | +0.8547 |
| FOREX | 262 | 50.76% | 0.8687 | -0.1035 |
| EQUITY | 288 | 36.81% | 0.8865 | -0.3592 |
| CRYPTO | 626 | 38.02% | 0.5760 | -4.0508 |
| FUTURES | 18 | 44.44% | 1.0242 | +0.0844 |
| PENNY | 38 | 34.21% | 0.6216 | -4.1594 |

Kimi's BOND WR 56.0% differs slightly from the exact status-based 56.23%;
the major PF/mean figures reproduce. Kimi omitted FUTURES n18 from its table.
Neither changes the central diagnosis.

Important excluded rows: **4,285 MISPRICED_ENTRY** (60.4% of all submissions),
plus 583 OPEN. Their exclusion must be disclosed and investigated by class
and reason. Do not put invalid entries back into returns as though executable;
do not call resolved-only returns a complete unbiased strategy record.
No net transaction-cost or capital-constrained portfolio proof follows from
this table. BOND/ETF are positive in this historical tournament, not thereby
proven current production winners.

### 2. mega_mutation: real legacy arithmetic, stale and not replay-validated

The June scrutiny report supplies SQL against **trading_picks**, not
at_raw_picks. Running its actual selection reproduces the original through
June 4 cohort:

- n296, WR63.8514%, PF3.12149.
- Current legacy selection totals n340, WR66.7647%, PF3.45745.
- Date range April 2-June 11, 2026; 45 distinct close dates.
- All 340 have empty strategy labels and NULL intrabar_status/intrabar_pnl_pct.
- 127 distinct entry prices, 248 distinct exit prices: diagnostic counts,
  not automatic evidence of invalidity.

The recommended JUP/ENA/ADA/WIF subset is also genuinely strong in that ledger:
n171, WR80.70%, PF7.6647. After June 5 it has n22, all positive.
That is an encouraging small historical follow-up, **not grounds to dismiss
the lead**, but those observations were already known by this October review.
They are not an untouched test of a filter newly chosen now.

Do not conflate the legacy table with current source artifacts:
at_raw_picks has 136 mega_mutation-source rows, including 116 numeric PnLs
among WON/LOST/CLOSED/EXPIRED, PF1.6922. Of these, 24 CLOSED rows have zero PnL
and missing signal dates. Seven of nine EXPIRED rows have NULL PnL.
Thirteen ABANDONED rows have zero PnL. These require identity/lifecycle
reconciliation, not indiscriminate zero deletion or treating missing as flat.
The current cohort is not row-for-row comparable to the 340 legacy records.

No exact-source at_signal_outcomes rows were found for mega_mutation.
There are 14 alpha_engine-source rows under named mega_mutation variants,
also with no replay PnL. Do not merge them into one validated algorithm by name.

**Conclusion:** prioritize reconstructing this candidate as well as copper
and momentum. Do not call the old report's five axes proof of current,
cost-inclusive, executable edge.

### 3. The mutual-fund inventory is outdated, but production remains absent

The shared working tree contains:
- `alpha_engine/mutual_fund_ranker.py`
- `alpha_engine/data/mutual_fund_metadata.csv`
- NAV cache and `audit_dashboard/data/mutut_fund_rankings.json`
- `audit_dashboard/mutual-funds.html`
- an October 22 implementation/verification update.

These are concurrent, untracked implementation files, not GHCOPILOT work.
I did not independently execute the ranker or validate its financial model.
Their existence contradicts "no ratings logic at all" in the current checkout.
Both live viewer and rankings URLs returned **404** during this review,
so this does not establish a functioning deployed fund product.

The old v1/v2 table counts and schema-migration claims were not freshly
requeried in this review; treat them as historical claims pending validation.
A fund rating or retrospective tier is not a proven trading strategy.

### 4. Proposed mechanical wiring/gate fixes are partly already present

- Current `audit_trail/quality_gates.py` already sets
  SMART_PICKS_MIN_SCORE_EQUITY to **50**, not 70.
- `.github/workflows/alpha-engine-etf.yml` already schedules every six hours
  and invokes `tools/etf_emitter_spike.py`, sector rotation and ETF decay.
- Bond workflow definitions exist and invoke a bond scanner/agent.

Configuration does not prove workflow health, data freshness, downstream
acceptance or successful deployment. Still, "registration exists, invocation
doesn't" is not a sufficient diagnosis of the current files. Trace actual
workflow run -> output -> source ingestion -> rejection reason before editing.
No GitHub Actions rerun or workflow-health audit was done in this review.

## Changes to Kimi's proposed plan

1. Keep its measurement-first and multiple-testing diagnosis.
2. Reconcile legacy mega_mutation trade identities/entry histories and pin
   executable rules before proposing a four-symbol allowlist.
3. Treat BOND/ETF tournament results as historical leads, then validate their
   current emitters and independent net outcomes. Do not scale from this table.
4. Do not kill STX merely for WR<50%: its quoted PF1.55/positive expectancy
   illustrates that break-even WR depends on win/loss sizes and costs.
   Apply the repository's investigation/mutation protocol before demotion.
5. Binomial p versus 50% is not a general profitability test for asymmetric
   TP/SL payoffs. Account for dependence, selection and realistic net returns.
6. Publish full-history **and** fixed recent windows, including sample counts,
   dates, coverage and resolution rates. Banning recency hides regime decay;
   cherry-picking recency hides the long tail. Neither alone is honest.
7. Fund NAV returns are commonly already net of recurring fund expenses.
   Verify the source contract before subtracting MER again. Category ranking
   and fee comparisons are not established evidence of predictive alpha.
8. Verify point-in-time inputs, next-bar execution, overlaps, portfolio
   drawdown and benchmark comparison; then freeze prospective paper rules.

The suggested 2-3-day ratings build estimate is not a validated delivery
commitment. A reliable NAV/total-return/benchmark/provenance pipeline is a
different requirement from a small viewer MVP.

## Evidence and boundaries

Read live public JSON and repository source; used canonical database helpers
in read-only transactions. No credentials or private per-trade payloads
published, no production mutations, no new market backtest, no guard changes.
This review does not individually re-prove every narrative/ML/provider
attribution or quoted paper in Kimi's report.

See [approach](APPROACH.MD),
[copper verification](GHCOPILOT_COPPER_VERIFICATION_2026-10-22.md),
[momentum verification](GHCOPILOT_MOMENTUM_VERIFICATION_2026-10-22.md),
and [current ownership/remaining work](GHCOPILOT_PREDICTION_REPAIR_AND_EDGE_PLAN.md).
