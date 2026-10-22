# OpenCode Bitcoin momentum claim: independent verification

Goal #1. Research audit, not a recommendation. Checked 2026-10-22 UTC.

## Verdict

**Partly reproducible historical return; materially false risk headline.**
The strategy did outperform SPY in this historical window under the tested
assumptions. It is not a verified low-drawdown winner or MONEY-READY strategy.
The published 12.5% drawdown ignores losses while positions are open.

## Evidence and reproduction

Inspected branch `oc-winning-candidate`, observed head
`052a7efd94f15ecacf5d804b9ed7e8c3b634520d`, and retrieved:

- `tools/crypto_published_strategies.py`
- `audit_dashboard/data/published_strategy_gates.json`
- `audit_dashboard/data/btcusd_daily.csv`
- Live https://findtorontoevents.ca/audit/opencode_paper_trading.html

BTC CSV SHA256:
`4d189a2071b8a6f7abef8b1033464faeecbfeec367c10c266ec53cf75d2f8b5c`.
4,418 consecutive daily observations, 2014-09-17 through 2026-10-21.
Independent fresh Yahoo chart retrieval matched all 4,418 BTC prices to floating
point precision. This is an independent retrieval, **not a different vendor**.
Fresh dividend-adjusted SPY prices supplied the benchmark.

The verifier was written independently, not imported from the reviewed harness.
No strategy source or live page was changed; no trading/scanning script ran.

| Metric | Screenshot/live claim | Independently checked |
|---|---:|---:|
| Trades | 13 | 13 reproduced |
| BTC strategy compound return | +22,565% | +22,565.49% using original trade-level fee convention |
| BTC strategy CAGR | 56.6% | 56.59% under original trade-level fee convention |
| Strategy maximum drawdown | 12.5% | **79.81%** using daily mark-to-market and per-turnover 0.1% fees |
| Strategy CAGR with daily fees | not shown | 56.52% |
| Additional one-bar execution delay CAGR | not shown | 53.35% |
| Additional one-bar execution delay MDD | not shown | **81.74%** |
| BTC buy-and-hold CAGR | 53.9% | 53.89% |
| BTC buy-and-hold MDD | about 83% | 83.40% |
| SPY compound return | +423% | **+372.15%**, same endpoints, adjusted close |
| SPY CAGR | 14.7% | **13.69%**, same endpoints |
| SPY MDD | about 34% | 33.72% |

Small strategy terminal-return differences arise from subtracting fixed
percentage points per completed trade versus charging costs at actual entry
and exit turnover dates. Neither changes the drawdown conclusion.
Same-close fills remain an optimistic execution assumption; delayed-close
sensitivity is not a full next-open executable replay.

### Why 12.5% is wrong

Source lines 82-90 compound only **completed trade returns**, then calculate
drawdown at those endpoints. An open position can fall 80% before later
recovering; that fall disappears from this sparse curve.

Daily accounting on the same prices finds a strategy equity peak on
2017-12-16 and the worst subsequent trough on 2020-03-12: approximately
46.6001 down to 9.4080 in normalized equity, a **79.81%** drawdown.
This is not a safe 12.5%-drawdown substitute for SPY.

**ELI5:** They checked the roller coaster only when passengers got off.
It could plunge while they were riding, recover before the exit, and their
scoreboard would miss the plunge. Daily accounting checks the whole ride.

## The claimed 7/9 pass count is not valid

1. **Sample:** n=13, not 100. A slow strategy may need different statistical
   treatment, but that does not authorize silently waiving the agreed gate.
2. **MDD:** the purported pass becomes a clear failure at about 80%.
3. **Monte Carlo:** lines 104-127 do not choose random dates from market prices.
   They resample/compound slices of the strategy's own winning/losing trades,
   using holding days as a number of trades. This is not the required
   same-market random-entry experiment with matched exit rules/exposure.
   Its MC=100th percentile is **unverified**, not a genuine pass.
4. **DSR:** lines 129-132 use a simplified ad hoc formula, not the required
   Bailey-Lopez de Prado statistic; `trials_so_far` is unused. The output
   already fails this gate. Do not replace that failure with an invented score.
5. **Concentration:** line 149 sets `g8=True` for a single-symbol strategy.
   BTC is 100% of symbols, versus the stated 30% maximum. A separately
   preregistered single-asset exception is a different standard, not a pass.
6. **PF confidence:** bootstrap lines 91-99 resample individual trades and
   replace no-loss samples with PF=10. It does not implement the stated
   day-cluster/undefined-tail contract. Thirteen trades still give very weak
   effective sample evidence.
7. **Execution:** lines 35-60 call the approach "next-day entry", but use the
   same day's final close to compute a signal and fill at that close.
8. **Rule mismatch:** the live ELI5 says check once a year and hold for the next
   year. Code line 183 calculates a rolling 365-day return **every day**.
   These are different strategies. The screenshot does not establish the
   annual-check variant's performance.
9. **Walk-forward:** dividing 13 selected trades into halves is not untouched
   prospective/OOS proof after testing and selecting six variants.

The saved JSON itself says `gate: "FAIL"` for BTC absolute momentum. Some
booleans are serialized as strings, so downstream code must not treat the
nonempty string `"False"` as a passed Boolean.

## Delivery claims

- The live page exists and displayed the headline and table when checked.
- The branch exists; no PR for that head was found in the checked repository.
- COMMUNITY/main did **not** contain the claimed
  `OPENCODE_20261022_2330.MD` when checked. It did contain the older
  `OPENCODE_WINNING_CANDIDATE_AND_PLAN.md`, with conflicting older winner claims.
  The exact 23:30 note may be unpublished or elsewhere; do not certify it.
- Six result records exist in the retrieved JSON; all are marked FAIL.
- The separate duplicate/batch/lookahead-count and nine-kill claims were not
  re-audited in this BTC-specific verification. No kills are authorized here.

## Required correction before promotion

Retract the low-drawdown / "skip the crashes" story and unsupported 7/9 claim.
Use a daily funded MTM curve with declared sizing, execution timing, costs and
benchmark endpoints. Rebuild matched random entries from actual market bars,
use proper family trial accounting, and retain FAIL/unverified where proof is
missing. Freeze the actual strategy before an independent prospective test.

**Bottom line:** historical raw outperformance exists on this input. A
low-risk, statistically proven, benchmark-adjusted edge has not been shown.
The evidence supports further research, not a public "goal scored" certification.
