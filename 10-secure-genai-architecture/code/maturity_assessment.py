# Day 30 - AI Security Maturity Assessment

controls = {

    "Input Guardrails": True,

    "Output Guardrails": True,

    "RAG Security": True,

    "Agent Security": True,

    "Audit Logging": True,

    "Threat Hunting": True,

    "Incident Response": True,

    "Governance": True,

    "Metrics": True

}

score = sum(controls.values())

print("\nAI Security Maturity Assessment\n")

print(f"Controls Implemented: {score}/9")

if score <= 2:

    level = "Level 1 - Initial"

elif score <= 4:

    level = "Level 2 - Developing"

elif score <= 6:

    level = "Level 3 - Defined"

elif score <= 8:

    level = "Level 4 - Managed"

else:

    level = "Level 5 - Optimized"

print(f"Maturity Level: {level}")
