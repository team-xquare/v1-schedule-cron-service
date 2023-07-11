from fastapi import APIRouter
from src.model import session_scope
from src.service.schedule import get_schedule
from src.model.schedule.scheduleEnum import TimeRange

app = APIRouter()


@app.post("/{time_range}")
async def add_schedule(time_range: TimeRange):
    with session_scope() as session:
        return get_schedule(session=session, time_range=time_range)
