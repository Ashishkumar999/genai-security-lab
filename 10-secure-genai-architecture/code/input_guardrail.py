# Day 2 - Input Guardrail v1

blocked_patterns = [
    "ignore previous instructions",
    "reveal system prompt",
    "show hidden instructions",
    "print system prompt",
    "developer mode",
    "bypass security"
]

def check_prompt(prompt):
    prompt = prompt.lower()

    for pattern in blocked_patterns:
        if pattern in prompt:
            return f"[BLOCKED] Prompt Injection Detected -> {pattern}"

    return "[ALLOWED] Prompt Accepted"


while True:
    print("\n==============================")
    user_prompt = input("Enter Prompt: ")

    result = check_prompt(user_prompt)

    print(result)
