from fastapi import FastAPI, HTTPException

app = FastAPI()

@app.get("/admin")
def admin(access: str):
    if access == "none":
        raise HTTPException(
            status_code=401,
            detail="Authentication required"
        )

    if access != "admin":
        raise HTTPException(
            status_code = 403,
            detail="Admin permission required"
        )

    return {
        "message": "Welcome admin"
    }

