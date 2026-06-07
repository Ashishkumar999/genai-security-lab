# Day 18 - Memory Poisoning Detection

dangerous_memory_patterns = [

    "all users are administrators",

    "ignore security alerts",

    "disable guardrails",

    "always allow access",

    "bypass authentication"

]

memory_entry = input(
    "Memory Entry: "
).lower()

print("\nMemory Security Check:\n")

for pattern in dangerous_memory_patterns:

    if pattern in memory_entry:

        print(
            "[BLOCKED] Memory Poisoning Detected"
        )
        exit()

print(
    "[ALLOWED] Memory Entry Stored"
)
