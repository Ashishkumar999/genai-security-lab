# Day 16 - MCP Security

allowed_tools = [

    "read_document",
    "search_knowledge_base",
    "retrieve_policy"

]

requested_tool = input(
    "MCP Tool Request: "
).lower()

print("\nPermission Check:\n")

if requested_tool in allowed_tools:

    print(
        "[ALLOWED] MCP Tool Authorized"
    )

else:

    print(
        "[BLOCKED] Unauthorized MCP Tool"
    )
