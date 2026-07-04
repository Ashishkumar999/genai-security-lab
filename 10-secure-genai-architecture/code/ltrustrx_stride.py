# Day 35 - LtrustRx STRIDE Model

stride_model = {

    "Web Dashboard":
    "Spoofing",

    "API Layer":
    "Tampering",

    "AI Risk Engine":
    "Denial of Service",

    "LLM":
    "Prompt Injection",

    "Policy Engine":
    "Elevation of Privilege",

    "Database":
    "Information Disclosure",

    "Audit Logs":
    "Repudiation"

}

print("\nLtrustRx STRIDE Threat Model\n")

for component, threat in stride_model.items():

    print(
        f"{component} -> {threat}"
    )
