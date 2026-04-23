from fastapi import FastAPI, Depends, HTTPException, status

FAKE_DB = {
    "users": {"alice": {"name": "Alice", "role": "admin"}},
    "items": ["hammer", "wrench", "drill"]
}

app = FastAPI()

def get_db():
    db = FAKE_DB
    try:
        yield db
    finally:
        print("Database connection Closed.")

def get_user_token(token: str, db = Depends(get_db)):
    user = db["users"].get(token)
    if not user:
        raise HTTPException(status_code= status.HTTP_401_UNAUTHORIZED)
    else:
        return user
    
@app.get("/items")
def get_item(db = Depends(get_db), user = Depends(get_user_token)):
    return {"user": user["name"], "items": db["items"]}

