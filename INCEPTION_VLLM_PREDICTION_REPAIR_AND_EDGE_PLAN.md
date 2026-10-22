# INCEPTION / VLLM — Prediction Repair and Edge Plan

**Agent:** INCEPTION / VLLM
**Date:** 2026-10-22
**Repo context:** `eltonaguiar/findtorontoevents_antigravity.ca` (audit + prediction system)

---

## Purpose

This document records the INCEPTION/VLLM position on why we do **not** yet have any proven profitable pick, what was broken, what was repaired, and the exact plan to reach an honestly-proven edge. It complements the live page at `/audit/inception_paper_trading.html` and the canonical working plan in `INCEPTION_VLLM_PLAN_PROFIT_PICK.md`.

## The honest state

A strict, read-only, out-of-sample walk-forward harness (chronological 50/50 split) over 3,446 cleaned resolved picks finds **zero cells passing the strict winner gate** (test n ≥ 10, PF ≥ 1.15, WR ≥ 0.50, train PF > 1.0, non-artifact). No asset class is statistically proven profitable.

| Class | n (test) | WR | PF | Verdict |
|-------|-----------|-----|-----|---------|
| FOREX | 26 | 53.8% | 3.15 | interesting but n too small |
| CRYPTO | 1,430 | 44.4% | 1.27 | positive PF but WR < 50% |
| EQUITY | 120 | 43.3% | 0.98 | no edge |
| ETF | 82 | 35.4% | 0.72 | no edge |
| COMMODITY | 8 | 50% | 1.03 | n too small |
| BOND / FUTURES | ~0–2 | — | ~0 | degenerate |

## What was broken and repaired

- **Frozen-exit resolver bug** (`audit_trail/universal_pick_resolver.py`): prices fetched once per run were stamped onto every unresolved pick of a symbol, manufacturing fake clustered "wins". Fixed via `_per_pick_price()` (first OHLC bar at/after the pick's own entry), with regression tests. Deployed to `main` as `305f9a79561`.
- **Standing artifact-detector CI gate** added (`wins > 2× distinct exit dates`) so fake clusters never silently poison reports. Currently fails on the 19-cell legacy report and goes green after a clean fixed-resolver re-run.

## The plan

1. **P0** — Fix the scorekeeper (resolver fix done; copy-trader lifecycle repair pending merge).
2. **P1** — Re-run harness on fixed-resolver data; open a sealed, timestamped, cost-inclusive forward paper cohort for the single strongest sleeve.
3. **P2** — Keep mutual-fund ranker as stable product; promote a sleeve to tactical rotation only after P1-3 validation.

**Decision gate:** a sleeve is promoted only when it clears the strict gate on fixed-resolver data **and** confirms on a sealed forward cohort with costs included.

## Closest candidates (not yet proven)

- `JUPUSDT|mega_mutation_macd_rsi_m048|LONG` — PF ~3.99 but train n < 10.
- `drawdown_recovery_rsi_eth/sol`, `multi_period_rsi_confluence_eth` — high train PF, need test-half confirmation.
- FOREX as a class — PF 3.15 but n too small.

Dedicated verification records:
- Database-quality audit: `INCEPTION_VLLM_DB_QUALITY_AUDIT_2026-10-22.md`
- Peer-claim verification (commodity_term_cot / HG=F): `INCEPTION_VLLM_PEER_CLAIM_COMMODITY_TERM_COT.md`
