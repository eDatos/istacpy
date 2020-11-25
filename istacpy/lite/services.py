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


def build_custom_response(api_response):
    api_index = api_response['dimension']['TIME']['representation']['index']
    index = tuple(api_index.keys())
    api_columns = api_response['dimension']['GEOGRAPHICAL']['representation']['index']
    columns = [geographical.get_title(code) for code in api_columns]
    observations = api_response['observation']
    num_rows = len(index)
    data = {}
    for i, column in enumerate(columns):
        data[column] = tuple(observations[i : i + num_rows])
        i += num_rows
    return dict(index=index, data=data)
