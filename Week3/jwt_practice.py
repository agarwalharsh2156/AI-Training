from jose import jwt
from datetime import datetime, timedelta

SECRET_KEY = "mysecret"
ALGORITHM = "HS256"

# Create a token
payload = {
    "sub": "alice",                                          # subject — who this token is for
    "exp": datetime.now() + timedelta(minutes=1)         # expiry
}
token = jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)
print("Token:", token)
print(type(token))
# tampering with the token with lead to JWT Error
token += "a"

# Decode it back
decoded = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
print("Decoded:", decoded)

##################################################################################################################################################

from fastapi import FastAPI, HTTPException, Depends, status
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from jose import jwt, JWTError
from datetime import datetime, timedelta
from pydantic import BaseModel

app = FastAPI()

SECRET_KEY = "mysecret"
ALGORITHM = "HS256"

FAKE_USERS = {
    "alice": "password123",
    "bob": "letmein"
}

class LoginRequest(BaseModel):
    username: str
    password: str

def create_token(username: str):
    payload = {
        "sub": username,
        "exp": datetime.utcnow() + timedelta(minutes=30)
    }
    return jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)

@app.post("/token")
def login(data: LoginRequest):
    stored_password = FAKE_USERS.get(data.username)
    if not stored_password or stored_password != data.password:
        raise HTTPException(status_code=401, detail="Wrong credentials")
    token = create_token(data.username)
    return {"access_token": token, "token_type": "bearer"}

security = HTTPBearer()

@app.get("/data")
def get_data(token: HTTPAuthorizationCredentials = Depends(security)):
    try:
        decoded = jwt.decode(token.credentials, SECRET_KEY, algorithms = [ALGORITHM])
    except JWTError:
        raise HTTPException(status_code= status.HTTP_401_UNAUTHORIZED)
    user = decoded.get("sub")
    expires = decoded.get("exp")
    if not user or (user not in FAKE_USERS):
        raise HTTPException(status_code= status.HTTP_401_UNAUTHORIZED)
    else:
        return {"message": "You are authenticated, you can have your data."}