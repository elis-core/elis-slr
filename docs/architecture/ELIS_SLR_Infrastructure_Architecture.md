# ELIS SLR Infrastructure Architecture v1.0

> **Metadata**  
> **Title:** ELIS SLR Infrastructure Architecture v1.0  
> **Repository:** elis-slr  
> **Status:** Approved  
> **Version:** 1.0  
> **Last Updated:** 2026-07-03  
> **Owner:** ELIS PM  
> **Approver:** Carlos Rocha (PO)

## Purpose

Authoritative architecture for the ELIS SLR production runtime.

## Repository Boundaries

### elis-core

Reusable runtime, A2A, OpenShell, NemoHermes integration, gateway
management, shared skills and governance.

### elis-slr

SLR application, agent manifests, provisioning, validation, model
assignments, runbooks and deployment artefacts.

## ELIS 2-Agent Principle

Every SLR activity SHALL be implemented by an independent agent pair:

-   Implementation agent
-   Validation agent

The validator must: - run in a separate sandbox; - use a separate
OpenShell gateway; - use a different model whenever feasible; - perform
adversarial validation before publication.

## Agent Matrix

  ------------------------------------------------------------------------------------------------------------------------
  Activity             Implementer Port       Model                                                   Validator Port
  ------------ ------------------- ---------- ----------------------------------- ----------------------------- ----------
  Harvest         elis-slr-harvest 8091       moonshotai/kimi-k2.6                   elis-slr-harvest-validator 8096

  Screening        elis-slr-screen 8092       nvidia/nemotron-3-ultra-550b-a55b       elis-slr-screen-validator 8097

  Extraction      elis-slr-extract 8093       mistralai/mistral-medium-3.5-128b      elis-slr-extract-validator 8098

  Synthesis         elis-slr-synth 8094       moonshotai/kimi-k2.6                     elis-slr-synth-validator 8099

  Protocol       elis-slr-protocol 8095       z-ai/glm-5.1                          elis-slr-protocol-validator 8100
  ------------------------------------------------------------------------------------------------------------------------

## Workflow

PM → Session Reset → Supervisor → Session Reset → Advisor → PM → ELIS
GitHub → PO