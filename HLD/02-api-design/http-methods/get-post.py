from fastapi import FastAPI

app = FastAPI()

@app.get("/products")
def get_products():
    return {
        "products":[
            "Laptop",
            "Mouse",
            "Keyboard"
        ]
    }

@app.post("/products")
def create_product(name: str):
    
    return {
        "message": "Product created",
        "product": name
    }



