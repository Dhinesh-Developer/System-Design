from fastapi import FastAPI, Header, HTTPException

app = FastAPI()

SECRET_KEY = "my-secret-key"

@app.get("/profile")
def profile(api_key: str | None = Header(default=None)):
    if api_key != SECRET_KEY:
        raise HTTPException(
            status_code = 401,
            detail = "Invalid API key"
        )

    return {
        "name": "Dhinesh",
        "role": "user"
    }


