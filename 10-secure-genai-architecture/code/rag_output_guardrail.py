import re

sensitive_patterns = [

    r"\d{3}-\d{2}-\d{4}",

    r"salary",

    r"api key",

    r"medical condition"

]

def inspect_response(response):

    response = response.lower()

    for pattern in sensitive_patterns:

        if re.search(pattern, response):

            return "[BLOCKED] Sensitive Data Detected"

    return "[ALLOWED] Response Safe"


with open("code/rag_documents.txt", "r") as file:

    document = file.read()

print("\nRetrieved Document:\n")

print(document)

print("\nSecurity Check:\n")

result = inspect_response(document)

print(result)
