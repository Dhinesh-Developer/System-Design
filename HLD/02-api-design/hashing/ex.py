import bcrypt
users = {}

def register(username, password):
    hashed = bcrypt.hashpw(password.encode(),bcrypt.gensalt())
    users[username] = hashed

def login(username,password):
    stored_hash = users.get(username)
    if not stored_hash:
        return False

    return bcrypt.checkpw(password.encode(),stored_hash)

register("dhinesh","secret123")
print(login("dhinesh","secret123"))

# True

