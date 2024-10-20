from fastapi import APIRouter, HTTPException
from typing import List
from server.schemas import BlogPost, BlogPostCreate
from server.repository import get_blog_post, get_blog_posts, create_blog_post, update_blog_post, delete_blog_post

blog_router = APIRouter(
    prefix="/blog",
    tags=["blog"],
)

@blog_router.get("/", response_model=List[BlogPost])
async def read_blog_posts(skip: int = 0, limit: int = 10):
    blog_posts = await get_blog_posts(skip=skip, limit=limit)
    return blog_posts

@blog_router.get("/{post_id}", response_model=BlogPost)
async def read_blog_post(post_id: str):
    blog_post = await get_blog_post(post_id=post_id)
    if blog_post is None:
        raise HTTPException(status_code=404, detail="Post not found")
    return blog_post

@blog_router.post("/", response_model=BlogPost)
async def create_blog_post(post: BlogPostCreate):
    return await create_blog_post(post)

@blog_router.put("/{post_id}", response_model=BlogPost)
async def update_blog_post(post_id: str, post: BlogPostCreate):
    updated_post = await update_blog_post(post_id=post_id, post=post)
    if updated_post is None:
        raise HTTPException(status_code=404, detail="Post not found")
    return updated_post

@blog_router.delete("/{post_id}", response_model=BlogPost)
async def delete_blog_post(post_id: str):
    deleted_post = await delete_blog_post(post_id=post_id)
    if deleted_post is None:
        raise HTTPException(status_code=404, detail="Post not found")
    return deleted_post
