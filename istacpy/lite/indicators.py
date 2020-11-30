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
        self.granularities = {
            Dimension.GEOGRAPHICAL: services.build_custom_granularity(
                response, Dimension.GEOGRAPHICAL, GeographicalGranularity
            ),
            Dimension.TIME: services.build_custom_granularity(
                response, Dimension.TIME, TimeGranularity
            ),
        }
        self.measures = services.build_custom_representation(
            response, Dimension.MEASURE, MeasureRepresentation
        )
        self.title = services.get_indicator_title(response)
        self.subject = services.get_indicator_subject(response)
        self.description = services.get_indicator_description(response)

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
        title = services.get_indicator_title(item)
        subject = services.get_indicator_subject(item)
        description = services.get_indicator_description(item)
        full_text = code + title + subject + description
        if re.search(search_query, full_text, flags=re.I):
            indicators.append((code, title))
    return indicators


def get_indicator(indicator_code):
    return Indicator(indicator_code)
