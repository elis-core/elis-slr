# ELIS SLR Infrastructure Implementation and Validation Guide v1.0

> **Metadata**  
> **Title:** ELIS SLR Infrastructure Implementation and Validation Guide v1.0  
> **Repository:** elis-slr  
> **Status:** Approved  
> **Version:** 1.0  
> **Last Updated:** 2026-07-03  
> **Owner:** ELIS PM  
> **Approver:** Carlos Rocha (PO)

## Programme

Provision the complete ELIS SLR runtime in the `elis-slr` repository
using the ELIS 2-Agent architecture.

## Session Lifecycle

Every new implementation or validation task starts with a fresh
Hermes/NemoHermes session. Continuations require explicit PM
designation.

## Sequential Deployment Order

1.  Harvest pair
2.  Screening pair
3.  Extraction pair
4.  Synthesis pair
5.  Protocol pair

Each pair must PASS independent validation before the next begins.

## ELIS 2-Agent Runtime

Each activity consists of:

-   One implementation sandbox
-   One validation sandbox
-   Independent OpenShell gateways
-   Independent managed inference routes
-   Different models whenever practical

## Agent Assignment

  -----------------------------------------------------------------------------------------------
  Activity                Implementer Model                   Validator Model
  ----------------------- ----------------------------------- -----------------------------------
  Harvest                 moonshotai/kimi-k2.6                nvidia/nemotron-3-ultra-550b-a55b

  Screening               nvidia/nemotron-3-ultra-550b-a55b   z-ai/glm-5.1

  Extraction              mistralai/mistral-medium-3.5-128b   nvidia/nemotron-3-ultra-550b-a55b

  Synthesis               moonshotai/kimi-k2.6                nvidia/nemotron-3-ultra-550b-a55b

  Protocol                z-ai/glm-5.1                        nvidia/nemotron-3-ultra-550b-a55b
  -----------------------------------------------------------------------------------------------

## Responsibilities

Supervisor: provision, configure and document.

Advisor: independently validate.

ELIS GitHub: commit only validated artefacts to `elis-slr`.

Success: reproducible infrastructure with every activity protected by an
independent validation agent.