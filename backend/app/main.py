from fastapi import FastAPI, Path
from routes import user_routes, matches
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
import os

load_dotenv()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], allow_credentials=True, allow_methods=["*"], allow_headers=["*"],
)

app.include_router(matches.router, prefix="/api/matches", tags=["Matches"])
app.include_router(user_routes.router)
