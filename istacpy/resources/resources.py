import requests


# Build API URL
def get_url(api, path, resource=None):
    url_root = "https://www.gobiernodecanarias.org/istac/api/" + api + "/v1.0/"
    if resource is None:
        url = url_root + path
    else:
        url = url_root + path + "/" + resource

    return url


# Example: parse_param("GEOGRAPHICAL[MUNICIPALITIES]")
def parse_param(param):

    if param is None:
        # Return a string
        param = ""

    else:
        param = param.strip()  # Remove white spaces (trim)
        param = param.replace("[", "%5B")  # Replace [ for %5B
        param = param.replace("]", "%5D")  # Replace ] for %5D
        param = param.replace(",", "%2C")  # Replace , for %2C
        param = param.replace("|", "%7C")  # Replace | for %7C
        param = param.replace("+", "%2B")  # Replace + for %2B
        param = param.replace("\"", "%22")  # Replace \" for %22
        param = param.replace(" ", "%20")  # Replace space for %20

    return param


def get_content(url):

    headers = {
        'Content-Type': 'application/json;charset=UTF-8',
        'Access-Control-Allow-Origin': '*',
    }
    content = None

    try:
        # Get content
        r = requests.get(url, headers=headers)
        # Decode JSON response into a Python dict:
        content = r.json()
    except requests.exceptions.HTTPError as e:
        print("Bad HTTP status code:", e)
    except requests.exceptions.RequestException as e:
        print("Network error:", e)

    return content
