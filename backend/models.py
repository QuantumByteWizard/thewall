from sqlalchemy import Column, Integer, String, DateTime
from database import Base
import datetime

class Post(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True, index=True)
    content = Column(String, index=True)
    timestamp = Column(DateTime, default=datetime.datetime.utcnow)
    color = Column(String, default="#ffffff")
    username = Column(String, index=True)
    reactions = Column(Integer, default=0)
    position_x = Column(Integer, default=0) # For visual layout if needed
    position_y = Column(Integer, default=0) 
    rotation = Column(Integer, default=0)
