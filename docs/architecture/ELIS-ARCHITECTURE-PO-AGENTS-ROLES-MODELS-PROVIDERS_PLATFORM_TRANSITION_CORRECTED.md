# ELIS Architecture — PO, Agents, Roles, Boards, Repositories, Models and Providers

## 1. Canonical Positioning

ELIS Core is now positioned as:

> **Open research and teaching AI platform for governed multi-agent workflows, auditable evidence, and responsible AI adoption in higher education.**

This replaces the earlier “AI Business Management Lab” framing. ELIS should now be described primarily as a **Research and Teaching AI Lab**, not as a business management lab.

The new positioning aligns ELIS with academic research, teaching innovation, assessment redesign, AI literacy, systematic literature review workflows, and evidence-based adoption of AI in higher education.

## 2. Governance Model

ELIS is governed by a Product Owner (PO). The PO is the final approval authority for scope, priorities, architecture decisions, execution gates, GitHub operations, runtime changes, production cutover, and exceptions.

ELIS is designed to support different POs across projects, research programmes, teaching pilots, and institutional deployments. “PO” is therefore a role, not a person-specific identity. A named PO may be assigned per initiative, but the architecture should remain reusable by other POs.

ELIS uses a governed multi-agent operating model with explicit separation between:

- research and teaching strategy;
- governance and risk review;
- runtime/platform operations;
- platform engineering, infrastructure, and programming execution;
- GitHub/remote repository operations;
- systematic literature review research workflows;
- evidence production, validation, and auditability.

No agent may expand its authority by implication. Advisor reviews and advises; PO approves. Supervisor operates runtime/profile/topology changes when authorised. ELIS GitHub performs GitHub operations when authorised. PM coordinates ELIS Core platform work only. ELIS SLR coordinates SLR research workflow only.

## 3. Canonical Repositories

| Repository | URL | Public Description | Purpose | Operating Owner |
|---|---|---|---|---|
| ELIS Core | `https://github.com/elis-core/elis-core` | Open research and teaching AI platform for governed multi-agent workflows, auditable evidence, and responsible AI adoption in higher education. | Core ELIS platform, governance, multi-agent workflows, implementation management, validation gates, evidence packets, runtime coordination patterns, schemas, CI, and operations | ELIS PM |
| ELIS SLR | `https://github.com/elis-core/elis-slr` | Systematic Literature Review platform for governed multi-agent research workflows, evidence pipelines, and protocol-compliant SLR execution. | SLR-specific research workflow, protocol documents, research evidence, PRISMA artefacts, systematic review outputs, and SLR evidence pipeline | ELIS SLR |
| Legacy repository | `https://github.com/rochasamurai/ELIS-Multi-AI-Agent-Platform` | Legacy/historical source repository | Historical OpenClaw-era source/provenance and fallback during migration | Read-only fallback unless PO approves otherwise |

The legacy repository must not be deleted, rewritten, or force-pushed during the Core/SLR split. The new repositories can be built and validated in parallel while the legacy repository remains available as fallback.

## 4. Canonical Kanban Boards

| Board Slug | Board Name | Purpose | Owner |
|---|---|---|---|
| `elis-core` | ELIS Core | ELIS Core platform, infrastructure, programming, implementation, validation, and governed operational work | ELIS PM |
| `elis-slr` | ELIS SLR | Protocol-compliant SLR workflow: harvest, screen, extract, synthesise, protocol evidence, PRISMA-aligned reporting artefacts where applicable, and evidence tracking | ELIS SLR |
| `elis-a2a-implementation` | ELIS A2A Implementation | Existing A2A implementation history and active A2A migration/implementation continuity | Existing A2A workflow owner |

The `default` Kanban board is a Hermes fallback/system board only and must not be used for ELIS work.

## 5. Top-Level Agent Hierarchy

```text
PO — Product Owner
│
├── ELIS Ideas
│   └── Exploration, innovation, future concepts, research and teaching pilots
│
├── ELIS Advisor
│   └── Governance, risk, readiness, protocol-boundary review
│
├── ELIS Supervisor
│   └── Runtime, profiles, boards, topology, workspaces, operational safety
│
├── ELIS GitHub
│   └── Authorised GitHub and remote repository operations only
│
├── ELIS PM
│   ├── Infrastructure Team
│   │   ├── infra-implementer-a
│   │   ├── infra-implementer-b
│   │   ├── infra-validator-a
│   │   └── infra-validator-b
│   │
│   └── Programming Team
│       ├── prog-implementer-a
│       ├── prog-implementer-b
│       ├── prog-validator-a
│       └── prog-validator-b
│
└── ELIS SLR
    └── SLR Research Team
        ├── slr-harvest-implementer
        ├── slr-harvest-validator
        ├── slr-screen-implementer
        ├── slr-screen-validator
        ├── slr-extract-implementer
        ├── slr-extract-validator
        ├── slr-synth-implementer
        ├── slr-synth-validator
        ├── slr-protocol-implementer
        └── slr-protocol-validator
```

## 6. Role Descriptions

### PO — Product Owner

The PO is the sole final decision authority for the assigned ELIS scope. The PO approves or rejects architecture, gates, migration plans, GitHub operations, runtime changes, cutover, rollback, exceptions, and production scope.

The PO directs ELIS through explicit approvals, stops, corrections, and priority decisions. The PO defines the research and teaching direction for the assigned initiative, approves pilots, and decides when evidence is sufficient to proceed.

### ELIS Ideas

ELIS Ideas explores concepts, opportunities, external references, innovation directions, and future research/teaching pilots. It is PO-triggered and does not execute platform, runtime, GitHub, PE, or SLR work.

Example exploration areas:

- assessment stress-testing pilots;
- AI literacy teaching scenarios;
- evidence maps for AI adoption in higher education;
- new research workflow designs;
- teaching innovation use cases;
- responsible AI adoption patterns.

### ELIS Advisor

ELIS Advisor provides governance, risk, readiness, and protocol-boundary review. Advisor may return PASS, PASS_WITH_REQUIRED_CORRECTIONS, or BLOCKED-style recommendations, but does not authorise execution.

Advisor does not mutate files, operate runtime, create profiles, dispatch agents, perform GitHub operations, or approve gates. PO approves; Advisor reviews and advises.

### ELIS Supervisor

ELIS Supervisor owns runtime and operations feasibility. Supervisor handles profile, Kanban, workspace, topology, identity/routing, service, and platform configuration work only when explicitly approved by PO.

Supervisor may prepare execution packets, evidence packets, rollback plans, operational diagnostics, staging plans, and runtime feasibility reviews. Supervisor must not perform GitHub remote operations unless separately authorised under the correct GitHub path, and should not perform PE implementation work unless PO explicitly grants an exception.

### ELIS GitHub

ELIS GitHub is the authorised agent for GitHub and remote repository operations. This includes clone, branch, commit, push, PR creation, PR update, check monitoring, and other GitHub-side operations when PO approves the specific gate.

ELIS GitHub must not perform local implementation outside its authorised GitHub operation scope. It must not force-push, rewrite history, delete repositories, change remotes, or alter repository settings unless PO explicitly approves that exact operation.

### ELIS PM

ELIS PM coordinates ELIS Core platform work. PM manages PE flow, task sequencing, evidence routing, implementation/validation coordination, and PO reporting.

In the repositioned architecture, ELIS PM does not manage “business management” activities. It coordinates the **core research and teaching AI platform** infrastructure and programming work that supports governed multi-agent workflows, auditable evidence, and responsible academic AI adoption.

PM must not create profiles, initialise boards, bind agents, mutate topology, activate gateways, edit secrets, propagate `.env` files, perform runtime/profile changes, push to GitHub, change remotes, migrate files, or execute production cutover.

PM must not dispatch SLR agents. SLR work belongs to ELIS SLR.

## 7. ELIS PM Teams

### Infrastructure Team

The Infrastructure Team handles infrastructure/platform implementation and validation under ELIS PM coordination.

| Agent | Role |
|---|---|
| `infra-implementer-a` | Infrastructure implementation agent |
| `infra-implementer-b` | Parallel or alternate infrastructure implementation agent |
| `infra-validator-a` | Infrastructure validation agent |
| `infra-validator-b` | Parallel or alternate infrastructure validation agent |

Infrastructure work supports the ELIS Core platform for research and teaching workflows, including runtime services, integration, deployment, monitoring, and operational reliability.

Implementers produce scoped changes and evidence. Validators independently review and validate. Implementers must not validate their own work.

### Programming Team

The Programming Team handles application/code implementation and validation under ELIS PM coordination.

| Agent | Role |
|---|---|
| `prog-implementer-a` | Programming implementation agent |
| `prog-implementer-b` | Parallel or alternate programming implementation agent |
| `prog-validator-a` | Programming validation agent |
| `prog-validator-b` | Parallel or alternate programming validation agent |

Programming implementers work on code, tests, scripts, schemas, tools, validators, evidence-generation logic, and application workflows. Validators review implementation quality, correctness, tests, and compliance.

## 8. ELIS SLR

ELIS SLR owns the Systematic Literature Review workflow on the `elis-slr` board and, after governed migration, the `elis-core/elis-slr` repository.

ELIS SLR is the research evidence branch of ELIS. It supports protocol-compliant systematic literature review execution, including harvesting, screening, extraction, synthesis, ELIS SLR Protocol evidence, PRISMA-aligned reporting artefacts where applicable, validation, and traceability.

ELIS SLR does not own ELIS Core platform work, infrastructure agents, programming agents, runtime topology, GitHub operations, or profile/board mutation. It coordinates research workflow only.

### ELIS SLR Protocol and PRISMA Alignment

ELIS SLR Protocol is an ELIS-defined systematic review protocol. It is PRISMA-informed and may produce PRISMA-aligned reporting artefacts, but PRISMA is not the canonical name of the ELIS protocol stage.

Therefore, the former PRISMA-stage agents are renamed as protocol agents:

- `slr-protocol-implementer`
- `slr-protocol-validator`

This preserves PRISMA compatibility while making clear that ELIS SLR has its own protocol, evidence model, governance gates, and validation workflow.

### SLR Research Team

| Agent | Role |
|---|---|
| `slr-harvest-implementer` | Executes literature search, source harvesting, corpus collection, and import preparation |
| `slr-harvest-validator` | Validates search coverage, source provenance, deduplication assumptions, and harvest evidence |
| `slr-screen-implementer` | Performs title/abstract/full-text screening according to protocol criteria |
| `slr-screen-validator` | Validates screening decisions, inclusion/exclusion consistency, and reviewer traceability |
| `slr-extract-implementer` | Extracts structured study data, metadata, methods, findings, and evidence fields |
| `slr-extract-validator` | Validates extracted fields, source fidelity, schema compliance, and extraction completeness |
| `slr-synth-implementer` | Produces thematic, quantitative, methodological, and evidence synthesis outputs |
| `slr-synth-validator` | Validates synthesis traceability, consistency with extracted data, and conclusion boundaries |
| `slr-protocol-implementer` | Maintains ELIS SLR Protocol evidence, reporting artefacts, flow counts, traceability records, and PRISMA-aligned reporting outputs where applicable |
| `slr-protocol-validator` | Validates ELIS SLR Protocol compliance, evidence traceability, flow counts, exclusions, reporting completeness, and PRISMA-aligned artefacts where applicable |

## 9. Research and Teaching Use-Case Orientation

ELIS Core should be presented as a platform for practical higher-education use cases, not as a general business management system.

Primary use-case families:

| Use-Case Family | Description |
|---|---|
| Systematic literature review | Governed Harvest → Screen → Extract → Synthesise → Protocol Evidence → Validate workflows |
| Research evidence mapping | Evidence maps for steering committees, research projects, policy questions, and AI adoption strategy |
| Assessment stress-testing | Testing assignment vulnerability to GenAI completion and producing redesign recommendations |
| AI literacy teaching activities | Student-facing exercises where learners critique, improve, and document AI-assisted work |
| Teaching case generation and validation | Drafting and validating teaching cases, instructor notes, discussion questions, and misconception maps |
| Feedback and rubric review | Checking clarity, consistency, and actionability of rubrics and feedback examples |
| Governance evidence packets | Producing auditable evidence for AI adoption decisions, pilots, and academic review |

## 10. Routing Rules

No cross-board dispatch is allowed.

| Work Type | Correct Route |
|---|---|
| ELIS Core platform / infrastructure / programming | ELIS PM → `elis-core` |
| A2A implementation continuity | `elis-a2a-implementation` until explicitly closed/migrated |
| SLR research workflow | ELIS SLR → `elis-slr` |
| Governance/risk/readiness/protocol deviation | ELIS Advisor |
| Runtime/profile/board/topology/tooling issue | ELIS Supervisor |
| GitHub/remote operation | ELIS GitHub after PO approval |
| Priority/exception/cutover/approval | PO |

PM and SLR may exchange status or dependency context only when authorised, but neither may dispatch agents or mutate the other board.

## 11. Current Model / Provider Information

The following model/provider information is confirmed from recent runtime messages or operational context. Entries marked “to confirm” should be verified with `hermes profile show <profile>` or equivalent profile inspection before being treated as canonical.

| Agent/Profile | Model | Provider | Status |
|---|---|---|---|
| ELIS PM | `deepseek/deepseek-v4-flash` | OpenRouter | Confirmed from latest PM reset message |
| ELIS Advisor | to confirm | to confirm | Verify from profile |
| ELIS Supervisor | to confirm | to confirm | Verify from profile |
| ELIS Ideas | to confirm | to confirm | Verify from profile |
| ELIS GitHub | to confirm | to confirm | Verify from profile |
| ELIS SLR | to confirm | to confirm | Verify from profile |
| Infrastructure agents | to confirm | to confirm | Verify from profile/config |
| Programming agents | to confirm | to confirm | Verify from profile/config |
| SLR research agents | to confirm | to confirm | Verify from profile/config |

Recommended verification command:

```bash
for profile in elis-pm elis-advisor elis-supervisor elis-ideas elis-github elis-slr; do
  echo "=== $profile ==="
  hermes profile show "$profile" || true
  echo
done
```

For implementer and validator agents, inspect the relevant Hermes Agent profile or approved ELIS workspace configuration once the final migration to Hermes Agent topology is complete. OpenClaw artefacts may be consulted only as legacy provenance or migration evidence unless explicitly revalidated and migrated.

## 12. Operating Principles

1. PO approves; agents do not self-authorise.
2. Advisor reviews and advises; Advisor does not approve execution.
3. Supervisor operates runtime/topology only after PO approval.
4. ELIS GitHub performs GitHub operations only after PO approval.
5. PM coordinates ELIS Core platform work only.
6. ELIS SLR coordinates SLR research work only.
7. Implementers implement; validators validate independently.
8. No cross-board dispatch.
9. No migration, push, remote change, rebinding, gateway activation, `.env` propagation, or cutover without explicit PO approval.
10. The legacy repository remains fallback/provenance until the new repos are built, validated, and PO approves any future cutover.
11. ELIS Core must be described as a research and teaching AI platform, not a business management lab.
12. ELIS outputs should be practical, auditable, and useful for research, teaching, assessment, AI literacy, and academic governance.
13. OpenClaw-related artefacts are legacy unless explicitly revalidated and migrated.
14. Canonical new-release directory names must be neutral ELIS paths and must not mention `samurai`, `openclaw`, or `hermes`.
15. `/srv/elis/` is the target server-side naming direction, but any filesystem change requires separate PO approval.

## 13. Platform Transition and Legacy Classification

The initial `elis-server` release was based on OpenClaw. The new `elis-server` release is based on Hermes Agent.

All OpenClaw-related files, paths, workspaces, references, and conventions are therefore classified as legacy unless explicitly revalidated and migrated under the Hermes Agent architecture.

OpenClaw artefacts may remain as historical provenance or temporary migration sources, but they must not be treated as canonical runtime architecture for the new ELIS release.

Canonical directory names for the new release must not mention `samurai`, `openclaw`, or `hermes`.

- `samurai` is a user/account name and must not define platform architecture.
- `openclaw` identifies the legacy platform basis.
- `hermes` identifies the runtime engine, but should not appear in canonical ELIS business/workspace directory names.

The target server-side naming direction is neutral ELIS infrastructure under `/srv`, subject to separate PO approval before any filesystem change. Candidate target paths include:

- `/srv/elis/repos/core/`
- `/srv/elis/repos/slr/`
- `/srv/elis/workspaces/core/`
- `/srv/elis/workspaces/slr/`
- `/srv/elis/runtime/`
- `/srv/elis/archive/legacy-openclaw/`

This section is documentation only. It does not authorise directory creation, renaming, file movement, workspace rebinding, profile mutation, gateway activation, service changes, GitHub operations, `.env` propagation, cleanup, or production cutover.

## 14. Public Description Summary

### ELIS Core

> Open research and teaching AI platform for governed multi-agent workflows, auditable evidence, and responsible AI adoption in higher education.

### ELIS SLR

> Systematic Literature Review platform for governed multi-agent research workflows, evidence pipelines, and protocol-compliant SLR execution.

### One-line ELIS Purpose

> ELIS helps universities turn AI use in research and teaching from ad hoc experimentation into governed, evidence-based practice.
