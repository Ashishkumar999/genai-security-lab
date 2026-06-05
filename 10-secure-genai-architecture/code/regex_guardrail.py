import re

patterns = [
    r"ignore.*previous.*instructions",
    r"reveal.*system.*prompt",
    r"show.*hidden.*instructions",
    r"developer.*mode",
    r"bypass.*security"
]

def check_prompt(prompt):

    prompt = prompt.lower()

    for pattern in patterns:

        if re.search(pattern, prompt):

            return f"[BLOCKED] Regex Match -> {pattern}"

    return "[ALLOWED] Prompt Accepted"


while True:

    print("\n========================")

    user_prompt = input("Enter Prompt: ")

    result = check_prompt(user_prompt)

    print(result)
