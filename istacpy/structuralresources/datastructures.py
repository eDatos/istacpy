from istacpy.resources import resources


def get_structuralresources_content_constraints(
    limit=25, offset=0, query=None, orderby=None
):
    """Get content constraints

    This function returns the content from ``/v1.0/contentConstraints``

    Args:
        limit (int): Results limit. By default ``limit = 25``.
        offset (int): Displacement. Result from which it is returned. By default
            ``offset = 0``.
        query (string): Query to filter the results.
        orderby (string): Field by which to sort the results.

    Examples:
        >>> get_structuralresources_content_constraints()
        >>> get_structuralresources_content_constraints(
        ...     query="ID EQ 2090",
        ...     orderby="ID ASC"
        ... )
    """
    # Parse query
    query = resources.parse_param(query)

    # Parse orderby
    orderby = resources.parse_param(orderby)

    # Build URL
    api = "structural-resources"
    path = "contentConstraints"
    params = (
        "?limit="
        + str(limit)
        + "&offset="
        + str(offset)
        + "&orderby="
        + orderby
        + "&query="
        + query
    )
    path = path + params
    url = resources.get_url(api, path)

    # Get content
    content = resources.get_content(url)

    return content


def get_structuralresources_content_constraints_agency(
    agencyid, limit=25, offset=0, query=None, orderby=None
):
    """Get content constraints agency

    This function returns the content from ``/v1.0/contentConstraints/{agencyID}``

    Args:
        agencyid (string): Identifier of the agency that publishes.
        limit (int): Results limit. By default ``limit = 25``.
        offset (int): Displacement. Result from which it is returned. By default
            ``offset = 0``.
        query (string): Query to filter the results.
        orderby (string): Field by which to sort the results.

    Examples:
        >>> get_structuralresources_content_constraints_agency("ISTAC")
    """
    # Parse query
    query = resources.parse_param(query)

    # Parse orderby
    orderby = resources.parse_param(orderby)

    # Build URL
    api = "structural-resources"
    path = "contentConstraints"
    resource = agencyid
    params = (
        "?limit="
        + str(limit)
        + "&offset="
        + str(offset)
        + "&orderby="
        + orderby
        + "&query="
        + query
    )
    resource = resource + params
    url = resources.get_url(api, path, resource)

    # Get content
    content = resources.get_content(url)

    return content


def get_structuralresources_content_constraints_agency_resource(
    agencyid, resourceid, limit=25, offset=0, query=None, orderby=None
):
    """Get content constraints agency resource

    This function returns the content from
        ``/v1.0/contentConstraints/{agencyID}/{resourceID}``

    Args:
        agencyid (string): Identifier of the agency that publishes.
        resourceid (string): Resource identifier.
        limit (int): Results limit. By default ``limit = 25``.
        offset (int): Displacement. Result from which it is returned. By default
            ``offset = 0``.
        query (string): Query to filter the results.
        orderby (string): Field by which to sort the results.

    Examples:
        >>> get_structuralresources_content_constraints_agency_resource("ISTAC", "CL_AREA")
    """
    # Parse query
    query = resources.parse_param(query)

    # Parse orderby
    orderby = resources.parse_param(orderby)

    # Build URL
    api = "structural-resources"
    path = "contentConstraints"
    resource = agencyid + "/" + resourceid
    params = (
        "?limit="
        + str(limit)
        + "&offset="
        + str(offset)
        + "&orderby="
        + orderby
        + "&query="
        + query
    )
    resource = resource + params
    url = resources.get_url(api, path, resource)

    # Get content
    content = resources.get_content(url)

    return content


def get_structuralresources_content_constraints_agency_resource_version(
    agencyid, resourceid, version
):
    """Get content constraints agency resource version

    This function returns the content from
    ``/v1.0/contentConstraints/{agencyID}/{resourceID}/{version}``

    Args:
        agencyid (string): Identifier of the agency that publishes.
        resourceid (string): Resource identifier.
        version (string): Specific version of the resource.

    Examples:
        >>> get_structuralresources_content_constraints_agency_resource_version(
        ...     "ISTAC",
        ...     "CL_AREA",
        ...     "01.000"
        ... )
    """
    # Build URL
    api = "structural-resources"
    path = "contentConstraints"
    resource = agencyid + "/" + resourceid + "/" + version
    url = resources.get_url(api, path, resource)

    # Get content
    # content = resources.get_content(url)

    return url


def get_structuralresources_content_constraints_agency_resource_version_regions(
    regioncode, agencyid, resourceid, version
):
    """Get content constraints agency resource version regions

    This function returns the content from
    ``/v1.0/contentConstraints/{agencyID}/{resourceID}/{version}/regions/``
    {regionCode}

    Args:
        regioncode (string) Region code.
        agencyid (string) Identifier of the agency that publishes.
        resourceid (string) Resource identifier.
        version (string) Specific version of the resource.

    Examples:
        >>> get_structuralresources_content_constraints_agency_resource_version_regions(
        ...     "0001",
        ...     "ISTAC",
        ...     "CL_AREA",
        ...     "01.000"
        ... )
    """
    # Build URL
    api = "structural-resources"
    path = "contentConstraints"
    resource = agencyid + "/" + resourceid + "/" + version + "/regions/" + regioncode
    url = resources.get_url(api, path, resource)

    # Get content
    # content = resources.get_content(url)

    return url


def get_structuralresources_data_structures(limit=25, offset=0, query=None, orderby=None):
    """Get data structures

    This function returns the content from ``/v1.0/datastructures``

    Args:
        limit (int): Results limit. By default ``limit = 25``.
        offset (int): Displacement. Result from which it is returned. By default
            ``offset = 0``.
        query (string): Query to filter the results.
        orderby (string): Field by which to sort the results.

    Examples:
        >>> get_structuralresources_data_structures()
        >>> get_structuralresources_data_structures(
        ...     query="ID EQ 2090",
        ...     orderby="ID ASC"
        ... )
    """
    # Parse query
    query = resources.parse_param(query)

    # Parse orderby
    orderby = resources.parse_param(orderby)

    # Build URL
    api = "structural-resources"
    path = "datastructures"
    params = (
        "?limit="
        + str(limit)
        + "&offset="
        + str(offset)
        + "&orderby="
        + orderby
        + "&query="
        + query
    )
    path = path + params
    url = resources.get_url(api, path)

    # Get content
    content = resources.get_content(url)

    return content


def get_structuralresources_data_structures_agency(
    agencyid, limit=25, offset=0, query=None, orderby=None
):
    """Get data structures agency

    This function returns the content from ``/v1.0/datastructures/{agencyID}``

    Args:
        agencyid (string): Identifier of the agency that publishes.
        limit (int): Results limit. By default ``limit = 25``.
        offset (int): Displacement. Result from which it is returned. By default
            ``offset = 0``.
        query (string): Query to filter the results.
        orderby (string): Field by which to sort the results.

    Examples:
        >>> get_structuralresources_data_structures_agency("ISTAC")
    """
    # Parse query
    query = resources.parse_param(query)

    # Parse orderby
    orderby = resources.parse_param(orderby)

    # Build URL
    api = "structural-resources"
    path = "datastructures"
    resource = agencyid
    params = (
        "?limit="
        + str(limit)
        + "&offset="
        + str(offset)
        + "&orderby="
        + orderby
        + "&query="
        + query
    )
    resource = resource + params
    url = resources.get_url(api, path, resource)

    # Get content
    content = resources.get_content(url)

    return content


def get_structuralresources_data_structures_agency_resource(
    agencyid, resourceid, limit=25, offset=0, query=None, orderby=None
):
    """Get data structures agency resource

    This function returns the content from ``/v1.0/datastructures/{agencyID}/{resourceID}``

    Args:
        agencyid (string): Identifier of the agency that publishes.
        resourceid (string): Resource identifier.
        limit (int): Results limit. By default ``limit = 25``.
        offset (int): Displacement. Result from which it is returned. By default
            ``offset = 0``.
        query (string): Query to filter the results.
        orderby (string): Field by which to sort the results.

    Examples:
        >>> get_structuralresources_data_structures_agency_resource("ISTAC", "CL_AREA")
    """

    # Parse query
    query = resources.parse_param(query)

    # Parse orderby
    orderby = resources.parse_param(orderby)

    # Build URL
    api = "structural-resources"
    path = "datastructures"
    resource = agencyid + "/" + resourceid
    params = (
        "?limit="
        + str(limit)
        + "&offset="
        + str(offset)
        + "&orderby="
        + orderby
        + "&query="
        + query
    )
    resource = resource + params
    url = resources.get_url(api, path, resource)

    # Get content
    content = resources.get_content(url)

    return content


def get_structuralresources_data_structures_agency_resource_version(
    agencyid, resourceid, version
):
    """Get data structures agency resource version

    This function returns the content from
    ``/v1.0/datastructures/{agencyID}/{resourceID}/{version}``

    Args:
        agencyid (string): Identifier of the agency that publishes.
        resourceid (string): Resource identifier.
        version (string): Specific version of the resource.

    Examples:
        >>> get_structuralresources_data_structures_agency_resource_version(
        ...     "ISTAC",
        ...     "CL_AREA",
        ...     "01.000"
        ... )
    """
    # Build URL
    api = "structural-resources"
    path = "datastructures"
    resource = agencyid + "/" + resourceid + "/" + version
    url = resources.get_url(api, path, resource)

    # Get content
    # content = resources.get_content(url)

    return url
