from typing import Optional
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    id: Optional[int] = None
    name: str
    description: Optional[str] = None
    price: float


_items = []
_next_id = 1


@app.get("/items/")
def list_items():
    return _items


@app.get("/items/{item_id}")
def get_item(item_id: int):
    for item in _items:
        if item["id"] == item_id:
            return item
    raise HTTPException(status_code=404, detail="Item not found")


@app.post("/items/", status_code=201)
def create_item(item: Item):
    global _next_id
    data = item.dict()
    data["id"] = _next_id
    _next_id += 1
    _items.append(data)
    return data


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
