from fastapi import FastAPI
app = FastAPI()

@app.get("/product")
def product():
    return {
        "id":101,
        "name":"Laptop",
        "price":55000
    }
