# Fastapi role check

from fastapi import FastAPI,HTTPException

app = FastAPI()

@app.delete("/users/{user_id}")
def delete_user(user_id:int, role:str):
    if role != "admin":
        raise HTTPException(
            status_code = 403,
            detail = "Admin access required"
        )

    return {
        "message": f"User {user_id} deleted"
    }


