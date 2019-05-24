from istacpy.resources import *


def get_indicators(q="", order="", limit=25, offset=0, fields=None, representation=None):
    """Get indicators

    This function returns a list of indicators published in the ISTAC-indicators database. An indicator is a measure
    used to know the intensity of a phenomenon in spacetime. This measure can refer to different spatial or temporal
    granularities.

    Args:
        q (string): Metadata query on which the searches can be built using ``id``, ``subjectCode`` or
            ``geographicValue``.
        order (string): Order. Possible values are: ``update`` and ``id``. Order criteria are ``ASC`` and ``DESC``.
        limit (int): Results limit. By default ``limit = 25``.
        offset (int): Displacement. Result from which it is returned.  By default ``offset = 0``.
        fields (string): Use of the answer by adding new fields. Possible values are: ``+metadata``, ``+data`` and
            ``+observationsMetadata``.
        representation (string): Allows filtering the observations by their value. Its use only makes sense when
            ``+data`` and/or ``+observationsMetadata`` has been included.

    Examples:
        >>> get_indicators(q = 'id IN ("AFILIACIONES", "EMPLEO_REGISTRADO_AGRICULTURA")', order = "id ASC",
                fields = "+data", representation ="GEOGRAPHICAL[35003|35005],MEASURE[ABSOLUTE]")

    """
    # URL params
    api = "indicators"
    path = "indicators"

    # Parse order
    if order is not None:
        order = parse_param(order)

    # Parse fields
    if fields is not None:
        fields = parse_param(fields)

    # Parse representation
    if representation is not None:
        representation = parse_param(representation)

    # Get indicators using query (q) parameter
    if q is not None:
        q = parse_param(q)
        params = "&order=" + order + "&limit=" + str(limit) + "&offset=" + str(
            offset) + "&fields=" + fields + "&representation=" + representation
        path = path + "?q=" + q + params
    else:
        params = "?order=" + order + "&limit=" + str(limit) + "&offset=" + str(
            offset) + "&fields=" + fields + "&representation=" + representation
        path = path + params

    # Get URL
    url = get_url(api, path)

    # Get content
    content = get_content(url)

    return content


def get_indicators_code(indicatorcode):
    """Get indicators code

    This function returns the metadata that describe the characteristics of a specific indicator,
    allowing the compression of the measured fact; also through the data request the complete data (for all spacetime)
    of the indicator is provided.

    Args:
        indicatorcode (string): an indicator code

    Examples:
        >>> get_indicators_code("AFILIACIONES")
        >>> get_indicators_code("PARO_REGISTRADO")
    """
    # URL params
    api = "indicators"
    path = "indicators"

    # Get URL
    url = get_url(api, path, resource=indicatorcode)

    # Get content
    content = get_content(url)

    return content


def get_indicators_code_data(indicatorcode, representation=None, granularity="", fields=None):
    """Get indicators code data

    This function returns complete data (for all spacetime) of the indicator.
    On the other hand, metadata describing the characteristics of a specific
    indicator are offered through the metadata request, allowing the compression
    of the measured fact.

    Args:
        indicatorcode (string): an indicator code
        representation (string): Allows filtering the observations by their value.
        granularity (string): Allows to filter the observations through the granularities of the same.
        fields (string): Allows you to customize the response by excluding fields. The possible values are:
            ``-observationsMetadata``.

    Examples:
        >>> get_indicators_code_data("AFILIACIONES")
    """
    # Parse representation
    if representation is not None:
        representation = parse_param(representation)

    # Parse granularity
    if granularity is not None:
        granularity = parse_param(granularity)

    # Parse fields
    if fields is not None:
        fields = parse_param(fields)

    # Build URL
    api = "indicators"
    path = "indicators"
    resource = indicatorcode + "/data" + "?representation=" + representation + "&granularity="\
        + granularity + "&fields=" + fields
    url = get_url(api, path, resource=resource)

    # Get content
    content = get_content(url)

    return content
