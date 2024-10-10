from fastapi import FastAPI

from item.router import ITEM_ROUTER
from clock_in.router import CLOCKIN_ROUTER


app = FastAPI()
app.include_router(ITEM_ROUTER)
app.include_router(CLOCKIN_ROUTER)
