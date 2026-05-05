# Practicing the basics of fastapi
from fastapi import FastAPI, Path
from typing import Optional
from pydantic import BaseModel

app = FastAPI()
students = {
    1: {
        "name" : "Harsh",
        "college": "PICA"
    },
    2: {
        "name": "Krisha",
        "college": "PICA"
    },
    3: {
        "name": "Mahi",
        "college": "Jai Hind"
    }
}



@app.get("/")
def index():
    return {"name": "hello there mate !!"}

# path parameter
@app.get("/get-student/{student_id}")
def student_details(student_id : int = Path(description="Enter a valid integer value", gt=0)):
    return students[student_id]

# query parameter
@app.get("/students")
def student_by_name(*, name:Optional[str] = None, college: str):
    for i in students:
        if students[i]["name"] == name:
            return students[i]
    return {"error": "Data Not Found"}

# POST method along with pydantic implementation
class Student(BaseModel):
    name:str
    college:str

@app.post("/students/{student_id}")
def add_student(student_id:int, student: Student):
    if student_id in students:
        return {"error": "Student on that id already exists"}
    else:
        students[student_id] = dict(student)
        return students[student_id]

# updating student using PUT
class UpdateStudent(BaseModel):
    name : Optional[str]
    college: Optional[str]

@app.put("/update-student/{student_id}")
def update_student(student_id: int, student: UpdateStudent):
    if student_id not in students:
        return {"error": "No student with that id exists in the database."}
    else:
        for key in students[student_id].keys():
            if getattr(student, key) != None:
                students[student_id][key] = getattr(student, key)
        return students[student_id]
    
# Deleting a student
@app.delete("/delete-student/{student_id}")
def delete_student(student_id: int):
    if student_id not in students:
        return {"error": "No student with that id exists."}
    else:
        del students[student_id]
        return {"message": "Student deleted."}