# P1-DEC-006 — JSON Canonical Format for Structured Data

| Field | Value |
|---|---|
| **Decision ID** | P1-DEC-006 |
| **Date** | 2026-08-03 |
| **Status** | Current |

## Context

The implementation plan originally specified JSONL (JSON Lines) for evidence packets and other structured data. During Advisor review, JSONL was identified as problematic: it complicates validation (each line is a separate JSON document), makes schema enforcement harder, and increases the risk of partial-write corruption.

## Decision

All Paper 1 structured data uses **JSON** (single document), not JSONL:

1. Evidence packets are single JSON documents containing arrays of proposition entries.
2. Search logs are single JSON documents (per lane, per run).
3. Coding outputs are single JSON documents.
4. Artifact IDs use the pattern `P1-A-<NNN>` (e.g., `P1-A-001`), replacing the earlier `ART-P1-<NNN>` pattern.

## Rationale

- Single JSON documents are atomically writable — no partial-write corruption.
- Schema validation operates on the whole document, catching cross-entry inconsistencies.
- Simpler parsing and serialisation in both Python and shell pipelines.
- `P1-A-<NNN>` pattern is shorter, unambiguous, and consistent with P1-DEC-<NNN> and P1-M<NN> naming.

## Consequences

1. All `.jsonl` references in the implementation plan are replaced with `.json`.
2. JSON schemas validate complete documents, not individual lines.
3. Artifact ID pattern `P1-A-<NNN>` replaces `ART-P1-<NNN>`.
4. Evidence packet format: `{propositions: [{id, statement, artifacts: [...], pesc_values: {...}, v: ...}, ...]}`.

## Related Kanban Tasks

| Task | Role |
|---|---|
| t_6bbf621a | Plan PATCH-03: JSONL→JSON, ID pattern |
| t_1f9cdf54 | Plan PATCH-05: history/ layer |

## Related Artifacts

- Implementation plan v1.0, §Data Formats
- evidence-packet.schema.json
- All 8 JSON schemas

## Supersedes

None.

## Superseded By

None.
