# Day 22 - Detection Engineering

attack_patterns = [

    "ignore previous instructions",
    "reveal system prompt",
    "developer mode"

]

prompt = input(
    "User Prompt: "
).lower()

print("\nDetection Engine:\n")

for pattern in attack_patterns:

    if pattern in prompt:

        print(
            "[ALERT] Prompt Injection Detected"
        )
        exit()

print(
    "[NO ALERT] Clean Prompt"
)
