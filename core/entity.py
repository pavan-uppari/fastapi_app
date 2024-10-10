from datetime import date
from functools import cached_property

from pydantic import (
    BaseModel,
    EmailStr,
    StrictStr,
    computed_field,
    PositiveInt,
    FutureDate,
)


class Item(BaseModel):

    id: PositiveInt
    name: StrictStr
    email: EmailStr
    quantity: PositiveInt
    expiry_date: FutureDate

    @computed_field
    @cached_property
    def created_date(self) -> date:
        "returns today date"

        return date.today()


class ClockIn(BaseModel):

    id: PositiveInt
    email: EmailStr
    location: StrictStr

    @computed_field
    @cached_property
    def created_date(self) -> date:
        "returns today date"

        return date.today()
