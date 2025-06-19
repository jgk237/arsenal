# from fastapi import APIRouter, Depends, HTTPException, status, Request
# from sqlalchemy.orm import Session
# from fastapi.security import OAuth2PasswordRequestForm
# import models, schemas
# from utils.auth import (
#     verify_password,
#     get_password_hash,
#     create_access_token,
#     create_refresh_token,
#     oauth2_scheme,
#     get_db
# )
# from jose import JWTError, jwt
# from datetime import timedelta
# import os

# router = APIRouter(
#     prefix="/auth",
#     tags=["auth"]
# )

# # Register new user
# @router.post("/register", response_model=schemas.UserOut)
# def register(user: schemas.UserCreate, db: Session = Depends(get_db)):
#     existing_user = db.query(models.User).filter(models.User.username == user.username).first()
#     existing_account_with_email = db.query(models.User).filter(models.User.email == user.email).first()
#     if existing_user or existing_account_with_email:
#         raise HTTPException(status_code=400, detail="Username or email already registered")
    
#     hashed_password = get_password_hash(user.password)
#     new_user = models.User(username=user.username, email=user.email, hashed_password=hashed_password)
#     db.add(new_user)
#     db.commit()
#     db.refresh(new_user)
#     return new_user

# # Login
# @router.post("/login")
# def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
#     user = db.query(models.User).filter(models.User.username == form_data.username).first()
#     if not user or not verify_password(form_data.password, user.hashed_password):
#         raise HTTPException(status_code=401, detail="Invalid credentials")

#     access_token = create_access_token(data={"sub": user.username}, expires_delta=timedelta(minutes=30))
#     refresh_token = create_refresh_token(data={"sub": user.username})
    
#     return {
#         "access_token": access_token,
#         "refresh_token": refresh_token,
#         "token_type": "bearer"
#     }

# @router.post("/refresh")
# async def refresh_token(request: Request, db: Session = Depends(get_db)):
#     SECRET_KEY = os.getenv("JWT_SECRET_KEY")
#     ALGORITHM = os.getenv("JWT_ALGORITHM", "HS256")
    
#     try:
#         # Get token from Authorization header
#         auth_header = request.headers.get("Authorization")
#         if not auth_header or not auth_header.startswith("Bearer "):
#             raise HTTPException(status_code=401, detail="Missing or invalid authorization header")
        
#         token = auth_header.split(" ")[1]
        
#         # Decode and validate token
#         payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        
#         if payload.get("type") != "refresh":
#             raise HTTPException(status_code=401, detail="Invalid token type")
            
#         username = payload.get("sub")
#         if not username:
#             raise HTTPException(status_code=401, detail="Invalid token payload")

#         # Create new access token
#         new_access_token = create_access_token(
#             data={"sub": username},
#             expires_delta=timedelta(minutes=30))
            
#         return {"access_token": new_access_token, "token_type": "bearer"}

#     except JWTError as e:
#         raise HTTPException(status_code=401, detail=f"Invalid token: {str(e)}")
from fastapi import APIRouter, Depends, HTTPException, status, Request
from fastapi.security import HTTPBearer
from sqlalchemy.orm import Session
import models, schemas
from utils.auth import (
    verify_password,
    get_password_hash,
    create_access_token,
    create_refresh_token,
    get_current_user,  # Now using HTTPBearer
    get_db
)
from jose import JWTError, jwt
from datetime import timedelta
import os

router = APIRouter(
    prefix="/auth",
    tags=["auth"]
)

security = HTTPBearer()  # Replaces oauth2_scheme

# Register endpoint (unchanged)
@router.post("/register", response_model=schemas.UserOut)
def register(user: schemas.UserCreate, db: Session = Depends(get_db)):
    existing_user = db.query(models.User).filter(models.User.username == user.username).first()
    existing_account_with_email = db.query(models.User).filter(models.User.email == user.email).first()
    if existing_user or existing_account_with_email:
        raise HTTPException(status_code=400, detail="Username or email already registered")
    
    hashed_password = get_password_hash(user.password)
    new_user = models.User(username=user.username, email=user.email, hashed_password=hashed_password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

# Updated login endpoint
@router.post("/login", response_model=schemas.TokenResponse)
def login(credentials: schemas.UserLogin, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.username == credentials.username).first()
    if not user or not verify_password(credentials.password, user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )

    access_token = create_access_token(data={"sub": str(user.id)})
    refresh_token = create_refresh_token(data={"sub": str(user.id)})
    
    return {
        "access_token": access_token,
        "refresh_token": refresh_token,
        "token_type": "bearer",
        "user_id": user.id
    }

@router.get("/me", response_model=schemas.UserOut)
async def get_me(user: models.User = Depends(get_current_user)):
    return user

@router.post("/refresh", response_model=schemas.TokenRefreshResponse)
async def refresh_token(
    request: Request,
    db: Session = Depends(get_db)
):
    """
    Refresh access token using a valid refresh token.
    Returns new access token if refresh token is valid.
    """
    SECRET_KEY = os.getenv("JWT_SECRET_KEY")
    ALGORITHM = os.getenv("JWT_ALGORITHM", "HS256")
    
    # Extract token from Authorization header
    auth_header = request.headers.get("Authorization")
    if not auth_header or not auth_header.startswith("Bearer "):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Missing or invalid authorization header",
            headers={"WWW-Authenticate": "Bearer"}
        )
    
    token = auth_header.split(" ")[1]
    
    try:
        # Verify and decode token
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        
        # Validate token type
        if payload.get("type") != "refresh":
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid token type (refresh token required)"
            )
            
        # Validate subject exists
        username = payload.get("sub")
        if not username:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid token payload (missing subject)"
            )
        
        # Verify user still exists
        user = db.query(models.User).filter(models.User.username == username).first()
        if not user:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="User no longer exists"
            )

        # Create new access token
        new_access_token = create_access_token(
            data={"sub": username},
            expires_delta=timedelta(minutes=30)
        )
        
        return {
            "access_token": new_access_token,
            "token_type": "bearer"
        }

    except JWTError as e:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=f"Invalid or expired refresh token: {str(e)}"
        )