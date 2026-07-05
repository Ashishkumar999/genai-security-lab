# OWASP LLM09 - Misinformation

known_facts = {

    "python creator":
    "guido van rossum",

    "linux creator":
    "linus torvalds",

    "owasp":
    "open worldwide application security project"

}

topic = input(
    "Topic: "
).lower()

answer = input(
    "LLM Answer: "
).lower()

print("\nFact Verification\n")

if topic in known_facts:

    if answer == known_facts[topic]:

        print(
            "[VERIFIED] Information Matches"
        )

    else:

        print(
            "[WARNING] Potential Misinformation"
        )

else:

    print(
        "[UNKNOWN] No Reference Data"
    )
