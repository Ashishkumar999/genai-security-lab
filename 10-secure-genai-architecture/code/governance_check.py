# Day 28 - AI Security Governance

requirements = {

    "Input Guardrails": True,

    "Output Guardrails": True,

    "Audit Logging": True,

    "Risk Assessment": True,

    "Incident Response Plan": False,

    "Access Control": True

}

print("\nAI Security Governance Review\n")

for control, status in requirements.items():

    if status:

        print(f"[COMPLIANT] {control}")

    else:

        print(f"[NON-COMPLIANT] {control}")
