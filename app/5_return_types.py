from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# without return types
# @app.get("/products")
# async def get_products():
#   return {"resposne" : "fastapi"}

# Without return type
# @app.post("/products")
# async def get_product(product: dict):
#   # return product
#   return "hello world"


class Product(BaseModel):
  id : int
  name: str
  price: float
 
  
class ProductOut(Product):
  name: str
  price : float
  
  
  
  
# @app.post("/product")
# async def get_product(product: Product):
#   # return product   
#   # return "hello world"
  

# With return type restriction 
# @app.post("/product")
# async def create_product(product: Product) -> Product:
#   # return "hello world" 
#   return product

@app.post("/product")
async def create_product(product: list[Product] ):
  return product

  
# @app.post("/product")
# async def create_product(product: Product ) -> ProductOut:
#   return product