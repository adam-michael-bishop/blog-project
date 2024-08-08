from pydantic import BaseModel, Field

class BlogPostBase(BaseModel):
    title: str
    content: str

class BlogPostCreate(BlogPostBase):
    pass

class BlogPost(BlogPostBase):
    id: str = Field(..., alias="_id")

    class Config:
        orm_mode = True
        allow_population_by_field_name = True
