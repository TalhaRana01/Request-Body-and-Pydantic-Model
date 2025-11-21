from fastapi import FastAPI, HTTPException, Path
from typing import Annotated
from pydantic import BaseModel


app = FastAPI()

items = {
  "apple": "A juicy fruit", 
  "banana": "A yellow delight"
  }

# Using HTTPExaception
@app.get("/item/{item_id}")
async def get_item(item_id:Annotated[str, Path(example="item-id")]):
  if item_id not in items:
    raise HTTPException(status_code=404, detail="Item Not found", headers={"x-error-type": "itemmissing"})
  return items[item_id]