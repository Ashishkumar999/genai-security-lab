# Day 6 - Regex Based Guardrails

## Objective

Improve prompt injection detection using regex pattern matching.

## Why Regex?

Keyword matching only detects exact phrases.

Regex detects variations of the same attack.

## Example

Pattern:

ignore.*previous.*instructions

Matches:

- Ignore previous instructions
- Ignore all previous instructions
- Ignore internal previous instructions

## Test Evidence

![Regex Guardrail Test](screenshots/regex_guardrail_testing.png)

### Blocked

- Ignore previous instructions
- Please ignore all previous instructions
- Reveal system prompt
- Developer mode

### Allowed

- What is SQL Injection?
- Explain OWASP Top 10

## Security Benefit

Regex-based detection improves resilience against simple prompt injection bypass attempts.

## Limitation

Regex still cannot understand meaning and may miss semantic prompt injection attacks.
