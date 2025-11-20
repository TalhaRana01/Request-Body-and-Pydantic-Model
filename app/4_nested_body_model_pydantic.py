from fastapi import FastAPI, Body
from pydantic import BaseModel, Field
from typing import Annotated


app = FastAPI()


#  Nested Body Models

# Submodel | Inherient Model
# class Category(BaseModel):
#   name : str = Field(title="Category Name", description="The name of the product category", max_length=50, min_length=1)
#   description : str | None = Field(default=None, title="Category Description", description="A brief description of the category", max_length=200)


# # Main  Model | Base Model
# class Product(BaseModel):
#   name: str = Field(title="This is product name", description="This is a product description", max_length=25)
#   price : float = Field(gt=1, le=100, title="this is product price", description="the product of price must be in USD")
#   stock: int = Field(default=None, ge=0, title="This is stock of product", description="This is stock of all products")
  
#   category: Category | None = Field(default=None)

class Category(BaseModel):
  name : str = Field(title="Category Name", description="The name of the product category", max_length=50, min_length=1)
  description : str | None = Field(default=None, title="Category Description", description="A brief description of the category", max_length=200)


# Main  Model | Base Model
class Product(BaseModel):
  name: str = Field(title="This is product name", description="This is a product description", max_length=25, examples=["product name"])
  price : float = Field(gt=1, title="this is product price", description="the product of price must be in USD", examples=["product price"])
  stock: int = Field(default=None, ge=0, title="This is stock of product", description="This is stock of all products", examples=[40])
  
  # As a list Category model
  # category: list[Category] | None = Field(default=None, title="Product category", description="The category to which the product belongs")
  category : Category
  
@app.post("/product")
async def create_product(product:Annotated[Product, Body(embed=True)]):
 return product