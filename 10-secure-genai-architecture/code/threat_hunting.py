# Day 23 - AI Threat Hunting

from collections import Counter

suspicious_patterns = [

    "ignore",
    "reveal",
    "developer",
    "hidden"

]

events = []

with open(
    "code/ai_security_events.log",
    "r"
) as file:

    events = file.readlines()

user_counter = Counter()

for event in events:

    lower_event = event.lower()

    for pattern in suspicious_patterns:

        if pattern in lower_event:

            user = event.split("|")[0]

            user_counter[user] += 1

print("\nThreat Hunting Results:\n")

for user, count in user_counter.items():

    if count >= 2:

        print(
            f"[SUSPICIOUS] {user} "
            f"triggered {count} events"
        )
