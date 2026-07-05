# OWASP LLM02 - Sensitive Information Disclosure

response = input(
    "LLM Response: "
)

sensitive_patterns = [

    "password",

    "api_key",

    "secret",

    "token",

    "ssn",

    "credit card"

]

print("\nOutput Analysis\n")

for pattern in sensitive_patterns:

    if pattern.lower() in response.lower():

        print(
            "[ALERT] Sensitive Information Detected"
        )

        print(
            f"Matched: {pattern}"
        )

        exit()

print(
    "[SAFE] No Sensitive Data Found"
)
