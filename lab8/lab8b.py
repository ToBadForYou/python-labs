
from calendar import *


def first_span(spans):
    "spans -> span"
    ensure(spans, is_time_spans)
    if is_empty_time_spans(spans):
        raise Exception('Empty spans.')
    else:
        return strip_tag(spans)[0]


def rest_spans(spans):
    "spans -> spans"
    ensure(spans, is_time_spans)
    if is_empty_time_spans(spans):
        return spans
    else:
        return attach_tag('time_spans', strip_tag(spans)[1:])


def new_time_spans():
    " -> spans"
    return attach_tag('time_spans', [])


def is_time_spans(object):
    "Python object -> Bool"
    return get_tag(object) == 'time_spans'


def is_empty_time_spans(spans):
    "spans -> Bool"
    return len(get_time_spans(spans)) == 0


def get_time_spans(spans):
    "spans -> List"
    return spans[1]


def sort_spans(span, spans):
    "span x spans -> spans"
    mid_i = len(spans) // 2
    if len(spans) == 0:
        spans.append(span)
    elif earliest_time(start_time(spans[mid_i]),
                       start_time(span)) == start_time(span):
        spans = sort_spans(span, spans[:mid_i]) + spans[mid_i:]
    else:
        spans = spans[:mid_i + 1] + sort_spans(span, spans[mid_i + 1:])
    return spans


def insert_span(span, spans):
    "span x spans -> spans"
    return attach_tag('time_spans', sort_spans(span, get_time_spans(spans)))


def show_time_spans(spans):
    "spans ->"
    for span in get_time_spans(spans):
        show_span(span)
        print("")
