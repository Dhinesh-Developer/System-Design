from fastapi import FastAPI

app = FastAPI()

@app.get("/health/live")
def liveness():
    return {
        "status": "alive"
    }

@app.get("/health/ready")
def readiness():
    database_ready = True
    if database_ready:
        return {
            "status":"ready"
        }
    return{
        "status":"not_ready"
    }