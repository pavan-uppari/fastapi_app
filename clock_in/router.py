from typing import Annotated

from fastapi import APIRouter, Query, HTTPException

from .params import FilterParams
from core.entity import ClockIn
from database import T_ClockIn

CLOCKIN_ROUTER = APIRouter()

RESOURCE_NOT_FOUND = HTTPException(status_code=404, detail="resource not found")


@CLOCKIN_ROUTER.post("/clock-in", status_code=201)
def create_clockin(clockin: ClockIn) -> ClockIn:
    "Create a clock in record"

    T_ClockIn.insert_one(clockin.model_dump(mode="json"))
    return clockin


@CLOCKIN_ROUTER.get("/clock-in/{clockin_id}")
def get_clockin(clockin_id: int) -> ClockIn:
    "Get clock in record with id"

    item = T_ClockIn.find_one({"id": clockin_id})
    if not item:
        raise RESOURCE_NOT_FOUND
    return ClockIn(**item)


@CLOCKIN_ROUTER.get("/clock-in")
def get_clockins(filter_params: Annotated[FilterParams, Query()]) -> list[ClockIn]:
    "Get clock in records with additional filters"

    param_dict = filter_params.model_dump(exclude_none=True, mode="json")

    query_filter = {}
    if created_date := param_dict.pop("created_date", None):
        query_filter["created_date"] = {"$gte": created_date}

    # except created_date, every other filter doesn't require gte
    query_filter.update(param_dict)

    items = T_ClockIn.find(query_filter)
    return [ClockIn(**item) for item in items]


@CLOCKIN_ROUTER.delete("/clock-in/{clockin_id}", status_code=204)
def delete_clockin(clockin_id: int):
    "Delete a clock in record"

    item = T_ClockIn.find_one_and_delete({"id": clockin_id})
    if not item:
        raise RESOURCE_NOT_FOUND


@CLOCKIN_ROUTER.put("/clock-in/{clockin_id}")
def update_clockin(clockin_id: int, item: ClockIn):
    "Update a clock in record"

    item = T_ClockIn.find_one_and_update(
        {"id": clockin_id}, {"$set": item.model_dump(mode="json")}
    )

    if not item:
        raise RESOURCE_NOT_FOUND

    return ClockIn(**item)
