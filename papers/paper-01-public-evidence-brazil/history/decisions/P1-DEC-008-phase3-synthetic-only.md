# P1-DEC-008 — Phase 3 Synthetic / Non-Operative Only

| Field | Value |
|---|---|
| **Decision ID** | P1-DEC-008 |
| **Date** | 2026-08-04 |
| **Status** | Current |

## Context

Phase 3 of the implementation plan was initially described as a "canary pilot" without clear boundaries on what data and operations were permitted. Advisor review flagged this ambiguity: could Phase 3 accidentally process real electoral data or produce operative PESC codes? The boundary needed to be explicit.

## Decision

Phase 3 is **synthetic and non-operative only**:

1. **No real electoral data**: All test data in Phase 3 is synthetic — generated test fixtures, not real TSE/CÂMARA/SENADO/FORNECEDOR data.
2. **No operative AI PESC coding**: AI models may be invoked to validate infrastructure (response format, schema compliance, latency), but outputs are discarded — no PESC codes from Phase 3 enter the evidence register.
3. **Infrastructure validation only**: Phase 3 validates that profiles can execute, schemas validate, sealed directories work, Kanban gates trigger, and logs are produced correctly.
4. **Boundary marker**: The transition from Phase 3 to Phase 4 is a hard gate. Phase 4 (Bounded Real Pilot) uses real data and produces operative PESC codes — but only after all 9 canaries pass and separate PO GO is obtained.

## Rationale

- Prevents accidental contamination of the evidence register with synthetic/test data.
- Ensures Phase 3 validates infrastructure without prematurely committing to analytic outputs.
- Provides a clear, auditable boundary between test and production.

## Consequences

1. Phase 3 synthetic data fixtures must be clearly marked and segregated from real data.
2. Evidence register is empty until Phase 4 GO.
3. Canary validation results are recorded but do not produce durable evidence artifacts.
4. Phase 4 readiness assessment includes verification that Phase 3 outputs were correctly discarded.

## Related Kanban Tasks

| Task | Role |
|---|---|
| t_d33788fa | Plan PATCH-01: Phase 4 wording |
| t_232d47dc | Advisor final validation |

## Related Artifacts

- Implementation plan v1.0, §Phase 3
- P1-M02 milestone (Phase 3 boundaries)

## Supersedes

None.

## Superseded By

None.
