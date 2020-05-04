
from calendar import *


def get_calendar_day(cal_day):
    "cal_day -> List"
    return cal_day[1]


def remove(cal_name, d, m, t):
    "String x Integer x String x String ->"
    day = new_day(d)
    mon = new_month(m)
    start = convert_time(t)
    cal_day = calendar_day(day, calendar_month(mon, fetch_calendar(cal_name)))
    new_date(day, mon)

    def try_remove(app):
        if start == start_time(get_span(app)):
            get_calendar_day(cal_day).remove(app)
            print("Appointment removed.")
    for_each_appointment(cal_day, try_remove)
