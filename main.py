from fastapi import FastAPI, HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from passlib.context import CryptContext
from datetime import datetime, timedelta
from jose import JWTError, jwt


# Define a FastAPI app
app = FastAPI()

# Define a secret key and an algorithm for the JSON Web Token (JWT)
SECRET_KEY = "mysecretkey"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

# Define a dictionary of fake users for demo purposes
fake_users_db = {
    "john.doe@example.com": {
        "email": "john.doe@example.com",
        "hashed_password": "$2b$12$L5hJ1x3mWmS64PvzAfR5oOZXjwSo1Wd4fnv/TAKX54iFLxJNcPfXC",
        "disabled": False,
    },
    "jane.doe@example.com": {
        "email": "jane.doe@example.com",
        "hashed_password": "$2b$12$OwJZB8Og6vgf/LkFM/Kx1.R3aW8NTvWX5keRJjbNYCf5hv4Z4d4gu",
        "disabled": True,
    },
}

# Define a password context for hashing passwords
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Define a function to verify a user's email and password
def verify_user(email: str, password: str):
    if email not in fake_users_db:
        return False
    user = fake_users_db[email]
    if not pwd_context.verify(password, user["hashed_password"]):
        return False
    return user

# Define a function to create an access token for a user
def create_access_token(data: dict, expires_delta: timedelta):
    to_encode = data.copy()
    expire = datetime.utcnow() + expires_delta
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

# Define an OAuth2 scheme for bearer tokens
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Define a route for creating a new user
@app.post("/register")
async def register(email: str, password: str):
    if email in fake_users_db:
        raise HTTPException(status_code=400, detail="Email already registered")
    hashed_password = pwd_context.hash(password)
    user = {"email": email, "hashed_password": hashed_password, "disabled": False}
    fake_users_db[email] = user
    access_token = create_access_token(data={"sub": email}, expires_delta=timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES))
    return {"access_token": access_token, "token_type": "bearer"}

# Define a route for getting an access token
@app.post("/token")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = verify_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(status_code=400, detail="Incorrect email or password")
    access_token = create_access_token(data={"sub": user["email"]}, expires_delta=timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES))
    return {"access_token": access_token, "token_type": "bearer"}

# Define a route that requires authentication
