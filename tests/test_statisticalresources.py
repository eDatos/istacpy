from istacpy.statisticalresources import cubes, queries

from .services import assert_valid_response


def test_get_statisticalresources_datasets():
    response = cubes.get_statisticalresources_datasets(
        orderby='id ASC', query='name ILIKE "PASAJEROS"'
    )
    assert_valid_response(response)


def test_get_statisticalresources_datasets_agency():
    response = cubes.get_statisticalresources_datasets_agency(
        agencyid='ISTAC', orderby='id ASC', query='name ILIKE "PASAJEROS"'
    )
    assert_valid_response(response)


def test_get_statisticalresources_datasets_agency_resource():
    response = cubes.get_statisticalresources_datasets_agency_resource(
        agencyid='ISTAC',
        resourceid='C00017A_000001',
        orderby='id ASC',
        query='name ILIKE "PASAJEROS"',
    )
    assert_valid_response(response)


def test_get_statisticalresources_datasets_agency_resource_version():
    response = cubes.get_statisticalresources_datasets_agency_resource_version(
        agencyid='ISTAC',
        resourceid='C00017A_000001',
        version='2.2',
        dim='TIME_PERIOD:2010',
        fields='-metadata',
    )
    assert_valid_response(response)


def test_get_statisticalresources_queries():
    response = queries.get_statisticalresources_queries(
        orderby='id ASC', query='name ILIKE "PASAJEROS"'
    )
    assert_valid_response(response)


def test_get_statisticalresources_queries_agency():
    response = queries.get_statisticalresources_queries_agency(
        agencyid='ISTAC', orderby='id ASC', query='name ILIKE "PASAJEROS"'
    )
    assert_valid_response(response)


def test_get_statisticalresources_queries_agency_resource():
    response = queries.get_statisticalresources_queries_agency_resource(
        agencyid='ISTAC',
        resourceid='C00017A_000001',
        orderby='id ASC',
        query='name ILIKE "PASAJEROS"',
    )
    assert_valid_response(response)
