# P1-DEC-007 — Canonical Repository Namespace

| Field | Value |
|---|---|
| **Decision ID** | P1-DEC-007 |
| **Date** | 2026-08-03 |
| **Status** | Current |

## Context

Paper 1 artifacts need a canonical location within the ELIS repository structure. The elis-slr repository (`elis-core/elis-slr`) hosts multiple papers; Paper 1 needed a stable, unambiguous namespace that separates its artifacts from other papers and from the SLR tooling code.

## Decision

Paper 1's canonical namespace is:

```
papers/paper-01-public-evidence-brazil/
```

within the `elis-core/elis-slr` repository (GitHub: `github.com/elis-core/elis-slr`).

The internal structure separates concerns:

| Path | Purpose |
|---|---|
| `evidence/` | P1-ART evidence discovery, packets, screening, candidates |
| `literature/` | P1-LIT literature discovery, screening, extraction |
| `runs/` | P1-ART and P1-LIT run outputs |
| `history/` | Project governance history |
| `manuscript/` | Manuscript drafts and supplementary materials |
| `reproducibility/` | Environment, hashes, prompts, manifests |
| `method/` | Method documentation and JSON schemas |
| `analysis/` | Sensitivity, institutional, derivation, profile analyses |
| `results/` | Tables and figures |
| `coding/` | PESC codes, adjudication, recode |
| `archive/` | Superseded artifacts |
| `reviews/` | Methodology and AI review records |

## Rationale

- `paper-01-public-evidence-brazil` is descriptive and unique within the elis-slr namespace.
- Evidence/literature split mirrors the P1-ART/P1-LIT governance split (P1-DEC-001).
- `runs/` uses P1-ART and P1-LIT subdirectories for track-level run isolation.
- Consistent with elis-core product-agnostic naming conventions (no agent names in directory paths).

## Consequences

1. All Paper 1 paths in implementation plan, schemas, and agent instructions use this namespace.
2. GitHub path references are stable for the lifetime of Paper 1.
3. Track-specific sealed trees are at `evidence/discovery/_sealed/` and `literature/discovery/_sealed/`.

## Related Kanban Tasks

| Task | Role |
|---|---|
| t_9eb5e9d0 | Plan PATCH-04: track-specific sealed paths |
| t_1f9cdf54 | Plan PATCH-05: history/ layer |

## Related Artifacts

- Implementation plan v1.0, §Repository Layout
- elis-core/elis-slr repository structure

## Supersedes

None.

## Superseded By

None.
