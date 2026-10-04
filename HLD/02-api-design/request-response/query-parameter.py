from fastapi import FastAPI

app = FastAPI()

@app.get("/search")
def search_users(name:str, age:int=18):
    return{
        "name": name,
        "age": age
    }

# Request:
# /search?name=Dhinesh&age=21