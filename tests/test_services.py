import urllib.parse

from istacpy import services


def test_build_entrypoint_url():
    url = services.build_entrypoint_url(
        api='indicators',
        path='indicators/AFILIACIONES/data',
        representation='GEOGRAPHICAL[35003|35005],MEASURE[ABSOLUTE]',
        granularity='GEOGRAPHICAL[MUNICIPALITIES|PROVINCES]',
        fields='-observationsMetadata',
    )
    url_parts = urllib.parse.urlsplit(url)

    assert url_parts.path == '/istac/api/indicators/v1.0/indicators/AFILIACIONES/data'
    assert url_parts.query == (
        'representation=GEOGRAPHICAL%5B35003%7C35005%5D%2CMEASURE%5BABSOLUTE%5D&'
        'granularity=GEOGRAPHICAL%5BMUNICIPALITIES%7CPROVINCES%5D&'
        'fields=-observationsMetadata'
    )
