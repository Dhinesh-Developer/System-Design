from fastapi import FastAPI, HTTPException

app = FastAPI()

users = {
    1: "Dhinesh",
    2: "Arun"
}

@app.get("/user/{user_id}")
def get_user(user_id:int):
    if user_id not in users:
        raise HTTPException(
            status_code = 404,
            detail="User not found"
        )

    return {
        "id": user_id,
        "name": users[user_id]
    }
    
