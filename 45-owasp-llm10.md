# Day 45 - OWASP LLM10 Unbounded Consumption

## Objective

Prevent excessive resource consumption by limiting prompt size.

## Example

Prompt:

(145-word prompt)

Result:

[BLOCKED] Prompt Too Large

## Test Evidence

![OWASP LLM10 Unbounded Consumption](screenshots/owasp_llm10_unbounded_consumption.png)

## Risk

Unlimited prompts may consume excessive compute resources, increase costs, and degrade service availability.

## Security Benefit

Prompt size limits and rate limiting help protect AI systems from resource exhaustion attacks.

## Real World Examples

- Excessive Token Usage
- API Abuse
- Resource Exhaustion
- Denial of Service
