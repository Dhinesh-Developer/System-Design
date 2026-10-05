from datetime import datetime, timedelta, timezone
import jwt

from fastapi import FastAPI,HTTPException,Depends
from fastapi.security import OAuth2PasswordBeared, OAuth2PasswordRequestForm

app = FastAPI()

SECRET_KEY = "change-this-in-production"
ALGORITHM = "HS256"

oauth2_scheme = OAuth2PasswordBeared(tokenUrl = "login")

users = {
    "dhinesh": {
        "username":"dhinesh",
        "password":"secret123",
        "role":"user"
    }
}


def create_token(username: str, role:str):
    payload = {
        "sub":username,
        "role":role,
        "exp":(
            datetime.now(timezone.utc) + timedelta(minutes=30)
        )
    }

    return jwt.encode(
        payload,SECRET_KEY,algorithm=ALGORITHM
    )

@app.post("/login")
def login(form_data:OAuth2PasswordRequestForm = Depends()):
    user = users.get(form_data.username)
    if not user:
        raise HTTPException(
            status_code = 401,
            detail = "Invalid credentials"
        )

    if user["password"] != form_data.password:
        raise HTTPException(
            status_code = 401,
            detail = "Invalid credentials"
        )

    token = create_token(
        user["username"],
        user["role"]
    )

    return {
        "access_token":token,
        "token_type":"bearer"
    }


def get_current_user(
    token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token,SECRET_KEY,algorithms=[ALGORITHM])
        return payload
    except jwt.InvalidTokenError:
        raise HTTPException(
            status_code = 401,
            detail = "Invalid token"
        )

@app.get("/profile")
def profile(current_user = Depends(get_current_user)):
    return{
        "username":current_user["sub"],
        "role":current_user["role"]
    }    




