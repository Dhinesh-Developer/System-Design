# simple login + token

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class LoginRequest(BaseModel):
    username: str
    password: str

USERS = {
    "dhinesh": "1234"
}    

@app.post("/login")
def login(data: LoginRequest):
    if USERS.get(data.username) != data.password:
        raise HTTPException(
            status_code=401,
            detail="Invalid credentails"
        )

    return {
        "access_token": "abc123",
        "token_type":"bearer"
    }


