# Class lifecycle and hidden recent-coverage audit — 2026-10-22

**Fixed database snapshot: 2026-10-22 22:31:05 UTC.** Goal #1; read-only evidence, not an investment recommendation or performance verdict.

## Scope and method

Canonical `tools.db_env.get_stocks_creds()` with PyMySQL; `REPEATABLE READ`, `START TRANSACTION WITH CONSISTENT SNAPSHOT, READ ONLY`, 40-second per-query server limit and 50-second socket read timeout. Only `at_raw_picks`, `at_signal_outcomes`, and table metadata were queried. No `trading_picks`, `strategy_perf_by_class`, raw payloads, credentials, scanners, generators, or mutations. Connection ended with rollback. Metadata estimates are not exact row counts. Exact SQL, timings, and all returned aggregate groups are retained in the companion JSON.

Requested classes are retained exactly as stored: CRYPTO/EQUITY/FOREX/COMMODITY/FUTURES/ETF/BOND/PENNY_STOCK/MEMECOIN. A missing group is reported as zero, not silently omitted. Recent intervals are inclusive and end at the fixed snapshot (48h = 2 days). Source names are not normalized across tables.

## Main findings

- There are **258 OPEN raw rows; zero have a known signal age >7 days**. Four CRYPTO OPEN rows lack signal timestamps, so their signal age is unknown; the remaining 254 have recent signals. Zero OPEN rows have `closed_at` or missing entry/TP/SL geometry. All OPEN rows pass the strict directional geometry screen. This snapshot does **not** support a known-age stale-OPEN backlog claim.
- A basic recent-7d/unflagged/geometry OPEN proxy retains **254/258** rows. It is **not** an executable-pick count: current market prices, TTLs, production gates, source validity, positions and risk eligibility were not checked. `was_stale` flags are not synonymous with the explicit >7-day signal-age test.
- **COMMODITY has zero raw rows but 503 outcome rows**, including 2 closures in 48h and 10 in 14d. **MEMECOIN has no raw signals since May 11 but 2 outcome closures in 48h and 6 in 14d.** These are table/class-cohort differences, not proof of missing ingestion or of erroneous class assignment. No row-level lineage was traced.
- PENNY_STOCK has 494 historical raw rows, no raw signals in 30d, and zero outcome rows under that stored class. FUTURES and BOND have recent raw signals but zero outcome closures in 48h.
- Literal raw `CLOSED` rows have **zero missing PnL across all requested classes**. The broader terminal union includes EXPIRED and ABANDONED; missing PnL/closure time in that union is a completeness diagnostic, not automatically an economic-outcome contradiction.
- Historical outcome completeness is uneven: CRYPTO has 23,346 missing PnL and 37,447 missing closure timestamps; MEMECOIN has 2,333 and 2,339 respectively. Do not compute a recent win rate or claim coverage from total outcome rows alone. Six outcome records close before their opening timestamp (EQUITY 2, FOREX 1, COMMODITY 3); these merit narrow investigation, not a platform-wide corruption claim.

## Raw table status census

| Class | Total | OPEN | WON | LOST | EXPIRED | CLOSED | ABANDONED |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CRYPTO | 66,770 | 89 | 13,623 | 18,515 | 6,496 | 19,386 | 8,661 |
| EQUITY | 14,197 | 34 | 6,922 | 4,910 | 1,143 | 932 | 256 |
| FOREX | 14,895 | 62 | 7,751 | 4,069 | 1,784 | 722 | 507 |
| COMMODITY | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| FUTURES | 8,020 | 25 | 3,383 | 3,445 | 898 | 91 | 178 |
| ETF | 1,740 | 48 | 640 | 792 | 124 | 33 | 103 |
| BOND | 214 | 0 | 57 | 125 | 15 | 0 | 17 |
| PENNY_STOCK | 494 | 0 | 7 | 12 | 237 | 114 | 124 |
| MEMECOIN | 2,001 | 0 | 142 | 223 | 532 | 923 | 181 |

## OPEN integrity and historical completeness

Terminal means WON/LOST/EXPIRED/CLOSED/ABANDONED. Missing geometry means at least one NULL entry/TP/SL; strict geometry additionally requires positive values and directional ordering. Counts below are full-history and can overlap. Missing signal time is counted independently of stale age.

| Class | OPEN >7d | OPEN no signal | OPEN + closed_at | CLOSED no PnL | Terminal no PnL | Terminal no closed_at | All no signal | All missing geometry | All nonpositive geometry |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CRYPTO | 0 | 4 | 0 | 0 | 6,185 | 12,686 | 13,880 | 4,167 | 213 |
| EQUITY | 0 | 0 | 0 | 0 | 1,094 | 1,450 | 1,000 | 991 | 36 |
| FOREX | 0 | 0 | 0 | 0 | 1,366 | 1,864 | 690 | 647 | 18 |
| COMMODITY | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| FUTURES | 0 | 0 | 0 | 0 | 881 | 1,219 | 5 | 0 | 0 |
| ETF | 0 | 0 | 0 | 0 | 116 | 223 | 40 | 8 | 7 |
| BOND | 0 | 0 | 0 | 0 | 14 | 31 | 4 | 0 | 0 |
| PENNY_STOCK | 0 | 0 | 0 | 0 | 236 | 280 | 106 | 392 | 0 |
| MEMECOIN | 0 | 0 | 0 | 0 | 525 | 869 | 564 | 177 | 3 |

All requested raw classes: zero missing `recorded_at`, zero future signal timestamps, zero closure-before-signal instances. OPEN missing geometry and OPEN-with-PnL are zero throughout. For historical flag totals and strict geometry counts, see JSON; these are not production eligibility labels.

## Raw recent signal coverage and latest dates

| Class | Signals 48h | Signals 14d | Signals 30d | Sources 14d / 30d | Symbols 14d / 30d | Latest signal | Latest recorded |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CRYPTO | 249 | 1,412 | 3,357 | 2 / 2 | 53 / 62 | 2026-10-22 19:03:48 | 2026-10-22 21:47:26 |
| EQUITY | 24 | 415 | 1,129 | 1 / 1 | 12 / 15 | 2026-10-22 18:54:42 | 2026-10-22 19:05:06 |
| FOREX | 46 | 690 | 2,153 | 1 / 1 | 10 / 12 | 2026-10-22 18:54:42 | 2026-10-22 19:05:06 |
| COMMODITY | 0 | 0 | 0 | 0 / 0 | 0 / 0 | — | — |
| FUTURES | 32 | 310 | 685 | 1 / 1 | 12 / 14 | 2026-10-22 16:52:51 | 2026-10-22 17:07:55 |
| ETF | 18 | 182 | 396 | 1 / 1 | 7 / 8 | 2026-10-22 14:50:50 | 2026-10-22 15:02:18 |
| BOND | 1 | 19 | 32 | 1 / 1 | 1 / 1 | 2026-10-20 22:45:04 | 2026-10-21 05:05:19 |
| PENNY_STOCK | 0 | 0 | 0 | 0 / 0 | 0 / 0 | 2026-05-12 14:57:31 | 2026-05-12 23:21:16 |
| MEMECOIN | 0 | 0 | 0 | 0 / 0 | 0 / 0 | 2026-05-11 01:10:29 | 2026-05-13 00:00:27 |

### Recent 30-day raw source coverage

| Class | Stored source | Signals | Distinct symbols | Distinct strategies | OPEN | Signals 48h / 14d |
| --- | --- | --- | --- | --- | --- | --- |
| CRYPTO | AlphaEngine | 3,339 | 62 | 98 | 85 | 248 / 1397 |
| CRYPTO | mega_mutation | 18 | 8 | 4 | 0 | 1 / 15 |
| FOREX | AlphaEngine | 2,153 | 12 | 7 | 62 | 46 / 690 |
| EQUITY | AlphaEngine | 1,129 | 15 | 7 | 34 | 24 / 415 |
| FUTURES | AlphaEngine | 685 | 14 | 13 | 25 | 32 / 310 |
| ETF | AlphaEngine | 396 | 8 | 12 | 48 | 18 / 182 |
| BOND | AlphaEngine | 32 | 1 | 1 | 0 | 1 / 19 |

### Most frequent recent raw symbols (top five per class)

These are signal-row counts, not independent trades or evidence of profitability. Full per-symbol groups and top-ten lists are in JSON.

| Class | Symbol: signal count (30d) |
| --- | --- |
| CRYPTO | XRPUSDT: 417, BNBUSDT: 376, DOGEUSDT: 363, ETHUSDT: 334, BTCUSDT: 305 |
| EQUITY | MSFT: 145, AAPL: 117, META: 115, AMD: 103, DNA: 97 |
| FOREX | USDCAD=X: 399, USDCHF=X: 329, NZDUSD=X: 259, GBPUSD=X: 231, AUDUSD=X: 226 |
| COMMODITY | No recent raw signals |
| FUTURES | ZC=F: 250, HG=F: 247, ES=F: 48, NG=F: 36, NQ=F: 35 |
| ETF | SPY: 153, QQQ: 125, IWM: 65, EFA: 39, TLT: 6 |
| BOND | IEF: 32 |
| PENNY_STOCK | No recent raw signals |
| MEMECOIN | No recent raw signals |

## Outcome census and recency

`closed_at` recency is independent of outcome label. Recent created/ingested rows can refer to older signals, and missing closure timestamps cannot be assigned to a recent closure cohort. Raw rows and outcome rows are not expected here to reconcile one-for-one.

| Class | Outcome total | Opened 48h / 14d | Closed 48h / 14d / 30d | Created 48h / 14d | Closed sources / symbols 14d | Latest opened | Latest closed | Latest created |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CRYPTO | 44,247 | 69 / 376 | 72 / 382 / 892 | 112 / 407 | 2 / 81 | 2026-10-22 18:54:42 | 2026-10-22 18:54:42 | 2026-10-22 22:30:32 |
| EQUITY | 697 | 2 / 19 | 2 / 19 / 42 | 4 / 19 | 1 / 4 | 2026-10-22 16:52:50 | 2026-10-22 16:55:45 | 2026-10-22 22:30:32 |
| FOREX | 1,856 | 27 / 86 | 21 / 76 / 227 | 40 / 86 | 1 / 12 | 2026-10-22 15:12:05 | 2026-10-22 15:30:38 | 2026-10-22 15:35:14 |
| COMMODITY | 503 | 2 / 10 | 2 / 10 / 16 | 4 / 10 | 1 / 4 | 2026-10-22 14:17:07 | 2026-10-22 15:30:38 | 2026-10-22 15:35:14 |
| FUTURES | 127 | 0 / 6 | 0 / 6 / 7 | 1 / 6 | 1 / 4 | 2026-10-18 12:50:30 | 2026-10-18 12:52:34 | 2026-10-20 22:31:11 |
| ETF | 165 | 2 / 4 | 2 / 4 / 13 | 3 / 4 | 1 / 3 | 2026-10-22 12:33:08 | 2026-10-22 15:30:41 | 2026-10-22 15:35:14 |
| BOND | 70 | 0 / 3 | 0 / 3 / 12 | 0 / 3 | 1 / 3 | 2026-10-14 14:12:13 | 2026-10-14 22:25:58 | 2026-10-14 22:30:38 |
| PENNY_STOCK | 0 | 0 / 0 | 0 / 0 / 0 | 0 / 0 | 0 / 0 | — | — | — |
| MEMECOIN | 2,454 | 2 / 6 | 2 / 6 / 7 | 3 / 6 | 1 / 3 | 2026-10-22 16:52:51 | 2026-10-22 16:55:45 | 2026-10-22 22:30:32 |

### Outcome labels (full history)

| Class | Stored label: count |
| --- | --- |
| CRYPTO | CLOSED: 4, EXPIRED: 218, LOST: 2,394, OPEN: 38, SL_HIT: 21,852, STALE_INGEST: 3, TP_HIT: 14,327, WON: 5,411 |
| EQUITY | EXPIRED: 10, LOST: 152, SL_HIT: 175, STALE_INGEST: 1, TP_HIT: 201, WON: 158 |
| FOREX | EXPIRED: 51, LOST: 738, RESOLVE_FAILED: 1, SL_HIT: 189, TP_HIT: 159, WON: 718 |
| COMMODITY | EXPIRED: 9, LOST: 277, SL_HIT: 87, TP_HIT: 62, WON: 68 |
| FUTURES | EXPIRED: 12, LOST: 17, SL_HIT: 37, TP_HIT: 53, WON: 8 |
| ETF | EXPIRED: 2, LOST: 70, SL_HIT: 23, TP_HIT: 4, WON: 66 |
| BOND | LOST: 36, SL_HIT: 21, TP_HIT: 6, WON: 7 |
| PENNY_STOCK | No rows |
| MEMECOIN | EXPIRED: 1, LOST: 52, RESOLVE_FAILED: 1, SL_HIT: 1,391, TP_HIT: 989, WON: 20 |

### Outcome historical completeness

| Class | Missing PnL | Missing opened_at | Missing closed_at | Closed before opened |
| --- | --- | --- | --- | --- |
| CRYPTO | 23,346 | 37,353 | 37,447 | 0 |
| EQUITY | 2 | 0 | 77 | 2 |
| FOREX | 2 | 0 | 346 | 1 |
| COMMODITY | 0 | 0 | 169 | 3 |
| FUTURES | 1 | 0 | 4 | 0 |
| ETF | 0 | 0 | 0 | 0 |
| BOND | 0 | 0 | 0 | 0 |
| PENNY_STOCK | 0 | 0 | 0 | 0 |
| MEMECOIN | 2,333 | 2,331 | 2,339 | 0 |

Zero outcome OPEN/PENDING/ACTIVE labels with a non-null closure time, and zero future opening/closure timestamps in the requested classes. This does not independently establish the correctness of PnL or label semantics.

### Recent outcome source coverage

Source union below includes any opened/closed/created timestamp in 30d; unlike the closure counts, this may include late ingests of old signals.

| Class | Stored source | Union rows | Symbols | Closed 48h / 14d | Latest closed | Latest created |
| --- | --- | --- | --- | --- | --- | --- |
| CRYPTO | alpha_engine | 890 | 110 | 71 / 377 | 2026-10-22 18:54:42 | 2026-10-22 22:30:32 |
| CRYPTO | crypto_signal_engine | 8 | 3 | 1 / 5 | 2026-10-22 01:51:13 | 2026-10-22 12:45:12 |
| FOREX | alpha_engine | 252 | 12 | 21 / 76 | 2026-10-22 15:30:38 | 2026-10-22 15:35:14 |
| EQUITY | alpha_engine | 42 | 9 | 2 / 19 | 2026-10-22 16:55:45 | 2026-10-22 22:30:32 |
| MEMECOIN | alpha_engine | 7 | 4 | 2 / 6 | 2026-10-22 16:55:45 | 2026-10-22 22:30:32 |
| FUTURES | alpha_engine | 8 | 5 | 0 / 6 | 2026-10-18 12:52:34 | 2026-10-20 22:31:11 |
| ETF | alpha_engine | 13 | 7 | 2 / 4 | 2026-10-22 15:30:41 | 2026-10-22 15:35:14 |
| COMMODITY | alpha_engine | 16 | 8 | 2 / 10 | 2026-10-22 15:30:38 | 2026-10-22 15:35:14 |
| BOND | alpha_engine | 12 | 3 | 0 / 3 | 2026-10-14 22:25:58 | 2026-10-14 22:30:38 |

## Boundary checks and interpretation

- Exact requested-class totals: **108,331 raw rows; 50,119 outcome rows**. Raw also has 145 UNKNOWN rows. Outcomes also have 25 UNKNOWN and 178 empty-class rows, excluded from class verdicts. None of these labels was reassigned.
- The current source footprint is narrow: raw 30-day coverage is AlphaEngine in every active class, plus mega_mutation in CRYPTO. Outcome sources use the distinct stored name alpha_engine, plus crypto_signal_engine for CRYPTO. Shared naming similarity is not proven lineage.
- FUTURES is retained separately from COMMODITY. Symbol overlap or economic asset family must not be used to silently equate these database cohorts.
- Historical empty timestamps and terminal-no-PnL counts are localized cohort limitations. They do not establish current pick corruption, performance failure, or deliberate misreporting.
- No public money_ready_verdict comparison was needed for this bounded task. Its deduplication, policy-clean, cost, horizon, class-normalization and eligibility rules were not replicated, so these totals must not replace its verdict cohort or the parent numerical screen.

## Verification and persistence

Aggregate-only checks passed: status counts sum to each class total; OPEN plus terminal counts reconcile; 48h ≤14d ≤30d raw signal counts; grouped recent source and symbol sums match each raw class recent total; all group LIMITs were below capacity (no truncation). JSON serialization and artifact existence verified. No database writes were performed.

Companion aggregate artifact: `GHCOPILOT_CLASS_LIFECYCLE_AUDIT_2026-10-22.json`. It contains exact SQL, query durations, snapshot clock, all returned aggregate results, definitions, limitations and validation flags. Query wall times total 3.083 seconds. Read-only objective complete; no repair, live deployment or production execution attempted.
