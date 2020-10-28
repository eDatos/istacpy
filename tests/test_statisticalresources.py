from istacpy.statisticalresources import cubes

from .services import is_valid_response


def test_get_statisticalresources_datasets():
    response = cubes.get_statisticalresources_datasets()
    assert is_valid_response(response) is True


def test_get_statisticalresources_datasets_agency():
    response = cubes.get_statisticalresources_datasets_agency('ISTAC')
    assert is_valid_response(response) is True


def test_get_statisticalresources_datasets_agency_resource():
    response = cubes.get_statisticalresources_datasets_agency_resource(
        'ISTAC', 'C00010A_000002'
    )
    assert is_valid_response(response) is True


def test_get_statisticalresources_datasets_agency_resource_version():
    response = cubes.get_statisticalresources_datasets_agency_resource_version(
        'ISTAC', 'C00010A_000002', '001.000'
    )
    assert is_valid_response(response) is True
