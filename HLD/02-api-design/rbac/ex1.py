permissions = {
    "admin": [
        "read","write","delete"
    ],

    "user": ["read"]
}

role = "user"

if "delete" in permissions[role]:
    print("Allowed")
else:
    print("Forbidden")    


