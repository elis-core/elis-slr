# P1-DEC-001 — Paper 1 Not Governed by ELIS SLR Protocol

| Field | Value |
|---|---|
| **Decision ID** | P1-DEC-001 |
| **Date** | 2026-07-31 |
| **Status** | Current |

## Context

The ELIS platform hosts an SLR capability (`elis-slr`) governed by the ELIS SLR Protocol and PRISMA guidelines. Paper 1 ("Public Evidence in Brazil") was initially positioned under this protocol. However, Paper 1's methodology diverges significantly from standard SLR — it employs proposition-level PESC coding, three-lane independent discovery (S0/S1/S2), and synthetic pilot validation. The question arose: should Paper 1 be governed by the SLR protocol, or should it be governed solely by its own validated methodology?

## Decision

Paper 1 is NOT governed by the ELIS SLR Protocol or PRISMA. Two governance domains are established:

- **P1-LIT** (literature discovery, screening, extraction): governed by the ELIS SLR Protocol — standard SLR pipeline.
- **P1-ART** (artifact evidence discovery, PESC coding, analysis): governed exclusively by Paper 1's own validated methodology.

This Decision applies to the ELIS SLR Agent Adaptation implementation plan v1.0 and all subsequent Paper 1 execution.

## Rationale

- Paper 1's PESC methodology is a novel proposition-level coding system not covered by PRISMA.
- Three-lane independent discovery with sealed outputs has no SLR protocol analogue.
- Synthetic pilot validation (Phase 3) is outside SLR scope.
- Clarifying the governance boundary prevents methodological conflation and ensures each domain is validated against its correct standard.

## Consequences

1. P1-LIT workflow must comply with the ELIS SLR Protocol (standard search, screening, extraction).
2. P1-ART workflow is validated solely against Paper 1 methodology v0.6.1.
3. Implementation plan must clearly demarcate P1-LIT and P1-ART sections.
4. Advisor validation checks methodology compliance within each domain independently.
5. Repository structure reflects the split: `papers/paper-01-public-evidence-brazil/evidence/` (P1-ART) and `papers/paper-01-public-evidence-brazil/literature/` (P1-LIT).

## Related Kanban Tasks

| Task | Role |
|---|---|
| t_1f9cdf54 | Plan PATCH-05: history/ layer bootstrapping |
| t_9eb5e9d0 | Plan PATCH-04: track-specific sealed paths |

## Related Artifacts

- Implementation plan v1.0, §P1-LIT/P1-ART governance domains
- Method v0.6.1

## Supersedes

None.

## Superseded By

None.
