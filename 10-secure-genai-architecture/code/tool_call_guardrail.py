allowed_tools = [

    "search_documents",
    "get_policy",
    "retrieve_faq"

]

requested_tool = input(
    "Requested Tool: "
).lower()

print("\nSecurity Check:\n")

if requested_tool not in allowed_tools:

    print(
        "[BLOCKED] Unauthorized Tool Call"
    )

else:

    print(
        "[ALLOWED] Tool Authorized"
    )
