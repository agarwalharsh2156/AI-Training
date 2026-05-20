from fastapi import FastAPI, Form
from typing import Optional

app = FastAPI()

@app.post("/login/")
def login(
    username: str = Form(...),           # 👈 Form field, required
    password: str = Form(...),           # 👈 Form field, required
    remember_me: Optional[bool] = Form(False)
):
    if username == "harsh" and password == "secret123":
        return {"message": f"Welcome {username}!"}
    return {"message": "Invalid credentials"}


from fastapi import FastAPI, Form
from typing import Optional

app = FastAPI()

@app.post("/login/")
def login(
    username: str = Form(...),           # 👈 Form field, required
    password: str = Form(...),           # 👈 Form field, required
    remember_me: Optional[bool] = Form(False)
):
    if username == "harsh" and password == "secret123":
        return {"message": f"Welcome {username}!"}
    return {"message": "Invalid credentials"}



from fastapi import FastAPI, Form, File, UploadFile
from typing import Optional

app = FastAPI()

@app.post("/register/", status_code=201)
async def register(
    username: str = Form(..., min_length=3, max_length=20),
    email: str = Form(...),
    password: str = Form(..., min_length=8),
    avatar: Optional[UploadFile] = File(None)
):
    avatar_info = None
    if avatar:
        contents = await avatar.read()
        avatar_info = {
            "filename": avatar.filename,
            "type": avatar.content_type,
            "size_kb": round(len(contents) / 1024, 2)
        }

    return {
        "username": username,
        "email": email,
        "avatar": avatar_info or "No avatar uploaded"
    }