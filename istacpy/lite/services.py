import re

from istacpy import config
from istacpy.lite.dimensions.geographical import (
    GeographicalGranularity,
    GeographicalRepresentation,
)
from istacpy.lite.dimensions.measure import MeasureRepresentation
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
    return MeasureRepresentation.get_code(query)


def build_api_representation(geo_codes, time_codes, measure_code):
    return f'GEOGRAPHICAL[{geo_codes}],TIME[{time_codes}],MEASURE[{measure_code}]'


def build_api_granularity(geographical_granularity, time_granularity):
    return f'GEOGRAPHICAL[{geographical_granularity}],TIME[{time_granularity}]'


def _normalize_value(value, typecast):
    try:
        value = typecast(value)
    except ValueError:
        value = config.VALUE_ERROR
    return value


def _get_ordered_representation_api_codes(api_response, dimension):
    index = api_response['dimension'][dimension]['representation']['index']
    # index is a dict
    items = sorted(tuple(index.items()), key=lambda i: i[1])
    return [item[0] for item in items]


def build_custom_response(api_response):
    index = _get_ordered_representation_api_codes(api_response, 'TIME')
    columns = _get_ordered_representation_api_codes(api_response, 'GEOGRAPHICAL')
    measures = _get_ordered_representation_api_codes(api_response, 'MEASURE')
    # only one measure is assumed
    measure = measures[0]
    observations = api_response['observation']

    typecast = MeasureRepresentation.get_typecast(measure)
    i, data, num_rows = 0, {}, len(index)

    for column in columns:
        values = observations[i : i + num_rows]
        annotated_values = sorted([(idx, value) for idx, value in zip(index, values)])
        data[column] = tuple(
            [_normalize_value(value[1], typecast) for value in annotated_values]
        )
        i += num_rows
    # sort index to be in coherence with sorted values
    index = sorted(index)

    # title index and columns
    titled_index = tuple([TimeRepresentation.get_title(item) for item in index])
    titled_data = {GeographicalRepresentation.get_title(k): v for k, v in data.items()}

    return dict(index=titled_index, data=titled_data)


def build_custom_granularity(api_response, dimension, granularity_handler):
    granularities = []
    for g in api_response['dimension'][dimension]['granularity']:
        code = g['code']
        id = granularity_handler.get_id(code)
        granularities.append(f'{code} ({id})')
    return granularities


def build_custom_representation(api_response, dimension, representation_handler):
    granularities = []
    for g in api_response['dimension'][dimension]['representation']:
        code = g['code']
        id = representation_handler.get_id(code)
        granularities.append(f'{code} ({id})')
    return granularities
