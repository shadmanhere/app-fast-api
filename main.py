from fastapi import FastAPI, HTTPException
from item import Item

# Create an instance of the FastAPI class
app = FastAPI()

# Define a route
@app.get("/")
async def read_root():
    return {"message": "Hello!, World"}

# GET request
@app.get("/items/{item_id}")
async def read_item(item_id: int):
    if item_id == 42:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"item_id": item_id}

# POST request
@app.post("/items/")
async def create_item(item: Item):
    return item

# PUT request
@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id}

# DELETE request
@app.delete("/items/{item_id}")
async def delete_item(item_id: int):
    return {"item_id": item_id, "deleted": True}

# Run the server
# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run(app, host="localhost", port=8000)
