from fastapi import FastAPI

from routers.item import ITEM_ROUTER


app = FastAPI()
app.include_router(ITEM_ROUTER)
