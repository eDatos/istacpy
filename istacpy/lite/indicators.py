import re

from istacpy.indicators import indicators as api_indicators
from istacpy.lite.dimensions.geographical import GeographicalGranularity
from istacpy.lite.dimensions.measure import MeasureGranularity
from istacpy.lite.dimensions.time import TimeGranularity

from . import services


def get_indicator(
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

    response = api_indicators.get_indicators_code_data(
        indicator,
        representation=representation,
        granularity=granularity,
        fields='-observationsMetadata',
    )

    return services.build_custom_response(response)


def get_granularities(indicator):
    response = api_indicators.get_indicators_code(indicator)

    geographical_granularities = services.build_custom_granularity(
        response, 'GEOGRAPHICAL', GeographicalGranularity
    )
    time_granularities = services.build_custom_granularity(
        response, 'TIME', TimeGranularity
    )

    return dict(
        geo=geographical_granularities,
        time=time_granularities,
    )


def get_indicators(search_query=''):
    response = api_indicators.get_indicators(limit=1000)

    indicators = []
    for item in response['items']:
        code = item['code']
        title_es = item['title'].get('es', 'No disponible')
        title_en = item['title'].get('en', 'Not available')
        subject_title = item['subjectTitle'].get('es', 'No disponible')
        full_text = code + title_en + title_es + subject_title
        if re.search(search_query, full_text, flags=re.I):
            indicators.append((code, title_es, title_en))
    return indicators
