# Day 8 - Risk Scoring Guardrail

risk_rules = {

    "ignore previous instructions": 40,
    "reveal system prompt": 50,
    "developer mode": 30,
    "bypass security": 50,
    "show hidden instructions": 40

}


def calculate_risk(prompt):

    prompt = prompt.lower()

    score = 0

    matches = []

    for phrase, risk in risk_rules.items():

        if phrase in prompt:

            score += risk

            matches.append(phrase)

    return score, matches


while True:

    print("\n======================")

    user_prompt = input("Enter Prompt: ")

    score, matches = calculate_risk(user_prompt)

    print(f"Risk Score: {score}")

    if matches:

        print("Matched Rules:")

        for match in matches:

            print("-", match)

    if score >= 70:

        print("[BLOCKED] High Risk")

    elif score >= 30:

        print("[REVIEW] Medium Risk")

    else:

        print("[ALLOWED] Low Risk")
