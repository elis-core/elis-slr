# P1-DEC-010 — H1–H4 Structural Human Gates

| Field | Value |
|---|---|
| **Decision ID** | P1-DEC-010 |
| **Date** | 2026-08-05 |
| **Status** | Current |

## Context

Paper 1's workflow includes critical decision points where AI outputs must be reviewed by a human (PO or designated researcher) before the pipeline can proceed. These gates need formal definition with clear entry/exit criteria and Kanban integration.

## Decision

Four structural human gates are placed at critical workflow boundaries:

| Gate | Name | Position | Reviewer | Blocks |
|---|---|---|---|---|
| H1 | Artifact Admission | After discovery union, before evidence packet creation | PO / Researcher | Artifacts entering evidence register |
| H2 | Evidence Packet Validation | After evidence packet assembly, before PESC coding | PO / Researcher | Invalid packets proceeding to coding |
| H3 | PESC Coding Review | After AI PESC coding, before adjudication | PO / Researcher | Incorrect codes entering adjudication |
| H4 | Interpretation | After analysis, before manuscript finalisation | PO / Researcher | Unreviewed interpretation entering manuscript |

Each gate is implemented as a **Kanban blocked/pending-human task**:

1. The preceding automated step completes and creates a gate task with status `blocked`.
2. The gate task is assigned to the PO (or delegated researcher).
3. The PO reviews the artifact(s) and either approves (unblocks) or rejects (returns with findings).
4. The downstream automated step cannot start until the gate task is unblocked.

## Rationale

- Structural gates ensure human oversight at the highest-risk workflow points.
- Kanban integration makes gate status visible and auditable.
- Blocked-task pattern prevents downstream automation from proceeding past an unreviewed gate.
- Four gates balance oversight with throughput — too many gates would stall the pipeline.

## Consequences

1. H1–H4 gate tasks are part of the P1-ART Kanban workflow.
2. PO/researcher availability is a dependency for Phase 4+ execution.
3. Gate task bodies must include clear review criteria and artifact references.
4. Human-gate operational compliance is an unresolved risk (see P1-M02).

## Related Kanban Tasks

| Task | Role |
|---|---|
| t_9eb5e9d0 | Plan PATCH-04: human-gate dependency wording |
| t_1f9cdf54 | Plan PATCH-05: history/ layer |

## Related Artifacts

- Implementation plan v1.0, §Human Gates
- P1-M02 milestone (H1–H4 gates)

## Supersedes

None.

## Superseded By

None.
