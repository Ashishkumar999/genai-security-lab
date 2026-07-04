# Day 27 - AI Risk Assessment

threats = {

    "Prompt Injection": {
        "likelihood": 5,
        "impact": 4
    },

    "Sensitive Data Leakage": {
        "likelihood": 4,
        "impact": 5
    },

    "Tool Abuse": {
        "likelihood": 3,
        "impact": 5
    },

    "Memory Poisoning": {
        "likelihood": 3,
        "impact": 3
    }

}

print("\nAI Risk Assessment\n")

for threat, values in threats.items():

    score = (
        values["likelihood"]
        * values["impact"]
    )

    print(
        f"{threat}: Risk Score = {score}"
    )
