import re

from . import geographical, granularities


def parse_geographical_query(query):
    parts = re.split(r'\s*\|\s*', query.strip().upper())
    geographical_granularity = granularities.GEOGRAPHICAL[parts[0]]
    if len(parts) > 1:
        islands = re.split(r'\s*,\s*', parts[1])
        items_geocodes = []
        for island in islands:
            geocodes = geographical.get_codes(island, geographical_granularity)
            items_geocodes.extend(geocodes)
    else:
        items_geocodes = []
    return geographical_granularity, '|'.join(items_geocodes)


def parse_time_query(query):
    parts = re.split(r'\s*\|\s*', query.strip().upper())
    time_granularity = granularities.TIME[parts[0]]
    if len(parts) > 1:
        time_codes = re.split(r'\s*,\s*', parts[1])
    else:
        time_codes = []
    return time_granularity, '|'.join(time_codes)


def parse_measure_query(query):
    return granularities.MEASURE[query]


def build_api_representation(geo_codes, time_codes, measure_code):
    return f'GEOGRAPHICAL[{geo_codes}],TIME[{time_codes}],MEASURE[{measure_code}]'


def build_api_granularity(geographical_granularity, time_granularity):
    return f'GEOGRAPHICAL[{geographical_granularity}],TIME[{time_granularity}]'
