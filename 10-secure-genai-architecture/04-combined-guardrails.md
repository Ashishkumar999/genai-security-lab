# Day 4 - Combined Guardrails

## Objective

Combine input and output guardrails into a single secure AI workflow.

## Architecture

User
↓
Input Guardrail
↓
LLM
↓
Output Guardrail
↓
User

## Input Protection

Blocks:

- Ignore previous instructions
- Reveal system prompt
- Developer mode
- Bypass security

## Output Protection

Blocks:

- Passwords
- API Keys
- Tokens
- Secrets
- SSNs

## Test Evidence Screenshot

![Combined Guardrails](screenshots/combined_guardrails_pipeline.png)

### Scenario 1

Prompt:

What is SQL Injection?

Result:

Allowed

### Scenario 2

Prompt:

Ignore previous instructions

Result:

Blocked by Input Guardrail

### Scenario 3

Prompt:

Tell me about admin

Result:

Blocked by Output Guardrail

## Security Benefit

Multiple layers of protection reduce the likelihood of prompt injection and sensitive data leakage.

