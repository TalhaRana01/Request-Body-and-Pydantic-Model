from fastapi import FastAPI
from pydantic import BaseModel, Field


app = FastAPI()


#  Nested Body Models

# Submodel | Inherient Model
class Category(BaseModel):
  name : str = Field(title="Category Name", description="The name of the product category", max_length=50, min_length=1)
  description : str | None = Field(default=None, title="Category Description", description="A brief description of the category", max_length=200)


# Main  Model | Base Model
class Product(BaseModel):
  name: str = Field(title="This is product name", description="This is a product description", max_length=25)
  price : float = Field(gt=1, le=100, title="this is product price", description="the product of price must be in USD")
  stock: int = Field(default=None, ge=0, title="This is stock of product", description="This is stock of all products")
  
  category: Category | None = Field(default=None)
  
@app.post("/product")
async def create_product(product: Product):
 return product