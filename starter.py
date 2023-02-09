from schedule import every, run_pending
from schedules7day import macro7day
from schedules30day import macro30days

every(30).days.do(macro30days())
every().monday.do(macro7day())

while True:
    run_pending()