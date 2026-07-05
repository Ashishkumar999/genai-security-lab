# OWASP LLM04 - Data Poisoning

document = input(
    "Document Content: "
).lower()

poison_patterns = [

    "ignore previous instructions",

    "reveal confidential data",

    "disable security",

    "bypass authentication",

    "developer mode"

]

print("\nDocument Analysis\n")

for pattern in poison_patterns:

    if pattern in document:

        print(
            "[ALERT] Potential Data Poisoning"
        )

        print(
            f"Matched: {pattern}"
        )

        exit()

print(
    "[SAFE] No Poisoning Indicators"
)
