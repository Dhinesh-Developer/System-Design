# rest_3.py

from fastapi import FastAPI

app = FastAPI()

orders = [
    {
        "id":101,
        "user_id":1,
        "product":"Laptop"
    },
    {
        "id":102,
        "user_id":1,
        "product":"Mouse"
    },
    {
        "id":103,
        "user_id":2,
        "product":"Keyboard"
    }
]


@app.get("/users/{user_id}/orders")
def get_user_orders(user_id:int):
    result = []

    for order in orders:
        if order["user_id"] == user_id:
            result.append(order)

    return result        

