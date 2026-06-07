documents = [

    {
        "department": "hr",
        "content": "Employee Leave Policy"
    },

    {
        "department": "finance",
        "content": "Annual Revenue Report"
    },

    {
        "department": "engineering",
        "content": "Internal System Architecture"
    }

]

user_department = "hr"

requested_department = input(
    "Enter Department To Access: "
).lower()

if requested_department != user_department:

    print(
        "[BLOCKED] Unauthorized Metadata Access"
    )

else:

    print(
        "\nAccessible Documents:\n"
    )

    for doc in documents:

        if doc["department"] == requested_department:

            print(doc["content"])
