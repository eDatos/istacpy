import re

from istacpy.indicators import geographic as api_geographic
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
        self.years_range = services.get_years_range(response)

    def get_data(self, *, geo=None, time=None, measure=None):
        geo = geo or list(self.granularities[Dimension.GEOGRAPHICAL].values())[0]
        time = time or list(self.granularities[Dimension.TIME].values())[0]
        measure = measure or list(self.measures.values())[0]

        geographical_granularity, geo_codes = services.parse_geographical_query(geo)
        time_granularity, time_codes = services.parse_time_query(time, self.years_range[-1])
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

        return IndicatorData(
            self, response, geographical_granularity, time_granularity, measure_code
        )

    def info(self):
        buffer = []
        buffer.append(f'· Class: {self.__class__.__module__}.{self.__class__.__name__}')
        buffer.append(f'· Indicator code: {self.indicator_code}')
        buffer.append(f'· Title: {self.title}')
        buffer.append(f'· Subject: {self.subject}')
        buffer.append(f'· Description: {self.description}')
        buffer.append(f'· Granularities: {self.granularities}')
        buffer.append(f'· Measures: {self.measures}')
        years_range = ','.join(str(y) for y in self.years_range)
        buffer.append(f'· Available years: {years_range}')
        print('\n'.join(buffer))

    def _quicklook(self):
        return f'{self.indicator_code} ({self.title})'

    def __repr__(self):
        return self._quicklook()

    def __str__(self):
        return self._quicklook()


class IndicatorData:
    def __init__(
        self, indicator, api_response, geographical_granularity, time_granularity, measure
    ):
        self.indicator = indicator
        self.granularity = {
            Dimension.GEOGRAPHICAL: geographical_granularity,
            Dimension.TIME: time_granularity,
        }
        self.measure = measure
        self.index, self.data = services.build_custom_response(api_response)
        self.shape = (len(self.index), len(self.data.keys()))
        self.num_observations = self.shape[0] * self.shape[1]

    @property
    def columns(self):
        return tuple(self.data.keys())

    def info(self):
        buffer = []
        buffer.append(f'· Class: {self.__class__.__module__}.{self.__class__.__name__}')
        buffer.append(f'· Indicator code: {self.indicator.indicator_code}')
        buffer.append(f'· Title: {self.indicator.title}')
        buffer.append(f'· Granularity: {self.granularity}')
        buffer.append(f'· Measure: {self.measure}')
        index = ','.join(self.index)
        buffer.append(f'· Index: {index}')
        columns = ','.join(self.columns)
        buffer.append(f'· Columns: {columns}')
        buffer.append(f'· Shape: {self.shape}')
        buffer.append(f'· Num. observations: {self.num_observations}')
        print('\n'.join(buffer))

    def _quicklook(self):
        buffer = []
        buffer.append(str(self.indicator))
        buffer.append(f'<{",".join(self.index)}>')
        buffer.append(str(self.data))
        return '\n'.join(buffer)

    def __repr__(self):
        return self._quicklook()

    def __str__(self):
        return self._quicklook()


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


def get_subjects():
    response = api_geographic.get_indicators_subjects()
    subjects = []
    for item in response['items']:
        subjects.append(services.get_subject_title(item))
    return tuple(subjects)
