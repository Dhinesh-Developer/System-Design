
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class UserV1(BaseModel):
    name : str

class UserV2(BaseModel):
    first_name: str
    last_name: str

@app.get("/api/v1/users")
def user_v1():
    return {
        "name": "Dhinesh"
    }

@app.get("/api/v2/users")
def user_v2():
    return {
        "first_name":"Dhinesh",
        "last_name":"kumar"
    }



