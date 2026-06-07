# Day 17 - Agent Memory Security

blocked_patterns = [

    "password",
    "api key",
    "secret",
    "token",
    "credit card"

]

memory_entry = input(
    "Memory To Store: "
).lower()

print("\nMemory Inspection:\n")

for pattern in blocked_patterns:

    if pattern in memory_entry:

        print(
            "[BLOCKED] Sensitive Memory Entry"
        )
        exit()

print(
    "[ALLOWED] Memory Stored"
)
