from typing import Union
from fastapi import FastAPI
from routers.user import user_router
from fastapi import APIRouter, FastAPI, Request, Response
from fastapi.routing import APIRoute

app = FastAPI()
router = APIRouter()

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

# @router.get("/test")
# async def timed():
#     return {"msg": "is"}

app.include_router(router, prefix="/user")
app.include_router(user_router, prefix="/user2")