from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()

class Product(BaseModel):
  id : int
  name : str
  price : float
  

# Without return type we can send any kind of data 
# we can return string value
# we can return JSON value
# we can return list values


# Examples:

@app.get("/product")
async def get_product():
  # return "hello world" 
  # return {"response" : "Ok"}
  # return [
  #   {"id": 1, "name": "laptop", "price": 25000},
  #   {"id": 2, "name": "mobile", "price": 50000},
  #   {"id": 3, "name": "mini laptop", "price": 75000}
  # ]
  
  
  


  
