# Day 37 - OWASP LLM02 Sensitive Information Disclosure

## Objective

Detect sensitive information in LLM responses.

## Example

Response:

API_KEY=123456789

Result:

[ALERT] Sensitive Information Detected

## Test Evidence

![OWASP LLM02 Sensitive Information Disclosure](screenshots/owasp_llm02_detection.png)

## Risk

Sensitive information may expose credentials, customer data, or internal secrets.

## Security Benefit

Output scanning helps prevent accidental disclosure.
