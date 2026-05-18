from pydantic import BaseModel, Field
from datetime import datetime

class User(BaseModel):
    name: str
    email: str
    password: str
    creation: datetime = Field(default_factory=datetime.now)
    updated_at: datetime = Field(default_factory=datetime.now)
