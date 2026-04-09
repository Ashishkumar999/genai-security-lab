# Azure OpenAI Security Notes

Azure OpenAI provides enterprise-grade deployment controls for large language models with integrated Azure security features.

Common Security Risks

Prompt injection attacks against enterprise copilots
Unauthorized retrieval from connected data sources
Over-permissive role assignments
Exposure through logging pipelines
Connector-based data leakage

Attack Surface Areas

System prompt exposure
Plugin and connector misuse
RAG dataset leakage
Token misuse via API keys
Misconfigured Azure RBAC roles

Example Threat Scenario

An internal user queries a Copilot-connected SharePoint dataset and retrieves documents outside their authorization scope due to improper access enforcement.

Impact

Sensitive enterprise data disclosure
Internal workflow exposure
Privilege escalation across connected services
Compliance violations

Mitigation Strategies

Use Managed Identity instead of API keys
Enforce Azure RBAC least privilege access
Enable content filtering policies
Apply dataset-level access enforcement
Monitor prompt injection attempts using Defender for Cloud
