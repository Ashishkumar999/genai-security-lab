# Day 4 - Combined Guardrails

blocked_input_patterns = [
    "ignore previous instructions",
    "reveal system prompt",
    "show hidden instructions",
    "developer mode",
    "bypass security"
]

sensitive_output_patterns = [
    "password",
    "api key",
    "secret",
    "token",
    "ssn"
]


def input_guardrail(prompt):

    prompt = prompt.lower()

    for pattern in blocked_input_patterns:

        if pattern in prompt:

            return False, f"[BLOCKED] Input Guardrail -> {pattern}"

    return True, "Input Passed"


def fake_llm(prompt):

    if "admin" in prompt.lower():
        return "The admin password is Admin123"

    return "Hello, I am a secure AI assistant."


def output_guardrail(response):

    response = response.lower()

    for pattern in sensitive_output_patterns:

        if pattern in response:

            return False, f"[BLOCKED] Output Guardrail -> {pattern}"

    return True, response


while True:

    print("\n==============================")

    user_prompt = input("Enter Prompt: ")

    allowed, result = input_guardrail(user_prompt)

    if not allowed:
        print(result)
        continue

    llm_response = fake_llm(user_prompt)

    allowed, result = output_guardrail(llm_response)

    if not allowed:
        print(result)
        continue

    print("[FINAL RESPONSE]")
    print(result)
