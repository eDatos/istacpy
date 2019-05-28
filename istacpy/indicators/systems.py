from istacpy.resources import resources


def get_indicators_systems(limit=25, offset=0):
    """Get indicators systems

    This function returns a list of indicator systems published in the ISTAC-indicators database.
    The indicators are simple or compound statistics, however a single indicator can rarely provide useful
    information about complex phenomena such as the economic situation, living conditions, schooling or others.
    Indicator systems are generally designed to generate more and more accurate information about the
    conditions of a phenomenon; and for this they are organized in dimensions or areas of analysis, under which the
    indicators are integrated.

    Args:
        limit (int): Results limit. By default ``limit = 25``.
        offset (int): Displacement. Result from which it is returned. By default ``offset = 0``.

    Examples:
        >>> get_indicators_systems()

    """
    # Build URL
    api = "indicators"
    path = "indicatorsSystems"

    path = path + "?limit=" + str(limit) + "&offset=" + str(offset)
    url = resources.get_url(api, path)

    # Get content
    content = resources.get_content(url)

    return content


def get_indicators_systems_code(indicatorsystemcode):
    """Get indicators system code

    This function returns metadata of a system of indicators published in the ISTAC-indicators database.
    The indicators are simple or compound statistics, however a single indicator can rarely provide useful
    information about complex phenomena such as the economic situation, living conditions, schooling or others.

    Args:
        indicatorsystemcode (string): an indicator system code

    Examples:
        >>> get_indicators_systems_code("C00075H")
    """
    # Build URL
    api = "indicators"
    path = "indicatorsSystems"
    resource = indicatorsystemcode
    url = resources.get_url(api, path, resource)

    # Get content
    content = resources.get_content(url)

    return content


def get_indicators_systems_code_instances(indicatorsystemcode, q=None, order=None, limit=25, offset=0, fields=None,
                                          representation=None, granularity=None):
    """Get indicators system code instances

    This function returns instances of indicators associated with a specific indicator system. An instance of an
    indicator is nothing more than a spatio-temporal query of an indicator when it is incorporated into a specific
    indicator system.

    Args:
        indicatorsystemcode (string): with an indicator system code
        q (string): Query of metadata on which the searches can be built are: ``id`` and ``geographicalValue``.
        order (string): Order. Possible values are: ``update`` and ``id`` and order criteria are ``ASC`` and ``DESC``.
        limit (int): Results limit. By default ``limit = 25``.
        offset (int): Displacement. Result from which it is returned.  By default ``offset = 0``.
        fields (string): Use of the answer by adding new fields. Possible values are: ``+metadata``, ``+data`` and
            ``+observationsMetadata``.
        representation (string): Allows filtering the observations by their value. Its use only makes sense when
            ``+data`` and/or ``+observationsMetadata`` has been included.
        granularity (string): Allows to filter the observations through the granularities of the same.
            Its use only makes sense when ``+data`` and/or ``+observationsMetadata`` has been included.

    Examples:
        >>> get_indicators_systems_code_instances("C00075H")
        >>> get_indicators_systems_code_instances("C00075H", q = 'id EQ "INDICADORES_MUNICIPALES"')
    """
    # Parse order
    order = resources.parse_param(order)

    # Parse fields
    fields = resources.parse_param(fields)

    # Parse representation
    representation = resources.parse_param(representation)

    # Parse granularity
    granularity = resources.parse_param(granularity)

    # Build URL
    api = "indicators"
    path = "indicatorsSystems"
    resource = indicatorsystemcode + "/indicatorsInstances"
    if q is not None:
        q = resources.parse_param(q)
        params = "?q=" + q + "&order=" + order + "&limit=" + str(limit) + "&offset=" + str(
            offset) + "&fields=" + fields + "&representation=" + representation + "&granularity=" + granularity
    else:
        params = "?order=" + order + "&limit=" + str(limit) + "&offset=" + str(
            offset) + "&fields=" + fields + "&representation=" + representation + "&granularity=" + granularity

    resource = resource + params
    url = resources.get_url(api, path, resource)

    # Get content
    content = resources.get_content(url)

    return content


def get_indicators_systems_code_instances_code(indicatorsystemcode, indicatorinstancecode):
    """Get indicators system code instances code

    This function returns metadata of an indicator set associated with a specific indicator system. An instance of an
    indicator is nothing more than a spatio-temporal query of an indicator when it is incorporated into a specific
    indicator system.

    Args:
        indicatorsystemcode (string) indicator system code
        indicatorinstancecode (string) indicator instance code
    Examples:
        >>> get_indicators_systems_code_instances_code("C00075H", "21af0477-d63b-493b-ad02-4ab181547223")
    """
    # Build URL
    api = "indicators"
    path = "indicatorsSystems"
    resource = indicatorsystemcode + "/indicatorsInstances/" + indicatorinstancecode
    url = resources.get_url(api, path, resource)

    # Get content
    content = resources.get_content(url)

    return content


def get_indicators_systems_code_instances_code_data(indicatorsystemcode, indicatorinstancecode, representation=None,
                                                    granularity=None, fields=None):
    """Get indicators system code instances code data

    This function returns data of an indicator unit associated with a specific indicator system. An instance of an
    indicator is nothing more than a spatio-temporal query of an indicator when it is incorporated into a specific
    indicator system.

    Args:
        indicatorsystemcode (string): Indicator system code
        indicatorinstancecode (string): Indicator instance code
        representation (string): Allows filtering the observations by their value.
        granularity (string): Allows to filter the observations through the granularities of the same.
        fields (string): Allows you to customize the response by excluding fields. The possible values are:
            ``-observationsMetadata``.

    Examples:
        >>> get_indicators_systems_code_instances_code_data("C00075H", "21af0477-d63b-493b-ad02-4ab181547223")
    """
    # Parse representation
    representation = resources.parse_param(representation)

    # Parse granularity
    granularity = resources.parse_param(granularity)

    # Parse fields
    fields = resources.parse_param(fields)

    # Build URL
    api = "indicators"
    path = "indicatorsSystems"
    resource = indicatorsystemcode + "/indicatorsInstances/" + indicatorinstancecode + "/data"
    params = "?representation=" + representation + "&granularity=" + granularity + "&fields=" + fields
    resource = resource + params
    url = resources.get_url(api, path, resource)

    # Get content
    content = resources.get_content(url)

    return content
