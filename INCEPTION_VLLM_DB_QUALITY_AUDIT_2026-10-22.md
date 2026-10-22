# INCEPTION / VLLM — Database Quality Audit

**Agent:** INCEPTION / VLLM
**Date:** 2026-10-22
**Source:** `at_pick_outcomes` (mysql.50webs.com, DB `ejaguiar1_stocks`), 59,276 rows queried 2026-10-22.

---

## Why this matters

The walk-forward harness and any per-asset-class "winner" claim is only as trustworthy as the resolved outcome feed. This audit checks whether picks per asset class are fed in properly, whether anything performs "too well to be real", and whether the taxonomy/resolution is sound.

## Per-asset-class counts and data-quality findings

| Class | Rows | Key data-quality finding |
|-------|------|--------------------------|
| CRYPTO | 33,539 | Date-clustered zero-loss "too good" strategies (Calendar Effect Crypto 105W/0L over 6 dates; HoffmannmanStripTrendStrategy 146W/0L over 16 dates) — feed/resolution artifacts, not edges. |
| FOREX | 15,976 | >80% of closed rows resolved TIME_EXPIRED (resolution bias). |
| COMMODITY | 5,882 | >80% resolved TIME_EXPIRED; fragmented taxonomy. |
| EQUITY | 2,232 | Fragmented taxonomy (STOCKS vs STOCK, PENNY vs PENNYSTOCK). |
| FUTURES | 446 | Mostly TIME_EXPIRED resolution. |
| INDEX | 314 | Nearly all TIME_EXPIRED resolution. |
| ETF | 181 | Small coverage. |
| BOND | 154 | Small coverage. |

## Structural findings

- **`forward_validated = 0` for all asset classes.** No pick is forward-validated, so no backfilled result can be treated as confirmed.
- **29,753 closed rows have `pnl_pct = 0`.** A large share of "closed" outcomes carry a zero P&L, consistent with `TIME_EXPIRED`/sentinel resolution rather than a genuine market exit.
- **Zero-loss date-clustered strategies** are artifacts of the frozen-exit resolver stamping one price snapshot across many picks of a symbol on the same date.

## Verdict

The database **cannot certify any edge yet**. It is a diagnostic feed, not a proof source. Any performance number traceable to `TIME_EXPIRED` resolution or date-clustered zero-loss cells is excluded from evidence. A sealed forward cohort (P1-3) with independent hourly price feeds is required before any class can be certified.

## What must be true to certify

1. Forward-only, timestamped prospective outcomes (no backfill).
2. Independent hourly price feeds, not stored DB exit prices.
3. Fixed cost assumptions applied (crypto 0.30 pp, others 0.10 pp, futures normalized unlevered notional).
4. Missing data stays visible; market sessions, funding, dividends, borrow and roll costs further audited.
