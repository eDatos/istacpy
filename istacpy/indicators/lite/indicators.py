import itertools
import re

from istacpy.exceptions import IndicatorNotFoundError
from istacpy.indicators import geographic as api_geographic
from istacpy.indicators import indicators as api_indicators
from istacpy.indicators.lite.dimensions.base import Dimension
from istacpy.indicators.lite.dimensions.geographical import GeographicalGranularity
from istacpy.indicators.lite.dimensions.measure import MeasureRepresentation
from istacpy.indicators.lite.dimensions.time import TimeGranularity

from . import services


class Indicator:
    def __init__(self, indicator_code):
        self.code = indicator_code
        self.api_response = api_indicators.get_indicators_code(indicator_code)
        if self.api_response.get('code') == '404':
            raise IndicatorNotFoundError(indicator_code)

        self.geographical_granularities = services.build_custom_dimension(
            self.api_response,
            'granularity',
            Dimension.GEOGRAPHICAL,
            GeographicalGranularity,
        )
        self.time_granularities = services.build_custom_dimension(
            self.api_response, 'granularity', Dimension.TIME, TimeGranularity
        )
        self.measures = services.build_custom_dimension(
            self.api_response, 'representation', Dimension.MEASURE, MeasureRepresentation
        )
        self._time_granularities_using_dashes = services.time_granularities_using_dashes(
            self.api_response, self.time_granularities.keys()
        )
        self.title = services.get_indicator_title(self.api_response)
        self.subject = services.get_indicator_subject(self.api_response)
        self.description = services.get_indicator_description(self.api_response)
        self.available_years = services.get_available_years(self.api_response)

    def get_data(self, *, geo=None, time=None, measure=None):
        """Get data from API on the basis of query strings from arguments.

        Parameters
        ----------
        geo : str
            Query string for geographical dimension. Defaults to the largest grain
            granularity with no filter.
        time : str
            Query string for time dimension. Defaults to the largest grain granularity with
            no filter.
        measure : str
            Indicates the representation of measure to use. Defaults to absolute measure.

        Returns
        -------
        IndicatorData
            Object with requested data and other metadata
        """
        geo = geo or list(self.geographical_granularities.values())[0]
        time = time or list(self.time_granularities.values())[0]
        measure = measure or list(self.measures.values())[0]

        (
            map_geographical_values,
            geographical_granularity,
            geo_codes,
        ) = services.parse_geographical_query(geo, self.geographical_granularities.keys())
        map_time_values, time_granularity, time_codes = services.parse_time_query(
            time, self._time_granularities_using_dashes, self.available_years
        )
        measure_code = services.parse_measure_query(measure, self.measures.keys())

        representation = services.build_api_representation(
            geo_codes, time_codes, measure_code
        )
        granularity = services.build_api_granularity(
            geographical_granularity, time_granularity
        )

        response = api_indicators.get_indicators_code_data(
            self.code,
            representation=representation,
            granularity=granularity,
            fields='-observationsMetadata',
        )

        return IndicatorData(
            self,
            response,
            geographical_granularity,
            time_granularity,
            measure_code,
            map_geographical_values,
            map_time_values,
        )

    def info(self):
        """Information about the object with a summary of the main attributes.
        Output is sent to stdout."""
        buffer = []
        buffer.append(f'· Class: {self.__class__.__module__}.{self.__class__.__name__}')
        buffer.append(f'· Indicator code: {self.code}')
        buffer.append(f'· Title: {self.title}')
        buffer.append(f'· Subject: {self.subject}')
        buffer.append(f'· Description: {self.description}')
        buffer.append(f'· Geographical granularities: {self.geographical_granularities}')
        buffer.append(f'· Time granularities: {self.time_granularities}')
        buffer.append(f'· Measures: {self.measures}')
        available_years = ','.join(str(y) for y in self.available_years)
        buffer.append(f'· Available years: {available_years}')
        print('\n'.join(buffer))

    def _quicklook(self):
        return f'{self.code} ({self.title})'

    def __repr__(self):
        return self._quicklook()

    def __str__(self):
        return self._quicklook()


class IndicatorData:
    def __init__(
        self,
        indicator,
        api_response,
        geographical_granularity,
        time_granularity,
        measure,
        map_geographical_values=True,
        map_time_values=True,
    ):
        self.indicator = indicator
        self.api_response = api_response
        self.geographical_granularity = geographical_granularity
        self.time_granularity = time_granularity
        self.measure = measure

        measure_unit_multiplier = services.get_measure_unit_multiplier(
            self.indicator.api_response, self.measure
        )
        self.index, self.data = services.build_custom_response(
            self.api_response,
            map_geographical_values,
            map_time_values,
            measure_unit_multiplier,
        )
        self.shape = (len(self.index), len(self.data.keys()))
        self.num_observations = self.shape[0] * self.shape[1]

    @property
    def columns(self):
        return tuple(self.data.keys())

    def info(self):
        """Information about the object with a summary of the main attributes.
        Output is sent to stdout."""
        buffer = []
        buffer.append(f'· Class: {self.__class__.__module__}.{self.__class__.__name__}')
        buffer.append(f'· Indicator code: {self.indicator.code}')
        buffer.append(f'· Title: {self.indicator.title}')
        buffer.append(f'· Geographical granularity: {self.geographical_granularity}')
        buffer.append(f'· Time granularity: {self.time_granularity}')
        buffer.append(f'· Measure: {self.measure}')
        index = ','.join(self.index)
        buffer.append(f'· Index: {index}')
        columns = ','.join(self.columns)
        buffer.append(f'· Columns: {columns}')
        buffer.append(f'· Shape: {self.shape}')
        buffer.append(f'· Num. observations: {self.num_observations}')
        print('\n'.join(buffer))

    def as_dataframe(self):
        """Convert current object to a Pandas Dataframe.

        Returns
        -------
        pandas.core.frame.DataFrame
            Dataframe containing index, columns and data from indicator.
        """
        import pandas as pd

        return pd.DataFrame(data=self.data, index=self.index)

    def as_list(self):
        """Convert current object to a list of values.

        Returns
        -------
        list
            List with flattened values from indicator data.
        """
        return list(itertools.chain(*self.data.values()))

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


def get_indicators(search_query='', *, subject_code=''):
    """Get available indicators on the API.

    Parameters
    ----------
    search_query : str
        Free text to look for against.
    subject_code : str
        Subject code to restrict search within that context.

    Returns
    -------
    tuple
        Tuple of tuples with first value as indicator code and second value as
        indicator title.
    """
    query = f'subjectCode EQ "{subject_code}"' if subject_code else ''
    response = api_indicators.get_indicators(q=query, limit=1000)

    indicators = []
    for item in response['items']:
        code = item['code']
        title = services.get_indicator_title(item)
        subject = services.get_indicator_subject(item)
        description = services.get_indicator_description(item)
        full_text = code + title + subject + description
        if re.search(search_query, full_text, flags=re.I):
            indicators.append((code, title))
    return tuple(sorted(indicators))


def get_indicator(indicator_code):
    """Get a concrete indicator through its code.

    Parameters
    ----------
    indicator_code :  str
        Indicator code as is set on API.

    Returns
    -------
    Indicator
        Object with all the information about the indicator.
    """
    return Indicator(indicator_code)


def get_subjects():
    """Get subjects on API in which indicators are sorted in.

    Returns
    -------
    tuple
        Tuple of tuples with first value as subject code and second value as
        subject title.
    """
    response = api_geographic.get_indicators_subjects()
    subjects = []
    for item in response['items']:
        code = item['code']
        title = services.get_subject_title(item)
        subjects.append((code, title))
    return tuple(sorted(subjects))
