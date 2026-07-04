# Day 29 - AI Security Metrics

metrics = {

    "Prompt Injections Blocked": 120,

    "Sensitive Data Leaks": 0,

    "Unauthorized Tool Calls": 3,

    "Memory Poisoning Attempts": 5,

    "Incident Response Cases": 2

}

print("\nAI Security KPI Dashboard\n")

for metric, value in metrics.items():

    print(
        f"{metric}: {value}"
    )
