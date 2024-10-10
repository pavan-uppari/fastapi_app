from datetime import date

from pydantic import BaseModel, EmailStr, Field, StrictStr


class FilterParams(BaseModel):

    email: EmailStr = Field(
        None, description="return clock in records with email exact match"
    )
    location: StrictStr = Field(
        None, description="return clock in records with exact location match"
    )
    created_date: date = Field(
        None, description="return clock in records created after provided date"
    )
