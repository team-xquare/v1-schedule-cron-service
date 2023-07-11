from uuid import uuid4
from sqlalchemy.orm import Session
from datetime import datetime, timedelta
from fastapi import HTTPException, status
from src.model.schedule.schedule import Schedules
from src.model.schedule.scheduleEnum import TimeRange
from src.service.outbound.neis import neis_request


def get_schedule(session: Session, time_range: TimeRange):
    time_range = 7 if time_range == TimeRange.week else 30

    date = datetime.now().date()

    start_date = str(date).replace("-", "")
    end_date = str(date + timedelta(days=time_range)).replace("-", "")

    response = neis_request(start_date=start_date, end_date=end_date)

    for i in response:
        is_schedules = session.query(Schedules).filter(Schedules.date == i['date'], Schedules.name == i['name']).first()
        if is_schedules:
            is_schedules.date = i['date']
            is_schedules.name = i['name']
        else:
            Schedules(**i, id=uuid4().bytes_le).save(session=session)
    return HTTPException(status_code=status.HTTP_200_OK)