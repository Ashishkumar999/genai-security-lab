# Vertex AI Security Notes

Google Vertex AI provides managed access to foundation models with integrated IAM, VPC isolation, and enterprise data governance controls.

Common Security Risks

Over-permissive IAM roles
Unauthorized dataset access
Prompt injection through application inputs
Training data leakage
Misconfigured service accounts

Attack Surface Areas

Vertex AI prediction endpoints
Service account permissions
Connected BigQuery datasets
Cloud Storage knowledge sources
RAG pipelines using enterprise documents

Example Threat Scenario

A misconfigured service account allows access to restricted BigQuery datasets connected to a Vertex AI retrieval pipeline, exposing sensitive enterprise records.

Impact

Sensitive dataset disclosure
Unauthorized model interaction
Cross-project data exposure
Privilege escalation across GCP services

Mitigation Strategies

Apply least privilege IAM roles
Restrict service account scope
Enable VPC Service Controls
Monitor access using Cloud Audit Logs
Enforce dataset-level authorization checks
