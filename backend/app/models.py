
from sqlalchemy import Column, Integer, String
# from app.database import Base
from database import Base
from sqlalchemy import (
    Column,
    Integer,
    String,
    Text,
    ForeignKey,
    DateTime,
    UniqueConstraint,
    Table
)
from sqlalchemy.orm import relationship, declarative_base
from datetime import datetime

post_tags = Table(
    'post_tags',
    Base.metadata,
    Column('post_id', Integer, ForeignKey('posts.id'), primary_key=True),
    Column('tag_id', Integer, ForeignKey('tags.id'), primary_key=True)
)

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True, nullable=False)
    email = Column(String(120), unique=True, nullable=False)
    hashed_password = Column(String(200), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    posts = relationship('Post', back_populates='author')
    comments = relationship('Comment', back_populates='author')
    replies = relationship('Reply', back_populates='author')
    votes = relationship('Vote', back_populates='user')


# --- Post Model ---
class Post(Base):
    __tablename__ = 'posts'

    id = Column(Integer, primary_key=True)
    title = Column(String(200), nullable=False)
    content = Column(Text, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    author_id = Column(Integer, ForeignKey('users.id'))

    author = relationship('User', back_populates='posts')
    comments = relationship('Comment', back_populates='post', cascade='all, delete-orphan')
    votes = relationship('Vote', back_populates='post', cascade='all, delete-orphan')
    tags = relationship('Tag', secondary=post_tags, back_populates='posts')


# --- Comment Model ---
class Comment(Base):
    __tablename__ = 'comments'

    id = Column(Integer, primary_key=True)
    content = Column(Text, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    author_id = Column(Integer, ForeignKey('users.id'))
    post_id = Column(Integer, ForeignKey('posts.id'))

    author = relationship('User', back_populates='comments')
    post = relationship('Post', back_populates='comments')
    replies = relationship('Reply', back_populates='comment', cascade='all, delete-orphan')
    votes = relationship('Vote', back_populates='comment', cascade='all, delete-orphan')


# --- Reply Model ---
class Reply(Base):
    __tablename__ = 'replies'

    id = Column(Integer, primary_key=True)
    content = Column(Text, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    author_id = Column(Integer, ForeignKey('users.id'))
    comment_id = Column(Integer, ForeignKey('comments.id'))

    author = relationship('User', back_populates='replies')
    comment = relationship('Comment', back_populates='replies')


# --- Vote Model (for both Post and Comment) ---
class Vote(Base):
    __tablename__ = 'votes'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    post_id = Column(Integer, ForeignKey('posts.id'), nullable=True)
    comment_id = Column(Integer, ForeignKey('comments.id'), nullable=True)
    value = Column(Integer, nullable=False)  # 1 = upvote, -1 = downvote
    created_at = Column(DateTime, default=datetime.utcnow)

    user = relationship('User', back_populates='votes')
    post = relationship('Post', back_populates='votes')
    comment = relationship('Comment', back_populates='votes')

    __table_args__ = (
        UniqueConstraint('user_id', 'post_id', name='unique_post_vote'),
        UniqueConstraint('user_id', 'comment_id', name='unique_comment_vote'),
    )


# --- Tag Model ---
class Tag(Base):
    __tablename__ = 'tags'

    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True, nullable=False)

    posts = relationship('Post', secondary=post_tags, back_populates='tags')
