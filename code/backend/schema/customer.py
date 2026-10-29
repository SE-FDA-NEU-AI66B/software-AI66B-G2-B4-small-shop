from typing import Optional
from datetime import date
from decimal import Decimal
from pydantic import BaseModel, EmailStr


class CustomerResponse(BaseModel):
    customer_id: int
    name: str
    phone: str
    email: Optional[EmailStr] = None
    total_spent: Decimal
    membership: Optional[str] = None
    created_at: Optional[date] = None