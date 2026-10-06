from fastapi import FastAPI
app = FastAPI()

def check_database():
    #simulating database connection
    return True

@app.get("/health")
def health():
    database = check_database()
    if database:
        return {
            "status":"healthy",
            "database":"up"
        }

    return{
        "status":"unhealthy",
        "database":"down"
    }


