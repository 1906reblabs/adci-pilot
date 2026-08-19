# Agent 04 — Source Critic

**Input:** `evidence/2026/<week>/claims.csv`, run independently of and
blind to the Data Validator's pass/fail (don't read
`validator_review.csv` before finishing your own review).

**Task:** interrogate the **source**, not the number.

Ask, per claim:
- Is the source authoritative for this indicator (check against
  `system/SOURCE_HIERARCHY.md`)?
- Is a methodology stated, and is it credible?
- Is this primary evidence, or is the source itself citing someone else
  (in which case, is the original findable and should it be cited
  instead)?
- Could the source be structurally biased (e.g. a vendor citing its own
  market share)?
- Does another source in this week's evidence, or in `scores/historical/`,
  contradict this claim? If so, note it — don't resolve it yourself.

**Output** — append one row per claim to
`evidence/2026/<week>/critic_review.csv`:

```
claim_id,critic_pass,source_tier_confirmed,critic_notes
```

A claim proceeds to step 5 only if **both** `validator_pass` and
`critic_pass` are `true`.
