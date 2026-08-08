# P1-DEC-011 — Phase 4 Bounded Pilot Requires Separate PO GO

| Field | Value |
|---|---|
| **Decision ID** | P1-DEC-011 |
| **Date** | 2026-08-06 |
| **Status** | Current |

## Context

The original implementation plan used the term "scale-up" to describe Phase 4, implying it was a linear continuation of Phase 3. Advisor review flagged this as misleading: Phase 4 involves real data, operative AI coding, and production evidence register entries — a fundamentally different risk profile from Phase 3's synthetic validation.

## Decision

Phase 4 is defined as a **Bounded Real Pilot** — NOT a scale-up from Phase 3:

1. **Bounded scope**: Limited artifact set, limited proposition set, defined time window.
2. **Real data**: Real electoral data from TSE, CÂMARA, SENADO, FORNECEDOR sources.
3. **Operative outputs**: PESC codes produced in Phase 4 are durable and enter the evidence register.
4. **Gate requirements**: Phase 4 requires ALL of:
   - All 9 blocker canaries passing (see P1-M02).
   - Advisor Phase 4 readiness validation.
   - Separate, explicit PO GO decision.
5. **Phase 5 (Full Execution)** similarly gated: requires successful Phase 4 pilot + separate PO GO.

Phase 4/5 are NOT authorised by the Phase 0–3 PO decision (P1-M02).

## Rationale

- "Scale-up" implies continuity; Phase 4 is a deliberate transition from test to production.
- Real data and operative coding carry risks (data quality, coding accuracy, interpretation validity) that Phase 3 cannot assess.
- A separate PO GO ensures governance visibility before production data is touched.
- Bounded scope limits blast radius if Phase 4 reveals methodological issues.

## Consequences

1. Phase 4 cannot begin until all 9 canaries pass and separate PO GO is obtained.
2. Phase 4 uses a limited artifact/proposition set — not the full corpus.
3. Phase 4 outputs are durable and enter the evidence register.
4. Phase 5 requires its own readiness assessment and PO GO.

## Related Kanban Tasks

| Task | Role |
|---|---|
| t_d33788fa | Plan PATCH-01: Phase 4 wording |
| t_1f9cdf54 | Plan PATCH-05: history/ layer |

## Related Artifacts

- Implementation plan v1.0, §Phase 4
- P1-M02 milestone (Phase 4/5 NOT authorised)

## Supersedes

None.

## Superseded By

None.
