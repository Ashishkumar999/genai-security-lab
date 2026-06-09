# Day 24 - AI Incident Response

incident_types = {

    "prompt_injection": "HIGH",

    "sensitive_data_leakage": "CRITICAL",

    "tool_abuse": "HIGH",

    "memory_poisoning": "MEDIUM",

    "unauthorized_agent": "HIGH"

}

incident = input(
    "Incident Type: "
).lower()

print("\nIncident Response:\n")

if incident in incident_types:

    severity = incident_types[incident]

    print(
        f"Severity: {severity}"
    )

    if severity == "CRITICAL":

        print(
            "Action: Disable AI Service Immediately"
        )

    elif severity == "HIGH":

        print(
            "Action: Investigate and Contain"
        )

    else:

        print(
            "Action: Monitor and Review"
        )

else:

    print(
        "Unknown Incident Type"
    )
