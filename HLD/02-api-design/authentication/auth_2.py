# Bearer token
from fastapi import FastAPI, Header, HTTPException

app = FastAPI()

VALID_TOKEN = "abc123"

@app.get("/profile")
def profile(authorization: str | None = Header(default=None)):
    expected = f"Bearer {VALID_TOKEN}"

    if authorization != expected:
        raise HTTPException(
            status_code = 401,
            detail = "Invalid token"
        )
    return {
        "name": "Dhinesh",
        "authenticated": True
    }


