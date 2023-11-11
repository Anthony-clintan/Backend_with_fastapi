from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
import json

app = FastAPI()

# Product model
class Product(BaseModel):
    id: int
    name: str
    price: float
    in_stock: bool

# In-memory database
products = []

@app.post("/product/")
async def create_product(product: Product):
    products.append(product)
    return product


@app.get('/products')
async def get_all_products():
    return products

@app.get("/product/{product_id}")
async def read_product(product_id: int):
    for product in products:
        if product.id == product_id:
            return product
    return {"error": "Product not found"}

@app.put("/product/{product_id}")
async def update_product(product_id: int, product: Product):
    for index, existing_product in enumerate(products):
        if existing_product.id == product_id:
            products[index] = product
            return product
    return {"error": "Product not found"}

@app.delete("/product/{product_id}")
async def delete_product(product_id: int):
    for index, existing_product in enumerate(products):
        if existing_product.id == product_id:
            products.pop(index)
            return {"message": "Product deleted"}
    return {"error": "Product not found"}
