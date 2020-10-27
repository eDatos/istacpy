from istacpy.resources import resources


def get_structuralresources_concept_types():
    """Get concept types

    This function returns the content from ``/v1.0/conceptTypes``

    Examples:
        >>> get_structuralresources_concept_types()
    """
    # Build URL
    api = "structural-resources"
    path = "conceptTypes"
    url = resources.get_url(api, path)

    # Get content
    content = resources.get_content(url)

    return content


def get_structuralresources_concept_schemes(limit=25, offset=0, query=None, orderby=None):
    """Get concept schemes

    This function returns the content from ``/v1.0/conceptschemes``

    Args:
        limit (int): Results limit. By default ``limit = 25``.
        offset (int): Displacement. Result from which it is returned. By default
            ``offset = 0``.
        query (string): Query to filter the results.
        orderby (string): Field by which to sort the results.

    Examples:
        >>> get_structuralresources_concept_schemes()
        >>> get_structuralresources_concept_schemes(
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
    path = "conceptschemes"
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


def get_structuralresources_concept_schemes_agency(
    agencyid, limit=25, offset=0, query=None, orderby=None
):
    """Get concept schemes agency

    This function returns the content from ``/v1.0/conceptschemes/{agencyID}``

    Args:
        agencyid (string): Identifier of the agency that publishes.
        limit (int): Results limit. By default ``limit = 25``.
        offset (int): Displacement. Result from which it is returned. By default
            ``offset = 0``.
        query (string): Query to filter the results.
        orderby (string): Field by which to sort the results.

    Examples:
        >>> get_structuralresources_concept_schemes_agency("ISTAC")
        >>> get_structuralresources_concept_schemes_agency(
        ...     "ESTAT",
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
    path = "conceptschemes"
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


def get_structuralresources_concept_schemes_agency_resource(
    agencyid, resourceid, limit=25, offset=0, query=None, orderby=None
):
    """Get concept schemes agency resource

    This function returns the content from ``/v1.0/conceptschemes/{agencyID}/{resourceID}``

    Args:
        agencyid (string): Identifier of the agency that publishes.
        resourceid (string): Resource identifier.
        limit (int): Results limit. By default ``limit = 25``.
        offset (int): Displacement. Result from which it is returned. By default
            ``offset = 0``.
        query (string): Query to filter the results.
        orderby (string): Field by which to sort the results.

    Examples:
        >>> get_structuralresources_concept_schemes_agency_resource(
        ...     agencyid="ISTAC",
        ...     resourceid="CL_AREA_ES"
        ... )
    """
    # Parse query
    query = resources.parse_param(query)

    # Parse orderby
    orderby = resources.parse_param(orderby)

    # Build URL
    api = "structural-resources"
    path = "conceptschemes"
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


def get_structuralresources_concept_schemes_agency_resource_version(
    agencyid, resourceid, version
):
    """Get concept schemes agency resource version

    This function returns the content from
    ``/v1.0/conceptschemes/{agencyID}/{resourceID}/{version}``

    Args:
        agencyid (string) Identifier of the agency that publishes.
        resourceid (string) Resource identifier.
        version (string) Specific version of the resource.

    Examples:
        >>> get_structuralresources_concept_schemes_agency_resource_version(
        ...     gencyid="ISTAC",
        ...     resourceid="CL_AREA",
        ...     version="01.000"
        ... )
    """
    # Build URL
    api = "structural-resources"
    path = "conceptschemes"
    resource = agencyid + "/" + resourceid + "/" + version
    url = resources.get_url(api, path, resource)

    # Get content
    # content = resources.get_content(url)

    return url


def get_structuralresources_concept_schemes_agency_resource_version_concepts(
    agencyid, resourceid, version, limit=25, offset=0, query=None, orderby=None
):
    """Get concept schemes agency resource version concepts

    This function returns the content from
    ``/v1.0/conceptschemes/{agencyID}/{resourceID}/{version}/concepts``

    Args:
        agencyid (string): Identifier of the agency that publishes.
        resourceid (string): Resource identifier.
        version (string): Specific version of the resource.
        limit (int): Results limit. By default ``limit = 25``.
        offset (int): Displacement. Result from which it is returned. By default
            ``offset = 0``.
        query (string): Query to filter the results.
        orderby (string): Field by which to sort the results.

    Examples:
        >>> get_structuralresources_concept_schemes_agency_resource_version_concepts(
        ...     agencyid="ISTAC",
        ...     resourceid="CL_AREA_ES",
        ...     version="01.000"
        ... )
    """
    # Parse query
    query = resources.parse_param(query)

    # Parse orderby
    orderby = resources.parse_param(orderby)

    # Build URL
    api = "structural-resources"
    path = "conceptschemes"
    resource = agencyid + "/" + resourceid + "/" + version + "/concepts"
    url = resources.get_url(api, path, resource)

    # Get content
    # content = resources.get_content(url)

    return url


def get_structuralresources_concept_schemes_agency_resource_version_concepts_id(
    agencyid, resourceid, version, conceptid
):
    """Get concept schemes agency resource version concepts (id)

    This function returns the content from
    ``/v1.0/conceptschemes/{agencyID}/{resourceID}/{version}/concepts/{conceptID}``

    Args:
        agencyid (string): Identifier of the agency that publishes.
        resourceid (string): Resource identifier.
        version (string): Specific version of the resource.
        conceptid (string): Concept identifier.

    Examples:
        >>> get_structuralresources_concept_schemes_agency_resource_version_concepts_id(
        ...     agencyid="ISTAC",
        ...     resourceid="CL_AREA_ES",
        ...     version="01.000",
        ...     conceptID = 0
        ... )
    """
    # Build URL
    api = "structural-resources"
    path = "conceptschemes"
    resource = agencyid + "/" + resourceid + "/" + version + "/concepts/" + conceptid
    url = resources.get_url(api, path, resource)

    # Get content
    # content = resources.get_content(url)

    return url
