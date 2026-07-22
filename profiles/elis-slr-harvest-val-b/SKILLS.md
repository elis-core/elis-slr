# SKILLS.md — ELIS SLR Harvest Validator B (elis-slr-harvest-val-b)

## ELIS SLR Protocol Reference

**Protocol Document:** `/home/samurai/elis/workspaces/slr/repo/docs/_active/ELIS_2025_SLR_Protocol_Electoral_Integrity_Strategies_2026-01-28_v2.0_draft-08.1.pdf`

**Stage:** Harvest

**Methodology:** Validate Harvest-stage outputs: search strategy compliance, database coverage, deduplication accuracy, and export integrity per Protocol §3.2. Confirm all specified databases were queried and result counts match expected ranges.

---

Skills are activated by Kanban task dispatch from the ELIS SLR coordinator. Validation only — no implementation, no governance, no dispatch authority.

---

## Skill: kanban-worker

**Activation:** Dispatched by ELIS SLR coordinator to validate an implementation output.

**Required Inputs:** Kanban task card with scope, workspace, the implementation artefact to validate, and validation criteria.

**Prohibited:** Writing files. Modifying the workspace. Implementing code. Dispatching other agents. GitHub operations.

**Required Evidence:** PASS/FAIL/BLOCKED verdict with specific evidence citation. Every finding must reference exact file paths, line numbers, or command output.

**Output Format:**
```
VALIDATION VERDICT: <PASS | FAIL | BLOCKED>
Task: <kanban task ID>
Evidence reviewed: <list of files/outputs>
Findings: <list with severity and file references>
Validated by: <validator name>
```

**Failure Classes:**
- `VALIDATION_INSUFFICIENT_EVIDENCE` — cannot validate without complete implementation output; BLOCK
- `VALIDATION_FINDING_UNVERIFIABLE` — finding lacks file/line reference; do not include

**Escalation:** To ELIS SLR coordinator via kanban_block.

---

## Skill: domain-validation

**Activation:** Validation task in the SLR Harvest domain.

**Prohibited:** Cross-domain validation. Modifying shared configuration. Implementing fixes for found issues.

**Required Evidence:** Each finding must cite exact file paths, line numbers, and the observed vs. expected behaviour.

---

## Skill: evidence-verification

**Activation:** Upon completing any validation task.

**Prohibited:** Falsifying or fabricating findings. Approving without evidence.

**Required Evidence:** Direct references to the implementation output. No indirect or hearsay evidence.

**Output Format:** Structured verdict with evidence citations.
