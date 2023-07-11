from datetime import datetime

import requests
from config import Config
from typing import List, Dict

NEIS_URL = "https://open.neis.go.kr/hub/SchoolSchedule?ATPT_OFCDC_SC_CODE=G10&SD_SCHUL_CODE=7430310&pSize=1000&KEY={API_KEY}&Type=json&AA_FROM_YMD={start_date}&AA_TO_YMD={end_date}"


def neis_request(start_date: str, end_date: str) -> List[Dict[str, str]]:
    response_data = requests.get(
        NEIS_URL.format(API_KEY=Config.KEY, start_date=start_date, end_date=end_date)
    ).json()

    rows = response_data['SchoolSchedule'][1]['row']
    date_and_events = [{"date": datetime.strptime(row['AA_YMD'], "%Y%m%d").date(), "name": row['EVENT_NM']} for row in
                       rows]

    return date_and_events
