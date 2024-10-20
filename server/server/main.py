from fastapi import FastAPI, Request, Header
from server.routers.blog import blog_router
from server.routers.stripe import stripe_router
import os
from dotenv import load_dotenv
import json
import uvicorn

app = FastAPI()

app.include_router(blog_router)
app.include_router(stripe_router)

@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI Blog API with MongoDB!"}

def start_app():
    uvicorn.run(app, host="0.0.0.0", port=5050, log_level="info")