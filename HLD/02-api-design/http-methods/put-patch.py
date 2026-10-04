from fastapi import FastAPI

app = FastAPI()

user = {
    "name":"Dhinesh",
    "age":21,
    "city":"Salem"
}

@app.put("/user")
def replace_user():
    global user

    user = {
        "name":"Dhinesh kumar",
        "age": 21,
        "city": "Chennai"
    }

    return user

@app.patch("/user")
def update_city(city: str):
    user["city"] = city
    return user


