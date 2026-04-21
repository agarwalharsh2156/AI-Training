# Question
# Build a UserProfile Pydantic model for a FastAPI POST /create-profile/ endpoint with these requirements:

# username — required, accepts alias "userName", min 3 chars, max 20 chars, strip whitespace
# email — required, string
# age — required, integer, must be between 18 and 100
# bio — optional string, defaults to "No bio provided"
# is_active — optional bool, defaults to True
# A computed field display_name that returns "@{username}" (e.g. "@arjun")

# The response should not expose age — create a separate UserProfileResponse model.

from pydantic import BaseModel, Field, ConfigDict, computed_field
from fastapi import FastAPI
from typing import Optional

class UserProfile(BaseModel):
    model_config = ConfigDict(
        str_strip_whitespace = True,
        populate_by_name = True
    )
    username : str = Field(..., alias = "userName", min_length= 3, max_length= 20) 
    email : str
    age : int = Field(..., le=100, ge= 18)
    bio : Optional[str] = Field(default="No bio provided")
    is_active: Optional[bool] = True

    @computed_field
    @property
    def display_name():
        return f"@{self.username}"
    

app = FastAPI()

@app.post("/create-profile/")
def create_profile(profile: UserProfile):
    ## Data saved in the database.
    return profile

