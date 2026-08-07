# P1-DEC-005 — ELIS Supervisor as S2 DeepSeek Lane

| Field | Value |
|---|---|
| **Decision ID** | P1-DEC-005 |
| **Date** | 2026-08-02 |
| **Status** | Current |

## Context

The S2 lane requires a DeepSeek-powered independent discovery agent. Two options were considered: (a) create a new dedicated `elis-slr-s2` profile, or (b) repurpose the existing `elis-supervisor` profile (which already uses deepseek/deepseek-v4-pro via OpenRouter).

## Decision

The existing **elis-supervisor** profile is reused as the S2 DeepSeek discovery lane. No new profile is created.

A **5-point critical role boundary** restricts elis-supervisor's S2 role:

1. **Discovery only**: Execute search prompts and return structured results — no PESC coding, no analysis, no manuscript drafting.
2. **No cross-lane communication**: Must not read S0 or S1 outputs during its discovery run.
3. **Sealed output**: Write results to `evidence/discovery/s2-deepseek/` and `literature/discovery/s2-deepseek/` only.
4. **Completion attestation**: Produce a completion manifest before exiting discovery role.
5. **No platform mutation**: Must not modify profiles, configurations, Kanban state, or gateway settings during discovery.

The 5-point boundary is enforced at task-creation time via Kanban task specification, not via technical access control.

## Rationale

- elis-supervisor already uses deepseek/deepseek-v4-pro — the correct model for S2.
- Creating a new profile would duplicate configuration and increase maintenance burden.
- The 5-point boundary provides clear operational guardrails without requiring technical access restrictions.
- Supervisor profile already has file-system access to the SLR workspace.

## Consequences

1. elis-supervisor serves dual role: platform operations + S2 discovery lane.
2. S2 tasks must include the 5-point boundary in their Kanban task body.
3. S2 discovery tasks are sequenced to not overlap with platform operations tasks.
4. Profile documentation must reflect the dual role.

## Related Kanban Tasks

| Task | Role |
|---|---|
| t_6b14ef48 | Execution packet preparation |
| t_1f9cdf54 | Plan PATCH-05: history/ layer |

## Related Artifacts

- Implementation plan v1.0, §S2 Lane
- elis-supervisor profile configuration

## Supersedes

None.

## Superseded By

None.
