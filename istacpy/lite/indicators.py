from istacpy.indicators.indicators import get_indicators_code_data, get_indicators_code
from istacpy.lite.dimensions.geographical import GeographicalGranularity
from istacpy.lite.dimensions.measure import MeasureGranularity
from istacpy.lite.dimensions.time import TimeGranularity

from . import services


def get_data(
    indicator,
    *,
    geo=GeographicalGranularity.MUNICIPALITIES_ID,
    time=TimeGranularity.YEARLY_ID,
    measure=MeasureGranularity.ABSOLUTE_ID,
):
    geographical_granularity, geo_codes = services.parse_geographical_query(geo)
    time_granularity, time_codes = services.parse_time_query(time)
    measure_code = services.parse_measure_query(measure)

    representation = services.build_api_representation(geo_codes, time_codes, measure_code)
    granularity = services.build_api_granularity(geographical_granularity, time_granularity)

    response = get_indicators_code_data(
        indicator,
        representation=representation,
        granularity=granularity,
        fields='-observationsMetadata',
    )

    return services.build_custom_response(response)


def get_granularities(indicator):
    response = get_indicators_code(indicator)

    geographical_granularities = services.build_custom_granularity(
        response, 'GEOGRAPHICAL', GeographicalGranularity
    )
    time_granularities = services.build_custom_granularity(
        response, 'TIME', TimeGranularity
    )

    return dict(geo=geographical_granularities, time=time_granularities)
