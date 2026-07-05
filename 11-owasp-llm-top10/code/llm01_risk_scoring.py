# OWASP LLM01 Risk Scoring

prompt = input(
    "Enter Prompt: "
).lower()

score = 0

patterns = {

    "ignore previous instructions": 5,

    "reveal system prompt": 5,

    "developer mode": 4,

    "show hidden instructions": 4,

    "bypass security": 5,

    "disable guardrails": 5

}

for pattern, risk in patterns.items():

    if pattern in prompt:

        score += risk

print("\nPrompt Analysis\n")

print(
    f"Risk Score: {score}"
)

if score >= 10:

    print("[CRITICAL] Block Prompt")

elif score >= 5:

    print("[HIGH] Review Prompt")

else:

    print("[LOW] Accept Prompt")
