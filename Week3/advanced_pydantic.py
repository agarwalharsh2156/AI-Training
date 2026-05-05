# Question
# Build a UserProfile Pydantic model for a FastAPI POST /create-profile/ endpoint with these requirements:

# username — required, accepts alias "userName", min 3 chars, max 20 chars, strip whitespace
# email — required, string
# age — required, integer, must be between 18 and 100
# bio — optional string, defaults to "No bio provided"
# is_active — optional bool, defaults to True
# A computed field display_name that returns "@{username}" (e.g. "@arjun")

# The response should not expose age — create a separate UserProfileResponse model.

from pydantic import BaseModel, Field, ConfigDict, computed_field, EmailStr, field_validator, model_validator
from fastapi import FastAPI, status
from typing import Optional

class UserProfile(BaseModel):
    model_config = ConfigDict(
        str_strip_whitespace = True,
        populate_by_name = True
    )
    username : str = Field(..., alias = "userName", min_length= 3, max_length= 20) 
    email : EmailStr
    age : int = Field(..., le=100, ge= 18)
    bio : Optional[str] = Field(default="No bio provided")
    is_active: Optional[bool] = True

    @computed_field
    @property
    def display_name(self) -> str:
        return f"@{self.username}"
    

app = FastAPI()

class ResponseProfile(BaseModel):
    username: str
    email: str
    bio: str
    is_active: bool
    display_name: str

@app.post("/create-profile/", response_model = ResponseProfile, status_code= status.HTTP_201_CREATED)
def create_profile(profile: UserProfile):
    ## Data saved in the database.
    return profile


# Build a POST /create-student/ endpoint with these nested models:
# ContactInfo model:

# phone — required string, exactly 10 characters
# email — required string
# emergency_contact — optional string, defaults to None

# Subject model:

# subject_name — required string
# marks — required int, between 0 and 100

# Student model:

# student_id — required string
# full_name — required string, min 2 chars
# contact — required, uses ContactInfo as nested model
# subjects — required, list of Subject models
# computed field percentage — average of all subject marks, rounded to 2 decimal places

# StudentResponse model should exclude contact.emergency_contact — so create a ContactInfoResponse without that field, and use it in your response model.

class ContactInfoModel(BaseModel):
    phone: str = Field(..., max_length=10, min_length=10)
    email: EmailStr
    emergency_contact: Optional[str] = None

class ContactInfoResponse(BaseModel):
    phone: str
    email: str

class SubjectModel(BaseModel):
    subject_name: str
    marks: int = Field(le=100, ge = 0)

class Student(BaseModel):
    student_id: str
    full_name: str = Field(..., min_length= 2)
    contact: ContactInfoModel
    subjects: list[SubjectModel]
    @computed_field
    @property
    def percentage(self) -> float:
        total_marks = sum(subject.marks for subject in self.subjects)
        average = total_marks / len(self.subjects)
        return round(average, 2) 

class StudentResponse(BaseModel):
    student_id: str
    full_name: str
    contact: ContactInfoResponse
    subjects: list[SubjectModel]
    percentage: float

@app.post("/create-student/", response_model=StudentResponse)
def create_student(student: Student) -> Student:
    # Data Saved
    return student


# Build a POST /register-event/ endpoint for event registration with these models and rules:
# EventRegistration model:

# participant_name — required, min 2 chars, auto-clean with mode="before" (strip + title case)
# email — required, valid email
# age — required, int, between 18 and 60
# event_name — required string
# ticket_count — required int, between 1 and 5
# ticket_price — required int, gt 0
# promo_code — optional string, defaults to None
# computed field total_cost — ticket_count × ticket_price, if promo_code == "SAVE10" apply 10% discount

# Validators:

# @field_validator on event_name — cannot contain special characters (only alphanumeric + spaces allowed)
# @model_validator — if ticket_count > 3, ticket_price must be less than 1000 (bulk discount rule — high quantity only allowed for cheaper tickets)

# EventResponse — exclude age and promo_code from response

class EventRegisteration(BaseModel):
    participant_name: str = Field(..., min_length=2)
    email: EmailStr
    age: int = Field(..., le = 60, ge = 18)
    event_name: str
    ticket_count: int = Field(..., le = 5, ge= 1)
    ticket_price: int = Field(..., gt = 0)
    promo_code: Optional[str] = None

    @computed_field
    @property
    def total_cost(self)->float:
        cost = self.ticket_count * self.ticket_price 
        if self.promo_code == "SAVE10":
            cost = cost * 0.9
        return round(cost, 2)
    
    @field_validator("event_name")
    @classmethod
    def validate_event_name(cls, value):
        if not value.replace(" ", "").isalnum():
            raise ValueError("Event Name must not contain any special characters except space.")
        return value
    
    @field_validator("participant_name", mode = "before")
    @classmethod
    def validate_participant(cls, value):
        value = value.strip().title()
        return value
    
    @model_validator(mode = "after")
    def class_validation(self):
        if self.ticket_price > 1000:
            if self.ticket_count > 3:
                raise ValueError("bulk discount rule — high quantity only allowed for cheaper tickets")
        return self
    
class EventResponse(BaseModel):
    participant_name: str
    email: EmailStr
    event_name: str
    ticket_count: int
    ticket_price: int
    total_cost: float

@app.post("/register-event/", response_model=EventResponse)
def register_event(event: EventRegisteration):
    # Event registeration made.
    return event

# Create two endpoints:

# GET /product/{id} — returns name, price, stock only. Use response_model_include.
# GET /product/{id}/public — returns everything except cost_price and warehouse_location. Use response_model_exclude.

class Product(BaseModel):
    name: str
    price: int
    cost_price: int        # internal, never expose
    stock: int
    discount: Optional[float] = None
    warehouse_location: str
