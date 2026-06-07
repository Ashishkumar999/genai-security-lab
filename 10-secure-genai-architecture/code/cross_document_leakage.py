import re

with open("code/retrieved_chunks.txt", "r") as file:

    data = file.read()

patients = re.findall(
    r"Patient:\s*(.*)",
    data
)

print("\nRetrieved Patients:\n")

for patient in patients:

    print(patient)

print("\nSecurity Check:\n")

if len(patients) > 1:

    print(
        "[BLOCKED] Cross-Document Data Leakage Detected"
    )

else:

    print(
        "[ALLOWED] Single Patient Record"
    )
