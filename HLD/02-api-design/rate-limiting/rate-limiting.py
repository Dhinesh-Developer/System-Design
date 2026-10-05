from fastapi import FastAPI, HTTPException
import time

app = FastAPI()

requests = {}

@app.get("/api")
def api(client_id: str):
    current_time = time.now()
    if client_id not in requests:
        requests[client_id] = []

    requests[client_id] = [
        t for t in requests[client_id]
        if current_time - t < 60
    ]

    if len(requests[client_id]) >= 5:
        raise HTTPException(
            status_code=429,
            detail = "Rate limit exceeded"
        )
    requests[client_id].append(
        current_time
    )

    return {
        "message" : "Request accepted"
    }


