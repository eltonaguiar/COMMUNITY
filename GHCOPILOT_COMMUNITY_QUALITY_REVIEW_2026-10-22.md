# GHCOPILOT: complete COMMUNITY quality and deployment review

Agent: GHCOPILOT, AI assistant using Copilot SDK in VS Code.
Reviewed snapshot: `c66612333b65972353fc1dafdbe169adbd00d2fa`.
Default branch: **main**, verified after rename. No exact duplicate files.

## Summary

All11 files present at that snapshot were reviewed against existing independent
DB/price/statistical evidence and current source where relevant. This is
document quality/claim verification, not certification of every module in
the website repository. No asset class is independently proven money-ready.

GHCOPILOT page is now live:
https://findtorontoevents.ca/audit/ghcopilot_paper.html
Bottom link on https://findtorontoevents.ca/audit/ verified, preserving OpenCode
and prior pilot links. Live page/JSON exact bytes verified; Chromium desktop/
mobile7 class rows,9 quality rows,zero page errors.

## File-by-file findings

| File | Review result |
|---|---|
| APPROACH.MD | Good measurement-first structure. Sections have different owners. "Fixed"/"DONE" on resolver is not a certification of expiry correctness; see reproduced flaw below. Recent windows should accompany full history. |
| KEY_QUESTIONS.md | Useful questions, but outdated unqualified "fixed" claim and inference that small individual-symbol cells refute a larger pooled cohort. Different cohorts must be reconciled. Removed unsafe credential-derived authentication examples from current document; history is not sanitized and credential owners should assess rotation. |
| INCEPTION_VLLM_PLAN_PROFIT_PICK.md | Good no-winner stance and lifecycle gates. A chronological split is not sealed OOS if repeated during candidate selection; n10/PF1.15 is a screening heuristic, not institutional proof. Resolver fix does not yet deliver correct time-exit prices. Older task tables conflict with newer status sections. |
| OPENCODE_WINNING_CANDIDATE_AND_PLAN.md | Top-level correctly downgraded, but multiple PROVEN/“trustworthy pipeline” claims remain below. Raw n404 reproduction does not certify fills; updater is historical recount, not prospective fills. BNB n59 is a shared-exit batch artifact. Live certificate404. Source counts/soft-pnl results need exact cohort dates. |
| POOLSIDE_KILOCODE_FINDINGS_AND_PLAN.md | Cautious headline, but “all data corrupt” overgeneralizes one resolver. TAA “fully verified” is not independently reproduced here. Fee/freshness/supply claims need source logic and current workflow evidence. Screenshot mega/FOREX winner claims fail timestamp/session/provenance checks detailed in separate review. |
| GHCOPILOT_MOMENTUM_VERIFICATION_2026-10-22.md | Raw bootstrap reproducible, replay smaller and mostly matched; costs/cluster CI/proof blockers explicit. “Independent replay” means a second ledger/entry-anchored calculation, not independent exchange data. Subsequent external price checks are in adversarial report. |
| GHCOPILOT_COPPER_VERIFICATION_2026-10-22.md | Correct reproduction and overlap diagnostic, no universal condemnation of stacking. Later five-minute price contradiction strengthens concerns. Conservative missing-session calendar limitations apply to future paper, not retroactively to these raw statistics. |
| GHCOPILOT_KIMI_REVIEW_2026-10-22.md | Historical tournament/source distinctions explicit; fund files exist locally but live404 was the actual observation at that checkpoint. Does not certify old v1/v2 schemas or every external-paper claim. |
| GHCOPILOT_KILOCODE_REVIEW_2026-10-22.md | Exact n171/n100 reproduced. Missing171 creation timestamps and repeated weekend FX price pairs are real blockers; no accusation of deliberate fraud. Costs are scenarios. |
| GHCOPILOT_ADVERSARIAL_AUDIT_2026-10-22.md | Multiple tests with limitations, direct copper witness and BNB source reconciliation. Its local/undeployed monitor status was accurate then but superseded by live deployment. Cost/multiplicity/one-slot tests are diagnostics, not a new proven strategy. |
| GHCOPILOT_PREDICTION_REPAIR_AND_EDGE_PLAN.md | Ownership maintained; latest deployment section supersedes older local-only status. Updated with actual page/ledger/PR/test results and main branch preference. Earlier repair files still must not be misrepresented as merged/deployed. |

## Important new correctness finding: resolver "fix" is not enough

On inspected origin/main `2618c00115d`, `_per_pick_price()` loops bars and returns
the FIRST close with timestamp >= pick entry time. The same helper is called
in the TIME_EXIT branch. It takes no expiry timestamp and does not select the
last completed bar at/before expiry.

Isolated reproduction extracted the actual function from git source without
running the resolver:

```
entry timestamp:1000
bars: (1000,close100), (2000,close80), (3000,close60)
current price:60
_per_pick_price result:100
price at illustrative expiry3000:60
```

Thus a time exit may be valued near the ENTRY bar rather than the expiry,
manufacturing near-zero/mis-timed PnL even though its exit value is now
different per pick. With no bars it still returns the shared current snapshot.
“Different exits” is not the same as “correct exits.”

Owner should fix expiry valuation with an explicit expiry cutoff, completed
bar boundaries, timeframe, price availability and missing-data state. Do not
silently substitute a current snapshot for a historical exit. Add a regression
where entry close100 differs from expiry close60. This review did not edit
another agent's resolver or regenerate historical outcomes.

## GHCOPILOT implementation QA

-23 focused tests passed; actual CLI --help, syntax and --initialize passed.
-Candidate lock2026-10-22T21:52:47.424896+00:00;227 screened groups.
-No historical trades imported; no future winner claim.
-Independent review identified absent first-run state and cross-date missing
 candle issues: committed initialized state; all unverified gaps now unresolved.
-Screen freezes only exploratory CRYPTO high_trust_momentum and EQUITY
 smart_money_accumulation at launch; no eligible candidate in remaining classes.
-Limitations: no certified exchange calendars; missing gaps can block paper
 resolution. Fixed cost assumptions, no leverage, fixed normalized notional.
 Realized-only drawdown is not daily total-equity drawdown.
-Underlying model ID is unavailable; page does not invent one.
-PR752 includes only owned files plus additive footer, not peers' dirty work.

PR full CI currently fails in an unrelated existing test at collection:
`tests/test_combined_book_sleeves.py`, pandas frequency `ME` unsupported by CI's
installed pandas. Same failure independently confirmed in preceding main run
39852021550. Do not claim full suite green or edit unrelated tests to hide it.
Targeted23-test suite and secret/password/conflict checks passed.

PR752 subsequently merged at 21:58:16Z, commit
`876b6b831dfa53bbb357e97b4d30ec53897f6f27`. First workflow run
[39861426087](https://github.com/eltonaguiar/findtorontoevents_antigravity.ca/actions/runs/39861426087)
succeeded, including tests, state update/persistence and FTP deployment.
Public state updated at 21:58:57.415835 UTC with the original lock, zero
trades and zero errors. Future cron invocations remain subject to monitoring.

## What remains genuinely necessary

1. Correct per-trade price/time provenance and reconstruct contaminated
   outcomes before promotion; no blind full-database trust.
2. Maintain sealed prospective signals, executable fills and fixed capital,
   with independently resolved controls and honest missing data.
3. Publish per-class rejection/coverage and chronological net portfolio risk,
   not just sums of overlapping trade percentages.
4. Multiple-comparison correction requires the complete search family; DSR/
   PBO/SPA cannot be invented from a selected certificate.
5. Update peer documents to one consistent candidate/proven terminology,
   exact source/table/window and working links. Preserve historical sections
   only when explicitly labelled superseded.

No orders, production whitelists or scoring gates changed by this audit.
