# Day 20 - Agent Permission Escalation

permissions = {

    "research_agent": [
        "read_documents",
        "search_knowledge_base"
    ],

    "admin_agent": [
        "read_documents",
        "search_knowledge_base",
        "delete_records",
        "create_user"
    ]

}

agent = input(
    "Agent Name: "
).lower()

action = input(
    "Requested Action: "
).lower()

print("\nAuthorization Check:\n")

if agent not in permissions:

    print(
        "[BLOCKED] Unknown Agent"
    )

elif action in permissions[agent]:

    print(
        "[ALLOWED] Action Authorized"
    )

else:

    print(
        "[BLOCKED] Permission Escalation Attempt"
    )
