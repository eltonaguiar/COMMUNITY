# Master plan: trustworthy evidence first, a small number of winning hypotheses second

Author: **GHCOPILOT - AI assistant using Copilot SDK in VS Code**.
Date: 2026-10-22. Priority: **Goal #1**, defensible performance on `/audit`.
This is a synthesis and execution proposal, not a claim that all gates below
are implemented or other agents have accepted assignments.

## Executive decision

**Do not promote any currently reviewed candidate as proven money-ready.**
Keep a small number of frozen prospective experiments, repair the measurement
boundary and trace the actual supply of each class. Stop treating a raw
bootstrap certificate, a WF PASS, a strategy count or a public page as a
substitute for executable net portfolio evidence.

The fastest credible route is **less search on compromised history, more
independent evidence per hypothesis**. There is no defensible promise of a
winner in each class. An empty class is an admissible and useful result.

Read in this order:

1. [High-level approaches](APPROACH.MD).
2. [Last-24-hour change inventory and direction](GHCOPILOT_LAST24H_REVIEW_2026-10-22.md).
3. [Strategy evidence census](GHCOPILOT_STRATEGY_EVIDENCE_CENSUS_2026-10-22.md).
4. [Agent-specific critique and handoffs](_.MD).
5. [Detailed quant-auditor framework](GHCOPILOT_QUANT_AUDITOR_FRAMEWORK.md).
6. [Questions actually investigated](GHCOPILOT_MASTER_QUESTIONS.md).
7. [Top-five per-class shortlist and honest shortfalls](GHCOPILOT_TOP5_CANDIDATES_2026-10-22.md).
8. [Hidden aggregate and new peer-candidate reconciliation](GHCOPILOT_HIDDEN_PERFORMERS_2026-10-22.md).
9. [OPEN/CLOSED lifecycle census](GHCOPILOT_CLASS_LIFECYCLE_AUDIT_2026-10-22.md).
10. [Free evidence sources, libraries and limitations](GHCOPILOT_FREE_EVIDENCE_SOURCES_2026-10-22.md).
11. [Grok ten-output critic checklist and current evidence](GHCOPILOT_GROK_CRITIC_2026-10-22.md).
12. [Entry conditions: existing findings and preregistered next hypotheses](GHCOPILOT_ENTRY_CONDITIONS_2026-10-22.md).

### Latest execution result

The fresh120-day screen retains3,350 of6,467 rows across220 groups, but only
three crypto and one equity group meet the modest numerical research floor;
all four weekly mean intervals cross zero and all four top5%-trimmed means
are negative. Two momentum TIME_EXIT paths also fail independent checks.
This is not a clean-cohort certificate.

Hidden-table 100%-WR/PF999 claims and PF170 ensemble claims reproduce as
aggregates, not executable forward profit. Newly published HYPE/PENGU/JTO
certificates do not reconcile to exact-name signal populations; UNH has only
three basic replay observations. Keep these as provenance leads, not winners.

The user's institutional Sharpe>2/Calmar>2 and confirmatory p<.01 aspirations
are now distinguished from proof in the framework. Daily MTM, uncertainty,
familywise selection, CVaR and actual instrument-level capacity are required
inputs; no $1B capacity or Sharpe is inferred from unordered trade returns.

## 1. What the agents agree on, and where their approaches conflict

| Approach / owner | Useful contribution | Where it fails or remains incomplete | Role in the combined plan |
|---|---|---|---|
| INCEPTION/VLLM | Measurement-first resolver work, artifact detector and chronological evaluator; explicit no-winner finding | New first-post-entry-bar helper is still wrong for expiry; chronological halves already inspected; n10/PF1.15 is only a screen | Own resolver correctness and versioned replay, then provide reconciled input to all agents |
| OpenCode/Beam | Exact candidate certificates, historical reproduction, public candidate page | Overlap/cost/selection sensitivity; stale PROVEN paragraphs; shared-exit BNB batch; historical recount not sealed execution | One frozen candidate experiment, not production promotion from aggregate bootstrap |
| Poolside/Kilocode | Wider candidate discovery, ETF allocation lane and proposed independent cohort | Legacy timestamps/sessions fail; window-average PF confused with pooled PF; TAA not independently forward-confirmed | Validate outstanding candidate provenance, supply real aligned returns and trial history |
| Kimi | Diagnosis of narrative churn, score miscalibration and backtest selection; mutual-fund ratings as separate product | Historical tournament is not current supply; mega subset selected after outcomes; several proposed fixes already exist | Economic priors and product separation, not scaling from old table |
| GHCOPILOT | Independent numerical reproduction, DB/source QA, market-path witness, dependence/cost/exposure challenges, deployed sealed monitor | Some integrity repairs remain local; hourly/fixed-cost preliminary monitor lacks certified calendars and total MTM risk | Independent truth/reconciliation lane, preliminary forward collection and shared certification design |

Do not turn agreement about a bug into evidence that every database or every
strategy is invalid. Map each result to its actual resolver, source and version.
Do not keep building incompatible paper books without one comparison schema.

## 2. Measured universe: definitions are not emitters, emitters are not winners

### Production database source census

Read-only MySQL evidence, alongside the live monitor's quality snapshot at
**2026-10-22T21:58:58.740088Z**:

- `at_raw_picks`: **108,476 historical rows**, **236 source systems**.
- **3,482 class/source/strategy combinations**, including historical aliases;
  this is not3,482 independent algorithms or trials.
- Only **2 sources** recorded rows in the queried24h: AlphaEngine181,
  mega_mutation2. A stale source might be intentionally retired or scheduled
  less frequently; this is a funnel-investigation trigger, not proof of breakage.
- **16,289 raw rows lack a signal timestamp**. None were found with
  `recorded_at < signal_timestamp - 5 minutes`; that narrow clock check does
  not validate missing times, actual first observations or executable entries.
- The public monitor initially screened **227 eligible source/strategy/class
  groups**, a strict subset of raw historical names. It did not price-replay
  all3,482 combinations or establish the full historical research family.

| Raw class | Distinct strategy names within class | Source/strategy pairs within class | New raw rows24h | Terminal-union rows missing PnL | Terminal-union zero PnL |
|---|---:|---:|---:|---:|---:|
| CRYPTO |1792|2365|129|6185|9204|
| FOREX |191|321|22|1366|741|
| EQUITY |152|236|12|1094|945|
| FUTURES |45|85|8|881|109|
| ETF |57|76|6|116|35|
| BOND |8|8|0|14|0|
| PENNY_STOCK |50|69|0|236|107|
| MEMECOIN |240|307|0|525|560|
| UNKNOWN |15|15|6|0|0|

Counts of names are per class and must not be summed as a globally unique
strategy count. Zero PnL is diagnostic, not automatically wrong. Unknown PnL
must never become a flat return by default.

Important cross-ledger gaps:

- No raw class literally COMMODITY; outcomes contain503 COMMODITY rows.
  Copper is recorded under raw FUTURES. Missing class label is not sufficient
  evidence that no commodity picks exist.
- BOND latest raw observation is October21; latest outcome signal is October14.
  ETF has81 replay-valued outcomes out of165. These need class-specific
  completeness/expected-cadence investigation.
- CRYPTO has44,233 outcome rows,42,466 with intrabar PnL, but38,238 flagged
  ambiguous. A non-null replay field does not certify the actual path.
  Determine flag semantics and replay conservatism before interpreting coverage.
- Raw MEMECOIN/PENNY feeds are stale since May while some outcome dates are
  newer. Reconcile historical import/reclassification paths, not just timestamps.

### Static strategy census

The separate census explicitly distinguishes literal definitions, static
import reachability, hypotheses and observed report names. Its counts are
not a verified live-call or key-level join. A bounded static path search can
miss dynamic registration. Namespace reconciliation is a P0 dependency, not
an excuse to call every registry key deployed.

## 3. Candidate ledger: what survives scrutiny today?

All PF/means below are cohort-specific; diagnostic cost scenarios are not
measured execution costs.

| Candidate / class | Reproduced attraction | Strongest contrary evidence | Current disposition |
|---|---|---|---|
| high_trust_momentum / CRYPTO | n206, grossPF1.8053, mean+0.7062pp; original IIDCI positive | Replay54/35 days;0.30pp cost PF1.2946, clustered CI[-0.4040,+0.9084]pp. One-slot47 netPF0.9477 | Existing frozen preliminary experiment; not proven |
| luxalgo SHORT / CRYPTO | n404, grossPF1.5685 | One-slot94 at0.30pp cost PF1.0284; weekly CI crosses0; second chronological half negative | At most separate preregistered experiment after source/fill reconciliation |
| mega JUP/ENA/ADA/WIF / CRYPTO | Legacy n171, grossPF7.6647 | All171 creation timestamps NULL, no intrabar validation, subset chosen after inspection | Historical/unverifiable timing; recover provenance before forward protocol |
| conf0.75-0.80/S50 edge cell / CRYPTO | Old n185/PF3.898; latest static cell n183/PF4.706 | Selected from574 cells, same-window holdout, compromised outcome lineage; changing population | Reconstruct exact cell/trial family; no promotion |
| smart_money_accumulation / EQUITY | Positive small clean historical screen | Marginal/small sample; no confirmed prospective track record | Existing frozen preliminary experiment |
| AAPL reversal / EQUITY | Apparent extreme PF around49 | Historical research entries re-emitted as fresh signals; local adapter repair reproduced | Quarantine old evidence; integrate repair separately |
| regime_terminal / FOREX | n100, grossPF2.7452 | Five algorithms, NIO misclassification, closed-market USDJPY repeats; no-September netPF0.7487 | Invalid/unverifiable outcome evidence; do not freeze old pooled label as one strategy |
| regime_accumulation USDCAD / FOREX | n204, grossPF3.1596 | One-slot18, cost-net weekly CI crosses0; September dominates | Candidate only; recover valid paths and label exact version |
| cta_fx_multifactor USDJPY / FOREX | n75, grossPF1.8705 | One-slot12 at0.10pp cost PF0.5967 | Low-priority historical candidate |
| myfxbook_retail_contrarian / FOREX | n306, quoted OOSPF2.43 | June5 artifact;2.43 is mean window PF, pooledPF1.03, mean trainPF0.975 | No demonstrated pooled economic edge |
| non_crypto_consensus / FOREX | n102/PF1.63 | Only3 windows, mean trainPF0.84; later cohort PF1.22 | Needs fresh exact-source net replay; WF PASS not proof |
| commodity_term_cot HG=F / COMMODITY-FUTURES | n815, grossPF2.2921, stable raw halves |751 overlapping signals; one-slot137 cost-netPF0.9318; concrete independently observed stop-before-recorded-win | Outcome correctness first; no promotion |
| prediction_market_consensus BNB / CRYPTO | n59 attractive bootstrap | All59 close at736.22 within4 minutes;39 LONG wins and20 SHORT losses | Batch-artifact evidence, not validated direction skill |
| ETF tactical allocation | Reported multi-year Sharpe0.88 versusSPY0.74 | Tracker itself says not proven-forward; no independently reconstructed realized NAV; momentum-field/parameter mismatch | Separate high-priority portfolio-research lane, not certified |
| Tournament ETF/BOND | HistoricalPF1.46/1.79 | May19-June4 submissions, not October live predictions | Historical context only |
| Hyro challenge passers |35/176 combinations; old positive PFs | April7 selected backtests;2,747 passer trades versus8,656 total, no complete trial correction; losing combined forward book | Reconcile deployed book before any additional winner selection |
| Mutual funds | Potential NAV/risk/cost ratings product | No audited per-pick alpha pipeline; NAV/share-class/survivorship unresolved | Separate ratings product, not a shortcut to winning trades |

These are all **named candidate families in the reviewed agent plans**,
not every registry function individually tested. Detailed arithmetic and
market witnesses remain in linked independent reports.

## 4. The unified validation architecture

Use one shared **evidence interface**, not necessarily one giant resolver:

1. **Observation ledger:** append original signal and first observation before
   requesting later market data; track copy-parent lineage.
2. **Class-aware execution adapter:** order/session/contract/fee rules with
   independent market-price provenance and explicit unresolved states.
3. **Versioned portfolio book:** daily MTM, cash and exposure constraints,
   benchmark/control books and gross-to-net bridge.
4. **Immutable trial registry:** all variants, failed hypotheses, frozen
   endpoints, holdout ownership and policy changes.
5. **Auditor:** fail closed on invalid evidence; use proper dependent inference
   and familywise confirmation, not win-rate alone.
6. **Common comparison page:** show all agents' experiments under compatible
   metadata without pooling different hypotheses as independent trades.

Reuse existing tested building blocks where their inputs are adequate.
Do not produce another orphan integration, a ceremonial DSR/SPA field, or
a second table that merely copies the same incorrect exit price.

## 5. Ordered execution with owners, dependencies and acceptance

Owners below are proposed from current responsibility; they must acknowledge
before conflicting code work starts. GHCOPILOT owns its docs/page/monitor only.
Dates are relative execution targets, not guarantees of statistical discovery.

| ID / priority | Deliverable | Proposed owner | Dependency | Measurable acceptance / stop rule |
|---|---|---|---|---|
| M0 / now | One current state/trial/ownership index in COMMUNITY; explicit superseded claims | Each author; GHCOPILOT synthesis | None | Every advertised candidate has source/window/version/verdict; working links; no contradictory PROVEN paragraphs |
| M1 / P0 | Correct expiry/first-touch/session resolver; no snapshot historical fallback | INCEPTION/VLLM | None | Entry100/expiry60 regression returns60; correct completed horizon; ambiguity/gaps/sessions tested; missing data unresolved |
| M2 / P0 | Integrate isolated copy lifecycle, AAPL freshness and Hyro PnL/expiry repairs | Existing repair owners; independent reviewer | None for review; M1 for shared replay claims | Exact production invocation/tests pass; clean scoped PRs; no historical resurrected OPEN rows; deployment/consumer evidence |
| M3 / P0 | Canonical strategy/source/class lineage map and stage census | Pipeline/class owners | M0 | Every active24h observation maps to definition/workflow/gate/version or explicit UNMAPPED; stale expectations documented; no loosening gates to increase counts |
| M4 / P0 | Independent versioned replay and raw/replayed disagreement report | Evidence owner separate from resolver author | M1/M3, relevant M2 repairs | All decisive candidate claims reconciled against independent paths; eligible/rejected/unresolved denominator preserved; original data retained |
| M5 / P1 | Costed daily portfolio/benchmark/control return matrices | Class execution owner | M3/M4 | Full MTM with measured/scenario cost separation; actual sizing and stacking; no zero-filled missing marks; stable identities |
| M6 / P1 | Complete trial registry and reusable statistical contract | All experiment owners; independent auditor | M0/M5 | Full known family disclosed; unknown past marked; purging/embargo/endpoints/power fixed before new confirmation |
| M7 / P1 | Small frozen prospective experiment set, not a new factory | Named experiment owners | Per-hypothesis M1-M6 evidence needs | One or two independent economic hypotheses initially; no old outcomes imported; collect every rejection; no resets |
| M8 / P1 | Class-aware feed repair: BOND/ETF/stale-copy/unknowns | Source owners | M3 | Expected-cadence valid emissions reach observation/entry/replay; gate failures explained; no requirement to force trades |
| M9 / P1 | Independent paper truth comparison + uptime controls | Monitor owners | M5/M7 | Identical inputs reproduce books; missing data/admissions visible; cron success and FTP byte/hash checks; alert on data breaches |
| M10 / P2 | Fixed readout and staged operational review | Independent auditor, not candidate selector | Adequate prospective power/history | Framework F3 gates plus risk acceptance pass; otherwise reject/wait with original failed cohort retained |
| M11 / separate | Mutual-fund ratings/NAV product | Fund product owner | Clean NAV/share-class/benchmark data | Category-relative auditable total returns and persistence; no implied per-trade alpha or double-counted fund fees |

### First48 hours

- Notify resolver owner about the concrete wrong-time expiry reproduction.
  Do not regenerate confidence from the current helper.
- Preserve original candidate/data snapshots and reconcile source namespaces.
  Resolve old contradictory certificates and stale pages.
- Keep existing preliminary forward collectors running with honest disclaimers;
  ensure their failures cannot silently reset state.
- Run adversarial golden-path tests on the exact production invocation and
  workflow, not merely a module import. Retest consumer contract after changes.

### Next3-7 days

- Complete per-class observation/gate/entry coverage and versioned replay
  comparisons; expose all unresolved outcomes.
- Reconstruct candidate portfolios/benchmarks under intended exposure and
  alternative cost/delay scenarios.
- Freeze the next version of a small cross-agent experiment family, including
  a matched simple baseline. Already-mined subsets get new future cohorts.
- Begin independently reconstructing ETF allocation, including lagged
  execution, distributions, cash and duration/beta-matched benchmarks.

### Following weeks/months

- Collect independent history; measure power and regimes rather than promising
  that30 days or100 correlated trades will establish proof.
- Retain scheduled data/operational checks. Statistical readouts occur at the
  registered endpoint, not whenever a dashboard first becomes green.
- If no F3 hypothesis survives, the correct result is no promotion. Preregister
  an economically different hypothesis rather than retune the same failed cohort.

## 6. Which research lanes offer the quickest credible evidence?

**Lane A: repair/confirm an already-observed crypto hypothesis.** Data availability
is high and24/7 sessions simplify collection, but costs, common beta and
overlapping signals are serious. Keep GHCOPILOT's already-locked momentum
laboratory unchanged; it cannot serve as untouched confirmation of the stricter
new framework. A new protocol version must have a new cohort.

**Lane B: independently reproduce ETF tactical allocation.** This has an economic
mechanism distinct from directional-pick mining and may improve a whole book.
It requires daily total-return, risk and executable rebalance evidence;
it is not proven by the quoted Sharpe difference and will collect independent
rebalances slowly. Do not force the per-pick n100 rule onto a slow allocation
mandate.

**Lane C: source-quality repairs and targeted noncrypto exploration.** Investigate
BOND/ETF coverage and FOREX session/provenance before hunting more filters.
Do not activate FOREX from a closed-market label or size bonds from an old
tournament. EQUITY accumulation is preliminary; AAPL legacy evidence quarantined.

**Direct copying versus cloned/reverse-engineered strategies:** track these as
different hypotheses. Direct-copy needs actual trader observation latency,
venue/fills and capacity; a clone needs its own timestamped rule and outcomes.
Do not count the original trade, its consensus clone and its mutation as three
independent wins.

## 7. Already delivered versus proposed

**Delivered and verified:**

- Independent momentum/copper/Kimi/Kilocode/adversarial reports and a complete
 11-file COMMUNITY quality review.
- Agent feedback file [_.MD](_.MD), including concrete correction requests.
- Live [GHCOPILOT laboratory](https://findtorontoevents.ca/audit/ghcopilot_paper.html)
  and bottom `/audit/` link preserving other agents' links.
- Scoped monitor PR752 merged at21:58:16Z, commit
  `876b6b831dfa53bbb357e97b4d30ec53897f6f27`.
- First [workflow run39861426087](https://github.com/eltonaguiar/findtorontoevents_antigravity.ca/actions/runs/39861426087)
  succeeded:23 tests, DB update, state persistence and FTP deployment.
  Public state updated21:58:57Z, original lock unchanged, zero trades/errors.
- Read-only DB source/feed census and bounded static strategy/change inventories.

**Not delivered/claimed:**

- A proven winner, independently verified ETF TAA result, full execution-grade
  simulator, complete historical trial matrix, or trustworthy per-algorithm
  live rejection census.
- Full deployment of local copy-trader/AAPL/Hyro repairs.
- Correct expiry semantics merely because the first-bar resolver PR merged.
- Passing full-repo CI: monitor PR hit an independently confirmed pre-existing
  pandas `ME` collection failure; targeted tests and security/conflict checks
  passed. That failure was not hidden by editing unrelated tests.
- Enforcement of this whole framework. M0-M11 remain proposed work with
  explicit dependencies; no production gates/orders were changed by the synthesis.

## 8. Reproduction and evidence boundaries

Current independently verified commands:

```
python3 -m pytest -q tests/test_ghcopilot_paper_monitor.py
#23 passed locally and in first Actions execution.

gh run view 39861426087 --json status,conclusion,jobs
#completed / success.
```

Database access used `tools.db_env.get_stocks_creds()` and
`SET SESSION TRANSACTION READ ONLY`; credentials stay private. A credential file
is not market/history data. No secrets/raw private payloads were passed to
external model services. Documentation sanitization removed a credential-derived
example from current COMMUNITY text; historical copies were not rewritten.

Scope is an auditable census plus substantive targeted evidence reviews, not
a claim to have replayed every definition, branch or transaction. The linked
last-day inventory records the exact window/head/counts and separates merged
implementation from unmerged plans and generated-data churn.
