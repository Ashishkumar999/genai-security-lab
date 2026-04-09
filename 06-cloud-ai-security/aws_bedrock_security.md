# AWS Bedrock Security Notes

AWS Bedrock enables secure enterprise access to foundation models through managed infrastructure and IAM-based access control.

Common Security Risks

Over-permissive IAM roles
Unauthorized model invocation
Prompt injection through application inputs
Sensitive data leakage via RAG pipelines
Cross-service data exposure through integrations

Attack Surface Areas

Foundation model invocation APIs
IAM policy misconfiguration
Knowledge base retrieval pipelines
Lambda integrations
S3-connected document sources

Example Threat Scenario

An application role with excessive Bedrock permissions allows unauthorized users to invoke restricted foundation models or retrieve sensitive embeddings from connected S3 knowledge bases.

Impact

Unauthorized model usage
Sensitive document exposure
Privilege escalation across AWS services
Increased operational cost through abuse

Mitigation Strategies

Apply least privilege IAM policies
Restrict model invocation permissions
Use VPC endpoints for Bedrock access
Enable CloudTrail logging for monitoring
Encrypt knowledge base storage with KMS
