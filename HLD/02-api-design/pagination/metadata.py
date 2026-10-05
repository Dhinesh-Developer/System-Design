from fastapi import FastAPI
app = FastAPI()

users = [
    f"user-{i}"
    for i in range(1,101)
]

@app.get("/users")
def get_users(page:int=1,limit:int=10):
    start = (page-1) * limit
    end = start + limit

    total = len(users)
    return {
        "page":page,
        "limit":limit,
        "total":total,
        "total_pages": (
            total + limit -1
        ),
        "data": users[start:end]
    }

