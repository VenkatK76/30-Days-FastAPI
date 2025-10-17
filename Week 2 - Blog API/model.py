from pydantic import BaseModel, Field, validator
from typing import Optional

class Post(BaseModel):
    title: str = Field(..., min_length=5, max_length=100, description="Title must be 5-100 chars long")
    content: str = Field(..., min_length=10, description="Content must be at least 10 characters long")
    published: bool = True
    tags: list[str] = []

    @validator("title")
    def check_title(cls, v):
        forbidden = ["test", "demo", "sample"]
        if any(word in v.lower() for word  in forbidden):
            raise ValueError("Title cannot be test/demo/sample generic")
        return v

class PostUpdate(BaseModel):
    id: Optional[int] = None
    title: Optional[str] = None
    content: Optional[str] = None
    published: Optional[bool] = None
    tags: Optional[list[str]] = None


