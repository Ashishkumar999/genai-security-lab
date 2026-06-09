# Day 19 - Multi-Agent Security

trusted_agents = [

    "research_agent",
    "policy_agent",
    "reporting_agent"

]

sending_agent = input(
    "Sending Agent: "
).lower()

print("\nTrust Validation:\n")

if sending_agent in trusted_agents:

    print(
        "[ALLOWED] Trusted Agent"
    )

else:

    print(
        "[BLOCKED] Untrusted Agent"
    )
