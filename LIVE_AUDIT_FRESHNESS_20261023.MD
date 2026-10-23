# Live audit: freshness, current predictions, and evidence quality

**Observation date: 2026-10-23, Coordinated Universal Time (UTC). Goal #1: trustworthy cross-asset audit evidence.**

## Bottom line — explain it like I am five

The main scoreboard was rebuilt today, and most predictions currently displayed were also issued today. But a newly printed scoreboard can contain old tickets. The tournament still contains hundreds of open tickets issued in May–June; the database-health report is from May; and the HyroTrader manual account snapshot is from April.

**Fresh predictions are not the same thing as profitable predictions.** No class appears in the current Money Ready list. United States-listed equity has current AAPL and SNDL predictions, but its policy-clean, cost-adjusted profit factor is below break-even. A different equity panel looks much stronger because it measures a different population.

**Direct database freshness remains unverified.** A certificate-validated Transport Layer Security (TLS) database connection failed before any Structured Query Language (SQL) ran. Public data were retrieved over verified HTTPS, without bypassing certificate checks.

## Scope and method

- Read-only live HTTP evidence: main dashboard plus funds, Top Picks Now, HyroTrader, tournament, and their actual linked/consumed data.
- Main payload retrieved **2026-10-23T15:59:10.817284+00:00**, from `https://findtorontoevents.ca/audit/data/dashboard_data.json?audit=20261023b`.
- Main payload `generated_at`: **2026-10-23T15:43:20.931727+00:00**, approximately 15 minutes 50 seconds before retrieval.
- Evidence gathering completed through **2026-10-23T16:01:56.073364+00:00**; report prepared immediately afterward.
- Sixteen successful source observations: main payload plus 15 additional page/payload observations. Five actual HTML surfaces inspected; seven dashboard asset classes covered.
- Initial generic HTTP requests received status 412. A normal explicit browser User-Agent received status 200 over verified HTTPS. No access-control bypass or alternate credential source was attempted.
- Database access used the existing `tools.db_env.get_stocks_creds` helper and system-trusted TLS, with bounded connection/read timeouts. Result: `OperationalError`, code **2003**, before handshake/query completion. No connection identifiers or credential values retained.
- Intended bounded metadata queries were not executed. Consequently there is **no independently verified current database row count, database clock, database time zone, ingestion timestamp, or resolver write timestamp**.
- No generators, forbidden pick scripts, mutations, deployments, trading, git operations, or shared-repository changes were performed.

**Research assumptions, not production policy:** flag a dashboard build older than two hours, an active source signal older than 24 hours, or a class with no observed close within 72 hours. These are investigative prompts, not trading expiry rules. No exchange-session, holiday, or weekend adjustment was applied. A new close is not proof that the close price or outcome is correct.

## Current active and recently closed population

The dashboard exposes **22 visible active picks**, **zero Smart Picks**, and **3,500 recent-closed records**. Its `active_raw` container has **4,271 records** and includes terminal statuses such as `EXPIRED`, `TP_HIT`, and `SL_HIT`; its name must not be mistaken for 4,271 currently tradable recommendations.

| Class | Visible active | Records in `active_raw` | Recent-closed container records | Visible active signal older than 24 hours |
|---|---:|---:|---:|---:|
| Cryptoassets (CRYPTO) | 2 | 3,707 | 2,111 | 0 |
| Equity (EQUITY) | 2 | 164 | 672 | 0 |
| Exchange-traded funds (ETF) | 10 | 52 | 514 | 1 |
| Foreign exchange (FOREX) | 2 | 229 | 166 | 0 |
| Commodities (COMMODITY) | 2 | 65 | 6 | 0 |
| Bonds (BOND) | 2 | 27 | 30 | 0 |
| Futures (FUTURES) | 2 | 25 | 1 | 0 |

Counts describe these particular payload containers, not the entire database or a common rolling window. The raw container additionally contains two SPORTS records, outside the seven-class scope. Commodity, bond, and futures labels are pipeline categories: the economic exposure of an exchange-traded product can overlap them.

### Active examples: source clocks, not scoreboard clocks

Times below are UTC where the original string contains `Z` or `+00:00`. Prices are published entry fields, not independently verified executable quotes. `—` means absent/empty.

| Class / symbol / direction | Published entry price | Source `timestamp` | Published `entry_time` |
|---|---:|---|---|
| CRYPTO / ETHUSDT / SHORT | 2,400.4 | 2026-10-23 15:08:48.250239+00:00 | 2026-10-23, date only |
| EQUITY / SNDL / LONG | 1.29 | 2026-10-23 14:06:56Z | 2026-10-23 14:06:56Z |
| EQUITY / AAPL / LONG | 348.22 | 2026-10-23 14:06:56Z | 2026-10-23 14:06:56Z |
| ETF / XLK / LONG | 182.34 | 2026-10-23 12:30:42.315765+00:00 | 2026-10-23 12:30:42.315882+00:00 |
| FOREX / EURGBP=X / LONG | 0.83772 | 2026-10-23 15:38:16.882751+00:00 | — |
| COMMODITY / SI=F / LONG | 54.07 | 2026-10-23 15:38:16.882760+00:00 | — |
| BOND / IEF / LONG | 91.055 | 2026-10-23 15:38:16.882709+00:00 | — |
| FUTURES / YM=F / LONG | 52,495 | 2026-10-23 14:11:45.629170+00:00 | 2026-10-23, date only |

**Created / updated / closed:** all examples above have no exposed `created_at` or `updated_at` value and empty `closed_at`. These are explicitly unknown database clocks, not values that can be replaced by `generated_at`. All are `OPEN` in this payload. Full original identifiers and two active examples per class are retained in the JSON evidence.

AAPL and SNDL are United States-listed equity examples; SNDL being US-listed does not imply a US-domiciled issuer. No separate US-only equity prediction page was discovered in the inspected main-page links; EQUITY is not assumed to mean exclusively US assets.

### Recently closed examples

| Class / symbol / direction | Entry price | Source `timestamp` | Published `entry_time` | Published `closed_at` | Outcome / published profit-and-loss percentage |
|---|---:|---|---|---|---|
| CRYPTO / AVAX-USD / LONG | 6.805 | 2026-06-08 01:03:11.500698, no zone | — | 2026-10-23 15:10:09Z | WON / +3.0 |
| EQUITY / AAPL / LONG | 340.609985 | 2026-10-21 14:09:08Z | — | 2026-10-23 13:40:12Z | WON / +2.6981 |
| ETF / SPY / LONG | 768.820007 | 2026-10-21 06:46:16Z | 2026-10-21 06:46:16Z | 2026-10-22 18:43:07.209155+00:00 | LOST / −0.9144 |
| FOREX / USDJPY=X / LONG | 156.977997 | 2026-10-23 08:13:43.998510+00:00 | 2026-10-23, date only | 2026-10-23 08:50:08.087186+00:00 | LOST / −0.5 |
| COMMODITY / NG=F / LONG | 3.035 | 2026-10-19 08:53:11.536634+00:00 | same as source timestamp | 2026-10-19 09:01:11.355006+00:00 | WON / +2.6359 |
| BOND / TLT / LONG | 80.264999 | 2026-10-22 13:57:42Z | 2026-10-22 13:57:42Z | 2026-10-22 16:40:30.884080+00:00 | WON / +1.51 |
| FUTURES / YM=F / LONG | 52,463 | 2026-10-15 22:45:24.658318+00:00 | 2026-10-15, date only | 2026-10-18 01:10:59.785361+00:00 | LOST / −0.4746 |

For these closed examples, `created_at` and `updated_at` are also absent. No missing `closed_at` was found within the 3,500-record container, but that does not establish completeness of historical database closures.

**Freshness interpretation:** source signals are current across all seven classes. The most recent commodity and futures closes in this container are approximately four and five days old, respectively: both breach the research 72-hour flag. AVAX demonstrates why a close written today can concern a signal issued months earlier. A timezone-naive timestamp is not proven UTC; UTC was assumed only for evidence sorting and its original string is preserved.

The recently closed AAPL and newly active AAPL are separate records, with different entry prices and timestamps. A symbol match alone is not a lifecycle join.

## Raw versus policy-clean net metrics

**Win rate** is the share of resolved trades counted as wins. **Profit factor** is total gains divided by the magnitude of total losses: below 1 means losses outweigh gains. **Net** means the registry applies its stated round-trip slippage model; it does not establish that every real-world fee, spread, market impact, financing charge, or tax has been measured.

The live registry was generated **2026-10-23T15:43:17Z**. Its methodology deduplicates by strategy/source, symbol, direction, trade date, and rounded entry price, removes defined non-crypto spot-flicker returns, and uses `pnl_pct > 0` as its win definition. Its net model is `alpha_engine.charter_slippage.deduct_slippage`, described by the source as fraction-unit round-trip basis points. Return-unit ambiguities in other panels were not silently normalized.

| Class | Registry raw: count / win rate / profit factor | Registry policy-clean net: count / win rate / profit factor |
|---|---|---|
| CRYPTO | 23,172 / 45.60% / 1.3283 | 19,785 / 46.19% / 0.2918 |
| EQUITY | 546 / 50.92% / 0.7882 | 494 / 54.86% / 0.8937 |
| ETF | 17 / 70.59% / 1.8685 | 16 / 75.00% / 1.8635 |
| FOREX | 448 / 37.05% / 0.7240 | 414 / 37.20% / 0.4418 |
| COMMODITY | 197 / 17.26% / 1.1724 | 15 / 33.33% / 0.5000 |
| BOND | 2 / 0.00% / 0 | No policy-clean net row returned |
| FUTURES | 55 / 27.27% / 3.7601 | 15 / 26.67% / 5.4348 |

**Do not promote the small profitable samples.** The ETF and futures net results each have fewer than 20 observations. The registry labels net rows as discovery and not promotion eligible. Raw-versus-net changes reflect both exclusions and cost adjustments, not costs alone.

### Why equity can appear profitable in one place and unprofitable in another

- Main payload `performance.by_asset_class.EQUITY`: **16 closed, 81.2% win rate, profit factor 13.19**. This is not the registry's raw population and not a verdict-grade net headline.
- Registry raw EQUITY: **546**, **50.92%**, **0.7882**.
- Registry policy-clean net EQUITY: **494**, **54.86%**, **0.8937**.
- Main `performance.asset_class_health.EQUITY` agrees with that net count and profit factor, but also carries separate daily policy-clean fields: **147**, **62.59%**, **1.506**.
- Current money-ready EQUITY sizing uses **intrabar truth**—outcomes checked inside the price bar rather than relying only on daily-bar ordering: **234**, **56.84%**, **0.8711**. The payload explicitly flags daily profit-factor inflation of approximately **1.73 times**. Equity verdict: **NOT_READY**.
- The dedicated money-ready sidecar, generated **2026-10-23T15:42:29.293773+00:00**, reports an empty `money_ready` list across nine classes.

These are distinct cohorts and methods, not interchangeable estimates of one fixed ledger. The dashboard's CRYPTO health count also differs slightly from the separately generated registry despite very close build times. Exact row-level reconciliation is blocked by unavailable database access.

### Current recency panels: important independent contradiction to resolve

Both recency sidecars were generated **2026-10-23T15:49:34+00:00**, with `fallback_mode=false`.

| Class | Fourteen-day closes / win rate / profit factor | Forty-eight-hour closes / win rate / profit factor |
|---|---|---|
| CRYPTO | 1,701 / 41.49% / 0.913 | 277 / 38.99% / 0.769 |
| EQUITY | 2,710 / 59.48% / 1.476 | **0 / unavailable / unavailable** |
| ETF | 233 / 21.89% / 0.799 | 9 / withheld for low sample / 0 |
| FOREX | 816 / 40.03% / 0.719 | 9 / withheld for low sample / 0 |
| FUTURES | 338 / 34.32% / 0.222 | 21 / 42.86% / 0.626 |
| BOND | 21 / 80.95% / 12.656 | 4 / withheld for low sample / infinite |
| COMMODITY | No class row returned | No class row returned |

The equity 14-day cohort identifies **100% AlphaEngine source concentration**. Its 48-hour panel has **27 active but zero closed**, whereas the dashboard recent-closed list includes today's AAPL close. **Do not average those panels or claim equity has no recent closures everywhere.** They plainly do not describe an identical population; the exact missing join/source/filter explanation is unverified. The bond infinity is a four-trade zero-loss denominator artifact, not an unlimited-return claim.

## Related live surfaces: what is fresh and what is not

1. **Funds — `https://findtorontoevents.ca/audit/funds.html`.** Its consumed `/audit/data/dashboard_payload.json` reports the same **15:43:20.931727** generation timestamp as the main payload; the set of 22 active pick identifiers matches exactly. This supports a current shared input snapshot, not independent fund profitability, holdings execution, or historical strategy selection. The separate historical fund case study is outside this audit.

2. **Top Picks Now — `https://findtorontoevents.ca/audit/picks-now.html`.** Actual consumed `/audit/data/picks_now.json` has **25 picks**, generated **2026-10-23T12:07:08.393360+00:00**, nearly four hours before retrieval. It breaches the research two-hour build flag despite the page being reachable now. Its gate explanation distinguishes discovery scores from intrabar-qualified strong-buy status. Do not substitute the main dashboard's newer timestamp for this feed's clock.

3. **AI Model Tournament — `https://findtorontoevents.ca/audit/ai-tournament.html`.** Leaderboard regenerated **2026-10-22T23:30:14.258744+00:00**, with **46 models**. But actual `ai_tournament_picks_latest.json` has **7,099 records** whose newest submission is **2026-06-04T13:28:40.568818+00:00**; oldest is May 19. Status counts: **582 OPEN**, **4,285 MISPRICED_ENTRY**, **1,037 WIN**, **1,195 LOSS**. All **582 open submissions exceed 24 hours**, in practice months old. A recently recomputed leaderboard is not a current forecast feed. Mispriced entries are a large integrity warning; this audit did not reprice or independently resolve them.

4. **HyroTrader — `https://findtorontoevents.ca/audit/hyrotrader/`.** The page explicitly distinguishes research scanner tables from its manual action log. The action-log payload `/audit/data/hyrotrader_picks.json` has **seven records**, an account `last_session_date` of **2026-04-08**, and no top-level generation timestamp. Its first example is `pending_entry`, direction `BOTH`, with no entry, stop, target, open, or close timestamp: a plan, not an executed current prediction. This establishes staleness of the manual snapshot, **not** that every separate live scanner on the page is stale. Separate live scanner payloads were not validated in this bounded pass.

## Database freshness: strongest limitation

Relevant operational table names, from the existing schema and pick-flow references:

- `at_raw_picks`: source pick ledger, lifecycle/status, recorded/close fields.
- `at_consensus_picks`: multi-source published layer.
- `at_signal_outcomes`: resolved outcomes and intrabar truth.
- `at_aggregation_runs`: ingestion cycles.
- `trading_picks`: dashboard-facing records and create/update clocks.
- `at_pick_outcomes`: explicitly named in registry source provenance; its current schema/rows were not queried.

The public `/audit/data/db_freshness.json` was retrieved successfully at **2026-10-23T15:59:57.294875+00:00**, but its own `generated_at` is **2026-05-23T18:29:59.406068+00:00**—approximately **153 days old**.

Its GREEN labels refer to May 23 `trading_picks` creation/resolution observations, not October. It also reports an old RED `at_signal_outcomes` check and a backtest timestamp-schema warning. **Neither those GREEN nor RED statuses can establish today's database health.** This is a stale monitor, not proof that today's database is stale or healthy.

The dashboard has its own `data_freshness.last_dashboard_build` of **15:48:02.393953**, later than the root `generated_at` of **15:43:20.931727**; `last_alpha_scan` is **15:10:08.100123**. Its `stale_warning=false` is not a per-source freshness guarantee. Metadata `payload_lag_seconds=4614.931727` corresponds to the gap from last code-change time to payload generation, not the age of a market signal at retrieval.

No claim in this report relies on HTTP response `Date`, successful page loading, or a file being downloadable as proof of underlying database freshness.

## Practical next steps, in priority order

1. Restore a current **read-only** database-health observation, then compare per-class ingestion and resolver clocks; investigate the monitor publication path without assuming current operational failure.
2. Quarantine tournament open tickets from any “current picks” interpretation until current submissions and entry-price integrity are demonstrated.
3. Label Top Picks Now with its own age, and the Hyro manual snapshot with its last session date.
4. Resolve the equity recent-close population mismatch using exact pick identifiers, source systems, status mapping, and close-time fields. Do not merge the cohorts by symbol alone.
5. Keep raw, policy-clean net, daily-bar, and intrabar results visibly separate. Do not size equity from the 81.2% small-subset tile or the daily profit factor 1.506.
6. Investigate commodity/futures closure cadence and the one older ETF signal using strategy-specific holding periods and exchange calendars before declaring a production freshness breach.

**Confidence:** high for retrieved payload values, URLs, timestamps, observed counts, and cross-payload active-ID equality; moderate for freshness interpretation under the stated research assumptions; unavailable for present database clock/rows, execution prices, complete lifecycle lineage, and actual realized investable performance.

## Exact retrieval inventory

All URLs below use `https://findtorontoevents.ca`; paths are shown for readability. Every listed observation returned HTTP 200. The compact evidence JSON retains full URLs, exact retrieval times, identifiers, original timestamp strings, source methodology, counts, and relevant excerpts.

| Source path | Retrieved UTC on 2026-10-23 |
|---|---|
| `/audit/data/dashboard_data.json?audit=20261023b` | 15:59:10.817284 |
| `/audit` | 15:59:57.440070 |
| `/audit/funds.html` | 15:59:57.367150 |
| `/audit/hyrotrader/` | 15:59:57.348794 |
| `/audit/data/db_freshness.json` | 15:59:57.294875 |
| `/audit/data/pf_registry.json` | 15:59:57.664599 |
| `/audit/data/pick_summary_stats_14d.json` | 15:59:57.374974 |
| `/audit/data/pick_summary_stats_48h.json` | 15:59:57.436794 |
| `/audit/picks-now.html` | 15:59:57.487573 |
| `/audit/ai-tournament.html` | 16:00:28.224911 |
| `/audit/data/dashboard_payload.json` | 16:00:29.259642 |
| `/audit/data/picks_now.json` | 16:00:28.204383 |
| `/audit/data/hyrotrader_picks.json` | 16:00:28.208259 |
| `/audit/data/money_ready_verdict.json` | 16:00:28.198863 |
| `/audit/data/ai_tournament_picks_latest.json` | 16:01:04.122451 |
| `/audit/data/ai_tournament_leaderboard.json` | 16:01:03.847641 |

**Evidence retention:** this report combines a delegated read-only observation
pass at 15:59-16:02 with a direct follow-up at 16:05. The sibling
[compact evidence](live_audit_freshness_20261023.json) retains the latter main
snapshot, all 22 active records, close examples, canonical verdict and registry
observations, fund rankings and tournament counts. It is **not a raw archive of
all 16 earlier observations**. In particular, the recency-panel, database-monitor,
Top Picks Now and manual-account details above are the earlier pass's attributed
observations with source URLs and retrieval times, not additional rows in that
compact JSON. Do not represent a file hash for one snapshot as verification of
all linked sites or direct database rows.

## Follow-up: every visible active instrument and our call

**Direct follow-up retrieved 2026-10-23T16:05:05.358777+00:00.** The main payload
was generated at 15:43:20.931727+00:00. Its Secure Hash Algorithm, 256-bit
(SHA-256) fingerprint is
`a91e6d871c1a87279ab7145bc751dee4222ca9cbb476742021319fba0baf7315`.

All 22 records below are published OPEN records, not verified fills or current
quotes. Twenty-one have `forward_validated=false`; a true field on the remaining
record is not independent forward confirmation. Some rows are backfilled; gate
flags vary. "LONG" means a prediction of rising prices; "SHORT" predicts falling
prices and can involve additional execution and risk constraints.

| Pipeline class | Symbol | Published direction | Published entry | Our call |
|---|---|---|---:|---|
| Crypto | ETHUSDT | SHORT | 2400.4 | PAPER-RESEARCH; no independently verified current edge |
| Crypto | HYPEUSDT | SHORT | 77.91000366 | PAPER-RESEARCH; source timestamp has no explicit time zone |
| Foreign exchange | AUDUSD=X | SHORT | 0.702938 | PAPER-RESEARCH; spread and funding not reconciled |
| Foreign exchange | EURGBP=X | LONG | 0.83772 | PAPER-RESEARCH; no demonstrated current edge |
| Equity | SNDL | LONG | 1.29 | UNASSESSED instrument-level edge; US listing does not establish US domicile |
| Equity | AAPL | LONG | 348.22 | PAPER-RESEARCH; the separate profitable AAPL close does not validate this new entry |
| Futures | ES=F | LONG | 7670.75 | HOLD-CLAIM; continuous-series symbol does not identify executable expiry |
| Futures | YM=F | LONG | 52495 | HOLD-CLAIM; contract, margin, expiry and fills unresolved |
| Commodity | SI=F | LONG | 54.07 | HOLD-CLAIM; silver exposure, not capital-safe |
| Commodity | PA=F | SHORT | 1051.6 | HOLD-CLAIM; palladium contract and short-execution risk unresolved |
| ETF | XLE | LONG | 67.57 | PAPER-RESEARCH energy-sector timing; no role-to-signal upgrade |
| ETF | EWY | LONG | 149.06 | PAPER-RESEARCH Korea equity timing |
| ETF | KWEB | SHORT | 23.21 | PAPER-RESEARCH China internet short; borrow/execution not established |
| ETF | VLUE | LONG | 193.8 | PAPER-RESEARCH US value-factor timing |
| ETF | KBE | SHORT | 65.83 | PAPER-RESEARCH banking-sector short |
| ETF | XLK | LONG | 182.34 | PAPER-RESEARCH technology-sector timing |
| Bond | IEF | LONG | 91.055 | PAPER-RESEARCH Treasury-duration timing; not insured cash |
| Bond | TLT | LONG | 81.440002 | PAPER-RESEARCH long-duration timing; can have large rate-driven losses |
| ETF | IYR | SHORT | 98.37 | PAPER-RESEARCH listed-property short |
| ETF | EFA | LONG | 103.15 | PAPER-RESEARCH developed-market equity timing |
| ETF | XLV | LONG | 181.3 | PAPER-RESEARCH health-care-sector timing |
| ETF | XLF | LONG | 56.256302 | PAPER-RESEARCH financial-sector timing; source October 22 rather than October 23 |

Original identifiers, stops, targets, source times and fields are preserved in
the compact evidence. We did not independently quote every instrument, validate
its entry price, certify a contract, or establish legal shorting access.
Pipeline ETF/BOND/FUTURES labels are not a consistent economic taxonomy;
the rows above name the actual exposure where identifiable.

### Separate current intrabar-truth sizing cohort

This is the canonical money-ready sidecar's cohort, **not** the registry's larger
discovery population or the current 22 active records.

| Class | Resolved count | Win rate | Profit factor | Published verdict / our stance |
|---|---:|---:|---:|---|
| Crypto | 3581 | 35.58% | 0.8980 | NOT_READY / research only |
| Equity | 234 | 56.84% | 0.8711 | NOT_READY / no current stock certified |
| Commodity | 229 | 40.17% | 1.0256 | WATCH / insufficient readiness evidence |
| Foreign exchange | 568 | 31.69% | 0.6465 | NOT_READY / losses exceed gains |
| Futures | 48 | 41.67% | 1.0610 | INSUFFICIENT_DATA / no upgrade |
| ETF | 30 | 0% | 0 | INSUFFICIENT_DATA / method/population caution |
| Bond | 0 | unavailable | unavailable | INSUFFICIENT_DATA / no evidence of current timing skill |
| Meme | 12 | 16.67% | 0.0719 | INSUFFICIENT_DATA / no upgrade |
| Penny | 1 | 0% | 0 | INSUFFICIENT_DATA / no upgrade |

ELI5: different boxes contain different tickets. A good result in one small
box does not make today's ticket in a different box a good bet.

## Important accounting corrections before using dashboard risk figures

The local source inspected in `tools/hf_stats.py` accumulates trade percentage
points for its drawdown field. It is not a funded account's peak-to-trough wealth
percentage. Similarly, the local generator's deprecated full-capital sequential
trade compound is invalid as a portfolio result when trades overlap.
Do not call a 208-point statistic a literal 208% unleveraged account loss, or a
-97.71% sequential illustration a reconciled funded account return.
The -42.31 field is rolling-100 in the inspected payload, not the raw all-trade
sum. Local source and deployed source identity were not fully established.

See [peer-method corrections](GHCOPILOT_20261023_PEER_METHOD_CORRECTIONS.MD).
Our conclusion of **no independently certified money-ready class** does not
require pretending those incompatible statistics are one portfolio.
