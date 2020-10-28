from istacpy.indicators import indicators, geographic, systems

from .services import assert_valid_response


# =====================================
# INDICATORS
# =====================================


def test_get_indicators():
    response = indicators.get_indicators()
    assert_valid_response(response)


def test_get_indicators_with_args():
    response = indicators.get_indicators(
        q='id IN ("AFILIACIONES", "EMPLEO_REGISTRADO_AGRICULTURA")',
        order='id ASC',
        fields='+data',
        representation='GEOGRAPHICAL[35003|35005], MEASURE[ABSOLUTE]',
    )
    assert_valid_response(response)


def test_get_indicators_code():
    response = indicators.get_indicators_code('AFILIACIONES')
    assert_valid_response(response)


def test_get_indicators_code_data():
    response = indicators.get_indicators_code_data('AFILIACIONES')
    assert_valid_response(response)


def test_get_indicators_geographic_granularities():
    response = geographic.get_indicators_geographic_granularities()
    assert_valid_response(response)


# =====================================
# GEOGRAPHIC
# =====================================


def test_get_indicators_geographic_values():
    response = geographic.get_indicators_geographical_values('REGIONS')
    assert_valid_response(response)


def test_get_indicators_subjects():
    response = geographic.get_indicators_subjects()
    assert_valid_response(response)


def test_get_indicators_time_granularities():
    response = geographic.get_indicators_time_granularities()
    assert_valid_response(response)


# =====================================
# SYSTEMS
# =====================================


def test_get_indicators_systems():
    response = systems.get_indicators_systems()
    assert_valid_response(response)


def test_get_systems_code():
    response = systems.get_indicators_systems_code('C00075H')
    assert_valid_response(response)


def test_get_indicators_systems_code_instances():
    response = systems.get_indicators_systems_code_instances('C00075H')
    assert_valid_response(response)


def test_get_indicators_systems_code_instances_with_args():
    response = systems.get_indicators_systems_code_instances(
        indicatorsystemcode='C00075H',
        q='id EQ "INDICADORES_MUNICIPALES"',
        order='id ASC',
        fields='+data',
        representation='GEOGRAPHICAL[35003|35005], MEASURE[ABSOLUTE]',
    )
    assert_valid_response(response)


def test_get_indicators_systems_code_instances_code_data():
    response = systems.get_indicators_systems_code_instances_code_data(
        'C00075H', '21af0477-d63b-493b-ad02-4ab181547223'
    )
    assert_valid_response(response)
