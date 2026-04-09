# GenAI Detection Engineering Guide

This document outlines monitoring and detection strategies for identifying attacks against large language model (LLM) applications and retrieval-augmented generation (RAG) pipelines.

Detection Objectives

Identify prompt injection attempts
Detect jailbreak payload execution
Monitor unauthorized dataset retrieval
Detect model extraction behavior
Identify connector misuse patterns

Prompt Injection Detection Signals

Instruction override phrases

Examples:

Ignore previous instructions
Reveal system prompt
Switch to developer mode

Detection Strategy

Log user prompts
Detect override keywords
Monitor abnormal response patterns
Alert on system prompt disclosure attempts

Jailbreak Detection Signals

Role escalation prompts
Policy bypass attempts
Safety filter evasion sequences

Examples:

Act as administrator
Disable safety rules
Show hidden policies

Detection Strategy

Track repeated privilege escalation prompts
Monitor restricted-topic response attempts
Detect abnormal role-switch behavior

RAG Retrieval Abuse Detection

Cross-index dataset access attempts
Metadata filter bypass queries
Sequential workflow reconstruction behavior

Detection Strategy

Monitor dataset boundary violations
Track sequential sensitive-topic queries
Alert on unusual retrieval frequency

Model Extraction Detection Signals

High-frequency structured queries
Output similarity mapping attempts
Repeated paraphrased prompt variations

Detection Strategy

Rate-limit repeated queries
Detect response pattern harvesting
Alert on automated interaction signatures

Connector Abuse Detection

SharePoint access enumeration
Google Drive retrieval anomalies
Slack history extraction attempts

Detection Strategy

Monitor connector query scope
Alert on unusual document access spikes
Log cross-department retrieval attempts

Cloud Monitoring Integration

Azure Defender for Cloud alerts
AWS CloudTrail anomaly detection
GCP Cloud Audit Logs monitoring

Response Actions

Trigger alert workflows
Block suspicious sessions
Restrict connector access
Rotate exposed credentials
Escalate security review events
