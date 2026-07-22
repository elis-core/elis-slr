## Scope

This PR ports the validated ELIS SLR Phase 1 baseline from the ELIS Core monorepo into the standalone `elis-core/elis-slr` repository.

### Commits (3)

1. **`3c48f83`** — Phase 1 canonical baseline: 7 ported protocol/docs files + 3 new (README, LICENSE placeholder, .gitignore)
2. **`f573fc7`** — Phase 1 remediation: strip OpenClaw references from `docs/slr/SLR_DOMAIN_SPEC.md`
3. **`19264df`** — Phase 1 remediation P6: Replace PE-OC-05 with "ELIS SLR" in `docs/slr/SLR_DOMAIN_SPEC.md` line 66

### Files changed (10)

| File | Change |
|---|---|
| `.gitignore` | Stripped OpenClaw-specific ignore rules |
| `LICENSE` | Stripped OpenClaw-specific license text |
| `README.md` | Updated for ELIS SLR standalone repo |
| `docs/_active/ELIS_2025_SLR_AMENDMENT_LOG_TEMPLATE.md` | New — amendment log template |
| `docs/_active/ELIS_2025_SLR_Protocol_Electoral_Integrity_Strategies_2026-01-28_v2.0_draft-08.1.pdf` | New — protocol PDF (1.1 MB) |
| `docs/_active/ELIS_2025_SLR_README_TEMPLATE.md` | New — README template |
| `docs/_active/ELIS_2025_SLR_REPO_SPEC.md` | New — repo specification |
| `docs/_active/ELIS_2025_SLR_RUN_AUDIT_CHECKLIST_TEMPLATE.md` | New — audit checklist template |
| `docs/architecture/ELIS-CORE-SLR-ARCHITECTURE-CHARTER-AND-ROUTING.md` | New — architecture charter |
| `docs/slr/SLR_DOMAIN_SPEC.md` | New — SLR domain specification |

### Out of scope

- Unrelated merged PR #1 (`docs/pe-ops-docs-publication-01-elis-slr`) is not part of this PR.
- This is Phase 1 baseline porting only — no new features, no runtime changes.

### Validation

- All commits validated by Advisor review cycle (t_7dfd75b8, t_2caf0729)
- Push dry-run confirmed successful
- No remote mutation occurred during recovery diagnostic (t_59812a88)
