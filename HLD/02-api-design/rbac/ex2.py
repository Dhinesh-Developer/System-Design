from fastapi import FastAPI, HTTPException
app = FastAPI()

def require_admin(role:str):
    if role != "admin":
        raise HTTPException(
            status_code = 403,
            detail = "Admin permission required"
        )

@app.delete("/users/{user_id}")
def delete_user(user_id:int, role:str):
    require_admin(role)

    return {
        "message":"User deleted"
    }

