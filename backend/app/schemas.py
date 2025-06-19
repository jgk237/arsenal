from pydantic import BaseModel, EmailStr
from typing import Optional, List
from datetime import datetime

# --------------------------
# User Schemas
# --------------------------

class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str

# For returning user details (without password)
class UserOut(BaseModel):
    id: int
    username: str
    email: EmailStr

    class Config:
        orm_mode = True

class UserResponse(BaseModel):
    id: int
    username: str
    email: EmailStr
    created_at: datetime

    class Config:
        orm_mode = True

class UserLogin(BaseModel):
    username: str
    password: str
# --------------------------
# Token Schemas
# --------------------------

class Token(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str = "bearer"


class TokenRefreshResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"


class TokenResponse(BaseModel):
    access_token: str
    token_type: str
    user_id: int
    refresh_token: str | None = None     

class TokenData(BaseModel):
    user_id: Optional[int] = None

# --------------------------
# Post Schemas
# --------------------------

class PostCreate(BaseModel):
    title: str
    content: str
    tags: Optional[List[str]] = []

class PostResponse(BaseModel):
    id: int
    title: str
    content: str
    created_at: datetime
    author: UserResponse

    class Config:
        orm_mode = True
