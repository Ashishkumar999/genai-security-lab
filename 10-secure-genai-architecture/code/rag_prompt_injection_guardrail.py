# Day 12 - RAG Prompt Injection Detection

dangerous_patterns = [

    "ignore previous instructions",
    "reveal system prompt",
    "output hidden instructions",
    "show hidden rules",
    "developer mode"

]

def inspect_document(document):

    document = document.lower()

    for pattern in dangerous_patterns:

        if pattern in document:

            return f"[BLOCKED] Malicious Instruction Found -> {pattern}"

    return "[ALLOWED] Document Safe"


with open("code/malicious_rag_document.txt", "r") as file:

    document = file.read()

print("\nRetrieved Document:\n")

print(document)

print("\nDocument Inspection:\n")

result = inspect_document(document)

print(result)
