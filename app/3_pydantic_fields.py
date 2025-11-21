from fastapi import FastAPI, Body
from typing import Annotated
from pydantic import BaseModel, Field


app = FastAPI()


class Product(BaseModel):
  name: str = Field(
    title="This is product name",
    description="This is a product description",
    min_length=10
    )
  
  price : float = Field(
    gt=1, le=100, 
    title="this is product price", 
    description="the product of price must be in USD"
    )
  
  stock: int = Field(
    default=None, ge=0, 
    title="This is stock of product", 
    description="This is stock of all products"
    )


@app.post("/product")
async def create_product(product: Product ):
  return product
