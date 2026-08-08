# P1-DEC-002 — Simplified Paper 1 Methodology (v0.6 → v0.6.1)

| Field | Value |
|---|---|
| **Decision ID** | P1-DEC-002 |
| **Date** | 2026-07-31 |
| **Status** | Current |

## Context

Methodology v0.6 was reviewed by Claude and Gemini (see review records). Both identified method complexity as the primary risk — greater than lane independence concerns. The original PESC schema was expansive and the derivation rules for proposition-level evidence value (V) were complex and difficult to validate.

## Decision

Paper 1 methodology is simplified from v0.6 to v0.6.1 with the following changes:

1. **PESC reduction**: Scope reduced to four fields — TYPE, PUB, DUR, AUT. Removed: SOURCE_TYPE, ACCESS, SCOPE, and other non-core fields.
2. **Deterministic V derivation**: V values (HIGH, MEDIUM, LOW, INCONCLUSIVE) derived via deterministic rules from PESC fields, not via AI judgement.
3. **Proposition-level aggregation**: PESC values aggregate at the proposition level, not at the artifact level. Eliminates second-pass artifact-to-proposition synthesis.
4. **V0 and Indeterminate rules**: Handled as schema constraints, not as separate AI coding passes.
5. **Comparator simplification**: Reduced from multi-axis to single-axis comparator.
6. **DUR/AUT separation**: Duration (DUR) and Authority (AUT) treated as independent PESC dimensions.
7. **TEST_STATEMENT requirements**: Test statements must be self-contained propositions testable against public data.

## Rationale

- Complexity was the #1 risk identified by both Claude and Gemini independent reviews.
- Deterministic rules reduce AI coding variance and improve reproducibility.
- Proposition-level aggregation eliminates a known error-prone synthesis step.
- Fewer PESC fields reduce coding burden without losing analytical power for Paper 1's research questions.

## Consequences

1. Method v0.6.1 supersedes v0.6 for all Paper 1 execution.
2. JSON schemas must reflect the reduced PESC field set (TYPE, PUB, DUR, AUT).
3. AI coding instructions reference v0.6.1 derivation rules, not v0.6.
4. Claude and Gemini reviews of v0.6 are retained as historical context but do not apply to v0.6.1.

## Related Kanban Tasks

| Task | Role |
|---|---|
| t_6bbf621a | Plan PATCH-03: JSONL→JSON, ID pattern |
| t_1f9cdf54 | Plan PATCH-05: history/ layer |

## Related Artifacts

- Method v0.6.1 (`ELIS_Paper_1_00_Draft_v0_6_1.md`)
- Implementation plan v1.0, §Method

## Supersedes

None.

## Superseded By

None.
