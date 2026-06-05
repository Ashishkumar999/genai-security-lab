# Day 7 - Semantic Style Guardrail

attack_intents = {

    "instruction_override": [
        "ignore previous instructions",
        "forget previous instructions",
        "start over",
        "disregard instructions",
        "new instructions only"
    ],

    "system_prompt_extraction": [
        "reveal system prompt",
        "show hidden instructions",
        "show hidden rules",
        "display internal prompt"
    ],

    "security_bypass": [
        "developer mode",
        "bypass security",
        "remove restrictions",
        "unrestricted mode"
    ]
}


def check_prompt(prompt):

    prompt = prompt.lower()

    for category, phrases in attack_intents.items():

        for phrase in phrases:

            if phrase in prompt:

                return f"[BLOCKED] Semantic Category Detected -> {category}"

    return "[ALLOWED] Prompt Accepted"


while True:

    print("\n=======================")

    user_prompt = input("Enter Prompt: ")

    result = check_prompt(user_prompt)

    print(result)
