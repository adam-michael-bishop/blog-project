import motor.motor_asyncio
from bson import ObjectId
from dotenv import load_dotenv
import os

load_dotenv()

MONGO_DB_PW = os.getenv("MONGO_DB_PW")
MONGO_DETAILS = f"mongodb+srv://abishop:{MONGO_DB_PW}@cluster0.73ipu.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)

database = client.blog_database

blog_collection = database.get_collection("blog_posts")

# Helper function to serialize MongoDB documents
def blog_post_helper(blog_post) -> dict:
    return {
        "id": str(blog_post["_id"]),
        "title": blog_post["title"],
        "content": blog_post["content"],
    }
