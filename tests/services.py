def is_valid_response(response):
    return all((isinstance(response, dict), 'kind' in response, 'selfLink' in response))
