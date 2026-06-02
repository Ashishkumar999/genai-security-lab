# Day 3 - Output Guardrail

sensitive_patterns = [
    "password",
    "api key",
    "secret",
    "token",
    "ssn",
    "credit card"
]

def check_output(response):

    response = response.lower()

    for pattern in sensitive_patterns:

        if pattern in response:

            return f"[BLOCKED] Sensitive Data Detected -> {pattern}"

    return "[ALLOWED] Response Safe"


while True:

    print("\n==============================")

    model_response = input("Enter LLM Response: ")

    result = check_output(model_response)

    print(result)
