def assert_valid_response(response):
    assert isinstance(response, dict)
    assert 'kind' in response
    assert 'selfLink' in response
