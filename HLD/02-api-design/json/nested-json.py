from fastapi import FastAPI
app = FastAPI()

@app.get("/order")
def order():

    return {
        "order_id": 1001,
        "customer": {
            "id":1,
            "name":"Dhinesh"
        },

        "items": [
            {
                "name":"Laptop",
                "price":55000
            },
            {
                "name": "Mouse",
                "price": 1000
            }
        ]
    }
