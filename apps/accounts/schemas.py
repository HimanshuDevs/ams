from pydantic import BaseModel, Field, EmailStr
from typing import Optional

class CreateUserForm(BaseModel):
    type          : Optional[str] = None
    full_name     : str = Field(..., max_length=150)
    username      : str = Field(..., max_length=50)
    email         : EmailStr = Field(..., max_length=50)
    password      : str = Field(..., min_length=6, max_length=255)

class UserLoginSchema(BaseModel):
    username       : str = Field(min_length=5)
    password       : str = Field(min_length=3)

class GetUserSchema(BaseModel):
    id             : int
    type           : Optional[str]
    full_name      : str
    username       : str
    email          : str

    model_config = {
        "from_attributes": True
    }

class CreateDepartmentSchema(BaseModel):
    department_name   : str
    submitted_by      : Optional[int] = None

class GetDepartmentSchema(BaseModel):
    id              : int
    department_name : str
    submitted_by    : Optional[int]

    model_config = {
        "from_attributes": True
    }