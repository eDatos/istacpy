import re

from istacpy import config
from istacpy.lite.dimensions.base import Dimension
from istacpy.lite.dimensions.geographical import (
    GeographicalGranularity,
    GeographicalRepresentation,
)
from istacpy.lite.dimensions.measure import MeasureRepresentation
from istacpy.lite.dimensions.time import TimeGranularity, TimeRepresentation
from istacpy.lite.i18n import Locale, Message, gettext


def parse_geographical_query(query):
    query = query.strip().upper()
    if m := re.match(r'^(=)?([A-Z])(?:\|(.*))?$', query, re.I):
        raw_output, granularity_id, filter = m.groups()
        granularity_code = GeographicalGranularity.get_code(granularity_id)
        if filter is not None:
            islands = re.split(r'\s*,\s*', filter)
            items_codes = []
            for island in islands:
                codes = GeographicalRepresentation.get_codes(island, granularity_code)
                items_codes.extend(codes)
        else:
            items_codes = []
        return raw_output is None, granularity_code, '|'.join(items_codes)


def parse_time_query(query, use_dash, latest_year=None):
    query = query.strip().upper()
    if m := re.match(r'^(=)?([A-Z])(?:\|(.*))?$', query, re.I):
        raw_output, granularity_id, filter = m.groups()
        granularity_code = TimeGranularity.get_code(granularity_id)
        use_dash = use_dash[granularity_code]
        if filter is not None:
            if filter == config.LATEST_VALUE_FLAG:
                year_ranges = [str(latest_year)]
            else:
                year_ranges = re.split(r'\s*,\s*', filter)
            items_codes = []
            for year_range in year_ranges:
                years = re.split(r'\s*:\s*', year_range)
                if len(years) > 1:
                    year_list = range(int(years[0]), int(years[1]) + 1)
                else:
                    year_list = years
                for year in year_list:
                    codes = TimeRepresentation.get_codes(year, granularity_code, use_dash)
                    items_codes.extend(codes)
        else:
            items_codes = []
        return raw_output is None, granularity_code, '|'.join(items_codes)


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


def build_custom_response(api_response, map_geographical_values=True, map_time_values=True):
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
    if map_geographical_values:
        data = {GeographicalRepresentation.get_title(k): v for k, v in data.items()}
    if map_time_values:
        index = tuple([TimeRepresentation.get_title(item) for item in index])

    return index, data


def build_custom_dimension(api_response, property, dimension, granularity_handler):
    granularity = api_response['dimension'][dimension][property]
    return {e['code']: granularity_handler.get_id(e['code']) for e in granularity}


def time_granularities_using_dashes(api_response, time_granularities):
    """
    Some indicators use time granularities whose codes include dashes . e.g. 2020-M1
    This functions detect which granularities use dashes in its representation.
    """
    dash_presence = {}
    for r in api_response['dimension'][Dimension.TIME]['representation']:
        granularity_code = r['granularityCode']
        if granularity_code not in dash_presence:
            dash_presence[granularity_code] = r['code'].find('-') != -1
        if len(dash_presence) == len(time_granularities):
            break
    return dash_presence


def get_indicator_title(api_response):
    text = api_response['title'].get(Locale.DEFAULT_LOCALE, gettext(Message.NON_AVAILABLE))
    return text.strip(' .')


def get_indicator_subject(api_response):
    text = re.sub(
        r'^[\s\d]+',  # clean leading digits
        '',
        api_response['subjectTitle'].get(
            Locale.DEFAULT_LOCALE, gettext(Message.NON_AVAILABLE)
        ),
    )
    return text.strip(' .')


def get_indicator_description(api_response):
    if 'conceptDescription' in api_response:
        text = api_response['conceptDescription'].get(
            Locale.DEFAULT_LOCALE, gettext(Message.NON_AVAILABLE)
        )
    else:
        text = gettext(Message.NON_AVAILABLE)
    return text.strip(' .')


def get_available_years(api_response):
    time_items = api_response['dimension'][Dimension.TIME]['representation']
    years = []
    for item in time_items:
        code = item['code']
        if year := re.findall(r'\d{4}', code):  # extract year
            years.append(int(year[0]))
    return sorted(list(set(years)))


def get_subject_title(api_response_item):
    title = api_response_item['title'].get(
        Locale.DEFAULT_LOCALE, gettext(Message.NON_AVAILABLE)
    )
    return re.sub(r'^[\s\d]+', '', title)
