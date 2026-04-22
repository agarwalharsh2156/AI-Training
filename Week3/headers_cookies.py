from fastapi import FastAPI, Header, Cookie, Response
from typing import Optional

app = FastAPI()

@app.get("/get-data/")
def get_data(
    x_api_key: str = Header(...),
    user_agent: Optional[str] = Header(None),
    session_key: Optional[str] = Cookie(None)  
):
    if not session_key:
        return {"message": "You are not logged in. Please login first."}
    if x_api_key != "get_data_access1234":
        return {"message": "Invalid API key. You are not authorised."}
    return {"message": "Here is your data.", "user_agent": user_agent}


@app.post("/login/")          
def login(response: Response):
    response.set_cookie(
        key="session_key",
        value="session_key_created123",
        httponly=True,
        max_age=3600       
    )
    return {"message": "You are logged in."}


@app.post("/logout/")         
def logout(response: Response, session_key: Optional[str] = Cookie(None)):
    if not session_key:
        return {"message": "You are not logged in."}
    response.delete_cookie(key="session_key")
    return {"message": "Logged out successfully."}