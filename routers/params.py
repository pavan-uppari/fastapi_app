from datetime import date

from pydantic import BaseModel, EmailStr, StrictInt, Field


class FilterParams(BaseModel):

    email: EmailStr = Field(None, description="return item with email exact match")
    expiry_date: date = Field(
        None, description="return items expiring after provided date"
    )
    created_date: date = Field(
        None, description="return items created after provided date"
    )
    quantity: int = Field(
        None, description="return items whose quantity is greater than provided value"
    )
