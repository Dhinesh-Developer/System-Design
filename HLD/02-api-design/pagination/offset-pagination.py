
from fastapi import FastAPI
app = FastAPI()

users = [
    f"User-{i}"
    for i in range(1, 101)
]

@app.get("/users")
def get_users(page:int = 1,limit:int = 10):
    start = (page - 1) * limit
    end = start + limit

    return {
        "page":page,
        "limit":limit,
        "user":users[start:end]
    }





