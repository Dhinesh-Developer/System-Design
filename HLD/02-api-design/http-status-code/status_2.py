from fastapi import FastAPI, status

app = FastAPI()

@app.post(
    "/users",
    status_code=status.HTTP_201_CREATED
)
def create_user(name: str):

    return {
        "message":"User created",
        "name": name
    }

