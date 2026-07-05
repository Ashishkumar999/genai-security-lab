# Day 42 - OWASP LLM07 System Prompt Leakage

## Objective

Detect leakage of hidden system prompts.

## Example

Response:

You are a helpful assistant designed by the company.

Result:

[ALERT] System Prompt Leakage

## Test Evidence

![OWASP LLM07 System Prompt Leakage](screenshots/owasp_llm07_prompt_leakage.png)

## Risk

Attackers may discover hidden instructions and security controls.

## Security Benefit

Prompt protection and output filtering reduce exposure.

## Real World Impact

- Prompt Extraction
- Security Bypass
- Agent Manipulation
- Internal Logic Disclosure
