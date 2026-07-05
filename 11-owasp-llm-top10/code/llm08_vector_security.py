# OWASP LLM08 - Vector Security

user_role = input(
    "User Role: "
).lower()

document_type = input(
    "Requested Document: "
).lower()

permissions = {

    "hr": ["employee records"],

    "finance": ["financial reports"],

    "admin": [
        "employee records",
        "financial reports"
    ]

}

print("\nVector Access Review\n")

if (
    user_role in permissions
    and document_type
    in permissions[user_role]
):

    print(
        "[APPROVED] Retrieval Allowed"
    )

else:

    print(
        "[BLOCKED] Unauthorized Retrieval"
    )
