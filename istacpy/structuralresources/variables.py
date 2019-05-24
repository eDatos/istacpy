from istacpy.resources import *


def get_structuralresources_variable_families(limit=25, offset=0, query=None, orderby=None):
    """Get variable families

    This function returns data from /v1.0/variablefamilies

    Args:
        limit (int): Results limit. By default ``limit = 25``.
        offset (int): Displacement. Result from which it is returned.  By default ``offset = 0``.
        query (string): Query to filter the results.
        orderby (string): Field by which to sort the results.

    Examples:
        >>> get_structuralresources_variable_families()
    """
    # Parse query
    if query is not None:
        query = parse_param(query)

    # Parse orderBy
    if orderby is not None:
        orderby = parse_param(orderby)

    # Build URL
    api = "structural-resources"
    path = "variablefamilies" + ".json"
    params = "?limit=" + str(limit) + "&offset=" + str(offset) + "&query=" + query + "&orderBy=" + orderby
    path = path + params
    url = get_url(api, path)

    # Get content
    content = get_content(url)

    return content


def get_structuralresources_variable_families_id(id):
    """Get variable families (id)

    This function returns data from /v1.0/variablefamilies/{id}

    Args:
        id (string): Variable family identificator.

    Examples:
        >>> get_structuralresources_variable_families_id("VRF_DEMOGRAFICAS")
    """
    # Build URL
    api = "structural-resources"
    path = "variablefamilies"
    resource = id + ".json"
    url = get_url(api, path, resource)

    # Get content
    content = get_content(url)

    return content


def get_structuralresources_variable_families_id_variables(id, limit=25, offset=0, query=None, orderby=None):
    """Get variable families (id) variables

    This function returns data from /v1.0/variablefamilies/{id}/variables

    Args:
        id (string): Variable family identificator.
        limit (int): Results limit. By default ``limit = 25``.
        offset (int): Displacement. Result from which it is returned.  By default ``offset = 0``.
        query (string): Query to filter the results.
        orderby (string): Field by which to sort the results.

    Examples:
        >>> get_structuralresources_variable_families_id_variables("VRF_DEMOGRAFICAS")
    """
    # Parse query
    if query is not None:
        query = parse_param(query)

    # Parse orderBy
    if orderby is not None:
        orderby = parse_param(orderby)

    # Build URL
    api = "structural-resources"
    path = "variablefamilies"
    resource = id + "/variables" + ".json"
    params = "?limit=" + str(limit) + "&offset=" + str(offset) + "&query=" + query + "&orderBy=" + orderby
    resource = resource + params
    url = get_url(api, path, resource)

    # Get content
    content = get_content(url)

    return content


def get_structuralresources_variables(limit=25, offset=0, query=None, orderby=None):
    """Get variables

    This function returns data from /v1.0/variables

    Args:
        limit (int): Results limit. By default ``limit = 25``.
        offset (int): Displacement. Result from which it is returned.  By default ``offset = 0``.
        query (string): Query to filter the results.
        orderby (string): Field by which to sort the results.

    Examples:
        >>> get_structuralresources_variables()
    """
    # Parse query
    if query is not None:
        query = parse_param(query)

    # Parse orderBy
    if orderby is not None:
        orderby = parse_param(orderby)

    # Build URL
    api = "structural-resources"
    path = "variables" + ".json"
    url = get_url(api, path)

    # Get content
    content = get_content(url)

    return content


def get_structuralresources_variables_id(id):
    """Get variables (id)

    This function returns data from /v1.0/variables/{id}

    Args:
        id (string): Variable identifier.

    Examples:
      >>> get_structuralresources_variables_id("VR_SEXO")
    """
    # Build URL
    api = "structural-resources"
    path = "variables"
    resource = id + ".json"
    url = get_url(api, path, resource)

    # Get content
    content = get_content(url)

    return content


def get_structuralresources_variableelements(variableid, limit=25, offset=0, query=None, orderby=None):
    """Get variableelements

    This function returns data from /v1.0/variables/{variableID}/variableelements

    Args:
        variableid (string) Variable identificator.
        limit (int) Results limit. By default ``limit = 25``.
        offset (int) Displacement. Result from which it is returned.  By default ``offset = 0``.
        query (string) Query to filter the results.
        orderby (string) Field by which to sort the results.

    Examples:
        >>> get_structuralresources_variableelements("VR_SEXO")
    """
    # Parse query
    if query is not None:
        query = parse_param(query)

    # Parse orderBy
    if orderby is not None:
        orderby = parse_param(orderby)

    # Build URL
    api = "structural-resources"
    path = "variables"
    resource = variableid + "/variableelements" + ".json"
    params = "?limit=" + str(limit) + "&offset=" + str(offset) + "&query=" + query + "&orderBy=" + orderby
    resource = resource + params
    url = get_url(api, path, resource)

    # Get content
    content = get_content(url)

    return content


def get_structuralresources_variableelements_resource(variableid, resourceid):
    """Get variableelements resource

    This function returns data from /v1.0/variables/{variableID}/variableelements/{resourceID}

    Args:
        variableid (string): Resource identificator.
        resourceid (string): Variable identificator.

    Examples:
        >>> get_structuralresources_variableelements_resource("VR_SEXO", "FEMALE")
    """
    # Build URL
    api = "structural-resources"
    path = "variables"
    resource = variableid + "/variableelements/" + resourceid + ".json"
    url = get_url(api, path, resource)

    # Get content
    content = get_content(url)

    return content


def get_structuralresources_geoinfo(variableid, resourceid, fields="", limit=25, offset=0, query=None, orderby=None):
    """Get geoinfo

    This function returns data from /v1.0/variables/{variableID}/variableelements/{resourceID}/geoinfo

    Args:
        variableid (string): Variable identificator.
        resourceid (string): Resource identificator.
        fields (string): Additional fields that you want to show in the answer.
        limit (int): Results limit. By default ``limit = 25``.
        offset (int): Displacement. Result from which it is returned.  By default ``offset = 0``.
        query (string): Query to filter the results.
        orderby (string): Field by which to sort the results.

    Examples:
      >>> get_structuralresources_geoinfo("VR_TERRITORIO", "MUN_ICOD_VINOS")
    """
    # Parse fields
    if fields is not None:
        fields = parse_param(fields)

    # Parse query
    if query is not None:
        query = parse_param(query)

    # Parse orderBy
    if orderby is not None:
        orderby = parse_param(orderby)

    # Build URL
    api = "structural-resources"
    path = "variables"
    resource = variableid + "/variableelements/" + resourceid + "/geoinfo" + ".json"
    params = "?fields=" + fields + "&limit=" + str(limit) + "&offset=" + str(offset) + "&query=" + query + "&orderBy=" \
             + orderby
    resource = resource + params
    url = get_url(api, path, resource)

    # Get content
    content = get_content(url)

    return content
