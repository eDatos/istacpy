import re
import uuid

import pandas as pd
import pytest

from istacpy import config, exceptions
from istacpy.indicators.lite import i18n, indicators
from istacpy.indicators.lite.dimensions.geographical import GeographicalGranularity
from istacpy.indicators.lite.dimensions.measure import MeasureRepresentation
from istacpy.indicators.lite.dimensions.time import TimeGranularity

# =================================================================
# FIXTURES
# =================================================================


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


@pytest.fixture
def subjects():
    return indicators.get_subjects()


# =================================================================
# TESTS
# =================================================================

def test_get_indicators(subjects):
    # The first topic ('0100000', 'Territory and environment') has no indicator.
    subject_code = subjects[0][0]
    results = indicators.get_indicators(subject_code=subject_code)
    assert len(results) == 0

    subject_code = subjects[1][0]
    results = indicators.get_indicators(subject_code=subject_code)
    assert len(results) > 0

    indicator_title = results[0][1]
    results = indicators.get_indicators(indicator_title, subject_code=subject_code)
    assert len(results) > 0

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
    for value in indicator_data.as_list():
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


def test_time_filter_first(population_indicator):
    query = 'Y|f'
    indicator_data = population_indicator.get_data(time=query)
    latest_year = population_indicator.available_years[0]
    assert str(latest_year) in indicator_data.index
    assert indicator_data.data is not None


def test_time_filter_last(population_indicator):
    query = 'Y|l'
    indicator_data = population_indicator.get_data(time=query)
    latest_year = population_indicator.available_years[-1]
    assert str(latest_year) in indicator_data.index
    assert indicator_data.data is not None


def test_spanish_response():
    i18n.set_spanish()
    indicator = indicators.get_indicator('POBLACION')
    assert indicator.title == 'Población'
    assert indicator.description.startswith('Número de personas')


def test_english_response():
    i18n.set_english()
    indicator = indicators.get_indicator('POBLACION')
    assert indicator.title == 'Population'
    assert indicator.description.startswith('Number of persons')


def test_monthly_indicator_codes(affiliation_indicator):
    time_query = 'M'
    indicator_data = affiliation_indicator.get_data(time=time_query)
    for value in indicator_data.index:
        # assert re.match(r'^\w{3} \d{4}$', value) is not None
        assert re.match(r'^\d{4}-\d{2}$', value) is not None


@pytest.mark.skip(
    reason="API doesn't filter indicators by years with monthly granularities using dashes"
)
def test_monthly_indicator_filter(affiliation_indicator):
    time_query = '=M|L'
    last_year = affiliation_indicator.available_years[-1]
    indicator_data = affiliation_indicator.get_data(time=time_query)
    returned_years = set([int(i[:4]) for i in indicator_data.index])
    assert last_year in returned_years and len(returned_years) == 1


def test_raw_output(affiliation_indicator):
    geographical_query = '=I'
    time_query = '=M'
    indicator_data = affiliation_indicator.get_data(geo=geographical_query, time=time_query)
    for value in indicator_data.index:
        # assert re.search(r'M\d\d$', value) is not None
        assert re.search(r'\d{4}-\d{2}$', value) is not None
    for value in indicator_data.columns:
        assert re.match(r'^ES\d{3}$', value) is not None


def test_unit_multiplier(active_population_indicator):
    # Unit multiplier shoud be "Thousands"
    indicator_data = active_population_indicator.get_data()
    # check all values are floats
    for value in indicator_data.as_list():
        assert isinstance(value, float)


def test_unit_multiplier_notdefined(population_indicator):
    # Unit multiplier for POBLACION with ANNUAL_PERCENTAGE_RATE is not defined
    indicator_data = population_indicator.get_data(measure='N')
    assert indicator_data.num_observations > 0


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
        population_indicator.get_data(geo='Z')
    with pytest.raises(Exception):
        population_indicator.get_data(time='Z')
    with pytest.raises(Exception):
        population_indicator.get_data(measure='Z')


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


def test_island_not_found(population_indicator):
    with pytest.raises(exceptions.IslandNotFoundError):
        population_indicator.get_data(geo='I|Hawai')


def test_get_indicators_bad_argument():
    with pytest.raises(TypeError):
        indicators.get_indicators(3.14)


def test_value_error(population_indicator):
    indicator_data = population_indicator.get_data(measure='J')
    values = set(indicator_data.as_list())
    assert config.VALUE_ERROR in values


def test_data_as_dataframe(population_indicator):
    indicator_data = population_indicator.get_data()
    df = indicator_data.as_dataframe()
    assert isinstance(df, pd.DataFrame)


def test_data_as_list(population_indicator):
    indicator_data = population_indicator.get_data()
    data_as_list = indicator_data.as_list()
    assert isinstance(data_as_list, list)
    assert len(data_as_list) > 0
