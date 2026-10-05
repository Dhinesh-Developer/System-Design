import bcrypt

password = "secret123"

password_bytes = password.encode()
hashed = bcrypt.hashpw(
    password_bytes,bcrypt.gensalt()
)

print(hashed)
# b'$2b$12$4P4Sl2YfjDm2lOf7M7Uwx.e5Dd530PSsjKEbiZrVANrn5lpVR/KOq'