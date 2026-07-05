# OWASP LLM10 - Unbounded Consumption

MAX_WORDS = 100

prompt = input("Enter Prompt: ")

word_count = len(prompt.split())

print("\nPrompt Analysis\n")

print(f"Word Count: {word_count}")

if word_count > MAX_WORDS:

    print("[BLOCKED] Prompt Too Large")

else:

    print("[SAFE] Prompt Accepted")
