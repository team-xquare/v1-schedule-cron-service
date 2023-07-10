from fastapi import APIRouter

from . import schedule

api_router = APIRouter()

api_router.include_router(schedule.app, prefix="/schedule", tags=["schedule"])