# MIGRATION STATUS

## Overview

This document tracks the migration of SLR protocol code from
`rochasamurai/ELIS-Multi-AI-Agent-Platform` to `elis-core/elis-slr`.

## Completed Phases

### M1 — Package & CLI (2026-07-28)

**Scope:** Make elis-core/elis-slr installable as a Python package with clean
SLR namespace and working CLI entrypoint.

**Files created:**
- `pyproject.toml` — Package build config, CLI entrypoint `elis-slr = "elis_slr.cli:main"`
- `requirements.txt` — Runtime dependencies (jsonschema, requests, PyYAML)
- `elis_slr/__init__.py` — Package init with version `2.0.0`
- `elis_slr/__main__.py` — `python -m elis_slr` support
- `elis_slr/cli.py` — CLI with `--help` and `--version` subcommands
- `tests/__init__.py` — Test package init
- `tests/test_m1_smoke.py` — Smoke tests (import, CLI, module execution)

**Verification:**
- `pip install -e ".[dev]"` — installs cleanly
- `elis-slr --help` — shows help
- `python -m elis_slr --help` — shows help
- `pytest` — all tests pass

**Reference:**
See `/home/samurai/.hermes/kanban/boards/elis-slr/artifacts/SLR-INDEPENDENT-RUNNABLE-MIGRATION-01-MANIFEST.md`
for the full migration manifest and future phase definitions.

## Known issue to fix during pipeline migration (not yet ported)

A 2026-07-30 code review of the pre-migration source
(`rochasamurai/ELIS-Multi-AI-Agent-Platform`'s `elis/pipeline/`, not yet
present in this package) found a silent data-loss bug in the merge stage:

- `elis/pipeline/merge.py:170` hardcodes `_meta.global` to `{}` when building
  the canonical Appendix A file, discarding the year-range/language/
  result-cap config that each per-source harvest step correctly populates
  (`elis/pipeline/search.py:488`).
- The next stage, `elis/pipeline/screen.py:269`, silently falls back to
  hardcoded defaults (1990–current, en/fr/es/pt) with no warning when
  `_meta.global` is empty — this would quietly corrupt inclusion/exclusion
  decisions for an entire literature review if it ran against real config
  that differs from those defaults.

As of this note, the merge/screen stages have not yet been ported into
`elis_slr` (M1 only covers packaging/CLI scaffolding), so this hasn't
affected any review run through this package. **When the merge/screen
stages are migrated (a future M-phase), carry the config through instead
of hardcoding `_meta.global`, and add a test asserting the merged output's
`_meta.global` matches the per-source harvest config rather than silently
defaulting.**