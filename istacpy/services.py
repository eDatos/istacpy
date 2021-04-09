import urllib.parse

import requests

from . import config


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
