# Day 7 - Semantic Guardrails

## Objective

Move beyond keyword and regex matching by grouping prompt injection attempts into attack categories.

## Categories

### Instruction Override

- Ignore previous instructions
- Forget previous instructions
- Start over
- Disregard instructions

### System Prompt Extraction

- Reveal system prompt
- Show hidden instructions
- Show hidden rules

### Security Bypass

- Developer mode
- Bypass security
- Remove restrictions

## Test Evidence

![Semantic Guardrail Test](screenshots/semantic_guardrail_testing.png)

### Blocked

- Ignore previous instructions
- Forget previous instructions
- Show hidden rules
- Remove restrictions

### Allowed

- What is SQL Injection?
- Explain OWASP Top 10

## Observation

Categorizing attacks provides better coverage than simple keyword matching.

## Limitation

The implementation still relies on predefined phrases and cannot fully understand language intent.

## Future Improvement

Use embeddings and LLM classifiers to understand semantic meaning.
