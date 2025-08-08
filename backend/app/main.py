from fastapi import FastAPI, Path
from routes import posts, comments, votes
from routes import user_routes
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
import os

load_dotenv()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], allow_credentials=True, allow_methods=["*"], allow_headers=["*"],
)

app.include_router(posts.router, prefix="/api/posts", tags=["Posts"])
app.include_router(user_routes.router)
app.include_router(comments.router)
app.include_router(votes.router)
