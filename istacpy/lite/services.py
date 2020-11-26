import re

from istacpy.lite.dimensions.geographical import (
    GeographicalGranularity,
    GeographicalRepresentation,
)
from istacpy.lite.dimensions.measure import MeasureGranularity
from istacpy.lite.dimensions.time import TimeGranularity, TimeRepresentation


def parse_geographical_query(query):
    parts = re.split(r'\s*\|\s*', query.strip().upper())
    granularity = GeographicalGranularity.get_code(parts[0])
    if len(parts) > 1:
        islands = re.split(r'\s*,\s*', parts[1])
        items_codes = []
        for island in islands:
            codes = GeographicalRepresentation.get_codes(island, granularity)
            items_codes.extend(codes)
    else:
        items_codes = []
    return granularity, '|'.join(items_codes)


def parse_time_query(query):
    parts = re.split(r'\s*\|\s*', query.strip().upper())
    granularity = TimeGranularity.get_code(parts[0])
    if len(parts) > 1:
        years = re.split(r'\s*,\s*', parts[1])
        items_codes = []
        for year in years:
            codes = TimeRepresentation.get_codes(year, granularity)
            items_codes.extend(codes)
    else:
        items_codes = []
    return granularity, '|'.join(items_codes)


def parse_measure_query(query):
    return MeasureGranularity.get_code(query)


def build_api_representation(geo_codes, time_codes, measure_code):
    return f'GEOGRAPHICAL[{geo_codes}],TIME[{time_codes}],MEASURE[{measure_code}]'


def build_api_granularity(geographical_granularity, time_granularity):
    return f'GEOGRAPHICAL[{geographical_granularity}],TIME[{time_granularity}]'


def build_custom_response(api_response):
    api_index = api_response['dimension']['TIME']['representation']['index']
    index = tuple(api_index.keys())
    api_columns = api_response['dimension']['GEOGRAPHICAL']['representation']['index']
    columns = [GeographicalRepresentation.get_title(code) for code in api_columns]
    observations = api_response['observation']
    num_rows = len(index)
    data = {}
    for i, column in enumerate(columns):
        data[column] = tuple(observations[i : i + num_rows])
        i += num_rows
    return dict(index=index, data=data)


def build_custom_granularity(api_response, dimension, granularity_handler):
    granularities = []
    for g in api_response['dimension'][dimension]['granularity']:
        code = g['code']
        id = granularity_handler.get_id(code)
        granularities.append(f'{code} ({id})')
    return granularities
