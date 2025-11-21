from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# @app.get("/products")
# async def get_products():
#   return {"resposne" : "fastapi"}


# @app.post("/products")
# async def get_product(product: dict):
#   # return product
#   return "hello world"


class Product(BaseModel):
  id : int
  name : str
  price : float
  
  
# @app.post("/product")
# async def get_product(product: Product):
#   # return product   
#   # return "hello world"
  

# @app.post("/product")
# async def create_product(product: Product) -> Product:
#   # return "hello world" 
#   return product



  