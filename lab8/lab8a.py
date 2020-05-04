
from calendar import *


def start_time(ts):
    "span -> time"
    ensure(ts, is_time_span)
    return strip_tag(ts)[0]


def end_time(ts):
    "span -> time"
    ensure(ts, is_time_span)
    return strip_tag(ts)[1]


def overlap(ts1, ts2):
    "span x span -> span"
    if are_overlapping(ts1, ts2):
        start_time1 = start_time(ts1)
        start_time2 = start_time(ts2)

        end_time1 = end_time(ts1)
        end_time2 = end_time(ts2)

        new_time1 = latest_time(start_time1, start_time2)
        new_time2 = earliest_time(end_time1, end_time2)

        return new_time_span(new_time1, new_time2)


def length_of_span(ts):
    "span -> duration"
    start = start_time(ts)
    end = end_time(ts)
    minute = get_integer(get_minute(end)) - get_integer(get_minute(start))
    hour = get_integer(get_hour(end)) - get_integer(get_hour(start))
    if minute < 0:
        minute += 60
        hour -= 1
    return new_duration(new_hour(hour), new_minute(minute))


def new_duration(hour, minute):
    "hour x minute -> duration"
    ensure(hour, is_hour)
    ensure(minute, is_minute)
    return attach_tag("duration", (hour, minute))
