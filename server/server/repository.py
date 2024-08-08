from bson import ObjectId
from server.database import blog_collection, blog_post_helper
from server.schemas import BlogPostCreate

async def get_blog_posts(skip: int = 0, limit: int = 10):
    # Fetch blog posts with skip and limit for pagination
    blog_posts = await blog_collection.find().skip(skip).limit(limit).to_list(length=limit)
    return [blog_post_helper(post) for post in blog_posts]

async def get_blog_post(post_id: str):
    # Fetch a single blog post by ID
    blog_post = await blog_collection.find_one({"_id": ObjectId(post_id)})
    if blog_post:
        return blog_post_helper(blog_post)

async def create_blog_post(post: BlogPostCreate):
    # Insert a new blog post
    blog_post = await blog_collection.insert_one(post.dict())
    new_post = await blog_collection.find_one({"_id": blog_post.inserted_id})
    return blog_post_helper(new_post)

async def update_blog_post(post_id: str, post: BlogPostCreate):
    # Update an existing blog post
    updated_post = await blog_collection.find_one_and_update(
        {"_id": ObjectId(post_id)},
        {"$set": post.model_dump()},
        return_document=True,
    )
    if updated_post:
        return blog_post_helper(updated_post)

async def delete_blog_post(post_id: str):
    # Delete a blog post
    deleted_post = await blog_collection.find_one_and_delete({"_id": ObjectId(post_id)})
    if deleted_post:
        return blog_post_helper(deleted_post)
