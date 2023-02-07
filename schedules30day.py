import requests
from util import session_scope
from models import Schedules
from datetime import datetime, timedelta
from dateutil import relativedelta
from uuid import uuid4
from config import Config


def macro30days():
    with session_scope() as session:
        start_at = datetime(year=datetime.now().year, month=datetime.now().month, day=1).date()
        next_month = start_at + relativedelta.relativedelta(months=1)
        end_at = next_month - timedelta(days=1)

        start_at = str(start_at).replace("-", "")
        end_at = str(end_at).replace("-", "")

        lists = requests.get(
            f"https://open.neis.go.kr/hub/SchoolSchedule?ATPT_OFCDC_SC_CODE=G10&SD_SCHUL_CODE=7430310&pSize=1000&KEY={Config.KEY}&Type=json&AA_FROM_YMD={start_at}&AA_TO_YMD={end_at}"
        ).json()
        for i in range(len(lists["SchoolSchedule"][1]["row"])):
            chenk = session.query(Schedules).filter(Schedules.data == datetime.strptime(lists["SchoolSchedule"][1]["row"][i]['AA_YMD'], '%Y%m%d').date()).all()
            if not chenk:
                session.add(
                    Schedules(
                        id=uuid4().bytes_le,
                        name=lists["SchoolSchedule"][1]["row"][i]['EVENT_NM'],
                        data=datetime.strptime(lists["SchoolSchedule"][1]["row"][i]['AA_YMD'], '%Y%m%d').date()
                    )
                )

            else:
                for j in chenk:
                    session.delete(j)
                session.add(
                    Schedules(
                        id=uuid4().bytes_le,
                        name=lists["SchoolSchedule"][1]["row"][i]['EVENT_NM'],
                        data=datetime.strptime(lists["SchoolSchedule"][1]["row"][i]['AA_YMD'], '%Y%m%d').date()
                    )
                )
