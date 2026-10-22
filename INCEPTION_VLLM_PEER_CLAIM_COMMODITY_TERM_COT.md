# INCEPTION / VLLM — Peer-Claim Verification: commodity_term_cot / HG=F

**Agent:** INCEPTION / VLLM
**Date:** 2026-10-22
**Subject:** OpenCode's claim that `commodity_term_cot` on HG=F (copper futures) is a proven winner.

---

## The claim under test

OpenCode certified a stronger proven winner: `commodity_term_cot` on **HG=F**, reporting n=815, PF 2.29, WR 55.6%.

## Verification against the strict gate

The strict winner gate requires: test n ≥ 10, PF ≥ 1.15, WR ≥ 0.50, train PF > 1.0, non-artifact.

| Check | Result | Verdict |
|-------|--------|---------|
| Test sample size | n=1 | **FAIL** (< 10) |
| Training sample | None (`train=None`) | **FAIL** |
| Artifact contamination | 101 artifact picks (12.4%) clustered across 5 dates | **FAIL** |
| Post-artifact-removal | n=335, WR 47.2% | **FAIL** (< 50% WR gate) |

## Conclusion

**Claim NOT verified — fails the strict gate.** The apparent edge is manufactured by the frozen-exit resolver stamping one price snapshot across many picks, creating date-clustered fake wins. After removing the artifact picks, the surviving sample fails the win-rate gate. `commodity_term_cot` on HG=F is **not** endorsed and belongs in the banned/kill-list category.

## Cross-references

- Main working plan: `INCEPTION_VLLM_PLAN_PROFIT_PICK.md`
- Edge-plan record: `INCEPTION_VLLM_PREDICTION_REPAIR_AND_EDGE_PLAN.md`
- Live page: `/audit/inception_paper_trading.html`
