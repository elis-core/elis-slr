# Pre-H1 Advisor Review — Provenance & Verification Record

| Field | Value |
|---|---|
| **Review ID** | REVIEW-PRE-H1-PROVENANCE |
| **Date** | 2026-08-08 |
| **Final PRE-H1 Advisor task** | t_431b5219 |
| **Verdict** | READY_FOR_H1 |
| **Verdict type** | ADVISOR_REVIEW_WAS_PATH_BOUND_NOT_HASH_BOUND |

## Context

The PRE-H1 Advisor review (t_431b5219) evaluated the Paper 1 Proposition Register, supporting schemas, and H1 review package against the methodology v0.6.1 and implementation plan v1.0. The review was performed using path-bound verification — file existence and structural completeness were assessed by file path, not by content hash.

The review returned `READY_FOR_H1`, confirming that all required artifacts were present and structurally valid.

## Subsequent Host-Level SHA256 Verification

Following the path-bound review, host-level SHA256 verification was established to pin content integrity for the H1 gate and all downstream tasks. These hashes are the canonical reference for artifact integrity:

| Artifact | SHA256 |
|---|---|
| `proposition-register.json` | cf56b2a4e125486994ad4808c759cc894655659580a6cc7ecfa20def9c214c23 |
| `proposition-register.schema.json` | 796104aca4700b45507c0dab7231167afe9c7355b43d8c45f8c48481de549f9b |
| `H1_REVIEW_PACKAGE.md` | 4acce649529fc30989c23966d5e0ea0fda3cd0ec1e201d0f572dabfd3f75140e |

## Post-Review H1 Package Correction

`ADVISOR_REVIEWED_H1_ATTACHMENT_SHA256` = `4acce649529fc30989c23966d5e0ea0fda3cd0ec1e201d0f572dabfd3f75140e`
(the `H1_REVIEW_PACKAGE.md` hash in the table above — the exact attachment `t_431b5219` reviewed)

`CANONICAL_H1_REVIEW_PACKAGE_SHA256` = `8ba4fb0c3eb0f9798d6c88e43aa8506329c82354ad6d34fdc0272788e77c485d`
(the `H1_REVIEW_PACKAGE.md` content committed to this repository — **not** the artifact `t_431b5219` reviewed; see change description below)

`POST_REVIEW_H1_PACKAGE_CHANGE`:
The canonical repository H1 review package differs from the Advisor-reviewed attachment only by two wording corrections:
1. "10 of 11-12 decision records" → "10 of 11 durable decision records"
2. "10/11-12 decisions referenced" → "10/11 durable decisions referenced"

No proposition text, TEST_STATEMENT, applicability mapping, essential-step mapping, scientific criterion, or H1 decision content changed. `t_431b5219`'s verdict (`READY_FOR_H1`) reviewed the Advisor-reviewed attachment above, path-bound per `ADVISOR_REVIEW_WAS_PATH_BOUND_NOT_HASH_BOUND`; it did not review the canonical repository package's post-correction byte content.

## Verification Notes

- The PRE-H1 Advisor (t_431b5219) did NOT itself record these SHA256 hashes — the host-level verification was established subsequently as an additional integrity safeguard for the H1 gate.
- Path-bound review was sufficient for the PRE-H1 verdict because the artifacts were structurally validated against schemas and content-checked for completeness.
- Hash-bound verification is the standard for H1 gate onward, ensuring that downstream tasks reference exactly the same byte-level content that was reviewed.

## Related Tasks

| Task | Role |
|---|---|
| t_431b5219 | PRE-H1 Advisor review (verdict: READY_FOR_H1) |
| t_6c89d092 | Canonical Paper 1 local repository preparation (this task) |