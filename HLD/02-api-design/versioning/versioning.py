from fastapi import FastAPI,APIRouter
app = FastAPI()

v1 = APIRouter(prefix="/api/v1")
v2 = APIRouter(prefix="/api/v2")

@v1.get("/users")
def users_v1():
    return {
        "version":"v1",
        "users": ["Dhinesh"]
    }

@v2.get("/users")
def users_v2():
    return {
        "version": "v2",
        "users": [
            {
                "id":1,
                "name":"Dhinesh"
            }
        ]
    }

app.include_router(v1)
app.include_router(v2)

