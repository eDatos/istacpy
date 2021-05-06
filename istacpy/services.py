import collections
import itertools
import re
import urllib.parse

import requests

from . import config

ResolvedAPIResponse = collections.namedtuple('ResolvedAPIResponse', 'dataframe codelists')


def build_entrypoint_url(api, path, **query):
    api_version = f'v{config.API_VERSION}'
    encoded_query = urllib.parse.urlencode(query)
    urlpath = '/'.join([api, api_version, path]) + '?' + encoded_query
    url = urllib.parse.urljoin(config.API_ROOT_URL, urlpath)
    return url


def get_content(url):
    headers = {
        'Accept': 'application/json',
        'Access-Control-Allow-Origin': '*',
    }
    try:
        if config.DEBUG:
            print(url)
        response = requests.get(url, headers=headers)
        content = response.json()
    except Exception as err:
        err.requested_url = url
        raise

    return content


def set_debug():
    config.DEBUG = True


def set_nodebug():
    config.DEBUG = False


def get_codelists_from_api_response(api_response: dict) -> dict:
    '''Extract dimension codelists from the metadata of API response'''

    dimensions = api_response['metadata']['dimensions']['dimension']
    codelists = {}
    for dimension in dimensions:
        dimension_id = dimension['id']
        dimension_values = dimension['dimensionValues']['value']
        codelist = {}
        for dimension_value in dimension_values:
            value_id = dimension_value['id']
            value_text = dimension_value['name']['text'][0]['value']
            codelist[value_id] = value_text

        codelists[dimension_id] = codelist
    return codelists


def convert_api_response_to_dataframe(api_response: dict):
    """Convert json API response (as dict) into a Pandas Dataframe.
    To that end, it's necessary to resolve the scalar product with
    dimensions and observations"""
    import pandas as pd

    dimensions = api_response['data']['dimensions']['dimension']

    observations = api_response['data']['observations']
    observations = re.split(r'\s*\|\s*', observations)

    dimension_codes = []
    dimension_titles = []

    for dimension in dimensions:
        dimension_titles.append(dimension['dimensionId'])
        representations = dimension['representations']['representation']
        codes = [r['code'] for r in sorted(representations, key=lambda c: c['index'])]
        dimension_codes.append(codes)

    dimension_codes_product = itertools.product(*dimension_codes)
    data = [dim + (obs,) for dim, obs in zip(dimension_codes_product, observations)]
    columns = dimension_titles + ['OBSERVACIONES']

    return pd.DataFrame(data, columns=columns)


def build_resolved_api_response(api_response: dict):
    item = ResolvedAPIResponse(
        dataframe=convert_api_response_to_dataframe(api_response),
        codelists=get_codelists_from_api_response(api_response),
    )
    return item
