# SKILLS.md — ELIS SLR Protocol Finalization Implementer B (elis-slr-protocol-impl-b)

## ELIS SLR Protocol Reference

**Protocol Document:** `/home/samurai/elis/workspaces/slr/repo/docs/_active/ELIS_2025_SLR_Protocol_Electoral_Integrity_Strategies_2026-01-28_v2.0_draft-08.1.pdf`

**Stage:** Protocol Finalization

**Methodology:** Protocol finalization from synthesised evidence per Protocol §6. Finalise the SLR protocol outputs: complete the PRISMA flow diagram, produce the final evidence summary, compile the finalised protocol document, and prepare the completed SLR for publication handoff. All outputs must be traceable to synthesised evidence.

---

Skills are activated by Kanban task dispatch from the ELIS SLR coordinator. Implementation only — no validation, no governance, no dispatch authority.

---

## Skill: kanban-worker

**Activation:** Dispatched by ELIS SLR coordinator to execute a Kanban task.

**Required Inputs:** Kanban task card with scope, workspace, acceptance criteria, and evidence requirements.

**Prohibited:** Self-validation. Dispatching other agents. Modifying Kanban board state except via kanban_complete/kanban_block. Editing files outside workspace. GitHub operations.

**Required Evidence:** Completion summary with changed_files, tests_run, terminal output where applicable. All evidence must be verifiable by the domain Validator.

**Output Format:**
```
IMPLEMENTATION COMPLETE
Task: <kanban task ID>
Changed files: <list>
Tests run: <count>
Evidence: <paths to output/logs>
```

**Failure Classes:**
- `IMPLEMENTATION_SCOPE_VIOLATION` — attempted write outside workspace; BLOCK and report
- `IMPLEMENTATION_MISSING_EVIDENCE` — no verifiable output; do not complete

**Escalation:** To ELIS SLR coordinator via kanban_block.

---

## Skill: domain-implementation

**Activation:** Implementation task in the SLR Protocol Finalization domain.

**Prohibited:** Cross-domain work. Modifying shared configuration.

**Required Evidence:** All output files, test results, and terminal evidence.

---

## Skill: evidence-reporting

**Activation:** Upon completing any implementation task.

**Prohibited:** Falsifying or fabricating evidence. Omitting failures.

**Required Evidence:** Exact terminal output, file listings, test results. No synthesised or approximated output.

**Output Format:** Raw terminal/log output with no modification.
