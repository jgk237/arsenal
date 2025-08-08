from pydantic import BaseModel, EmailStr, conint
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
    upvotes: int
    downvotes: int

    class Config:
        orm_mode = True

class CommentBase(BaseModel):
    content: str

class CommentCreate(CommentBase):
    pass

class CommentResponse(CommentBase):
    id: int
    author_id: int
    post_id: int
    created_at: datetime
    upvotes: int
    downvotes: int

    class Config:
        orm_mode = True


class ReplyBase(BaseModel):
    content: str

class ReplyCreate(ReplyBase):
    pass

class ReplyResponse(ReplyBase):
    id: int
    author_id: int
    comment_id: int
    created_at: datetime

    class Config:
        orm_mode = True


class ReplyBase(BaseModel):
    content: str

class ReplyCreate(ReplyBase):
    pass

class ReplyResponse(ReplyBase):
    id: int
    author_id: int
    comment_id: int
    created_at: datetime

    class Config:
        orm_mode = True

class VoteCreate(BaseModel):
    value: conint(ge=-1, le=1)  # -1 = downvote, 0 = remove, 1 = upvote

class VoteOut(BaseModel):
    id: int
    post_id: int | None = None
    comment_id: int | None = None
    user_id: int
    value: int
    created_at: datetime

    class Config:
        orm_mode = True
