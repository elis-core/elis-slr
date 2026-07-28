# ELIS 2025 SLR

Systematic Literature Review repository for **Electoral Integrity Strategies (ELIS 2025)**.

**Repo:** [github.com/elis-core/elis-slr](https://github.com/elis-core/elis-slr)

## Repository map

- `docs/_active/` — Canonical protocol source and support templates
  - `ELIS_2025_SLR_Protocol_*_v2.0_draft-08.1.pdf` — Protocol source document
  - `ELIS_2025_SLR_AMENDMENT_LOG_TEMPLATE.md` — Amendment log template
  - `ELIS_2025_SLR_README_TEMPLATE.md` — Full README template (protocol-level detail)
  - `ELIS_2025_SLR_RUN_AUDIT_CHECKLIST_TEMPLATE.md` — Run audit checklist template
  - `ELIS_2025_SLR_REPO_SPEC.md` — Repository specification
- `docs/slr/` — Domain specification
  - `SLR_DOMAIN_SPEC.md` — SLR domain specification
- `docs/architecture/` — Architecture reference
  - `ELIS-CORE-SLR-ARCHITECTURE-CHARTER-AND-ROUTING.md` — Architecture charter (canonical authority in shared governance)

## Governance

This is a **Phase 1 canonical baseline** of the SLR protocol and supporting documentation.
- Public/private posture: under PO review
- Licence: deferred pending PO decision
- No direct pushes to `main` without PO approval
- Architecture charter canonical authority resides in shared governance at `~/.hermes/profiles/_shared/architecture/`

## Status

**M1 (Package & CLI) — COMPLETE** (2026-07-28)
The `elis-slr` package is now installable from source:
- `pip install -e ".[dev]"` — installs the package with dev dependencies
- `elis-slr --help` — shows CLI help
- `python -m elis_slr --help` — module execution
- `pytest` — runs smoke tests (M1 scope)

See `MIGRATION.md` for full migration status and future phases.

Phase 1 canonical baseline staged 2026-07-14. No remote push, no CI/CD, no CLI/migration in this phase.
See `docs/_active/ELIS_2025_SLR_README_TEMPLATE.md` for the full population-ready template.