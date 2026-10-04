from typing import Optional
from decimal import Decimal
from pydantic import BaseModel, EmailStr, Field


# Base schema with shared fields
class EmployeeBase(BaseModel):
    name: str = Field(..., min_length=1, max_length=100)
    email: EmailStr
    phone: Optional[str] = Field(None, max_length=20)
    role: str = Field(..., max_length=50)
    status: str = Field(..., max_length=50)


# Schema for creating a new employee
class EmployeeCreate(EmployeeBase):
    pass


# Schema for updating employee details (all fields optional)
class EmployeeUpdate(BaseModel):
    name: Optional[str] = Field(None, min_length=1, max_length=100)
    email: Optional[EmailStr] = None
    phone: Optional[str] = Field(None, max_length=20)
    role: Optional[str] = Field(None, max_length=50)
    status: str = Field(..., max_length=50)


# Schema for JSON responses
class EmployeeResponse(EmployeeBase):
    employee_id: int

    class Config:
        from_attributes = True