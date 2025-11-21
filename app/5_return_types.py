from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

class Product(BaseModel):
  id : int
  name : str
  price : float
  stock: int | None = None
  
class ProductOut(BaseModel):
  name : str
  price : float
  
  
  
class BaseUser(BaseModel):
  username : str
  full_name : str | None = None
  

class UserIn(BaseUser):
  password: str
  
  
 

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
  
# @app.post("/products")
# async def create_product(product: Product) -> Product:
#   return product

# @app.post("/products")
# async def create_product(product: List[Product]) -> List[Product]:
#   return product
# @app.post("/products")
# async def create_product(product: Product) -> ProductOut:
#   return product


# @app.post("/user")
# async def create_user(user: UserIn) -> BaseUser:
#   return user

##------------------------------------
## Response Model
##-----------------------------------

# with response_model Parameter
# @app.get("/products", response_model=Product)
# async def get_product():
  # return {"id": 1, "name": "Laptop", "price": 33.56, "stock" : 5}
  
# @app.get("/products", response_model=List[Product])
# async def get_product():
  # return {"id": 1, "name": "Laptop", "price": 33.56, "stock" : 5}
  
  # return [
  #   {"id": 1, "name": "laptop", "price": 25000},
  #   {"id": 2, "name": "mobile", "price": 50000},
  #   {"id": 3, "name": "mini laptop", "price": 75000}
  # ]
  
# @app.post("/products", response_model=Product)
# async def cerate_product(product: Product):
#   return product


# @app.post("/products", response_model=List[Product])
# async def cerate_product(product: List[Product]):
#   return product

@app.post("/users", response_model=BaseUser)
async def cerate_user(user: UserIn):
  return user
  


  


  
