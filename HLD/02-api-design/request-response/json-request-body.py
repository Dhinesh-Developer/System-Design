from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    name: str
    age: int
    city: str

@app.post("/users")
def create_user(user: User):
    return {
        "message": "User created",
        "user": user
    }

