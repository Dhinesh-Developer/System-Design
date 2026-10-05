from fastapi import FastAPI

app = FastAPI()

users = [
    {
        "id":1,
        "name":f"User-{i}"
    }
    for i in range(1,101)
]

@app.get("/users")
def get_users(cursor:int=0,limit:int=10):
    res = [
        user for user in users
        if user["id"] > cursor
    ]

    res = res["limit"]

    next_cursor = (
        res[-1]["id"]
        if res else None
    )

    return {
        "data": res,
        "next_cursor": next_cursor
    }



