from fastapi import FastAPI
import redis
import json
import time

app = FastAPI()

redis_client = redis.Redis(
    host = "localhost",
    port = 6379,
    decode_responses = True
)

@app.get("/users/{user_id}")
def get_user(user_id:int):
    key = f"user:{user_id}"
    #check redis

    cached = redis_client.get(key)

    if cached:
        return{
            "source":"redis",
            "data":json.loads(cached)
        }

    #simulate database
    time.sleep(1)
    user = {
        "id":user_id,
        "name":"Dhinesh"
    }

    #Store in redis
    redis_client.set(
        key,json.dumps(user)
    )

    return {
        "source":"database",
        "data":user
    }
    



