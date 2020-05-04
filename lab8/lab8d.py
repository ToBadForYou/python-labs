

def show_free(cal_name, d, m, t1, t2):
    "String x Integer x String x String x String ->"
    day = new_day(d)
    mon = new_month(m)
    start = convert_time(t1)
    end = convert_time(t2)
    cal_day = calendar_day(day, calendar_month(mon, fetch_calendar(cal_name)))
    show_time_spans(free_spans(cal_day, start, end))


def spans_copy(spans):
    "spans -> spans"
    time_spans = get_time_spans(spans)
    new_spans = new_time_spans()
    for span in time_spans:
        new_spans = insert_span(span, new_spans)
    return new_spans


def free_spans(cal_day, start1, end1, spans=new_time_spans()):
    "calendar_day x time x time (x spans) -> spans"
    span1 = new_time_span(start1, end1)
    if is_empty_calendar_day(cal_day):
        return insert_span(span1, spans_copy(spans))
    app = first_appointment(cal_day)
    start2 = start_time(get_span(app))
    end2 = end_time(get_span(app))
    span2 = new_time_span(start2, end2)
    if not are_overlapping(span1, span2):
        return insert_span(span1, spans_copy(spans))
    if earliest_time(start1, start2) == start1 and start1 != start2:
        spans = free_spans(rest_calendar_day(cal_day), start1, start2, spans)
    if latest_time(end1, end2) == end1 and end2 != end1:
        spans = free_spans(rest_calendar_day(cal_day), end2, end1, spans)
    return spans
