from fastapi import FastAPI
from server.routers import blog
import uvicorn

app = FastAPI()

app.include_router(blog.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI Blog API with MongoDB!"}

def start_app():
    uvicorn.run(app, host="0.0.0.0", port=5050, log_level="info")