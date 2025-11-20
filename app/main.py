from fastapi import FastAPI

app = FastAPI(
  title="Request Body and Pydantic Model",
  version="0.1.0"
)

@app.get("/products")
async def get_products():
  return {"response": "all products"}