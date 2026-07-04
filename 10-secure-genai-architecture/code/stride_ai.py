# Day 31 - STRIDE for AI Systems

stride = {

    "Spoofing":
    "Fake users or agents",

    "Tampering":
    "Prompt injection or memory poisoning",

    "Repudiation":
    "User denies malicious actions",

    "Information Disclosure":
    "Sensitive data leakage",

    "Denial of Service":
    "Prompt flooding or token exhaustion",

    "Elevation of Privilege":
    "Unauthorized tool execution"

}

print("\nSTRIDE Threat Model\n")

for category, example in stride.items():

    print(
        f"{category}: {example}"
    )
