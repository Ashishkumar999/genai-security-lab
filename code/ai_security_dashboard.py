# Day 47 - AI Security Risk Dashboard

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

risk_score = 0
findings = []

print("\n========== AI Security Dashboard ==========\n")

for category, patterns in checks.items():

    for pattern in patterns:

        if pattern in prompt:

            findings.append(category)

            risk_score += 25

if risk_score == 0:

    severity = "LOW"

elif risk_score <= 25:

    severity = "MEDIUM"

elif risk_score <= 50:

    severity = "HIGH"

else:

    severity = "CRITICAL"

print(f"Risk Score : {risk_score}/100")

print(f"Severity   : {severity}")

print("\nFindings:")

if findings:

    for finding in set(findings):

        print(f"- {finding}")

else:

    print("- No security issues detected")

print("\nScan Completed")
