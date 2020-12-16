import itertools
import re
import uuid

import pytest

from istacpy import exceptions
from istacpy.lite import i18n, indicators
from istacpy.lite.dimensions.geographical import GeographicalGranularity
from istacpy.lite.dimensions.measure import MeasureRepresentation
from istacpy.lite.dimensions.time import TimeGranularity


@pytest.fixture
def population_indicator():
    return indicators.get_indicator('POBLACION')


@pytest.fixture
def active_population_indicator():
    return indicators.get_indicator('POBLACION_ACTIVA')


@pytest.fixture
def affiliation_indicator():
    return indicators.get_indicator('AFILIACIONES')


@pytest.fixture
def activity_rate_indicator():
    return indicators.get_indicator('TASA_ACTIVIDAD')


def test_get_subjects():
    subjects = indicators.get_subjects()
    assert len(subjects) > 0


def test_get_indicators():
    all_indicators = indicators.get_indicators()
    assert len(all_indicators) > 0


def test_indicator(population_indicator):
    assert population_indicator.code is not None
    assert population_indicator.title is not None
    assert population_indicator.subject is not None
    assert population_indicator.description is not None
    assert population_indicator.geographical_granularities is not None
    assert population_indicator.time_granularities is not None
    assert population_indicator.measures is not None
    assert population_indicator.available_years is not None


def test_indicator_data(population_indicator):
    indicator_data = population_indicator.get_data()
    assert indicator_data.indicator == population_indicator
    assert indicator_data.geographical_granularity is not None
    assert indicator_data.time_granularity is not None
    assert indicator_data.measure is not None
    assert indicator_data.index is not None
    assert indicator_data.columns is not None
    assert indicator_data.shape is not None
    assert indicator_data.data is not None


def test_geographical_granularity(population_indicator):
    geographical_granularity_id = 'I'
    indicator_data = population_indicator.get_data(geo=geographical_granularity_id)
    geographical_granularity_code = GeographicalGranularity.get_code(
        geographical_granularity_id
    )
    assert indicator_data.geographical_granularity == geographical_granularity_code
    assert 'Tenerife' in indicator_data.columns
    assert 'Tenerife' in indicator_data.data.keys()


def test_time_granularity(population_indicator):
    time_granularity_id = 'Y'
    indicator_data = population_indicator.get_data(time=time_granularity_id)
    time_granularity_code = TimeGranularity.get_code(time_granularity_id)
    assert indicator_data.time_granularity == time_granularity_code
    assert '2000' in indicator_data.index
    assert indicator_data.data is not None


def test_measure(population_indicator):
    measure_id = 'A'
    indicator_data = population_indicator.get_data(measure=measure_id)
    measure_code = MeasureRepresentation.get_code(measure_id)
    assert indicator_data.measure == measure_code
    # check all values are integers
    for value in itertools.chain(*indicator_data.data.values()):
        assert isinstance(value, int)


def test_geographical_filter(population_indicator):
    query = 'M|Gran Canaria'
    indicator_data = population_indicator.get_data(geo=query)
    assert 'Agaete' in indicator_data.columns
    assert 'Agaete' in indicator_data.data.keys()


def test_time_filter(population_indicator):
    query = 'Y|2002:2005,2015'
    indicator_data = population_indicator.get_data(time=query)
    years = ('2002', '2003', '2004', '2005', '2015')
    for year in years:
        assert year in indicator_data.index
    years = ('2000', '2001', '2007')
    for year in years:
        assert year not in indicator_data.index
    assert indicator_data.data is not None


def test_time_filter_latest(population_indicator):
    query = 'Y|latest'
    indicator_data = population_indicator.get_data(time=query)
    latest_year = population_indicator.available_years[-1]
    assert str(latest_year) in indicator_data.index
    assert indicator_data.data is not None


def test_english_response():
    i18n.set_english()
    indicator = indicators.get_indicator('POBLACION')
    assert indicator.title == 'Population'
    assert indicator.description.startswith('Number of persons')


def test_monthly_indicator(affiliation_indicator):
    time_query = 'M'
    indicator_data = affiliation_indicator.get_data(time=time_query)
    for value in indicator_data.index:
        assert re.match(r'^\w{3} \d{4}$', value) is not None


def test_raw_output(affiliation_indicator):
    geographical_query = '=I'
    time_query = '=M'
    indicator_data = affiliation_indicator.get_data(geo=geographical_query, time=time_query)
    for value in indicator_data.index:
        assert re.search(r'M\d\d$', value) is not None
    for value in indicator_data.columns:
        assert re.match(r'^ES\d{3}$', value) is not None


def test_unit_multiplier(active_population_indicator):
    # Unit multiplier shoud be "Thousands"
    indicator_data = active_population_indicator.get_data()
    # check all values are floats
    for value in itertools.chain(*indicator_data.data.values()):
        assert isinstance(value, float)


def test_indicator_info(population_indicator, capsys):
    population_indicator.info()
    captured = capsys.readouterr()
    assert len(captured.out.split('\n')) >= 9


def test_indicator_data_info(population_indicator, capsys):
    indicator_data = population_indicator.get_data()
    indicator_data.info()
    captured = capsys.readouterr()
    assert len(captured.out.split('\n')) >= 10


def test_indicator_quicklook(population_indicator):
    assert len(str(population_indicator)) >= 1
    assert len(repr(population_indicator)) >= 1


def test_indicator_data_quicklook(population_indicator):
    indicator_data = population_indicator.get_data()
    assert len(str(indicator_data)) >= 3
    assert len(repr(indicator_data)) >= 3


def test_indicator_not_found():
    with pytest.raises(exceptions.IndicatorNotFoundError):
        indicators.get_indicator(str(uuid.uuid1()))


def test_dimension_not_found(population_indicator):
    with pytest.raises(Exception):
        population_indicator.get_data(geo='@')
    with pytest.raises(Exception):
        population_indicator.get_data(time='@')
    with pytest.raises(Exception):
        population_indicator.get_data(measure='@')


def test_dimension_not_available(affiliation_indicator, activity_rate_indicator):
    with pytest.raises(exceptions.GranularityNotAvailableError):
        affiliation_indicator.get_data(geo='C')
    with pytest.raises(exceptions.GranularityNotAvailableError):
        affiliation_indicator.get_data(time='Y')
    with pytest.raises(exceptions.MeasureNotAvailableError):
        activity_rate_indicator.get_data(measure='N')


def test_query_malformed(population_indicator):
    queries = (
        {'geo': 'I|'},
        {'geo': 'I|Tenerife,'},
        {'time': 'Y|200'},
        {'time': 'Y|2001_2002'},
        {'measure': 'A-'},
        {'measure': '$$'},
    )
    for query in queries:
        with pytest.raises(exceptions.QueryMalformedError):
            population_indicator.get_data(**query)
