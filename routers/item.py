from typing import Annotated

from fastapi import APIRouter, Query

from .params import FilterParams
from .errors import RESOURCE_NOT_FOUND
from core.entity import Item
from database import T_Item

ITEM_ROUTER = APIRouter()


@ITEM_ROUTER.post("/items/", status_code=201)
def create_item(item: Item) -> Item:
    "Create an item"

    T_Item.insert_one(item.model_dump(mode="json"))
    return item


@ITEM_ROUTER.get("/items/{item_id}")
def get_item(item_id: int) -> Item:
    "Get an item with id"

    item = T_Item.find_one({"id": item_id})
    if not item:
        raise RESOURCE_NOT_FOUND
    return Item(**item)


@ITEM_ROUTER.get("/items/")
def get_items(filter_params: Annotated[FilterParams, Query()]) -> list[Item]:
    "Get items with additional filters"

    params_dict = filter_params.model_dump(exclude_none=True, mode="json")

    query_filter = {}
    if email_filter := params_dict.pop("email", None):
        query_filter["email"] = email_filter

    # except email, every other filter requires $gte
    query_filter.update({key: {"$gte": value} for key, value in params_dict.items()})

    items = T_Item.find(query_filter)

    return [Item(**item) for item in items]


@ITEM_ROUTER.get("/items/group-by-email/")
def get_item_count_per_email():
    "Get item count per email"

    result = T_Item.aggregate([{"$group": {"_id": "$email", "count": {"$sum": 1}}}])
    return list(result)


@ITEM_ROUTER.delete("/items/{item_id}", status_code=204)
def delete_item(item_id: int):
    "Delete an item"

    item = T_Item.find_one_and_delete({"id": item_id})
    if not item:
        raise RESOURCE_NOT_FOUND


@ITEM_ROUTER.put("/items/{item_id}")
def update_item(item_id: int, item: Item) -> Item:
    "Update an item"

    item = T_Item.find_one_and_update(
        {"id": item_id}, {"$set": item.model_dump(mode="json")}
    )
    if not item:
        raise RESOURCE_NOT_FOUND

    return Item(**item)
