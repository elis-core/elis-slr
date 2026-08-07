# P1-DEC-003 — Proposition-Level PESC Aggregation

| Field | Value |
|---|---|
| **Decision ID** | P1-DEC-003 |
| **Date** | 2026-08-01 |
| **Status** | Current |

## Context

The original methodology (v0.6) envisioned two-pass processing: first, PESC-code each artifact individually; second, synthesise artifact-level codes into proposition-level evidence values. This two-pass approach introduces a known failure mode: second-pass AI synthesis can introduce hallucination, inconsistency, and loss of traceability from artifact to proposition.

## Decision

PESC aggregation is performed directly at the proposition level in a single pass:

1. Each **proposition** (test statement) is the unit of analysis.
2. All relevant artifacts are evaluated against the proposition simultaneously.
3. V derivation operates on the proposition's artifact set as a whole — not per-artifact then synthesised.
4. Traceability is maintained from proposition → artifact set, recorded in the evidence packet JSON.

This eliminates the artifact-to-proposition synthesis pass entirely.

## Rationale

- Single-pass processing eliminates a known AI hallucination vector.
- Traceability from proposition to artifact set is direct and auditable.
- Reduces total AI coding operations by approximately 40% (eliminates synthesis pass).
- Consistent with the deterministic V derivation rules adopted in P1-DEC-002.

## Consequences

1. Evidence packet JSON schema must support proposition-level aggregation (artifact array per proposition).
2. PESC coding instructions must specify per-proposition evaluation, not per-artifact.
3. Second-pass synthesis is removed from the P1-ART workflow.
4. Coding quality checks validate proposition-level consistency, not artifact-level consistency.

## Related Kanban Tasks

| Task | Role |
|---|---|
| t_d33788fa | Plan PATCH-01: schema manifest, 9th canary |
| t_1f9cdf54 | Plan PATCH-05: history/ layer |

## Related Artifacts

- Method v0.6.1, §Proposition-Level Aggregation
- Implementation plan v1.0, §P1-ART workflow
- evidence-packet.schema.json

## Supersedes

None.

## Superseded By

None.
