from fastapi import FastAPI

app = FastAPI()

@app.get("/api/v1/users")
def users_v1():
    return {
        "name": "Dhinesh"
    }

@app.get("/api/v2/users")
def users_v2():
    return {
        "first_name": "Dhinesh",
        "last_name": "Kumar"
    }



