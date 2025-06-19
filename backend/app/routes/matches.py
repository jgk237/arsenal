# import httpx
# import os
# from fastapi import APIRouter, HTTPException

# router = APIRouter()
# API_TOKEN = os.getenv("FOOTBALL_API_TOKEN")
# BASE_URL = "https://api.football-data.org/v2"

# HEADERS = {
#     "X-Auth-Token":API_TOKEN 
# }

# # Arsenal's team ID on football-data.org is 57

# @router.get("/season/{year}")
# async def get_arsenal_matches_by_season(year: int):
#     url = f"{BASE_URL}/teams/57/matches?season={year}"
#     print(API_TOKEN)
#     async with httpx.AsyncClient() as client:
#         response = await client.get(url, headers=HEADERS)
#         print(response.json())
#         if response.status_code != 200:
#             raise HTTPException(status_code=response.status_code, detail="Error fetching matches")

#         data = response.json()
#         return data["matches"]  # You can filter/reshape this if needed

# # You can add more endpoints, like /next or /last
import httpx
from fastapi import APIRouter, Depends, HTTPException

from models import User
from utils.auth import get_current_user

router = APIRouter()
BASE_URL = "https://api.football-data.org/v4"

# Hardcode your token directly here for testing
API_TOKEN = "2d67a8fdf13e44a18d24a1a1b4261ee1"  # Replace with your real token

HEADERS = {
    "X-Auth-Token": API_TOKEN
}


@router.get("/season/{year}")
async def get_arsenal_matches_by_season(year: int, user: User = Depends(get_current_user)):
    url = f"{BASE_URL}/competitions/PL/matches"
    
    print("\n=== REQUEST DETAILS ===")
    print(f"URL: {url}")
    print(f"Headers: {HEADERS}")
    
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(url, headers=HEADERS)
            
            print("\n=== RESPONSE DETAILS ===")
            print(f"Status Code: {response.status_code}")
            print(f"Response Headers: {dict(response.headers)}")
            print(f"Response Body: {response.text[:200]}...")  # Print first 200 chars
            
            if response.status_code != 200:
                raise HTTPException(
                    status_code=response.status_code,
                    detail=f"Error from football-data.org: {response.text}"
                )
            
            return response.json()["matches"]
            
        except Exception as e:
            print("\n=== ERROR ===")
            print(f"Exception: {str(e)}")
            raise HTTPException(
                status_code=500,
                detail=f"Internal server error: {str(e)}"
            )