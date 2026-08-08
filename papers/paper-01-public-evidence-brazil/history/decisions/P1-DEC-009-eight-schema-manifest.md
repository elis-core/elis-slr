# P1-DEC-009 — 8-Schema Manifest with Consolidated Canary

| Field | Value |
|---|---|
| **Decision ID** | P1-DEC-009 |
| **Date** | 2026-08-04 |
| **Status** | Current |

## Context

The initial implementation plan specified 12 JSON schemas, each with its own validation canary — 12 individual canaries. Advisor review identified this as excessive: 12 canaries create maintenance burden, increase false-positive risk, and dilute attention from genuinely critical validations.

## Decision

The schema manifest is reduced from 12 to 8 JSON schemas:

| # | Schema | Validates |
|---|---|---|
| 1 | `artifact.schema.json` | Artifact metadata and source attribution |
| 2 | `search-log.schema.json` | Discovery search log entries |
| 3 | `screening-decision.schema.json` | Include/exclude decisions with rationale |
| 4 | `evidence-packet.schema.json` | Proposition-level evidence packets |
| 5 | `pesc-code.schema.json` | PESC coding records (TYPE, PUB, DUR, AUT) |
| 6 | `proposition.schema.json` | Test statement propositions |
| 7 | `run-manifest.schema.json` | Run-level output manifest |
| 8 | `adjudication.schema.json` | Coding adjudication records |

The 12 individual schema canaries are replaced by a **single consolidated JSON Schema Validation Canary** (canary #6) that validates all 8 schemas in one pass.

A **9th canary** (S0 completeness/sufficiency) is added, bringing the total blocker canary count to 9.

## Rationale

- ı2 individual canaries were redundant — schema validation is a single concern.
- Consolidated canary reduces maintenance and false-positive noise.
- 8 schemas cover all required data types without gaps.
- 9 total canaries maintain the required gate density for Phase 4.

## Consequences

1. Schema validation is pass/fail for all 8 schemas — partial pass is not a valid state.
2. Canary #6 (consolidated schema) replaces ı2 former individual canaries.
3. The 9 blocker canaries are: profile, isolation, manifest, union, human-gate, schema, no-operative-AI, traceability, S0 completeness/sufficiency.

## Related Kanban Tasks

| Task | Role |
|---|---|
| t_a76c4822 | Plan PATCH-02: 12→8 schemas |
| t_d33788fa | Plan PATCH-01: 9th canary |
| t_1f9cdf54 | Plan PATCH-05: history/ layer |

## Related Artifacts

- Implementation plan v1.0, §JSON Schema Manifest
- All 8 schema files (`method/schemas/`)
- P1-M02 milestone (9 canary status)

## Supersedes

None.

## Superseded By

None.
