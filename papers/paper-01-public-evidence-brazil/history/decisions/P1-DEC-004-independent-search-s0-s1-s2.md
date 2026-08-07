# P1-DEC-004 — Independent S0/S1/S2 Search Architecture

| Field | Value |
|---|---|
| **Decision ID** | P1-DEC-004 |
| **Date** | 2026-08-01 |
| **Status** | Current |

## Context

Paper 1 requires discovery of public evidence artifacts across three independent lanes to ensure coverage diversity and prevent single-model bias. The lanes must operate independently — outputs from one lane must not influence another lane's search or selection.

## Decision

Three independent discovery lanes are established:

| Lane | Model | Role | Profile |
|---|---|---|---|
| S0 | Deterministic | Systematic search (structured queries, fixed sources) | elis-slr pipeline |
| S1 | moonshotai/kimi-k2.6 | AI-assisted discovery | Dedicated SLR profile |
| S2 | deepseek/deepseek-v4-pro | Independent AI discovery | elis-supervisor |

Lane independence is enforced via:

1. **Sealed output directories**: Each lane writes to its own sealed directory (`evidence/discovery/s0-systematic/`, `evidence/discovery/s1-kimi/`, `evidence/discovery/s2-deepseek/`).
2. **Completion attestation**: Each lane produces a completion manifest before its outputs are unioned.
3. **No cross-lane communication**: Agents in different lanes do not share search strategies, intermediate results, or selection decisions.
4. **Union is the first cross-lane operation**: Results from all three lanes are combined only in the union step, after all lanes have completed and attested.
5. **Track-specific sealed trees**: `evidence/discovery/_sealed/` and `literature/discovery/_sealed/` are separate.

## Rationale

- Independent lanes prevent single-model echo-chamber effects in discovery.
- Sealed directories provide file-system-level enforcement of independence.
- Completion attestation creates auditable proof that no lane was influenced by another's output.
- Three lanes (systematic + two AI) provide methodological triangulation.

## Consequences

1. Three discovery subdirectories under both `evidence/discovery/` and `literature/discovery/`.
2. Each lane's outputs are sealed until all three complete.
3. Lane-specific search-log formats may differ (S0: structured queries; S1/S2: AI prompts + results).
4. Union step must verify all three completion attestations before proceeding.
5. The S2 lane (elis-supervisor) has a 5-point boundary restricting its role (see P1-DEC-005).

## Related Kanban Tasks

| Task | Role |
|---|---|
| t_9eb5e9d0 | Plan PATCH-04: track-specific sealed paths |
| t_1f9cdf54 | Plan PATCH-05: history/ layer |

## Related Artifacts

- Implementation plan v1.0, §Discovery Architecture
- Sealed directory manifests

## Supersedes

None.

## Superseded By

None.
