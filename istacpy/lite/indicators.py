from istacpy.indicators.indicators import get_indicators_code_data

from . import services


def get_data(indicator, *, geo='M', time='Y', measure='A'):
    geographical_granularity, geo_codes = services.parse_geographical_query(geo)
    time_granularity, time_codes = services.parse_time_query(time)
    measure_code = services.parse_measure_query(measure)

    representation = services.build_api_representation(geo_codes, time_codes, measure_code)
    granularity = services.build_api_granularity(geographical_granularity, time_granularity)

    return get_indicators_code_data(
        indicator,
        representation=representation,
        granularity=granularity,
        fields='-observationsMetadata',
    )
