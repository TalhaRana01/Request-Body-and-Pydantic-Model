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
# @app.post("/products", status_code=status.HTTP_201_CREATED)
# async def create_product(new_product: Product):
#   print(new_product.id)
#   print(new_product.name)
#   print(new_product.price)
#   print(new_product.stock)
  
#   return new_product



# Add new calculated attribute 
# @app.post("/products", status_code=status.HTTP_201_CREATED)
# async def create_product(new_product: Product):
#   # convert into disctionary data type
#   product_dict = new_product.model_dump()
#   # calculating tax percentage on product price
#   price_with_tax = new_product.price + (new_product.price * 15/100)
#   # update product price with tax
#   product_dict.update({"price_with_tax": price_with_tax})
  
#   return product_dict

# Combining Request Body with Path Parameters

@app.put("/products/{product_id}", status_code=status.HTTP_201_CREATED)
async def create_product(product_id: int , new_updated_product: Product):
  return {"product_id": product_id, "new_updated_product": new_updated_product}



# Adding Query Parameters

@app.put("/products/{product_id}")
async def create_product(product_id: int , new_updated_product: Product, discount: float | None = None):
  return {"product_id": product_id, "new_updated_product": new_updated_product, "discount": discount}





# {
#   "id": 1,
#   "name": "product1",
#   "price": 25.5,
#   "stock": 10
# }
  