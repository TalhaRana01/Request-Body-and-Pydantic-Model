from fastapi import FastAPI, Body
from typing import Annotated
from pydantic import BaseModel



app = FastAPI()

# Multiple Body Paramters

class Product(BaseModel):
  name: str
  price: float
  stock : int | None = None
  
class Seller(BaseModel):
  username : str
  full_name : str | None = None
  
  
# @app.post("/product")
# async def create_product(product: Product, seller: Seller):
#   return {"product": product, "seller": seller}

# Make body parameter optional
# @app.post("/product")
# async def create_product(product: Product, seller: Seller | None = None):
#   return {"product": product, "seller": seller}

# Singular value in body

@app.post("/product")
async def create_product(
  product: Product,   # Product Pydentic Schema
  seller: Seller,     # Seller Pydantic Schema
  secret_key : Annotated[str, Body()]   # Extra Schema that is not defined in Pydantic Schema
  ):
  
  return {"product": product, "seller": seller, "secret_key": secret_key}
  