# Day 9 - LLM Judge Simulation

suspicious_intents = [

    "ignore previous instructions",
    "reveal system prompt",
    "show hidden instructions",
    "developer mode",
    "bypass security",
    "remove restrictions"

]

def judge_prompt(prompt):

    prompt = prompt.lower()

    for item in suspicious_intents:

        if item in prompt:

            return "UNSAFE"

    return "SAFE"


while True:

    print("\n======================")

    user_prompt = input("Enter Prompt: ")

    verdict = judge_prompt(user_prompt)

    print(f"Judge Verdict: {verdict}")

    if verdict == "UNSAFE":

        print("[BLOCKED] Prompt rejected")

    else:

        print("[ALLOWED] Prompt accepted")
