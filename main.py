from fastapi import FastAPI

# Create an instance of the FastAPI class
app = FastAPI()

# Define a route
@app.get("/")
async def read_root():
    return {"message": "Hello, World"}

# Run the server
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8000)
