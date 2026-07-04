# Day 33 - STRIDE for AI Agents

agent_stride = {

    "Spoofing":
    "Fake agent identity",

    "Tampering":
    "Memory poisoning or tool manipulation",

    "Repudiation":
    "Agent actions without audit logs",

    "Information Disclosure":
    "Sensitive memory leakage",

    "Denial of Service":
    "Infinite agent loops",

    "Elevation of Privilege":
    "Unauthorized tool execution"

}

print("\nAgent STRIDE Threat Model\n")

for category, threat in agent_stride.items():

    print(
        f"{category}: {threat}"
    )
