import urllib.parse

import pandas as pd

from istacpy import services
from istacpy.statisticalresources import queries


def test_build_entrypoint_url():
    url = services.build_entrypoint_url(
        api='indicators',
        path='indicators/AFILIACIONES/data',
        representation='GEOGRAPHICAL[35003|35005],MEASURE[ABSOLUTE]',
        granularity='GEOGRAPHICAL[MUNICIPALITIES|PROVINCES]',
        fields='-observationsMetadata',
    )
    url_parts = urllib.parse.urlsplit(url)

    assert (
        url_parts.path == '/api/estadisticas/indicators/v1.0/indicators/AFILIACIONES/data'
    )
    assert url_parts.query == (
        'representation=GEOGRAPHICAL%5B35003%7C35005%5D%2CMEASURE%5BABSOLUTE%5D&'
        'granularity=GEOGRAPHICAL%5BMUNICIPALITIES%7CPROVINCES%5D&'
        'fields=-observationsMetadata'
    )


def test_convert_api_response_to_dataframe():
    COLUMNS = (
        'MEDIDAS',
        'TIME_PERIOD',
        'SEXO',
        'SITUACION_ECONOMICA_ICC',
        'VALORACION',
        'OBSERVACIONES',
        'TERRITORIO', 
        'ESTADO_OBSERVACION',
    )

    api_response = queries.get_statisticalresources_queries_agency_resource(
        agencyid='ISTAC', resourceid='C00086B_000006'
    )
    df = services.convert_api_response_to_dataframe(api_response)
    assert isinstance(df, pd.DataFrame)
    assert tuple(df.columns) == COLUMNS
    assert df.size >= 1728


def test_get_codelists_from_api_response():
    DIMENSIONS = (
        'MEDIDAS',
        'TIME_PERIOD',
        'SEXO',
        'SITUACION_ECONOMICA_ICC',
        'VALORACION',
    )
    api_response = queries.get_statisticalresources_queries_agency_resource(
        agencyid='ISTAC', resourceid='C00086B_000006'
    )
    cl = services.get_codelists_from_api_response(api_response)
    assert isinstance(cl, dict)
    assert tuple(cl.keys()) == DIMENSIONS
    assert all([isinstance(m, dict) for m in cl.values()])
    assert all([len(m) > 0 for m in cl.values()])
