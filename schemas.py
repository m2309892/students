from pydantic import BaseModel, EmailStr
from typing import Optional

class StudentBase(BaseModel):
    first_name: str
    last_name: str
    email: EmailStr
    phone: Optional[str] = None
    faculty: str
    course: int

class StudentCreate(StudentBase):
    pass

class StudentUpdate(StudentBase):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    email: Optional[EmailStr] = None
    phone: Optional[str] = None
    faculty: Optional[str] = None
    course: Optional[int] = None

class Student(StudentBase):
    id: int

    class Config:
        from_attributes = True 