import bcrypt

password = "secret123"

hashed = bcrypt.hashpw(
    password.encode(),
    bcrypt.gensalt()
)

if bcrypt.checkpw(
    password.encode(),
    hashed
):
    print("password correct")
else:
    print("wrong password")


# password correct