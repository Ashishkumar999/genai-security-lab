# Day 14 - Cross Document Data Leakage

## Objective

Detect situations where retrieved RAG documents contain data belonging to multiple users.

## Threat

Multiple user records may be retrieved and exposed through a single query.

## Example

Patient: John Smith

Diagnosis: Diabetes

Patient: Sarah Jones

Diagnosis: Cancer

## Detection Result

[BLOCKED] Cross-Document Data Leakage Detected

## Test Evidence

![Cross Document Leakage](screenshots/cross_document_leakage_detected.png)


## Security Benefit

Prevents exposure of unrelated user records through RAG retrieval.

## Real World Impact

Cross-document leakage can expose:

- Patient Records
- Financial Information
- HR Data
- Internal Enterprise Information

Proper validation should occur before sending retrieved documents to the LLM.
