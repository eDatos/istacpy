import re

from istacpy import config
from istacpy.lite.dimensions.base import Dimension
from istacpy.lite.dimensions.geographical import (
    GeographicalGranularity,
    GeographicalRepresentation,
)
from istacpy.lite.dimensions.measure import MeasureRepresentation
from istacpy.lite.dimensions.time import TimeGranularity, TimeRepresentation
from istacpy.lite.locale import Locale


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
        year_ranges = re.split(r'\s*,\s*', parts[1])
        items_codes = []
        for year_range in year_ranges:
            years = re.split(r'\s*:\s*', year_range)
            if len(years) > 1:
                year_list = range(int(years[0]), int(years[1]) + 1)
            else:
                year_list = years
            for year in year_list:
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


def _normalize_value(value):
    typecast = float if value.find('.') != -1 else int
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
    index = _get_ordered_representation_api_codes(api_response, Dimension.TIME)
    columns = _get_ordered_representation_api_codes(api_response, Dimension.GEOGRAPHICAL)
    observations = api_response['observation']

    i, data, num_rows = 0, {}, len(index)
    for column in columns:
        values = observations[i : i + num_rows]
        annotated_values = sorted([(idx, value) for idx, value in zip(index, values)])
        data[column] = tuple([_normalize_value(value[1]) for value in annotated_values])
        i += num_rows
    # sort index to be in coherence with sorted values
    index = sorted(index)

    # title index and columns
    titled_index = tuple([TimeRepresentation.get_title(item) for item in index])
    titled_data = {GeographicalRepresentation.get_title(k): v for k, v in data.items()}

    return dict(index=titled_index, data=titled_data)


def build_custom_granularity(api_response, dimension, granularity_handler):
    granularities = {}
    for g in api_response['dimension'][dimension]['granularity']:
        code = g['code']
        id = granularity_handler.get_id(code)
        granularities[code] = id
    return granularities


def build_custom_representation(api_response, dimension, representation_handler):
    granularities = {}
    for g in api_response['dimension'][dimension]['representation']:
        code = g['code']
        id = representation_handler.get_id(code)
        granularities[code] = id
    return granularities


def get_indicator_title(api_response):
    text = api_response['title'].get(Locale.DEFAULT_LOCALE, Locale.non_available_msg())
    return text.strip(' .')


def get_indicator_subject(api_response):
    text = re.sub(
        r'^[\s\d]+',  # clean leading digits
        '',
        api_response['subjectTitle'].get(Locale.DEFAULT_LOCALE, Locale.non_available_msg()),
    )
    return text.strip(' .')


def get_indicator_description(api_response):
    if 'conceptDescription' in api_response:
        text = api_response['conceptDescription'].get(
            Locale.DEFAULT_LOCALE, Locale.non_available_msg()
        )
    else:
        text = Locale.non_available_msg()
    return text.strip(' .')


def get_years_range(api_response):
    time_items = api_response['dimension'][Dimension.TIME]['representation']
    years = []
    for item in time_items:
        code = item['code']
        if year := re.findall(r'\d{4}', code):  # extract year
            years.append(int(year[0]))
    return sorted(list(set(years)))
