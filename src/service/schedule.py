from uuid import uuid4
from sqlalchemy.orm import Session
from datetime import datetime, timedelta, date
from fastapi import HTTPException, status
from typing import Tuple
from src.model.schedule.schedule import Schedules
from src.model.schedule.scheduleEnum import TimeRange
from src.service.outbound.neis import neis_request


def get_schedule(session: Session, time_range: TimeRange):
 
    date = datetime.now().date()

    if time_range == TimeRange.week:
        start_date, end_date = get_start_end_date(date=date, days=7)
    elif time_range == TimeRange.month:
        start_date, end_date = get_start_end_date(date=date, days=30)
    elif time_range == TimeRange.year:
        start_date = str(datetime(year=datetime.now().year, month=1, day=1).date()).replace("-", "")
        end_date = str(datetime(year=datetime.now().year, month=12, day=31).date()).replace("-", "")
        print(start_date, end_date)
    else:
        return HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="is not enum only week, month, year")

    response = neis_request(start_date=start_date, end_date=end_date)

    for i in response:
        is_schedules = session.query(Schedules).filter(Schedules.date == i['date'], Schedules.name == i['name']).first()
        if is_schedules:
            is_schedules.date = i['date']
            is_schedules.name = i['name']
        else:
            Schedules(**i, id=uuid4().bytes_le).save(session=session)

    return HTTPException(status_code=status.HTTP_200_OK)


def get_start_end_date(date: date, days=int) -> Tuple[str, str]:
    start_date = str(date).replace("-", "")
    end_date = str(date + timedelta(days=days)).replace("-", "")

    return start_date, end_date
