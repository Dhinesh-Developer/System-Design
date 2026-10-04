from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Product(BaseModel):
    name: str
    price: float
    quantity: int

@app.post("/products")
def create_product(product: Product):
    total = product.price * product.quantity

    return{
        "product": product,
        "total": total
    }


