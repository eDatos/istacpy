from istacpy.indicators import indicators, geographic, systems

from .services import is_valid_response


# =====================================
# INDICATORS
# =====================================


def test_get_indicators():
    response = indicators.get_indicators()
    assert is_valid_response(response) is True


def test_get_indicators_code():
    response = indicators.get_indicators_code('AFILIACIONES')
    assert is_valid_response(response) is True


def test_get_indicators_code_data():
    response = indicators.get_indicators_code_data('AFILIACIONES')
    assert is_valid_response(response) is True


def test_get_indicators_geographic_granularities():
    response = geographic.get_indicators_geographic_granularities()
    assert is_valid_response(response) is True


# =====================================
# GEOGRAPHIC
# =====================================


def test_get_indicators_geographic_values():
    response = geographic.get_indicators_geographical_values('REGIONS')
    assert is_valid_response(response) is True


def test_get_indicators_subjects():
    response = geographic.get_indicators_subjects()
    assert is_valid_response(response) is True


def test_get_indicators_time_granularities():
    response = geographic.get_indicators_time_granularities()
    assert is_valid_response(response) is True


# =====================================
# SYSTEMS
# =====================================


def test_get_indicators_systems():
    response = systems.get_indicators_systems()
    assert is_valid_response(response) is True


def test_get_systems_code():
    response = systems.get_indicators_systems_code('C00075H')
    assert is_valid_response(response) is True


def test_get_indicators_systems_code_instances():
    response = systems.get_indicators_systems_code_instances('C00075H')
    assert is_valid_response(response) is True


def test_get_indicators_systems_code_instances_code_data():
    response = systems.get_indicators_systems_code_instances_code_data(
        'C00075H', '21af0477-d63b-493b-ad02-4ab181547223'
    )
    assert is_valid_response(response) is True
