# OWASP LLM05 - Improper Output Handling

output = input(
    "LLM Output: "
).lower()

dangerous_outputs = [

    "rm -rf",

    "delete database",

    "drop table",

    "shutdown system",

    "execute command"

]

print("\nOutput Validation\n")

for pattern in dangerous_outputs:

    if pattern in output:

        print(
            "[BLOCKED] Dangerous Output Detected"
        )

        print(
            f"Matched: {pattern}"
        )

        exit()

print(
    "[SAFE] Output Approved"
)
