from fastapi import FastAPI

app = FastAPI()

users = []

@app.get("/users")
def get_users():
    return users

@app.post("/users")
def create_user(name: str):
    user = {
        "id": len(users)+1,
        "name": name
    }
    users.append(user)
    return user

@app.delete("/users/{user_id}")
def delete_user(user_id:int):
    for user in users:
        if user["id"] == user_id:
            users.remove(user)

            return{
                "message":"User deleted"
            } 
    return {
        "message":"User not found"
    }


