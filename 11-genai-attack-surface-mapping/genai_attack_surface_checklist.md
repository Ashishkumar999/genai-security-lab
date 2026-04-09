# GenAI Attack Surface Mapping Checklist

This checklist helps identify exposed attack surfaces in large language model (LLM) and retrieval-augmented generation (RAG) applications.

Model Layer

Identify model provider (OpenAI, Azure OpenAI, Bedrock, Vertex AI)
Check model access authentication method
Review token exposure risks
Test model rate limiting controls

Prompt Layer

Check system prompt exposure risks
Test prompt reflection vulnerabilities
Attempt instruction override payloads
Attempt jailbreak payload execution

Application Layer

Enumerate exposed API endpoints
Test session handling logic
Check authentication enforcement
Test role-based access control boundaries

Retrieval Layer (RAG)

Identify connected knowledge bases
Test metadata filtering enforcement
Attempt cross-index leakage
Attempt chunk stitching reconstruction

Connector Layer

Identify SharePoint integrations
Identify Google Drive connectors
Identify Slack connectors
Test connector scope enforcement

Cloud Layer

Review IAM role permissions
Check service account exposure
Validate dataset-level access controls
Review logging pipeline exposure risks

Monitoring Layer

Check prompt logging coverage
Verify anomaly detection alerts
Review connector access monitoring
Confirm dataset retrieval audit trails

Output Handling Layer

Check response filtering controls
Test policy enforcement mechanisms
Validate sensitive data redaction
Monitor structured output leakage
