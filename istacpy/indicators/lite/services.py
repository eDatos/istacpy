import re

from istacpy import config
from istacpy.exceptions import (
    GranularityNotAvailableError,
    MeasureNotAvailableError,
    QueryMalformedError,
)
from istacpy.indicators.lite.dimensions.base import Dimension
from istacpy.indicators.lite.dimensions.geographical import (
    GeographicalGranularity,
    GeographicalRepresentation,
)
from istacpy.indicators.lite.dimensions.measure import MeasureRepresentation
from istacpy.indicators.lite.dimensions.time import TimeGranularity, TimeRepresentation
from istacpy.indicators.lite.i18n import Locale, Message, gettext


def _expand_island_subcodes(filter, granularity_code):
    items_codes = []
    if filter is not None:
        islands = re.split(r'\s*,\s*', filter)
        for island in islands:
            codes = GeographicalRepresentation.get_codes(island, granularity_code)
            items_codes.extend(codes)
    return items_codes


def parse_geographical_query(query, available_granularities):
    if m := re.match(
        r'^(=)?([A-Z])(?:\|([\s\w]+(?:,[\s\w]+)*))?$', query.strip().upper(), re.I
    ):
        raw_output, granularity_id, filter = m.groups()
        try:
            granularity_code = GeographicalGranularity.get_code(granularity_id)
        except KeyError as err:
            raise Exception(
                f'"{granularity_id}" not found as geographical granularity identifier'
            ) from err
        if granularity_code not in available_granularities:
            raise GranularityNotAvailableError(granularity_code)
        items_codes = _expand_island_subcodes(filter, granularity_code)
        return raw_output is None, granularity_code, '|'.join(items_codes)
    else:
        raise QueryMalformedError(query)


def _expand_year_subcodes(filter, granularity_code, available_years, use_dash):
    items_codes = []
    if filter is not None:
        filter = filter.replace('F', str(available_years[0]))
        filter = filter.replace('L', str(available_years[-1]))
        year_ranges = re.split(r'\s*,\s*', filter)
        items_codes = []
        for year_range in year_ranges:
            years = re.split(r'\s*[:-]\s*', year_range)
            if len(years) > 1:
                year_list = range(int(years[0]), int(years[1]) + 1)
            else:
                year_list = years
            for year in year_list:
                codes = TimeRepresentation.get_codes(year, granularity_code, use_dash)
                items_codes.extend(codes)
    return items_codes


def parse_time_query(query, use_dash, available_years):
    if m := re.match(
        r'^(=)?([A-Z])'
        r'(?:\|((?:\d{4}|[FL])(?:[:-](?:\d{4}|[FL]))?'
        r'(?:,(?:\d{4}|[FL])(?:[:-](?:\d{4}|[FL]))?)*))?$',
        query.strip().upper(),
        re.I,
    ):
        raw_output, granularity_id, filter = m.groups()
        try:
            granularity_code = TimeGranularity.get_code(granularity_id)
        except KeyError as err:
            raise Exception(
                f'"{granularity_id}" not found as time granularity identifier'
            ) from err
        try:
            use_dash = use_dash[granularity_code]
        except KeyError as err:
            raise GranularityNotAvailableError(granularity_code) from err

        items_codes = _expand_year_subcodes(
            filter, granularity_code, available_years, use_dash
        )
        return raw_output is None, granularity_code, '|'.join(items_codes)
    else:
        raise QueryMalformedError(query)


def parse_measure_query(query, available_measures):
    if re.match(r'^\w$', query, re.I):
        try:
            measure_code = MeasureRepresentation.get_code(query)
        except KeyError as err:
            raise Exception(f'"{query}" not found as measure representation') from err
        if measure_code not in available_measures:
            raise MeasureNotAvailableError(measure_code)
        return measure_code
    else:
        raise QueryMalformedError(query)


def build_api_representation(geo_codes, time_codes, measure_code):
    return f'GEOGRAPHICAL[{geo_codes}],TIME[{time_codes}],MEASURE[{measure_code}]'


def build_api_granularity(geographical_granularity, time_granularity):
    return f'GEOGRAPHICAL[{geographical_granularity}],TIME[{time_granularity}]'


def _normalize_value(value, unit_multiplier):
    try:
        typecast = float if value.find('.') != -1 else int
        value = typecast(value) * unit_multiplier
    except (AttributeError, ValueError):
        value = config.VALUE_ERROR
    return value


def _get_ordered_representation_api_codes(api_response, dimension):
    index = api_response['dimension'][dimension]['representation']['index']
    # index is a dict
    items = sorted(tuple(index.items()), key=lambda i: i[1])
    return [item[0] for item in items]


def build_custom_response(
    api_response,
    map_geographical_values=True,
    map_time_values=True,
    measure_unit_multiplier=1,
):
    index = _get_ordered_representation_api_codes(api_response, Dimension.TIME)
    columns = _get_ordered_representation_api_codes(api_response, Dimension.GEOGRAPHICAL)
    observations = api_response['observation']

    i, data, num_rows = 0, {}, len(index)
    for column in columns:
        values = observations[i : i + num_rows]
        annotated_values = sorted([(idx, value) for idx, value in zip(index, values)])
        data[column] = tuple(
            [
                _normalize_value(value[1], measure_unit_multiplier)
                for value in annotated_values
            ]
        )
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
    api_codes = [e['code'] for e in api_response['dimension'][dimension][property]]
    dimension = {}
    for code, id in granularity_handler.SWAPPED_CODES.items():
        if code in api_codes:
            dimension[code] = id
    return dimension


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


def get_measure_unit_multiplier(api_response, measure_code):
    api_representation = api_response['dimension'][Dimension.MEASURE]['representation']
    for representation in api_representation:
        if representation['code'] == measure_code:
            try:
                unit_mulitiplier_code = representation['quantity']['unitMultiplier']['en']
                unit_multiplier = MeasureRepresentation.get_unit_multiplier(
                    unit_mulitiplier_code
                )
            except KeyError:
                unit_multiplier = 1
            return unit_multiplier
    return 1
