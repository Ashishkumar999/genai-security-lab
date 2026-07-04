# OWASP LLM01 - Prompt Injection

prompt = input(
    "Enter Prompt: "
).lower()

attack_patterns = [

    "ignore previous instructions",

    "reveal system prompt",

    "developer mode",

    "show hidden instructions"

]

print("\nAnalysis:\n")

for pattern in attack_patterns:

    if pattern in prompt:

        print(
            "[ALERT] Prompt Injection Detected"
        )
        exit()

print(
    "[SAFE] Prompt Accepted"
)
