# Day 46 - AI Security Scanner Engine

prompt = input("Enter Prompt: ").lower()

checks = {

    "Prompt Injection": [
        "ignore previous instructions",
        "developer mode",
        "reveal system prompt"
    ],

    "Sensitive Data Request": [
        "password",
        "api key",
        "secret",
        "token"
    ],

    "System Prompt Extraction": [
        "show hidden instructions",
        "system prompt",
        "internal instructions"
    ],

    "Excessive Agency": [
        "delete database",
        "shutdown server",
        "create admin account"
    ]

}

print("\n===== AI Security Scan =====\n")

issues_found = 0

for category, patterns in checks.items():

    for pattern in patterns:

        if pattern in prompt:

            print(f"[ALERT] {category}")

            print(f"Matched: {pattern}\n")

            issues_found += 1

if issues_found == 0:

    print("[SAFE] No security issues detected.")

else:

    print(f"Total Issues Found: {issues_found}")
