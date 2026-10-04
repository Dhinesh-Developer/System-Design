# simple REST API

from fastapi import FastAPI

app = FastAPI()

@app.get("/users")
def get_users():
    return {
        "users": [
            "Dhinesh","Kumar","Arun"
        ]
    }

# {
#   "users": [
#     "Dhinesh",
#     "Kumar",
#     "Arun"
#   ]
# }