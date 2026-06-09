from datetime import datetime

agent = input(
    "Agent Name: "
)

action = input(
    "Requested Action: "
)

blocked_actions = [

    "delete_records",
    "execute_command",
    "disable_guardrails"

]

if action in blocked_actions:

    result = "BLOCKED"

else:

    result = "ALLOWED"

log_entry = (

    f"{datetime.now()} | "
    f"Agent={agent} | "
    f"Action={action} | "
    f"Result={result}\n"

)

with open(
    "code/security_audit.log",
    "a"
) as log_file:

    log_file.write(
        log_entry
    )

print("\nSecurity Decision:\n")

print(result)
