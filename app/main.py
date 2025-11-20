from fastapi import FastAPI, status
from pydantic import BaseModel

app = FastAPI(
  title="Request Body and Pydantic Model",
  version="0.1.0"
)

# With Pydantic validation 

class Product(BaseModel):
  id : int
  name : str
  price : float
  stock : int | None = None   # optional field


# Basic create route without request body validation 
# Create or insert Data
# @app.post("/products")
# async def get_products(new_product : dict):
#   """
#     Ya without pydantic validation ha 
#     request body main kuch data  hi bhej skty hain
    
#   """
#   return {"response": "Product created", "new_product": new_product}



# @app.post("/products", status_code=status.HTTP_201_CREATED)
# async def create_product(new_product: Product):
#   """
#       Hum ny Pydantic class main 
#       already define kr diya ha data type ky sath  es liye humhan  
#       request body wo fields required hogi agr koi missing hui to error aye ga
#   """
#   return {"message": "Product created", "product": new_product}

# Accessing Attribute inside a function
@app.post("/products", status_code=status.HTTP_201_CREATED)
async def create_product(new_product: Product):
  print(new_product.id)
  print(new_product.name)
  print(new_product.price)
  print(new_product.stock)
  
  return new_product


# {
#   "id": 1,
#   "name": "product1",
#   "price": 25.5,
#   "stock": 10
# }
  