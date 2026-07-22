# ELIS Shared Skill — Authoritative Kanban PE Workflow

**File:** `AUTHORITATIVE_KANBAN_PE_WORKFLOW_SKILL.md`
**Purpose:** Shared Kanban governance skill for ELIS PM, ELIS Advisor, and ELIS Supervisor.
**Installed:** 2026-06-24 by ELIS Supervisor under PO authorisation.
**Canonical path:** `/home/samurai/.hermes/profiles/_shared/skills/AUTHORITATIVE_KANBAN_PE_WORKFLOW_SKILL.md`

---

# 1. Shared Skill

## Skill ID

`AUTHORITATIVE_KANBAN_PE_WORKFLOW_SKILL`

## Purpose

Ensure that ELIS Kanban boards are used as authoritative, auditable workflow records for governed PE execution, rather than as informal notes or incomplete task dispatches.

This skill prevents:

- Discord-only operational context;
- under-populated parent PE cards;
- ambiguous implementation tasks;
- premature execution before Advisor/PO gates;
- overwritten failed validation evidence;
- wrong-board task creation;
- loss of proposal/evidence provenance;
- unsafe execution from incomplete task bodies.

## Applies To

- ELIS PM
- ELIS Advisor
- ELIS Supervisor
- ELIS GitHub, where GitHub operations are involved

## Core Rule

A Kanban task is actionable only if its body is self-contained or explicitly cites authoritative stored artefacts within Kanban or repository paths.

Discord messages may notify, summarise, or request action, but Discord-only context is not authoritative for implementation, validation, closeout, or production-readiness decisions.

---

# 2. Board Targeting Rule

Every Kanban call must explicitly specify the intended board.

For A2A production work, use:

```text
board="elis-a2a-implementation"
```

Do not rely on the global current-board pointer.

Do not switch the global current-board pointer away from another active board, such as `elis-slr`, unless PO explicitly approves.

## Failure Classes

- `WRONG_KANBAN_BOARD`
- `IMPLICIT_BOARD_POINTER_USED`
- `GLOBAL_BOARD_POINTER_SIDE_EFFECT`
- `BOARD_TARGETING_MISSING`

---

# 3. Parent PE Control Card Rule

Each PE must have one authoritative parent PE control card.

The parent card must contain, or explicitly reference by stored Kanban comment ID or repository artefact path, the complete current PE control record.

## Minimum Required Parent PE Card Sections

```text
PE identifier:
Objective:
Scope:
Non-scope:
Current baseline:
Blocker inventory:
Role assignments:
Approval-gate table:
Gate plan:
Evidence requirements:
Rollback / recovery plan:
Hard constraints:
Current status:
Child-card index:
Provenance:
```

The parent PE card must be self-contained enough for Advisor review without requiring Discord history, private memory, or unstated assumptions.

If the canonical proposal is too long for the parent task body, it may live in a named parent-card comment, but the parent body must explicitly identify:

```text
Canonical proposal location:
Parent task:
Canonical comment ID:
Supersedes:
Current status:
```

## Forbidden Parent-Card Placeholders

The following are not acceptable substitutes for stored authoritative content:

```text
See Discord
As discussed
Per the thread
TBD
Same as before
Use prior context
As agreed earlier
Refer to chat
```

## Failure Classes

- `PARENT_PE_CARD_INCOMPLETE`
- `DISCORD_ONLY_CONTEXT_USED`
- `CANONICAL_PROPOSAL_NOT_IDENTIFIED`
- `PE_CONTROL_RECORD_NOT_SELF_CONTAINED`
- `PROVENANCE_MISSING`

---

# 4. Child Card Per Gate / Action Rule

Each gate or action must have its own child card.

Do not combine proposal validation, implementation, runtime execution, validation, rollback, and closeout into one ambiguous card.

## Allowed Child Card Types

```text
proposal-readiness
pre-flight
baseline-discovery
implementation-packet
implementation
implementation-evidence
runtime-smoke-test
rollback-evidence
resubmission
certification
closeout
```

## Required Child Card Fields

Every child card must include:

```text
PE:
Gate:
Task:
Owner:
Board:
Parent task:
Card type:
Card state:
Approval basis:
Scope:
Out of scope:
Inputs:
Required actions:
Required evidence:
Expected output:
Stop condition:
Next dependency:
```

## Failure Classes

- `CHILD_CARD_AMBIGUOUS`
- `GATE_TYPE_MISSING`
- `CARD_BODY_INCOMPLETE`
- `STOP_CONDITION_MISSING`
- `NEXT_DEPENDENCY_MISSING`

---

# 5. Card Lifecycle Rule

Execution cards must follow this lifecycle:

```text
proposed → advisor-reviewed → po-approved → executing → executed → verified
```

ELIS Supervisor may execute only from a card in `po-approved` state.

ELIS Advisor may validate proposal-readiness before PO approves execution, but implementation validation requires implementation evidence from an approved execution card.

ELIS PM must not create implementation execution cards before:

1. Advisor returns `PASS` on proposal-readiness where required;
2. PO explicitly approves the next gate;
3. the implementation card is self-contained;
4. the implementation card is marked `po-approved`.

## Failure Classes

- `PREMATURE_IMPLEMENTATION_CARD`
- `EXECUTION_WITHOUT_PO_APPROVAL`
- `EXECUTION_FROM_UNAPPROVED_CARD`
- `VALIDATION_BEFORE_EVIDENCE`
- `GATE_SEQUENCE_VIOLATION`

---

# 6. Failed / Blocked Card Preservation Rule

Failed, blocked, crashed, or superseded cards must remain historical evidence.

Do not overwrite, erase, or mutate failed evidence to make a later attempt appear clean.

A resubmission must be a new child card that links to:

- the failed or blocked card;
- what changed;
- the corrected authoritative proposal or evidence location.

## Minimum Resubmission Fields

```text
Supersedes task:
Reason for prior FAIL/BLOCKED:
What changed:
Corrected authoritative source:
Requested review scope:
Out of scope:
Stop condition:
```

## Failure Classes

- `FAILED_CARD_OVERWRITTEN`
- `SUPERSESSION_NOT_DECLARED`
- `RESUBMISSION_WITHOUT_CHANGELOG`
- `HISTORICAL_EVIDENCE_LOST`

---

# 7. External Context Rejection Rule

Agents must reject task bodies that rely on external, unstored context.

Any of the following phrases or equivalents in an actionable card require `BLOCKED` unless the card also contains the full referenced content or a durable cited artefact:

```text
as discussed in Discord
per the channel
as agreed
see thread
as noted earlier
same as before
use context above
refer to previous chat
```

Ambiguous pronouns whose antecedent is outside the task body also make the card unsafe for execution.

## Failure Classes

- `EXTERNAL_CONTEXT_REFERENCE_DETECTED`
- `DISCORD_CONTEXT_REQUIRED`
- `AMBIGUOUS_ANTECEDENT`
- `CARD_NOT_SELF_CONTAINED`

---

# 8. Implementation Shell Packet Rule

For platform, runtime, service, repository, or production operations, ELIS Supervisor must execute from a self-contained hardened shell packet, not ad-hoc command fragments.

The implementation card must either embed the shell packet or cite it by path and hash.

## Minimum Shell Packet Requirements

```text
5-path EXIT trap
pre-existing process guard
fail() routing
deterministic evidence capture
cleanup verification
rollback or safe-stop behaviour
absolute paths
no hidden network exposure
no unauthorised service persistence
```

A list of commands in a card is not sufficient for production/runtime execution unless explicitly authorised by PO for a read-only diagnostic gate.

## Failure Classes

- `SHELL_PACKET_MISSING`
- `AD_HOC_COMMAND_EXECUTION`
- `PACKET_HASH_MISSING`
- `EXIT_TRAP_MISSING`
- `CLEANUP_VERIFICATION_MISSING`
- `ROLLBACK_PATH_MISSING`

---

# 9. Evidence Card Rule

Implementation evidence must be returned in a child evidence card or in a cited durable artefact.

## Minimum Implementation Evidence

```text
Gate/action identifier:
Parent PE link:
PO approval reference:
Implementation summary:
Exact artefacts changed:
Command/check evidence:
Before/after evidence:
Acceptance criteria mapping:
Rollback evidence or rollback readiness:
Known deviations:
Residual risks:
Evidence provenance:
Supersession status:
```

For runtime/platform work, evidence should include:

```text
shell packet verification output
per-action exit codes
named evidence files with absolute paths
timestamped evidence archive path
port/service verification output
cleanup confirmation
orphan-process check
```

## Failure Classes

- `IMPLEMENTATION_EVIDENCE_INCOMPLETE`
- `ACCEPTANCE_CRITERIA_NOT_MAPPED`
- `BEFORE_AFTER_EVIDENCE_MISSING`
- `ROLLBACK_EVIDENCE_MISSING`
- `EVIDENCE_PROVENANCE_MISSING`

---

# 10. Role-Specific Requirements

## 10.1 ELIS PM Requirements

ELIS PM owns Kanban structure, gate sequencing, and parent-card completeness.

ELIS PM must:

1. Create or maintain one authoritative parent PE control card.
2. Use one child card per gate/action.
3. Use explicit board targeting on every Kanban call.
4. Keep the parent card self-contained and current.
5. Record canonical proposal locations when stored in comments.
6. Maintain the child-card index.
7. Preserve failed, blocked, crashed, and superseded cards as historical evidence.
8. Create resubmission cards instead of overwriting failed cards.
9. Request Advisor validation only after the parent card passes the Parent PE Completeness Checklist.
10. Create implementation cards only after Advisor `PASS` and PO approval.
11. Never treat Discord-only context as authoritative.
12. Never perform implementation, validation, GitHub operations, or runtime changes unless explicitly authorised by role-specific governance.

### PM Pre-Advisor Checklist

Before requesting Advisor proposal-readiness validation, ELIS PM must confirm in the parent card:

```text
[ ] Parent PE card is self-contained.
[ ] Canonical proposal location is identified.
[ ] Gate 0/baseline evidence is included or cited.
[ ] Blocker inventory is current.
[ ] Role assignments are explicit.
[ ] Approval-gate table is present.
[ ] Gate plan is ordered and unambiguous.
[ ] Evidence requirements are measurable.
[ ] Rollback/recovery plan is present.
[ ] Hard constraints are explicit.
[ ] Failed/superseded cards are indexed.
[ ] No "see Discord", "TBD", or unstated assumptions remain.
```

If any item fails, ELIS PM must not request Advisor review.

### PM Failure Classes

- `PM_PARENT_CARD_UNDERPOPULATED`
- `PM_REQUESTED_REVIEW_TOO_EARLY`
- `PM_CREATED_IMPLEMENTATION_CARD_TOO_EARLY`
- `PM_USED_DISCORD_ONLY_CONTEXT`
- `PM_FAILED_TO_INDEX_CHILD_CARDS`
- `PM_FAILED_TO_DECLARE_SUPERSESSION`

---

## 10.2 ELIS Advisor Requirements

ELIS Advisor owns independent validation and must validate only authoritative stored content.

ELIS Advisor must:

1. Validate against the parent PE card, child card, cited Kanban comments, and durable artefacts only.
2. Ignore Discord-only context unless it has been copied into Kanban or a cited artefact.
3. Return `BLOCKED` if the parent PE card is incomplete.
4. Return `BLOCKED` if a child task lacks required gate/action fields.
5. Return `FAIL` when the proposal/evidence is substantively wrong.
6. Preserve failed validation as historical evidence.
7. Require resubmission via a new child card when prior validation failed or crashed.
8. Verify that implementation evidence maps to acceptance criteria.
9. Verify implementation/validation separation.
10. Verify no PO approval bypass.
11. Verify no hidden production, persistence, external exposure, or GitHub operation claim.

### Advisor Proposal-Readiness Minimum

ELIS Advisor should not perform proposal-readiness validation unless the parent card contains:

```text
PE identifier
Objective
Scope and non-scope
Authoritative proposal
Baseline/current state
Blocker inventory
Role assignments
Approval-gate table
Gate plan
Evidence requirements
Rollback/recovery plan
Hard constraints
Current status
Child-card index
Provenance
```

Missing content means:

```text
BLOCKED — PARENT_PE_CARD_INCOMPLETE
```

### Advisor Implementation-Validation Minimum

ELIS Advisor should not validate implementation unless the evidence card contains:

```text
Gate/action identifier
Parent PE link
PO approval reference
Implementation summary
Exact artefacts changed
Command/check evidence
Before/after evidence
Acceptance criteria mapping
Rollback evidence or readiness
Known deviations
Residual risks
Evidence provenance
Supersession status
```

Missing content means:

```text
BLOCKED — IMPLEMENTATION_EVIDENCE_INCOMPLETE
```

### Advisor Failure Classes

- `ADVISOR_VALIDATED_DISCORD_CONTEXT`
- `ADVISOR_REVIEWED_INCOMPLETE_PARENT`
- `ADVISOR_ACCEPTED_UNMAPPED_EVIDENCE`
- `ADVISOR_ACCEPTED_MISSING_PO_APPROVAL`
- `ADVISOR_FAILED_TO_REQUIRE_RESUBMISSION`
- `ADVISOR_VALIDATED_IMPLEMENTER_WORK`

---

## 10.3 ELIS Supervisor Requirements

ELIS Supervisor owns approved implementation/execution and must not infer missing instructions.

ELIS Supervisor must:

1. Execute only from a `po-approved` implementation card.
2. Refuse execution from proposed, advisor-reviewed, ready, vague, or incomplete cards.
3. Require self-contained implementation scope.
4. Require explicit out-of-scope boundaries.
5. Require parent PE card backlink.
6. Require PO approval reference.
7. Require shell packet path/hash or inline hardened shell packet for runtime/platform operations.
8. Require evidence checklist and stop condition.
9. Require rollback instructions or EXIT-trap rollback.
10. Stop and report `BLOCKED` if the task relies on Discord-only context.
11. Return implementation evidence in a structured evidence card/comment with absolute paths, outputs, exit codes, and cleanup verification.
12. Never validate its own implementation.

### Supervisor Pre-Execution Checklist

Before execution, ELIS Supervisor must confirm:

```text
[ ] Card state is po-approved.
[ ] Parent PE card is linked.
[ ] PO approval reference is present.
[ ] Scope is self-contained.
[ ] Out-of-scope is explicit.
[ ] Shell packet is embedded or cited by path + SHA.
[ ] Evidence checklist is machine-verifiable.
[ ] Rollback or EXIT-trap recovery is defined.
[ ] Stop condition is explicit.
[ ] Next dependency is identified.
[ ] No external Discord-only context is required.
```

If any item fails, ELIS Supervisor must return:

```text
BLOCKED — IMPLEMENTATION_CARD_INCOMPLETE
```

### Supervisor Evidence Minimum

After approved execution, ELIS Supervisor must return:

```text
PE:
Gate:
Task:
Parent task:
Implementation card:
Execution status:
Files changed:
Runtime objects changed:
Commands or shell packet used:
Shell packet SHA:
Exit codes:
Evidence files:
Evidence archive:
Before/after checks:
Port/service checks:
Rollback readiness:
Cleanup confirmation:
Known deviations:
Residual risks:
Next dependency:
```

### Supervisor Failure Classes

- `SUPERVISOR_EXECUTED_UNAPPROVED_CARD`
- `SUPERVISOR_USED_AD_HOC_COMMANDS`
- `SUPERVISOR_INFERRED_FROM_DISCORD`
- `SUPERVISOR_EXECUTED_INCOMPLETE_CARD`
- `SUPERVISOR_FAILED_TO_CAPTURE_EVIDENCE`
- `SUPERVISOR_VALIDATED_OWN_WORK`
- `SUPERVISOR_RUNTIME_CLEANUP_INCOMPLETE`

---

# 11. Installation Instructions

## Recommended Implementation Pattern

Add this skill to all three agent `SKILLS.md` files:

- ELIS PM `SKILLS.md`
- ELIS Advisor `SKILLS.md`
- ELIS Supervisor `SKILLS.md`

Preferred approach:

1. Store the shared skill text in a canonical shared file if the ELIS profile structure supports shared skill imports.
2. Add a short local reference in each role-specific `SKILLS.md`.
3. If shared imports are not supported, copy the full shared skill content into each `SKILLS.md`.
4. Keep the role-specific subsection relevant to each agent visible and close to the top of that agent's operational skills.

## Suggested Canonical Shared File

```text
/home/samurai/.hermes/profiles/_shared/skills/AUTHORITATIVE_KANBAN_PE_WORKFLOW_SKILL.md
```

---

# 12. PM SKILLS.md Addition

Add near PM's PE coordination, dispatch, and Kanban orchestration skills:

```markdown
## Required Skill: AUTHORITATIVE_KANBAN_PE_WORKFLOW_SKILL

ELIS PM must apply `AUTHORITATIVE_KANBAN_PE_WORKFLOW_SKILL` before creating, updating, dispatching, validating, resubmitting, or closing any governed Kanban PE task.

PM is responsible for:
- explicit board targeting;
- one authoritative parent PE control card;
- one child card per gate/action;
- complete parent-card proposal and evidence index;
- child-card gate typing;
- failed/blocked card preservation;
- resubmission card creation;
- Advisor review only after parent completeness;
- implementation card creation only after Advisor PASS and PO approval.

PM must not rely on Discord-only context as authoritative Kanban content.
```

---

# 13. Advisor SKILLS.md Addition

Add near Advisor's validation and policy-review skills:

```markdown
## Required Skill: AUTHORITATIVE_KANBAN_PE_WORKFLOW_SKILL

ELIS Advisor must apply `AUTHORITATIVE_KANBAN_PE_WORKFLOW_SKILL` before validating proposal-readiness, implementation evidence, rollback evidence, certification, or closeout.

Advisor validates only authoritative stored content:
- parent PE card;
- child gate/action card;
- cited Kanban comments;
- cited repository artefacts;
- cited logs/evidence archives.

Advisor must return `BLOCKED — PARENT_PE_CARD_INCOMPLETE` if a parent PE card is not self-contained.

Advisor must return `BLOCKED — IMPLEMENTATION_EVIDENCE_INCOMPLETE` if implementation evidence does not map to acceptance criteria or lacks required provenance.

Advisor must not validate Discord-only context or infer missing proposal/evidence from chat history.
```

---

# 14. Supervisor SKILLS.md Addition

Add near Supervisor's implementation/execution and runtime-operation skills:

```markdown
## Required Skill: AUTHORITATIVE_KANBAN_PE_WORKFLOW_SKILL

ELIS Supervisor must apply `AUTHORITATIVE_KANBAN_PE_WORKFLOW_SKILL` before executing any implementation, runtime, service, repository, or production task.

Supervisor may execute only from a self-contained implementation card in `po-approved` state.

Supervisor must return `BLOCKED — IMPLEMENTATION_CARD_INCOMPLETE` if the card lacks:
- parent PE backlink;
- PO approval reference;
- self-contained scope;
- explicit out-of-scope;
- shell packet path/hash or inline hardened shell packet;
- evidence checklist;
- rollback or EXIT-trap recovery;
- stop condition;
- next dependency.

Supervisor must not execute from Discord-only context, ad-hoc command fragments, or ambiguous Kanban cards.
```

---

# 15. Rollout Instructions for PM

Use this procedure to add the skill safely:

1. Open a governed documentation/profile update task.
2. Assign implementation to the authorised implementation agent.
3. Assign validation to the authorised validation agent.
4. Do not edit live runtime files directly unless PO approves the path and scope.
5. Confirm exact current profile paths before editing.
6. Add or update the shared skill file.
7. Add the PM, Advisor, and Supervisor local `SKILLS.md` references.
8. Validate that all three agents can read and apply the new skill in a fresh session or controlled reset.
9. Preserve evidence:
   - file paths changed;
   - before/after diff;
   - validation result;
   - restart/reset requirement, if any;
   - no model/provider/config drift.
10. Report PASS / FAIL / BLOCKED to PO.

---

# 16. Acceptance Criteria

The skill update is complete only when:

- The shared Kanban skill exists in the agreed canonical location or is copied into all three `SKILLS.md` files.
- PM `SKILLS.md` contains PM-specific Kanban obligations.
- Advisor `SKILLS.md` contains Advisor-specific validation obligations.
- Supervisor `SKILLS.md` contains Supervisor-specific execution obligations.
- All three agents explicitly recognise:
  - Kanban parent card is authoritative;
  - child cards are one-per-gate/action;
  - Discord-only context is not authoritative;
  - failed cards remain historical evidence;
  - resubmissions require new cards;
  - implementation requires Advisor PASS and PO approval;
  - Supervisor executes only from `po-approved` implementation cards.
- A fresh-session or controlled reset acknowledgement confirms the updated skill is loaded or accessible.
- No unauthorised runtime, model/provider, GitHub, or service changes occurred during the skill update.

---

# 17. Non-Goals

This skill does not:

- authorise implementation work;
- authorise runtime or service changes;
- authorise GitHub operations by PM;
- replace PO approval;
- replace Advisor validation;
- replace deterministic scripts/checkers;
- certify A2A production readiness;
- change model/provider configuration;
- change board ownership;
- change the global Kanban current-board pointer.

---

# 18. ELIS PE REPORTS MACRO EVENT RULE

**Rule ID:** `ELIS_PE_REPORTS_MACRO_EVENT_RULE`

## 18.1 Purpose

This rule provides a compact operational visibility stream for governed PE activity in `#elis-pe-reports`, while keeping Kanban and durable artefacts as the authoritative record.

`#elis-pe-reports` is a notification and situational-awareness channel only. The authoritative record remains one of: the parent PE Kanban card; the child gate/action Kanban card; a cited Kanban comment; a cited repository artefact; a cited evidence archive; or a cited GitHub PR/check (where GitHub operations were authorised).

## 18.2 Core Rule

For governed PE work, each ELIS agent must post a compact macro-event report to `#elis-pe-reports` when a task reaches a meaningful lifecycle event. Agents should not post for every minor comment, typo fix, internal note, or non-state-changing update.

## 18.3 Events Requiring a Report

Agents must post to `#elis-pe-reports` for these macro events:

```text
STARTED
PASS
FAIL
BLOCKED
SUPERSEDED
CANCELLED
READY_FOR_PO
PO_APPROVAL_REQUIRED
RUNTIME_OR_PROFILE_CRASH
GITHUB_ACTION_REQUIRED
CLOSEOUT_READY
```

## 18.4 Required Report Format

Each report must use this compact format:

```text
PE:
Task:
Kanban board:
Kanban task:
Agent:
Event:
Verdict:
Summary:
Next required actor:
Next required action:
Authoritative record:
```

**Field requirements:**

| Field | Requirement |
|---|---|
| `PE` | PE identifier, for example `PE-OPS-A2A-PRODUCTION-02` |
| `Task` | Human-readable task/gate title |
| `Kanban board` | Exact board name |
| `Kanban task` | Exact task ID |
| `Agent` | Reporting agent (ELIS PM, ELIS Advisor, ELIS Supervisor, ELIS GitHub) |
| `Event` | One macro event from the allowed event list |
| `Verdict` | `PASS`, `FAIL`, `BLOCKED`, `PARTIAL`, `CANCELLED`, `SUPERSEDED`, or `N/A` |
| `Summary` | One or two concise sentences |
| `Next required actor` | PO, PM, Advisor, Supervisor, ELIS GitHub, or none |
| `Next required action` | Concrete next action |
| `Authoritative record` | Kanban card/comment ID, artefact path, evidence archive, or PR/check reference |

## 18.5 Content Limits

Reports must be concise. Do not paste into `#elis-pe-reports`: full proposals; long validation reports; shell outputs; logs; diffs; evidence packets; full Kanban task bodies; full Markdown artefacts; secrets or environment values; model/provider credentials; anything that should live in Kanban or a repository artefact.

Instead, cite the authoritative record. Preferred references:

```text
Kanban: board=<board>, task=<task_id>, comment=<comment_id>
Artefact: <absolute or repo-relative path>
Evidence archive: <absolute path>
GitHub: PR #<number>, check name, commit SHA
```

## 18.6 Authority Boundary

A report in `#elis-pe-reports` does not: authorise implementation; authorise runtime changes; authorise service/systemd changes; authorise GitHub operations; replace Advisor validation; replace PO approval; replace Kanban evidence; replace repository artefacts; close a PE; certify production readiness. Any agent treating a Discord report as authority must classify the action as blocked.

## 18.7 Relationship to Kanban

Kanban remains the authoritative workflow record. For every `#elis-pe-reports` macro-event post, there must be an authoritative Kanban task/comment or cited artefact. A valid report must include the Kanban board and task ID unless the event is an early PO escalation before a task exists. In that exceptional case, the next action must be to create or update the relevant Kanban record.

## 18.8 Failure Classes

```text
PE_REPORT_MISSING
PE_REPORT_TOO_VERBOSE
PE_REPORT_USED_AS_AUTHORITY
PE_REPORT_WITHOUT_KANBAN_REFERENCE
PE_REPORT_DUPLICATES_FULL_EVIDENCE
PE_REPORT_OMITS_NEXT_ACTOR
PE_REPORT_OMITS_AUTHORITATIVE_RECORD
PE_REPORT_POSTED_TO_WRONG_CHANNEL
PE_REPORT_CONTAINS_UNSAFE_DETAIL
```

## 18.9 Role-Specific Requirements

### 18.9.1 ELIS PM

ELIS PM must post to `#elis-pe-reports` for: PE start or resumption; parent PE card creation/update when it changes authoritative status; gate transition; Advisor validation request; Advisor `PASS`, `FAIL`, or `BLOCKED` received; PO approval required; implementation task creation after PO approval; closeout readiness; PE pause or hold.

PM reports must make clear when PO action is required. PM must not use the report as a substitute for updating the parent PE card or child-card index.

### 18.9.2 ELIS Advisor

ELIS Advisor must post to `#elis-pe-reports` for: validation `STARTED`; validation `PASS`; validation `FAIL`; validation `BLOCKED`; evidence insufficiency; readiness for PO decision; recommendation to supersede or resubmit.

Advisor reports must not paste the full validation body. They must cite the validation task/card/comment where the full verdict lives.

### 18.9.3 ELIS Supervisor

ELIS Supervisor must post to `#elis-pe-reports` for: implementation/execution `STARTED`; implementation/execution `PASS`; implementation/execution `FAIL`; implementation/execution `BLOCKED`; runtime/profile crash; evidence-ready status; cleanup completed; rollback completed or rollback required.

Supervisor reports must cite the implementation card and evidence artefact path. They must not paste full shell output or logs into `#elis-pe-reports`.

### 18.9.4 ELIS GitHub

ELIS GitHub must post to `#elis-pe-reports` for authorised GitHub macro events: GitHub operation `STARTED`; branch created; commit pushed; PR created; PR updated; checks failed; checks passed; merge ready; merged; GitHub operation `FAIL` or `BLOCKED`.

ELIS GitHub must include PR number, branch, head SHA, and check names where relevant.

---

# 19. TOKEN BUDGET AUTO RESET RULE

**Rule ID:** `TOKEN_BUDGET_AUTO_RESET_RULE`
**Purpose:** Prevent token/context overload, stale context, hallucinated continuity, and unsafe execution in long-running ELIS agent sessions.

## 19.1 Source Basis

This rule is based on documented agent context-management practices.

Relevant sources:

- Microsoft AutoGen — *Introduction to Transform Messages*: token limits and preprocessing chat history to stay within acceptable token ranges. URL: `https://microsoft.github.io/autogen/0.2/docs/topics/handling_long_contexts/intro_to_transform_messages/`
- Microsoft AutoGen — *Conversation Patterns*: chat summarisation and token usage calculation. URL: `https://microsoft.github.io/autogen/0.2/docs/tutorial/conversation-patterns/`
- Microsoft AutoGen — `token_count_utils`: token counting utilities. URL: `https://microsoft.github.io/autogen/0.2/docs/reference/token_count_utils/`
- LangChain / LangGraph — *Memory overview*: short-term thread-scoped memory vs long-term memory across conversations/sessions. URL: `https://docs.langchain.com/oss/python/concepts/memory`
- LangChain — *Long-term memory*: memory persisted across threads/sessions. URL: `https://docs.langchain.com/oss/python/langchain/long-term-memory`
- Microsoft Semantic Kernel — *Chat history reducers*: token-based reduction to keep chat history within model token limits. URL: `https://learn.microsoft.com/en-us/semantic-kernel/concepts/ai-services/chat-completion/chat-history`

Important distinction: the general principle is documented best practice. The exact ELIS thresholds and Kanban reset workflow below are ELIS governance policy.

## 19.2 Core Rule

If an ELIS agent exceeds the configured token/context threshold, it must not continue substantive reasoning or execution from overloaded context.

Instead, the agent must:

1. stop before additional substantive work;
2. preserve current state in an authoritative Kanban handoff or durable artefact;
3. post a compact macro-event report to `#elis-pe-reports`;
4. require or initiate a fresh session/reset;
5. continue only after the fresh session returns a reset/binding acknowledgement grounded in authoritative Kanban/durable artefacts.

Overloaded live context must not be treated as authoritative continuity. Kanban and durable artefacts remain authoritative.

## 19.3 Thresholds

```text
WARN:            >20,000 input tokens
RESET_REQUIRED:  >50,000 input tokens
HARD_STOP:       >80,000 input tokens
```

Optional stricter ceiling for high-risk governance/runtime work:

```text
ABSOLUTE_HARD_STOP: >90,000 input tokens
```

### WARN

At `WARN`, the agent may continue, but must: use compact output; avoid broad history reads; avoid large context expansion; avoid unnecessary file/session searches; prefer current Kanban card and cited artefacts; prepare for possible reset if work will continue.

### RESET_REQUIRED

At `RESET_REQUIRED`, the agent must: stop after the current safe step; write a compact reset handoff to Kanban or durable artefact; post a compact macro-event report to `#elis-pe-reports`; require a fresh session before further substantive reasoning or execution; not create new implementation/runtime/GitHub work before reset.

### HARD_STOP

At `HARD_STOP`, the agent must not perform further substantive reasoning, implementation, validation, runtime changes, GitHub operations, or gate decisions. Allowed actions only: preserve state; write reset handoff; post macro-event report; request/reset into a fresh session.

## 19.4 Required Reset Handoff

When `RESET_REQUIRED` or `HARD_STOP` is reached, the agent must create a reset handoff in the authoritative Kanban record or a cited durable artefact.

Minimum handoff format:

```text
PE:
Board:
Parent task:
Current child task:
Agent:
Role:
Reason for reset:
Token state: WARN / RESET_REQUIRED / HARD_STOP
Observed token count or evidence source:
Last safe completed action:
Current status:
Open blockers:
Authoritative proposal/evidence references:
Next required actor:
Next required action:
Forbidden actions after reset:
```

The handoff must be concise and deterministic. Do not paste full logs, full proposals, or long evidence packets into the handoff. Cite the authoritative record.

## 19.5 Required Macro-Event Report

The agent must post a compact report to `#elis-pe-reports` when reset is required.

Format:

```text
PE:
Task:
Kanban board:
Kanban task:
Agent:
Event: RESET_REQUIRED / HARD_STOP
Verdict: BLOCKED
Summary:
Next required actor:
Next required action:
Authoritative record:
```

The Discord report is notification only. It does not replace the Kanban handoff and does not authorise continuation.

## 19.6 Reset / Binding Acknowledgement

After reset, the new session must not continue until it returns a reset/binding acknowledgement.

Minimum acknowledgement:

```text
Agent identity:
Session state: fresh after reset
PE:
Board:
Parent task:
Current child task:
Role:
Allowed scope:
Forbidden scope:
Authoritative context loaded:
- parent PE card:
- current child card:
- latest reset handoff:
- cited evidence:
Prior session context discarded: YES / NO
Kanban governance rules loaded: YES / NO
#elis-pe-reports rule loaded: YES / NO
Verdict: RESET_ACK_CONFIRMED / RESET_ACK_BLOCKED
Blockers:
```

No continuation is allowed without `RESET_ACK_CONFIRMED`. This preserves the existing ELIS rule: `NO_RESET_ACK_NO_DISPATCH`.

## 19.7 Role-Specific Duties

### 19.7.1 ELIS PM

PM must monitor token/context load during coordination and Kanban work. At `WARN`, PM must: compact responses; avoid unnecessary broad context recalls; rely on parent PE card, current child card, and cited evidence. At `RESET_REQUIRED`, PM must: update the parent PE card or current child card with a reset handoff; post `RESET_REQUIRED` to `#elis-pe-reports`; stop creating new child tasks until reset acknowledgement; not dispatch implementation or validation from overloaded context. At `HARD_STOP`, PM must: perform only state-preservation actions; request/reset; resume only after reset/binding acknowledgement. PM must not create implementation cards from an overloaded session.

### 19.7.2 ELIS Advisor

Advisor must monitor token/context load during validation. At `WARN`, Advisor must: validate only against authoritative Kanban/cited artefacts; avoid broad history expansion unless explicitly necessary. At `RESET_REQUIRED`, Advisor must: stop validation after current safe step; record a validation reset handoff; post `RESET_REQUIRED` to `#elis-pe-reports`; continue validation only from a fresh session after reset acknowledgement. At `HARD_STOP`, Advisor must not issue `PASS`, `FAIL`, certification, or closeout advice from overloaded context. It may only preserve state and require reset. Advisor must not validate Discord-only context or memory summaries.

### 19.7.3 ELIS Supervisor

Supervisor must monitor token/context load during implementation, runtime diagnostics, and evidence packaging. At `WARN`, Supervisor must: avoid expanding context beyond the approved implementation card and shell packet; keep execution evidence concise and durable. At `RESET_REQUIRED`, Supervisor must: stop before new execution steps; preserve current execution/evidence state; post `RESET_REQUIRED` to `#elis-pe-reports`; require a fresh session before continuing. At `HARD_STOP`, Supervisor must not execute commands, edit files, start/stop services, perform runtime changes, or conduct rollback unless immediate safe cleanup is already required by an active shell packet. It may only preserve state and request/reset. Supervisor must never infer missing implementation instructions from overloaded context.

### 19.7.4 ELIS GitHub

ELIS GitHub must apply the same reset thresholds to GitHub operations. At `RESET_REQUIRED` or `HARD_STOP`, ELIS GitHub must not create PRs, push commits, re-run checks, merge, or mutate GitHub state until a fresh session confirms reset/binding acknowledgement and re-loads the authorised GitHub operation card.

## 19.8 Dispatcher / Runtime Implementation Levels

- **Level 1 — Skills / Prompt Governance:** Add this rule to agent skills and require agents to self-enforce. Low-risk, fast to deploy, no runtime changes. Recommended immediate step.
- **Level 2 — Kanban Dispatcher Preflight:** Before claiming or continuing a Kanban task, the dispatcher checks session token usage if available. Requires dispatcher integration. Recommended future implementation PE.
- **Level 3 — Gateway / Session Watchdog:** Hermes gateway or session manager monitors context load and enforces reset automatically. Runtime/platform risk. Recommended only after Level 1 and Level 2 are stable.

## 19.9 Token Count Evidence

Agents may use any reliable available source for token count evidence, including: model/gateway usage metadata; Hermes run/session telemetry; dispatcher logs; provider API usage; local tokenizer estimate; explicit reset banner/context indicator; agent-reported context size at reset. If exact token counts are unavailable, agents must use conservative classification when the runtime reports very large context.

## 19.10 Failure Classes

```text
TOKEN_BUDGET_WARN_IGNORED
TOKEN_BUDGET_RESET_REQUIRED
TOKEN_BUDGET_HARD_STOP
OVERLOADED_CONTEXT_USED_FOR_DECISION
OVERLOADED_CONTEXT_USED_FOR_IMPLEMENTATION
OVERLOADED_CONTEXT_USED_FOR_VALIDATION
RESET_HANDOFF_MISSING
RESET_ACK_MISSING
RESET_ACK_INCOMPLETE
CONTINUATION_FROM_STALE_CONTEXT
TOKEN_COUNT_SOURCE_MISSING
TOKEN_BUDGET_DISPATCH_BLOCKED
```

## 19.11 Non-Goals

This rule does not: implement dispatcher automation; implement gateway/session watchdogs; change Hermes runtime; change model/provider settings; authorise GitHub operations; authorise A2A implementation; authorise service/systemd changes; authorise production readiness; replace Kanban evidence; replace PO approval; replace Advisor validation.

## 19.12 Recommended Next PE

```text
PE-OPS-TOKEN-EFFICIENCY-01 — Add Compact Agent Validation Mode and Token/Context Overload Controls
```

Suggested scope: token telemetry discovery; dispatcher preflight; threshold enforcement; reset handoff automation; reset/binding acknowledgement checks; `#elis-pe-reports` macro-event automation; compact validation prompts; blocked continuation from stale/overloaded context; tests for token-threshold behaviour. This PE should remain separate from A2A production unless PO explicitly prioritises it.