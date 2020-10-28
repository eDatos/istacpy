from istacpy.statisticalresources import cubes

from .services import assert_valid_response


def test_get_statisticalresources_datasets():
    response = cubes.get_statisticalresources_datasets()
    assert_valid_response(response)


def test_get_statisticalresources_datasets_agency():
    response = cubes.get_statisticalresources_datasets_agency('ISTAC')
    assert_valid_response(response)


def test_get_statisticalresources_datasets_agency_resource():
    response = cubes.get_statisticalresources_datasets_agency_resource(
        'ISTAC', 'C00010A_000002'
    )
    assert_valid_response(response)


def test_get_statisticalresources_datasets_agency_resource_version():
    response = cubes.get_statisticalresources_datasets_agency_resource_version(
        'ISTAC', 'C00010A_000002', '001.000', 'TIME_PERIOD:2010'
    )
    assert_valid_response(response)
