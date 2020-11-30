import re

from istacpy.indicators import indicators as api_indicators
from istacpy.lite.dimensions.base import Dimension
from istacpy.lite.dimensions.geographical import GeographicalGranularity
from istacpy.lite.dimensions.measure import MeasureRepresentation
from istacpy.lite.dimensions.time import TimeGranularity

from . import services


class Indicator:
    def __init__(self, indicator_code):
        self.indicator_code = indicator_code
        response = api_indicators.get_indicators_code(indicator_code)
        self.granularities = {}
        self.granularities[Dimension.GEOGRAPHICAL] = services.build_custom_granularity(
            response, Dimension.GEOGRAPHICAL, GeographicalGranularity
        )
        self.granularities[Dimension.TIME] = services.build_custom_granularity(
            response, Dimension.TIME, TimeGranularity
        )
        self.representations = services.build_custom_representation(
            response, Dimension.MEASURE, MeasureRepresentation
        )
        self.title_es = response['title'].get('es', 'No disponible')
        self.title_en = response['title'].get('en', 'Not available')

    def get_data(
        self,
        *,
        geo=GeographicalGranularity.MUNICIPALITIES_ID,
        time=TimeGranularity.YEARLY_ID,
        measure=MeasureRepresentation.ABSOLUTE_ID
    ):
        geographical_granularity, geo_codes = services.parse_geographical_query(geo)
        time_granularity, time_codes = services.parse_time_query(time)
        measure_code = services.parse_measure_query(measure)

        representation = services.build_api_representation(
            geo_codes, time_codes, measure_code
        )
        granularity = services.build_api_granularity(
            geographical_granularity, time_granularity
        )

        response = api_indicators.get_indicators_code_data(
            self.indicator_code,
            representation=representation,
            granularity=granularity,
            fields='-observationsMetadata',
        )

        self.data = services.build_custom_response(response)
        return self.data


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


def get_indicator(indicator_code):
    return Indicator(indicator_code)
