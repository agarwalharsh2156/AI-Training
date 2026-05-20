from passlib.context import CryptContext

context = CryptContext(schemes="bcrypt")
hashed = context.hash("password")
print(context.verify("apassword", hashed))

FAKE_USERS = {
    "alice" : context.hash("password123"),
    "bob" : context.hash("letmein")
}

from fastapi import FastAPI, Form

app = FastAPI()
@app.post("/authenticate/")
def authenticate_user(user_name: str = Form(...), password: str = Form(...)):
    pass