# Paper 1 Timeline

Concise chronological history of material Paper 1 events — methodology, architecture, validation, authorisation. Cross-references decisions, reviews, and milestones. Not conversation logs.

---

## 2026-07-28

- **Method v0.6 drafted.** Initial Paper 1 methodology with multi-dimensional PESC coding and two-pass artifact-to-proposition synthesis.
  - See: change-log.md (method v0.6)

## 2026-07-30

- **Claude reviews method v0.6.** Identifies method complexity as primary risk — greater than lane independence. Recommends PESC reduction, deterministic V derivation, proposition-level aggregation, comparator simplification.
  - See: reviews/claude-v0.6-review.md

- **Gemini reviews method v0.6.** Concurs with Claude on complexity risk. Adds sealed-directory enforcement for lane independence, S0 deterministic baseline, and Phase 3 synthetic-only scoping.
  - See: reviews/gemini-v0.6-review.md

## 2026-07-31

- **Claude/Gemini reviews reconciled.** Convergent findings — no contradictions. All 11 recommendations adopted.
  - See: reviews/claude-gemini-reconciliation.md
  - Decisions: P1-DEC-001 (governance separation), P1-DEC-002 (method simplification)

- **Method v0.6.1 adopted.** PESC reduced to TYPE/PUB/DUR/AUT, deterministic V derivation, proposition-level aggregation.
  - See: change-log.md (method v0.6.1)

## 2026-08-01

- **S0/S1/S2 discovery architecture adopted.** Three independent lanes: S0 (deterministic systematic), S1 (Kimi k2.6), S2 (DeepSeek v4-pro via elis-supervisor).
  - See: P1-DEC-004 (independent search architecture)

- **Proposition-level aggregation adopted.** Single-pass PESC coding at the proposition level eliminates artifact-to-proposition synthesis step.
  - See: P1-DEC-003 (proposition-level aggregation)

## 2026-08-02

- **S2 lane assigned to existing elis-supervisor profile.** No new profile created. 5-point critical role boundary defined.
  - See: P1-DEC-005 (supervisor as S2)

## 2026-08-03

- **JSON canonical format adopted.** All structured data uses JSON (single document), not JSONL. Artifact ID pattern P1-A-<NNN>.
  - See: P1-DEC-006 (JSON canonical format)

- **Paper 1 repository namespace established.** Canonical path: `papers/paper-01-public-evidence-brazil/` within `elis-core/elis-slr`.
  - See: P1-DEC-007 (repository namespace)

## 2026-08-04

- **Phase 3 scoped as synthetic/non-operative only.** No real electoral data in Phase 3. Real data begins Phase 4 with separate PO GO.
  - See: P1-DEC-008 (Phase 3 synthetic-only)

- **8-schema manifest with consolidated canary adopted.** Reduced from 12 schemas; single consolidated P1 JSON Schema Validation Canary.
  - See: P1-DEC-009 (8-schema manifest)

- **Advisor correction cycle begins.** First PARTIAL verdict. Patch cycle starts.
  - See: reviews/advisor-validation-correction-cycle.md

## 2026-08-05

- **H1–H4 human gates defined.** Structural checkpoints at artifact admission (H1), Evidence Packet Validation (H2), PESC Coding Review (H3), final manuscript (H4).
  - See: P1-DEC-010 (human gates H1–H4)

- **Phase 4 scoped as bounded pilot.** Limited artifact scope, real data for the first time, all 9 canaries as gate condition.
  - See: P1-DEC-011 (Phase 4 bounded pilot)

## 2026-08-07

- **Advisor final validation PASS.** All 6 correction cycles complete. Verdict: PASS_FOR_PO_DECISION.
  - See: reviews/2026-08-07-advisor-final-execution-plan-validation.md
  - See: reviews/advisor-validation-correction-cycle.md

- **PO authorises Phases 0–3.** Phase 4/5 NOT authorised. 9 blocker canaries gate Phase 4. H1–H4 structural gates active. S1/S2 independence boundary enforced.
  - See: milestones/P1-M02-execution-plan-approved.md

- **Implementation plan v1.0 finalised.** Five patch revisions applied (PATCH-01 through PATCH-05). Project history layer bootstrapped.
  - See: milestones/P1-M02-execution-plan-approved.md
