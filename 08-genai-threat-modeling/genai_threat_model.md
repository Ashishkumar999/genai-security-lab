# GenAI Threat Modeling Guide

This document outlines a structured approach to threat modeling large language model (LLM) applications and retrieval-augmented generation (RAG) systems.

Threat Modeling Objectives

Identify attack surfaces in GenAI applications
Protect system prompts and internal policies
Prevent unauthorized dataset retrieval
Secure connectors and plugins
Reduce model abuse risks

Core GenAI Attack Surfaces

User input interface
System prompt layer
Retrieval pipelines (RAG)
External connectors and plugins
Model inference APIs
Training datasets
Memory persistence layers

Example Threat Categories

Prompt Injection Attacks

Override system instructions
Extract hidden policies
Manipulate assistant behavior

Jailbreak Attacks

Bypass safety controls
Escalate privilege roles
Expose restricted workflows

RAG Pipeline Attacks

Cross-index leakage
Metadata filter bypass
Chunk stitching reconstruction

Connector Exploitation

SharePoint exposure
Google Drive leakage
Slack history extraction
Email connector abuse

Model Abuse Attacks

Model extraction attempts
Token abuse
Inference cost amplification

Cloud Configuration Risks

IAM misconfiguration
Dataset permission failures
Service account exposure
Logging pipeline leakage

Threat Modeling Methodology

Step 1 — Identify assets

System prompts
Datasets
Embeddings
Connectors
API keys

Step 2 — Identify trust boundaries

User input vs system prompt
Model vs retrieval pipeline
Application vs cloud provider services

Step 3 — Map attack paths

Injection through prompts
Unauthorized retrieval attempts
Connector enumeration
Model cloning attempts

Step 4 — Define mitigations

Prompt filtering
Dataset-level authorization
IAM least privilege enforcement
Connector isolation policies
Monitoring and anomaly detection
