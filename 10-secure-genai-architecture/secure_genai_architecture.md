# Secure GenAI Architecture Design Patterns

This document describes recommended architecture patterns for building secure large language model (LLM) applications in enterprise environments.

Security Objectives

Protect system prompts
Prevent unauthorized dataset retrieval
Control connector exposure
Detect prompt injection attempts
Limit model abuse and extraction risks

Secure GenAI Reference Architecture Layers

Layer 1 — User Input Validation Layer

Apply prompt sanitization
Filter injection keywords
Enforce schema-based input validation
Detect role escalation attempts

Layer 2 — Prompt Security Layer

Separate system prompts from user prompts
Store system prompts securely
Prevent prompt reflection in outputs
Apply prompt templating controls

Layer 3 — Retrieval Security Layer (RAG Protection)

Enforce dataset-level authorization
Apply metadata filtering
Prevent cross-index retrieval leakage
Monitor sequential sensitive queries

Layer 4 — Model Access Control Layer

Restrict API access using identity-aware policies
Apply token usage limits
Detect automated query behavior
Prevent model extraction attempts

Layer 5 — Connector Isolation Layer

Restrict SharePoint connector scope
Limit Google Drive dataset access
Apply Slack message visibility filters
Monitor cross-source retrieval attempts

Layer 6 — Cloud Security Layer

Use least privilege IAM roles
Enable private endpoints
Encrypt embeddings storage
Rotate API credentials regularly

Layer 7 — Monitoring and Detection Layer

Log prompt activity
Detect jailbreak attempts
Track dataset boundary violations
Monitor connector access anomalies

Example Secure Deployment Pattern

User → Input Filter → Prompt Template Engine → Authorization Check → RAG Retrieval Filter → LLM → Output Filter → Monitoring Pipeline

Architecture Benefits

Reduces prompt injection risk
Prevents connector data leakage
Protects system prompt confidentiality
Limits model abuse exposure
Improves monitoring visibility
