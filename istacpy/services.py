import urllib.parse

import requests
import os

from . import config


def build_entrypoint_url(api, path, **query):
    api_version = f'v{config.API_VERSION}'
    encoded_query = urllib.parse.urlencode(query)
    urlpath = os.path.join(api, api_version, path) + '?' + encoded_query
    url = urllib.parse.urljoin(config.API_ROOT_URL, urlpath)
    return url


def get_content(url):
    headers = {
        'Accept': 'application/json',
        'Access-Control-Allow-Origin': '*',
    }
    content = None

    try:
        response = requests.get(url, headers=headers)
        content = response.json()
    except requests.exceptions.HTTPError as e:
        print("Bad HTTP status code:", e)
    except requests.exceptions.RequestException as e:
        print("Network error:", e)

    return content
