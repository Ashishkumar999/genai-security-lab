# Day 32 - STRIDE for RAG

rag_stride = {

    "Spoofing":
    "Unauthorized user impersonation",

    "Tampering":
    "Poisoned RAG documents",

    "Repudiation":
    "User denies retrieval requests",

    "Information Disclosure":
    "Sensitive document leakage",

    "Denial of Service":
    "Retriever overload attacks",

    "Elevation of Privilege":
    "Metadata filter bypass"

}

print("\nRAG STRIDE Threat Model\n")

for category, threat in rag_stride.items():

    print(
        f"{category}: {threat}"
    )
