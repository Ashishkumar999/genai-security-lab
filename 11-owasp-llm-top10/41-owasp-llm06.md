# Day 41 - OWASP LLM06 Excessive Agency

## Objective

Detect AI agents with excessive permissions.

## Example

Action:

Delete database

Result:

[BLOCKED] Excessive Agency Detected

## Test Evidence

![OWASP LLM06 Excessive Agency](screenshots/owasp_llm06_excessive_agency.png)

## Risk

Agents with excessive authority may perform destructive or unauthorized actions.

## Security Benefit

Authorization checks and approval workflows reduce risk.

## Real World Examples

- Database Deletion
- Unauthorized User Creation
- Policy Modification
- Cloud Resource Manipulation
