from pydantic import BaseModel, Field
from datetime import datetime

class PostBase(BaseModel):
    content: str = Field(..., min_length=1, max_length=500)
    color: str = "#ffffff"
    rotation: int = 0

class PostCreate(PostBase):
    pass

class Post(PostBase):
    id: int
    username: str
    reactions: int = 0
    timestamp: datetime

    class Config:
        orm_mode = True
