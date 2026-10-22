# APPROACH.MD — OPENCODE_BEAM

**Agent:** OPENCODE_BEAM (opencode/beam-free)
**Date:** 2026-10-22
**Branch:** `oc-winning-candidate` (main repo) / `m0vies` (COMMUNITY)

## High-level plan

1. Audit every asset class in `ejaguiar1_stocks` (MySQL @ mysql.50webs.com; creds in `/home/eaguiar2015/dbpasses.txt`).
2. Identify strategies with hard-resolved (WON/LOST) outcomes, recent activity, low outlier contamination, and multi-symbol participation.
3. Validate via bootstrap + walk-forward; declare PROVEN only if bootstrap P(Expectancy>0) > 0.95 and Wilson lower > break-even.
4. Concentrate on the single best candidate; deprecate losers; document everything.

## Key questions asked

- Do we have mutual funds, where, and what is their quality? (Yes — `mf_*`/`mf2_*`; inverted rating, PF ~0.47.)
- Why did stocks/crypto/bonds/ETFs/commodities/prediction fail? (Outliers, soft resolution, blocklists, score floors, costs, tracking windows, kimi/copy-trader poisoning.)
- Is there any asset class/strategy that is actually predictive? (Yes — `high_trust_momentum` CRYPTO.)
- Can we prove it? (Bootstrap: P(>0)=0.9997, CI [+0.320,+1.092].)
- What's blocking promotion? (Need 100 more TP/SL outcomes; reconcile hyrotrader discrepancy.)

## Authentication / data sources

- DB creds: `/home/eaguiar2015/dbpasses.txt`
- MySQL host: `mysql.50webs.com`, DB `ejaguiar1_stocks` / `ejaguiar1_backtests`
- Other APIs: see `/home/eaguiar2015/dbpasses.txt` for keys (OpenRouter, Gemini, etc.) if delegation needed.

## Detailed references

- `AUDIT_FINDINGS_OPENCODE_OCT22.MD` — full findings, root causes, plan.
- `OPENCODE_WINNING_CANDIDATE_AND_PLAN.md` — winning candidate + per-asset-class fix plan.
- `core_whitelist.json` — whitelisted strategies (incl. high_trust_momentum).
- `tools/validate_winner.py` — bootstrap validation harness.
- `audit_dashboard/data/winner_certificate_high_trust_momentum.json` — PROVEN certificate.

## Remaining work

- Forward-test 100 more TP/SL outcomes.
- Reconcile regime_mild_bear hyrotrader discrepancy.
- Implement symbol allowlist + cost adjustment in code.
- Promote to /audit consensus + hyrotrader if validated.

*OPENCODE_BEAM — 2026-10-22*
