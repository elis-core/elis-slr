# SKILLS.md — ELIS SLR

Skills are activated by PO request or SLR pipeline triggers. Kanban tools only. No file/terminal access. No PE board operation.

---

## Skill: kanban-orchestrator

**Activation:** Automatically loaded on every dispatched worker. Provides Kanban lifecycle guidance — orient, work, heartbeat, block, complete — plus pitfalls, retry diagnostics, and handoff shapes.

**Reference:** See `/home/samurai/.hermes/profiles/elis-slr/skills/devops/kanban-orchestrator/SKILL.md` for full orchestration workflow.

**Required Inputs:** Task dispatch context from `elis-slr` board.

**Prohibited:** Worker implementation, worker validation, direct file/terminal access.

**Required Evidence:** `kanban_complete` with structured handoff metadata, `kanban_create` for fan-out decomposition with `idempotency_key` protection.

**Escalation:** To PO for board unavailability or coordinator-level blockers.

---

## Skill: slr-task-decomposition

**Activation:** PO issues an SLR research directive, or a prior pipeline stage completes and the next stage needs tasks.

**Required Inputs:** SLR directive with scope, protocol stage reference, domain (Harvest/Screen/Extract/Synthesise/PRISMA), expected output format.

**Prohibited:** Dispatching PE, programming, or infrastructure agents. Creating tasks on `elis-core` or `elis-a2a-implementation` boards. Decomposing without protocol reference.

**Required Evidence:** Created Kanban task IDs, status summary with counts per state, protocol stage reference.

**Output Format:**
```
SLR PIPELINE: <directive-ref> / Stage: <Harvest|Screen|Extract|Synthesise|PRISMA>
Protocol ref: <ELIS SLR Protocol §X.Y>
Tasks created: T-<id>: <summary> → assigned: <agent>
Board snapshot: triage=N, todo=N, in-progress=N, blocked=N, done=N, archived=N
Next stage: <description> — requires PO or Advisor review
```

**Failure Classes:**
- `SLR_DECOMPOSITION_AMBIGUOUS` — directive scope unclear; request PO clarification
- `SLR_KANBAN_CREATE_FAILED` — board unavailable or permission denied; report to PO
- `SLR_PROTOCOL_REFERENCE_MISSING` — no protocol section cited; block and request PO supplement

**Escalation:** To PO.

---

## Skill: slr-gate-packet-authoring

**Activation:** An SLR pipeline stage completes and evidence is ready for Advisor review before PO.

**Required Inputs:** All evidence from completed SLR stage tasks, agent outputs, and verification results.

**Prohibited:** Claiming stage completion without evidence. Omitting the protocol reference. Routing directly to PO without Advisor review when protocol requires it.

**Required Evidence:** Evidence checklist with provenance for each item. Protocol stage reference. Agent identity and scope.

**Output Format:**
```
SLR GATE PACKET: <directive-ref> / Stage: <name>
Protocol ref: <ELIS SLR Protocol §X.Y>
Evidence:
  [x] item 1 — <provenance>
  [x] item 2 — <provenance>
  [ ] item 3 — MISSING — <gap description>
Classification: <READY_FOR_REVIEW | INCOMPLETE | BLOCKED>
Next: <Advisor review | PO approval | return to agent>
```

**Failure Classes:**
- `SLR_GATE_INCOMPLETE_EVIDENCE` — evidence gaps exist; flag as INCOMPLETE
- `SLR_GATE_SCOPE_DRIFT` — evidence references out-of-scope work; flag and escalate
- `SLR_GATE_PROTOCOL_DEVIATION` — output does not match protocol requirements; BLOCKED

**Escalation:** To PO and ELIS Advisor (via PO).

---

## Skill: slr-pipeline-status

**Activation:** PO requests SLR pipeline status summary.

**Required Inputs:** Board name (`elis-slr`), optional domain filter.

**Prohibited:** Omitting active states. Reporting without timestamp. Including PE board data.

**Required Evidence:** Full `elis-slr` board snapshot with counts per status and task IDs per domain.

**Output Format:**
```
SLR STATUS: elis-slr @ <ISO timestamp>
Harvest: triage=N, todo=N, in-progress=N, blocked=N, done=N
Screen: triage=N, todo=N, in-progress=N, blocked=N, done=N
Extract: triage=N, todo=N, in-progress=N, blocked=N, done=N
Synthesise: triage=N, todo=N, in-progress=N, blocked=N, done=N
PRISMA: triage=N, todo=N, in-progress=N, blocked=N, done=N
Active tasks: <task-id>: <summary> — <status> — <domain>
Blockers: <list of blocked tasks with blocker descriptions>
Next approval required: <Advisor review | PO approval>
```

**Failure Classes:**
- `SLR_STATUS_BOARD_UNAVAILABLE` — Kanban board not accessible; report to PO
- `SLR_STATUS_CROSS_BOARD_LEAK` — PE tasks detected on SLR board; escalate to PO

**Escalation:** To PO.

---

## Skill: slr-protocol-reference

**Activation:** Any SLR task decomposition, gate packet, or pipeline status report.

**Required Inputs:** The specific protocol section relevant to the current activity.

**Prohibited:** Operating without citing the protocol. Approximating protocol requirements from memory.

**Required Evidence:** Exact protocol section reference with document path.

**Output Format:**
```
PROTOCOL: ELIS SLR Protocol v2.0 draft-08.1
Section: <§X.Y — Section name>
Requirement: <quoted or paraphrased requirement from the protocol>
Compliance: <COMPLIANT | PARTIAL | NON_COMPLIANT> — <rationale>
Path: /home/samurai/elis/workspaces/slr/repo/docs/_active/ELIS_2025_SLR_Protocol_Electoral_Integrity_Strategies_2026-01-28_v2.0_draft-08.1.pdf
```

**Failure Classes:**
- `SLR_PROTOCOL_UNAVAILABLE` — protocol document not accessible; block and report to PO
- `SLR_PROTOCOL_DEVIATION_DETECTED` — activity does not match protocol requirement; flag in gate packet

**Escalation:** To PO for protocol interpretation questions. Do not self-interpret.

---

## Skill: slr-handoff-request

**Activation:** An SLR task needs to be handed off from one domain to the next (e.g. Harvest → Screen).

**Required Inputs:** Source domain, target domain, completed task ID, handoff evidence, and protocol stage transition reference.

**Prohibited:** Handing off without PO awareness. Claiming a stage is complete when evidence is missing. Handing off across the Core/SLR boundary without PO approval.

**Required Evidence:** Handoff note with source evidence, target scope, protocol reference, and acceptance criteria.

**Output Format:**
```
SLR HANDOFF: <source-domain> → <target-domain>
Completed task: <task-id>: <summary>
Evidence: <paths or references to completed outputs>
Protocol ref: <§X.Y — stage transition criteria>
Target scope: <bounded description for next stage>
Acceptance criteria: <what the target domain must verify before proceeding>
Approval state: <PO approved | PENDING PO | ADVISOR REVIEW>
```

**Failure Classes:**
- `SLR_HANDOFF_TARGET_UNAVAILABLE` — target domain agents not reachable; escalate to PO
- `SLR_HANDOFF_EVIDENCE_MISSING` — source stage evidence incomplete; do not hand off
- `SLR_HANDOFF_CROSS_BOUNDARY` — attempted handoff to PE/Core agents; BLOCKED

**Escalation:** To PO.

---

## Skill: candidate-lesson-capture

**Activation:** Repeated PO correction, repeated blocker, validation failure, wrong domain/worktree/tool/path incident, successful repeatable workflow, token-heavy or inefficient loop, security or governance near miss, or recurring ambiguity in profile instructions.

**Required Inputs:** The incident or pattern observed.

**Required Evidence:**
- What happened and when
- Which agent/role was involved
- Which rule, skill, workflow, or boundary failed or succeeded
- Exact file/path/PE/task if relevant
- Proposed reusable improvement

**Prohibited:** Editing profile files, editing shared governance, creating hooks, changing config, restarting services, mutating GitHub, treating memory or Obsidian notes as authority, self-authorising durable behavioural changes, implementing candidate lessons.

**Output Format:**
```
CANDIDATE_LESSON
Title: <short title>
Source incident/pattern: <description>
Affected agents: <list>
Proposed skill/rule/check: <description>
Evidence: <paths/messages/commands>
Risk if adopted: <LOW|MEDIUM|HIGH|CRITICAL>
Risk if ignored: <LOW|MEDIUM|HIGH|CRITICAL>
Requires PE: <YES|NO>
Recommended owner: <PO|Advisor|PM|Supervisor|elis-github|future implementer>
Next gate: <PO triage | Advisor review | PE proposal>
```

**Failure Classes:**
- `SELF_MODIFICATION_ATTEMPT_BLOCKED` — do not edit profile files
- `HIDDEN_AUTHORITY_RISK` — do not embed mutation authority
- `UNAPPROVED_SKILL_MUTATION` — do not modify skills without PE
- `MEMORY_AS_AUTHORITY_RISK` — memory is not authority
- `OBSIDIAN_NOTE_NOT_AUTHORITY` — notes do not override governance
- `GOVERNANCE_WEAKENING_RISK` — proposed change must not weaken role boundaries
- `RUNTIME_MUTATION_REQUIRES_PE` — runtime changes require PE
- `GITHUB_MUTATION_REQUIRES_HANDOFF` — GitHub changes require PO-approved handoff to elis-github

**Escalation:** To PO for triage.