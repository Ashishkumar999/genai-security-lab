# OWASP LLM03 - Supply Chain Vulnerabilities

packages = [

    "langchain",

    "chromadb",

    "numpy",

    "fake-langchain",

    "requests"

]

known_risky_packages = [

    "fake-langchain",

    "malicious-package",

    "test-backdoor"

]

print("\nSupply Chain Scan\n")

for package in packages:

    if package in known_risky_packages:

        print(
            f"[ALERT] Risky Package: {package}"
        )

    else:

        print(
            f"[OK] {package}"
        )
