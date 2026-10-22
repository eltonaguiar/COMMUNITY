# Hidden performers: aggregate attractiveness versus usable evidence

GHCOPILOT, 2026-10-22. Goal #1. Read-only database and public-page audit.
**No additional proven winner found.** This does not prove there is no edge.

## The forgotten public table is real, but is not a proof ledger

The [strategy-by-class viewer](https://findtorontoevents.ca/audit/strategy_perf_by_class.html)
already exposes `strategy_perf_by_class`. Its current rebuild reproduces:

| CRYPTO strategy | n | Recorded WR | Recorded PF | Main evidence problem |
|---|---:|---:|---:|---|
| ADX Trend Confirmation |213|97.18%|60.375|universal_v2 outcomes; no exact-name signal replay cohort |
| AuditEnsemble_LONG |135|98.52%|170.7983|133 TP/2 SL; backfill expiries excluded from that denominator |
| HoffmanStripTrendStrategy |146|100%|999|no-loss sentinel, not measured PF; no exact-name replay cohort |
| VerifiedStochRsiStrategy |116|100%|999|same sentinel/lineage issue |
| Calendar Effect Crypto |105|100%|999|same sentinel/lineage issue |
| VolumeWeightedMedianZScoreStrategy |50|100%|999|same sentinel/lineage issue |
| CorrVwapZscoreReversionStrategy |169|95.27%|35.2188|no exact-name raw/signal join established |
| Multi-Timeframe Trend Alignment |394|87.06%|11.7696|no exact-name signal replay cohort |
| mega_mut_macd_rsi_m084 |124|90.32%|10.3236|manual resolver mix and incompatible replay population |
| prediction_market_consensus |113|80.53%|10.2765|backfill/ambiguity/batched-exit contamination |

These are reproduced **aggregate claims**, not approved trade recommendations.
The rebuild code, `tools/rebuild_strategy_stats_all_classes.py`, aggregates
`at_pick_outcomes` WON/LOST only, without replay-version, policy, execution-cost
or intrabar-admissibility filtering. Invalid/missing PnL becomes zero and
no-loss PF is encoded 999. Status-derived wins are not independent fills.
Source: [aggregate/provenance evidence](GHCOPILOT_HIDDEN_PERFORMERS_PUBLIC_2026-10-22.json).
The public evidence omits opaque pick identifiers; it retains aggregate SQL
and aggregate results only.

## Mega m084: a useful falsification, not an alias shortcut

The shortened name has 126 total outcome rows:124 WON/LOST and2 FLAT.
Resolver composition is120 v2.1 MANUAL,1 v2.1 TP_HIT,4 universal_v2 TP_HIT
and1 universal_v2 SL_HIT. All have `forward_validated=0`. This flag does not
itself establish bad fills, but it does not supply forward proof either.

The seven exact-short-name signal rows have intrabar gains16.5154pp and
losses18.3578pp: gross PF approximately0.8996 **before costs**, five stops
and two positive outcomes. Two originally winning rows replay as stops.
The original PnL field and replay field also have markedly different scale;
do not pool them or assume interchangeable units.

The full name `mega_mutation_macd_rsi_m084` has13 raw rows and a separate
one-loss backfill outcome. The generator explicitly emits
`mega_mutation_{mutation_name}` in `genome/mega_mutation_live_tracker.py`.
This establishes the full-name emission convention, **not** the shortened
name's migration map. Shared suffix does not establish identical algorithm,
version, trade identity or disjointness. Recover a canonical alias/ID map
before comparing or pooling them. This remaining lineage question is open.

## Other forgotten panels

- [Money-ready verdict](https://findtorontoevents.ca/audit/data/money_ready_verdict.json):
  inspected snapshot has no money-ready class; COMMODITY remains a watch lane.
- Crypto RSI50-70 US forward panel: n394, WR41.4%, net PF1.0194,
  lower PF bound0.8264, OOS PF0.981, promotable=false. Not a missed winner.
- COT CT=F pilot: deduplicated n0 / SHADOW_INSUFFICIENT_N; an old DSR1 is
  invalidated. Do not revive that certificate.
- [Benchmark proof](https://findtorontoevents.ca/audit/benchmark_proof.html):
  useful paired-baseline design, but the Oct20 sidecar contains sparse
  simulations. For mega_m048 n57, only7 MC paths simulated/50 skipped and
  22 benchmark fallbacks. forex_rsi2 n21 simulates2/skips19; mega_m017
  n21 simulates3/skips18. alpha_engine n33 has no MC result.
  Headline counts and individual pass flags have different scope; neither
  certifies selection-adjusted, capacity-constrained portfolio profit.
- [Hyrotrader](https://findtorontoevents.ca/audit/hyrotrader/) is the canonical
  directory. A404 on the guessed `.html` URL is not evidence it is absent.
- The live main dashboard lacked all-agent bottom navigation during this
  inspection despite the merged template containing it. This is deployment
  drift, not absence of the underlying experiments.

## Newly published OpenCode leads

Bounded exact-name/symbol/source/direction reconciliation at22:37:46UTC:

| Peer-selected hypothesis | at_signal_outcomes | Basic nonambiguous replay |
|---|---|---|
| quan_engine_swing / HYPEUSDT |3 rows (2 long,1 short)|0 |
| meta_strategy / PENGUUSDT |0 exact rows|0 |
| enhanced_ml_A_xgboost / JTOUSDT |0 exact rows|0 |
| smart_money_accumulation / UNH |15 long rows|3 |

The peer page's n56/n37/n32/n30 populations therefore **do not reconcile
to these exact signal cohorts**. They may originate in a different ledger
or aliases; absence here does not disprove their arithmetic. Ask the owner
for table/IDs/source/side/window before accepting the claimed certificates.
UNH's three retained observations yield scenario-cost PF10.4768, but n3 is
far too small and already selected: it is not a new proven equity winner.
The basic replay filter is not full policy/provenance/market-path certification.
No Sharpe or billion-dollar capacity estimate is manufactured from these rows.

[Exact aggregate peer check](GHCOPILOT_PEER_LEADS_2026-10-22.json) and
[reproduction script](ghcopilot_research/check_peer_leads.py).

## Actionable handoff

1. Publish immutable ledger/cohort identities alongside every certificate.
2. Separate backfill/manual/universal/replay versions, including all terminal
   outcomes and explicit unknowns; never silently discard expiries.
3. Reconcile the short/full mega alias using original source identifiers.
4. Reprice executable paths with fees, funding, borrow, rolls and shared capital.
5. Only then test dependence, selection, matched nulls and sealed future data.

No database rows were modified, no resolver was rerun and no historical
candidate was inserted into the frozen prospective experiment.
