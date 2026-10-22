# Last-24-hour website repository audit

## Scope and exact counts

**Goal #1: trustworthy, genuinely profitable audit strategies—not more apparent winners.**

- Inclusive committer-time window: **2026-10-21 21:58:48Z–2026-10-22 21:58:48Z**.
- Pinned fetched `origin/main`: **060ac04f9478b66d1d35b3c2295348c437cc9a64**, committed at **21:58:59Z**, eleven seconds after the window. Its post-window ledger commit is excluded. Every reachable commit was explicitly filtered by committer epoch; no date-pruned ancestry traversal was used.
- **2,066 qualifying commits; 19 merges; 34 authors; 590 unique changed paths.**
- Artifact-aware classification: **2 implementation commits; 2,064 generated-data/report automation commits**. Both implementation commits also contain tests and release documentation; one adds a workflow. Automatically refreshed HTML/Pine/report markdown is not counted as a new strategy implementation.
- Path types: **569 data/generated, 14 documentation, 4 implementation, 2 tests, 1 workflow**. Twelve documentation paths are automatically refreshed reports; two are authored release notes.
- Largest author totals: `github-actions[bot]` **1,560**; `GitHub Action` **54**; `Signal Engine Bot` **48**; `Gainer Predictor` **47**. The JSON contains all 34 authors and every commit/path.
- First qualifying commit: `b8cd633f5018`, **Oct 21 21:59:45Z**. Last: `876b6b831dfa`, **Oct 22 21:58:15Z**.

Commit paths are unions of differences against all parents; merge paths can repeat earlier changes. They are not independent implementation counts. The JSON records this method explicitly.

## What actually landed on main

| Commit | Change and wiring | Assessment |
|---|---|---|
| `305f9a79561f` | `audit_trail/universal_pick_resolver.py`, five new helper tests, release note | Attempts to repair clustered/frozen exits, but introduces two confirmed production-path regressions below. |
| `876b6b831dfa` / PR **#752** | `tools/ghcopilot_paper_monitor.py`, 23 regression cases, hourly workflow, owned HTML/JSON, additive template footer | A genuinely wired, explicitly preliminary research sidecar: frozen candidate/protocol digest, prospective observations, next-hour entry, conservative bracket replay, fixed costs/notional, independent random-direction controls, no DB writes/orders. Not a demonstrated profitable sleeve. |

There were **no main-window source changes** to prediction generators, strategy implementations, copy-trader ingestion/scoring, mutual-fund allocation, or quality-gate modules. Their numerous refreshed outputs must not be described as deployed repairs. For example: copy-trader `pick_quality_report.json` changed in 62 commits and prediction-market `orchestrator_summary.json` in 54, without corresponding source fixes.

The generated Pine file's net diff contained **14 changed lines, all version/date/display metadata**, not trading-rule changes.

Monitor workflow run **39861426087** was dispatched at **21:58:22Z**, inside the interval, and completed successfully at **21:59:07Z**, after it. Its observed success is therefore post-window completion evidence, not an in-window completed validation. The workflow really calls the monitor; it is not an orphan module.

## Confirmed main regressions and artifact failures

### P0 — Expiry is priced at the first post-entry candle

`305f9a79561f`, `audit_trail/universal_pick_resolver.py`, `_per_pick_price` and lines **1503–1519**:

The helper iterates chronologically and immediately returns the **first** close at/after entry. `TIME_EXIT` uses that value as its expiry price. This does not reconstruct an exit-time price; varying exit prices between picks is not evidence of valid fills.

**Deterministic reproduction:** entry 100; first post-entry close 101; expiry/latest close 90. The new path selects 101 and reports **+1%**, rather than **−10%** at the horizon. The docstring says “latest,” the implementation and release note say/use “first.” The five new tests bless the first-candle behavior and do not test expiry.

### P0 — Intrabar success references an uninitialized or previous-pick variable

Same commit, lines **1446–1484**:

`pp_price` is assigned only when intrabar replay has **not** found an exit, but every successful resolution dictionary now reads it. An initial intrabar hit can abort the resolver with **UnboundLocalError**; a later hit can inherit another pick’s `pp_price` in provenance.

Compiling the exact dictionary assignment with the same conditional-local lifetime reproduced **UnboundLocalError** without invoking the resolver. No new test exercises the main-loop intrabar-success branch.

### P1 — Seven refreshed files are not strict JSON

Of **543 changed `.json` files** checked at the pinned tree, **536 passed** and **7 contained NaN/Infinity**:

- `alpha_engine/data/ml_health_status.json`
- `alpha_engine/data/online_learner_state.json`
- `audit_dashboard/data/hyro_ml_pick_rankings.json`
- `audit_dashboard/data/money_ready_archive/money_ready_2026-10-21.json`
- `audit_dashboard/data/money_ready_archive/money_ready_2026-10-22.json`
- `audit_dashboard/data/money_ready_verdict.json`
- `reports/pick_flow_snapshot.json`

Most are inherited defects, not new code regressions. Against pre-window first-parent baseline `14a945552bbe`, `pick_flow_snapshot.json` changed from strict-valid to nonfinite PF; the new Oct 22 archive materializes the existing nonfinite DSR issue. Latest dashboard-output refresh evidence includes `ffe7a5b6a0a9`. Default Python JSON decoding hides these failures; browser `JSON.parse` rejects them. The inventory contains exact key paths, baseline comparisons and latest touching commits.

## Remote branches and PRs: separately bounded inspection

The metadata snapshot enumerates **161 local remote refs** and **159 live server branch heads**. The local count includes the `origin/HEAD` alias and the monitor branch already deleted server-side. Server `main` had advanced beyond the pinned local snapshot; that later state was not silently substituted.

The complete bounded GitHub PR search returned **2** records:

- **#751**, OPEN, `feat/gha-actions-health`, updated **21:32:03Z**.
- **#752**, MERGED at **21:58:16Z**, updated **21:58:18Z**.

Eight local branches contain **44 distinct window commits absent from main by ancestry**. This is **not** 44 unmerged changes: two branch tips are proven patch-ID-equivalent to squash commits already on main. Five non-deployment, non-equivalent branches remain:

| Branch / tip | Substantive inspection and disposition |
|---|---|
| `docs/audit-findings-grokweb-oct22` / `1b2149c68c12` | One new repository audit-findings document; no pipeline implementation. Its assertions are not treated as independently verified profit evidence. |
| `feat/walkforward-strategy-eval` / `3cd2fa4886da` | Harness, eight tests and report. Seven pure tests passed; filesystem-fixture test was not run. Confirmed cleaner accepts **OPEN positive-PnL rows and NaN**. Closing-time 50/50 split is not purged/embargoed; costs, multiplicity and uncertainty gates are absent. Artifact cells remain in class metrics although excluded from winners. The report has **19 artifact cells, zero winners**. Exploratory triage—not “strict institutional proof.” |
| `feat/artifact-detector-ci` / `ac2764d1ed4f` | Includes the preceding harness plus checker/workflow/tests. Scheduled job only reads a committed report selected by filesystem modification time; no report regeneration, age/schema check, resolver/data trigger or live evidence refresh. Three distinct-price legitimate wins in one day also trigger its date-count heuristic. It cannot establish current resolver safety. |
| `feat/gha-actions-health` / `37512a97392a` | PR #751: actual workflow caller and existing-library reuse. Deliberately nonblocking unless `FAIL_IF_UNHEALTHY=1`; bulk fetch capped at 400 runs and no-run workflows can appear healthy. Useful diagnostics, not proof of complete 48-hour pipeline coverage. |
| `oc-winning-candidate` / `365a88f5e986` | Twelve commits, ten changed paths. Page now says **no strategy is PROVEN**, but three certificates still say **PROVEN** and `high_trust_momentum` remains whitelist **active**, weight **0.20**. Active weights total **1.20**; all listed weights **1.85**. Validator bootstraps raw WON/LOST PnL IID without costs, overlap correction, multiple-testing control or a locked forward cohort. “Paper” updater only recounts historical rows and has **no workflow caller**. Credential defaults exist in new scripts; values are intentionally omitted. Do not merge as profit certification or automatic promotion. |

Remaining branches: `fix/frozen-exit-resolver` / `cf1e992582de` and `feat/ghcopilot-audited-paper-monitor-20261022` / `0b09699c22c3` are exact squash-patch equivalents of the two main implementation commits; `gh-pages` / `6081a770d4ae` is a separate deployment history with **24** window commits and no common ancestor with main. The JSON includes all branch heads, qualifying unique commits, merge bases and changed-path manifests. Branch inspections are substantive source reviews, not audits of every branch data row.

## Verification and limits

- Pinned-source existing regression functions: **28/28 passed**, called directly in memory, including parametrized monitor cases. This was **not a pytest collection run**: the shared working tree lacks the newly merged monitor files; it was not overwritten.
- Resolver synthetic checks exposed both P0 defects despite those passing tests.
- Unmerged walk-forward pure tests: **7/7 passed**; adversarial probes exposed open-row/nonfinite admission and heuristic false positives.
- Changed main Python files: **4/4 AST syntax passed**; inspected branch Python instances: **13/13 passed**.
- No merge-conflict markers found in the changed main Python/JSON checked. Syntax success does not establish accounting correctness.
- No generators, scanners, DB queries, trading actions or deployment were run. No repository code was changed. No COMMUNITY material was read. Data-row profitability, current external prices and production-vs-FTP equivalence are outside this report.

## Direction and next priorities

**Direction is mixed:** main gained an honest prospective measurement sidecar, while most activity remains generated-output churn. The resolver repair currently worsens accounting, and unmerged “winner” work still mixes exploratory historical scores with promotion artifacts. **This interval establishes no new genuinely profitable asset class.**

1. Repair/test expiry-time selection and intrabar variable lifetime before trusting new resolver cohorts; quarantine affected outcomes by resolver/source provenance rather than deleting history.
2. Standardize one strict finite, timestamped, identity-deduplicated outcome ledger; separate price observations, first-touch exits and time-expiry exits. Fix strict-JSON serialization.
3. Reconcile HTML, certificate JSON and whitelist states. Keep every disputed sleeve research-only; prevent unsupported weights/promotions.
4. Harden then wire the walk-forward/artifact checks to refreshed evidence: entry/exit purging, overlap/exposure controls, net costs, multiple testing, fresh data hashes and deterministic tests. A static report-check job is insufficient.
5. Preserve the sealed monitor and collect independent forward outcomes/control excess returns; add exchange-session support and measured cost/risk models before interpreting non-crypto gaps or realized-only drawdown as readiness.

## Independent pre-change source quote requested by parent

Pinned `origin/main` `060ac04f9478b66d1d35b3c2295348c437cc9a64`, `audit_dashboard/ghcopilot_paper.html`, lines **33–35**, verbatim:

```html
<p><a href="https://github.com/eltonaguiar/COMMUNITY/blob/main/GHCOPILOT_ADVERSARIAL_AUDIT_2026-10-22.md">Independent price-path/statistical audit</a> |
<a href="https://github.com/eltonaguiar/COMMUNITY/blob/main/GHCOPILOT_KILOCODE_REVIEW_2026-10-22.md">Kilocode winner verification</a> |
<a href="opencode_paper_trading.html">OpenCode/Beam page (separate agent)</a></p>
```

## Deliverables

- [GHCOPILOT_LAST24H_CHANGE_INVENTORY_2026-10-22.json](GHCOPILOT_LAST24H_CHANGE_INVENTORY_2026-10-22.json): exhaustive main commit/path/author manifest, complete enumerated branch-head metadata, recent PR metadata, branch delta manifests, validation evidence and ranked findings.
- `GHCOPILOT_LAST24H_REVIEW_2026-10-22.md`: this report.

Both reside in `/home/eaguiar2015/.copilot/session-state/6ae35344-e1a9-4f7d-8404-327db32bfdd0/files/`.
