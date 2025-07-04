# ----------------
# test_services.py

import urllib.parse
from istacpy import services
from istacpy.statisticalresources import queries


def test_build_entrypoint_url():
    print('==> test_build_entrypoint_url')
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

    url = services.build_entrypoint_url(
        api='indicators',
        path='geographicalValues',
        geographicalGranularityCode='REGIONS',
        subjectCode='',
        systemCode='',
    )

    url_parts = urllib.parse.urlsplit(url)

    assert (
        url_parts.path == '/api/estadisticas/indicators/v1.0/geographicalValues'
    )
    assert url_parts.query == (
        'geographicalGranularityCode=REGIONS&'
        'subjectCode=&'
        'systemCode='
    )


# -------------------
# test_indicators.py

from istacpy.indicators import indicators, geographic, systems

from .services import assert_valid_response

def test_get_indicators_geographical_values():
    print('==> test_get_indicators_geographical_values')
    response = geographic.get_indicators_geographical_values(
        geographicalgranularitycode='REGIONS', subjectcode='061'
    )
    print(f'[DEBUG.1] {response}')
    assert response['code'] == '500'

    response = geographic.get_indicators_geographical_values('REGIONS')
    #    geographicalgranularitycode='REGIONS')
    print(f'[DEBUG.2] {response}')
    assert_valid_response(response)

 