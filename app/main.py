from fastapi import FastAPI

app = FastAPI(
  title="Request Body and Pydantic Model",
  version="0.1.0"
)

# Create or insert Data
@app.post("/products")
async def get_products(new_product : dict):
  return {"response": "Product created", "new_product": new_product}