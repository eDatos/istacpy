from istacpy.resources import resources


def get_structuralresources_variable_families(limit=25, offset=0, query=None, orderby=None):
    """Get variable families

    This function returns data from ``/v1.0/variablefamilies``

    Args:
        limit (int): Results limit. By default ``limit = 25``.
        offset (int): Displacement. Result from which it is returned. By default
            ``offset = 0``.
        query (string): Query to filter the results.
        orderby (string): Field by which to sort the results.

    Examples:
        >>> get_structuralresources_variable_families()
    """
    # Parse query
    query = resources.parse_param(query)

    # Parse orderBy
    orderby = resources.parse_param(orderby)

    # Build URL
    api = "structural-resources"
    path = "variablefamilies"
    params = (
        "?limit="
        + str(limit)
        + "&offset="
        + str(offset)
        + "&query="
        + query
        + "&orderBy="
        + orderby
    )
    path = path + params
    url = resources.get_url(api, path)

    # Get content
    content = resources.get_content(url)

    return content


def get_structuralresources_variable_families_id(id):
    """Get variable families (id)

    This function returns data from ``/v1.0/variablefamilies/{id}``

    Args:
        id (string): Variable family identificator.

    Examples:
        >>> get_structuralresources_variable_families_id("VRF_DEMOGRAFICAS")
    """
    # Build URL
    api = "structural-resources"
    path = "variablefamilies"
    resource = id
    url = resources.get_url(api, path, resource)

    # Get content
    content = resources.get_content(url)

    return content


def get_structuralresources_variable_families_id_variables(
    id, limit=25, offset=0, query=None, orderby=None
):
    """Get variable families (id) variables

    This function returns data from ``/v1.0/variablefamilies/{id}/variables``

    Args:
        id (string): Variable family identificator.
        limit (int): Results limit. By default ``limit = 25``.
        offset (int): Displacement. Result from which it is returned. By default
            ``offset = 0``.
        query (string): Query to filter the results.
        orderby (string): Field by which to sort the results.

    Examples:
        >>> get_structuralresources_variable_families_id_variables("VRF_DEMOGRAFICAS")
    """
    # Parse query
    query = resources.parse_param(query)

    # Parse orderBy
    orderby = resources.parse_param(orderby)

    # Build URL
    api = "structural-resources"
    path = "variablefamilies"
    resource = id + "/variables"
    params = (
        "?limit="
        + str(limit)
        + "&offset="
        + str(offset)
        + "&query="
        + query
        + "&orderBy="
        + orderby
    )
    resource = resource + params
    url = resources.get_url(api, path, resource)

    # Get content
    content = resources.get_content(url)

    return content


def get_structuralresources_variables(limit=25, offset=0, query=None, orderby=None):
    """Get variables

    This function returns data from ``/v1.0/variables``

    Args:
        limit (int): Results limit. By default ``limit = 25``.
        offset (int): Displacement. Result from which it is returned. By default
            ``offset = 0``.
        query (string): Query to filter the results.
        orderby (string): Field by which to sort the results.

    Examples:
        >>> get_structuralresources_variables()
    """
    # Parse query
    query = resources.parse_param(query)

    # Parse orderBy
    orderby = resources.parse_param(orderby)

    # Build URL
    api = "structural-resources"
    path = "variables"
    url = resources.get_url(api, path)

    # Get content
    content = resources.get_content(url)

    return content


def get_structuralresources_variables_id(id):
    """Get variables (id)

    This function returns data from ``/v1.0/variables/{id}``

    Args:
        id (string): Variable identifier.

    Examples:
      >>> get_structuralresources_variables_id("VR_SEXO")
    """
    # Build URL
    api = "structural-resources"
    path = "variables"
    resource = id
    url = resources.get_url(api, path, resource)

    # Get content
    content = resources.get_content(url)

    return content


def get_structuralresources_variableelements(
    variableid, limit=25, offset=0, query=None, orderby=None
):
    """Get variableelements

    This function returns data from ``/v1.0/variables/{variableID}/variableelements``

    Args:
        variableid (string) Variable identificator.
        limit (int) Results limit. By default ``limit = 25``.
        offset (int) Displacement. Result from which it is returned. By default
            ``offset = 0``.
        query (string) Query to filter the results.
        orderby (string) Field by which to sort the results.

    Examples:
        >>> get_structuralresources_variableelements("VR_SEXO")
    """
    # Parse query
    query = resources.parse_param(query)

    # Parse orderBy
    orderby = resources.parse_param(orderby)

    # Build URL
    api = "structural-resources"
    path = "variables"
    resource = variableid + "/variableelements"
    params = (
        "?limit="
        + str(limit)
        + "&offset="
        + str(offset)
        + "&query="
        + query
        + "&orderBy="
        + orderby
    )
    resource = resource + params
    url = resources.get_url(api, path, resource)

    # Get content
    content = resources.get_content(url)

    return content


def get_structuralresources_variableelements_resource(variableid, resourceid):
    """Get variableelements resource

    This function returns data from
    ``/v1.0/variables/{variableID}/variableelements/{resourceID}``

    Args:
        variableid (string): Resource identificator.
        resourceid (string): Variable identificator.

    Examples:
        >>> get_structuralresources_variableelements_resource("VR_SEXO", "FEMALE")
    """
    # Build URL
    api = "structural-resources"
    path = "variables"
    resource = variableid + "/variableelements/" + resourceid
    url = resources.get_url(api, path, resource)

    # Get content
    content = resources.get_content(url)

    return content


def get_structuralresources_geoinfo(
    variableid, resourceid, fields="", limit=25, offset=0, query=None, orderby=None
):
    """Get geoinfo

    This function returns data from
    ``/v1.0/variables/{variableID}/variableelements/{resourceID}/geoinfo``

    Args:
        variableid (string): Variable identificator.
        resourceid (string): Resource identificator.
        fields (string): Additional fields that you want to show in the answer.
        limit (int): Results limit. By default ``limit = 25``.
        offset (int): Displacement. Result from which it is returned. By default
            ``offset = 0``.
        query (string): Query to filter the results.
        orderby (string): Field by which to sort the results.

    Examples:
      >>> get_structuralresources_geoinfo("VR_TERRITORIO", "MUN_ICOD_VINOS")
    """
    # Parse fields
    fields = resources.parse_param(fields)

    # Parse query
    query = resources.parse_param(query)

    # Parse orderBy
    orderby = resources.parse_param(orderby)

    # Build URL
    api = "structural-resources"
    path = "variables"
    resource = variableid + "/variableelements/" + resourceid + "/geoinfo"
    params = (
        "?fields="
        + fields
        + "&limit="
        + str(limit)
        + "&offset="
        + str(offset)
        + "&query="
        + query
        + "&orderBy="
        + orderby
    )
    resource = resource + params
    url = resources.get_url(api, path, resource)

    # Get content
    content = resources.get_content(url)

    return content
