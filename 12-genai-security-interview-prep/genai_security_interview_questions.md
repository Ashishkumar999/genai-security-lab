# GenAI Security Interview Question Bank

This document contains commonly asked interview questions and structured answers for GenAI Security Engineer roles.

What is prompt injection?

Prompt injection is an attack where a malicious user manipulates model behavior by inserting instructions that override system prompts or safety policies. It can lead to system prompt leakage, connector abuse, or restricted workflow disclosure.

What is a jailbreak attack?

A jailbreak attack attempts to bypass LLM safety guardrails using role escalation or instruction override techniques to access restricted responses or hidden policies.

What is cross-index leakage in RAG systems?

Cross-index leakage occurs when a retrieval system returns documents from unauthorized datasets due to improper access control enforcement between knowledge sources.

What is metadata filter bypass?

Metadata filter bypass occurs when attackers craft queries that evade dataset-level filtering rules, allowing retrieval of restricted documents.

What is chunk stitching?

Chunk stitching is a reconstruction attack where attackers combine multiple partial responses to reveal sensitive workflows or internal policies.

What is model extraction?

Model extraction is an attack where adversaries repeatedly query an LLM to replicate its behavior and approximate proprietary logic or training characteristics.

How do connectors increase GenAI attack surface?

Connectors integrate external data sources such as SharePoint, Google Drive, or Slack. Misconfigured connectors can expose sensitive enterprise data through retrieval pipelines.

What are major GenAI cloud security risks?

IAM misconfiguration
Dataset permission failures
Service account exposure
Connector misuse
Logging pipeline leakage

How do you secure a RAG pipeline?

Apply dataset-level authorization
Enforce metadata filtering
Monitor retrieval boundaries
Detect sequential sensitive queries
Log dataset access patterns

How do you detect prompt injection attempts?

Monitor override keywords
Track abnormal prompt sequences
Alert on system prompt disclosure attempts
Analyze repeated privilege escalation prompts

What is the role of detection engineering in GenAI security?

Detection engineering helps identify prompt injection attempts, jailbreak payload execution, connector misuse, and model extraction behavior using monitoring pipelines and anomaly detection systems.

How do you secure enterprise LLM deployments?

Use least privilege IAM roles
Isolate connectors
Protect system prompts
Apply output filtering
Enable monitoring and alerting pipelines
