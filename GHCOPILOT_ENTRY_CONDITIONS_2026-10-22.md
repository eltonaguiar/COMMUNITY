# Entry conditions: useful hypotheses, not a new proven winner

GHCOPILOT, 2026-10-22. Goal #1. Existing-condition audit, not a new backtest.

## Current public evidence

- The existing **RSI14 hourly50-70 / US-session13:30-21UTC** crypto lane has
  n394, net PF1.0194, PF lower bound0.8264 and chronological OOS net PF0.981.
  `promotable=false`. Its 16bp assumed cost is below our30bp stress scenario.
  It is not a better-than-random, economically confirmed entry condition.
- The published confidence0.75-0.80 / score-decile50 / AlphaEngine crypto
  cell is now n183, PF4.706, train PF5.707 and inspected holdout PF3.534.
  It is selected from574 cells, and several displayed variants contain
  the same183 observations. They are not independent corroborations.
  The90-day moving cohort is not sealed future confirmation; the source
  outcome/market-path concerns remain. A Bonferroni label cannot repair
  invalid inputs or make a naive dependent win-rate z-test valid.
- The live money-ready feed still has zero approved classes. Parsing it
  with strict JSON fails on NaN: a browser JSON consumer may fail before
  seeing the verdict. This agrees with the last-day strict-JSON audit.
  Do not silently substitute zero or a successful verdict.

These are snapshot findings, not universal condemnation of entry conditioning.
The current independent research shortlist and newly published peer cohorts
are reconciled in the linked reports, rather than pooled into this cell.

## Next conditions worth preregistering

Use a small, economically motivated family; avoid searching every RSI,
confidence, symbol, session and direction intersection. A changed filter is a
new trial and starts a new cohort.

| Condition family | Mechanism | Required guard / exact evidence before testing |
|---|---|---|
| Volatility-scaled trend entry | Avoid buying noise below executable cost | Lagged volatility/trend; fixed lookback; entry after completed bar; same risk budget as simple trend baseline |
| Liquidity/spread/cost eligibility | Gross edge may be untradeable | Point-in-time bid/ask/depth, turnover and size limits; assess missed opportunities and selection denominator |
| Prespecified regime interaction | Trend and mean reversion behave differently | Regime computed only from past data, frozen labels and boundaries; enough independent periods in each state |
| Release-timed carry/COT/macroeconomics | Trade information actually available to us | Publication timestamps/vintages, lagged position/rate data, calendar and roll/funding costs |
| Genuine copy-trader observation delay | Determine whether follower fills preserve source advantage | Original trader identity/fill, first observed timestamp, feasible post-observation fill and full fees; survivor-free trader set |
| Cross-asset confirmation | Separate broad beta from incremental information | Fixed contemporaneous information availability, paired risk-matched control, no duplicate exposure counted as new evidence |

## Is the additional risk worth taking?

Not yet established for the existing cells. Compare daily **net excess return**
and tail loss at identical capital/exposure, including rejected/missing signals.
Publish cost break-even, delay/spread/impact stress, turnover, drawdown,
CVaR/expected shortfall and capacity limits. A lower win rate can be preferable
if payoffs and downside improve; a higher win rate can be worse after costs.

Use training-only feature/scaling fits, purged and embargoed development folds,
a separately held final sample and a genuinely prospective fixed readout.
Use paired dependent resampling/randomization and familywise correction.
Require adequate power at the minimum economically meaningful effect.
If aligned full-family returns or actual execution inputs are unavailable,
DSR/PBO/SPA/capacity are **not evaluable**, not passed.

The current paper lock is unchanged. Do not pick the next filter by whichever
historical cell turns green today. A new experiment requires committed
preregistration before new backtesting under repository policy.

## References and reproducibility

- [Live entry condition](https://findtorontoevents.ca/audit/data/crypto_rsi5070_us_forward_status.json)
- [Live selected cells](https://findtorontoevents.ca/audit/data/top_edges_per_class.json)
- [Nine-class shortlist](GHCOPILOT_TOP5_CANDIDATES_2026-10-22.md)
- [Hidden/new peer candidates](GHCOPILOT_HIDDEN_PERFORMERS_2026-10-22.md)
- [Proposed auditor framework](GHCOPILOT_QUANT_AUDITOR_FRAMEWORK.md)
- [Master plan](GHCOPILOT_MASTER_PLAN_2026-10-22.md)

This report inspects existing results. No newly tuned strategy or backtest
was run, no real orders placed and no production database rows changed.
