# Day 26 - Architecture Review

controls = {

    "Input Guardrail": True,

    "Output Guardrail": True,

    "Metadata Filter": True,

    "Tool Authorization": True,

    "Audit Logging": True,

    "Memory Validation": False

}

print("\nArchitecture Review\n")

for control, status in controls.items():

    if status:

        print(
            f"[PASS] {control}"
        )

    else:

        print(
            f"[FAIL] {control}"
        )
