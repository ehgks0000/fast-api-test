from fastapi import APIRouter, Depends, HTTPException

user_router = APIRouter(tags=["index"])

@user_router.get(
    "/",
    responses={200: {"description": "ok"}},
)
async def index() -> dict:
    return {"system": True}