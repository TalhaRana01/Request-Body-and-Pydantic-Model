from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

class Product(BaseModel):
  id : int
  name : str
  price : float
  stock: int | None = None
  

# Without return type we can send any kind of data 
# we can return string value
# we can return JSON value
# we can return list values


# Examples:

# @app.get("/product")
# async def get_product():
  # return "hello world" 
  # return {"response" : "Ok"}
  # return [
  #   {"id": 1, "name": "laptop", "price": 25000},
  #   {"id": 2, "name": "mobile", "price": 50000},
  #   {"id": 3, "name": "mini laptop", "price": 75000}
  # ]
  
  
# @app.get("/product")
# async def get_product()-> Product:
#   return {"id" : 1, "name": "product 1", "price": 55.6, "stock": 1, "discount": True}

# @app.get("/product")
# async def get_product()-> List[Product]:
#   return [
#     {"id": 1, "name": "laptop", "price": 25000},
#     {"id": 2, "name": "mobile", "price": 50000},
#     {"id": 3, "name": "mini laptop", "price": 75000}
#   ]
  

  


  
