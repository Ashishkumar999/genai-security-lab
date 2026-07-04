# Day 34 - STRIDE Workshop

components = {

    "User":
    "Spoofing",

    "Input Guardrail":
    "Tampering",

    "RAG":
    "Information Disclosure",

    "Memory":
    "Tampering",

    "Tools":
    "Elevation of Privilege",

    "MCP Server":
    "Denial of Service",

    "Audit Logs":
    "Repudiation"

}

print("\nAI STRIDE Workshop\n")

for component, threat in components.items():

    print(
        f"{component} -> {threat}"
    )
