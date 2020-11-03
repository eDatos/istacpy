import os

from istacpy import services

API = 'structural-resources'


def get_structuralresources_content_constraints(limit=25, offset=0, query='', orderby=''):
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
    path = 'contentConstraints'
    url = services.build_entrypoint_url(
        API, path, limit=limit, offset=offset, query=query, orderBy=orderby
    )
    return services.get_content(url)


def get_structuralresources_content_constraints_agency(
    agencyid, limit=25, offset=0, query='', orderby=''
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
    path = os.path.join('contentConstraints', agencyid)
    url = services.build_entrypoint_url(
        API, path, limit=limit, offset=offset, query=query, orderBy=orderby
    )
    return services.get_content(url)


def get_structuralresources_content_constraints_agency_resource(
    agencyid, resourceid, limit=25, offset=0, query='', orderby=''
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
        >>> get_structuralresources_content_constraints_agency_resource(
        ...     "ISTAC",
        ...     "CSM_C00010A_SIE"
        ... )
    """
    path = os.path.join('contentConstraints', agencyid, resourceid)
    url = services.build_entrypoint_url(
        API, path, limit=limit, offset=offset, query=query, orderBy=orderby
    )
    return services.get_content(url)


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
        ...     "CSM_C00010A_SIE",
        ...     "01.000"
        ... )
    """
    path = os.path.join('contentConstraints', agencyid, resourceid, version)
    url = services.build_entrypoint_url(API, path)
    return services.get_content(url)


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
        ...     "CSM_C00010A_SIE",
        ...     "01.000"
        ... )
    """
    path = "contentConstraints"
    path = os.path.join(
        'contentConstraints', agencyid, resourceid, version, 'regions', regioncode
    )
    url = services.build_entrypoint_url(API, path)
    return services.get_content(url)


def get_structuralresources_data_structures(limit=25, offset=0, query='', orderby=''):
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
    path = 'datastructures'
    url = services.build_entrypoint_url(
        API, path, limit=limit, offset=offset, query=query, orderBy=orderby
    )
    return services.get_content(url)


def get_structuralresources_data_structures_agency(
    agencyid, limit=25, offset=0, query='', orderby=''
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
    path = os.path.join('datastructures', agencyid)
    url = services.build_entrypoint_url(
        API, path, limit=limit, offset=offset, query=query, orderBy=orderby
    )
    return services.get_content(url)


def get_structuralresources_data_structures_agency_resource(
    agencyid, resourceid, limit=25, offset=0, query='', orderby=''
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
        >>> get_structuralresources_data_structures_agency_resource(
        ...     "ISTAC",
        ...     "DSD_C00010A_00001"
        ... )
    """
    path = os.path.join('datastructures', agencyid, resourceid)
    url = services.build_entrypoint_url(
        API, path, limit=limit, offset=offset, query=query, orderBy=orderby
    )
    return services.get_content(url)


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
        ...     "DSD_C00010A_00001",
        ...     "01.001"
        ... )
    """
    path = os.path.join('datastructures', agencyid, resourceid, version)
    url = services.build_entrypoint_url(API, path)
    return services.get_content(url)
