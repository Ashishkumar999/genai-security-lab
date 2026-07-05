# OWASP LLM06 - Excessive Agency

action = input(
    "Requested Action: "
).lower()

restricted_actions = [

    "delete database",

    "delete users",

    "shutdown server",

    "modify permissions",

    "create admin account"

]

print("\nAgency Review\n")

for dangerous in restricted_actions:

    if dangerous in action:

        print(
            "[BLOCKED] Excessive Agency Detected"
        )

        print(
            f"Restricted Action: {dangerous}"
        )

        exit()

print(
    "[APPROVED] Action Allowed"
)
