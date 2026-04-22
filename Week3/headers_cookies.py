from fastapi import FastAPI, Header, Cookie, Response
from typing import Optional

app = FastAPI()
@app.get("/get-data/")
def get_data(
    x_api_key : str = Header(...),
    user_agent: Optional[str] = Header(None),
    session_key: str = Cookie(None)
):
    if session_key:
        if x_api_key == "get_data_access1234":
            return "Here is your data."
        else:
            return "You are not authorised to access this data."
    else:
        return "You are not logged in, please login to access the app features."
    

@app.get("/login/")
def login(response:Response):
    response.set_cookie(
        key = "session_key",
        value= "session_key_created123",
        httponly = True,
        expires= 30
    )
    return {"message": "You are logged in"}

@app.get("/logout/")
def logout(response: Response, session_key: str= Cookie(None)):
    if session_key:
        response.delete_cookie(
            key = "session_key"
        )
        return {"message": "User logged out."}
    else:
        return {"message": "You first need to login idiot."}