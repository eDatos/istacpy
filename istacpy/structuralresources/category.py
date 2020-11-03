import os

from istacpy import services

API = 'structural-resources'


def get_structuralresources_categorisations(limit=25, offset=0, query='', orderby=''):
    """Get categorisations

    This function returns the content from ``/v1.0/categorisations``

    Args:
        limit (int): Results limit. By default ``limit = 25``.
        offset (int): Displacement. Result from which it is returned.  By default
            ``offset = 0``.
        query (string): Query to filter the results.
        orderby (string): Field by which to sort the results.

    Examples:
        >>> get_structuralresources_categorisations()
        >>> get_structuralresources_categorisations(
        ...     query="ID EQ 2090",
        ...     orderby="ID ASC"
        ... )
    """
    path = 'categorisations'
    url = services.build_entrypoint_url(
        API, path, limit=limit, offset=offset, query=query, orderBy=orderby
    )
    return services.get_content(url)


def get_structuralresources_categorisations_agency(
    agencyid, limit=25, offset=0, query='', orderby=''
):
    """Get categorisations agency

    This function returns the content from ``/v1.0/categorisations/{agencyID}``

    Args:
        agencyid (string): Identifier of the agency that publishes.
        limit (int): Results limit. By default ``limit = 25``.
        offset (int): Displacement. Result from which it is returned.  By default
            ``offset = 0``.
        query (string): Query to filter the results.
        orderby (string): Field by which to sort the results.

    Examples:
        >>> get_structuralresources_categorisations_agency("ISTAC")
    """
    path = os.path.join('categorisations', agencyid)
    url = services.build_entrypoint_url(
        API, path, limit=limit, offset=offset, query=query, orderBy=orderby
    )
    return services.get_content(url)


def get_structuralresources_categorisations_agency_resource(
    agencyid, resourceid, limit=25, offset=0, query='', orderby=''
):
    """Get categorisations agency resource

    This function returns the content from ``/v1.0/categorisations/{agencyID}/{resourceID}``

    Args:
        agencyid (string): Identifier of the agency that publishes.
        resourceid (string): Resource identifier.
        limit (int): Results limit. By default ``limit = 25``.
        offset (int): Displacement. Result from which it is returned.  By default
            ``offset = 0``.
        query (string): Query to filter the results.
        orderby (string): Field by which to sort the results.

    Examples:
        >>> get_structuralresources_categorisations_agency_resource("ISTAC", "cat2")
    """
    path = os.path.join('categorisations', agencyid, resourceid)
    url = services.build_entrypoint_url(
        API, path, limit=limit, offset=offset, query=query, orderBy=orderby
    )
    return services.get_content(url)


def get_structuralresources_categorisations_agency_resource_version(
    agencyid, resourceid, version
):
    """Get categorisations agency resource version

    This function returns the content from
    ``/v1.0/categorisations/{agencyID}/{resourceID}/{version}``

    Args:
        agencyid (string): Identifier of the agency that publishes.
        resourceid (string): Resource identifier.
        version (string): Specific version of the resource.

    Examples:
        >>> get_structuralresources_categorisations_agency_resource_version(
        ...     "ISTAC",
        ...     "cat2",
        ...     "01.000"
        ... )
    """
    path = os.path.join('categorisations', agencyid, resourceid, version)
    url = services.build_entrypoint_url(API, path)
    return services.get_content(url)


def get_structuralresources_category_schemes(limit=25, offset=0, query='', orderby=''):
    """Get category schemes

    This function returns the content from ``/v1.0/categoryschemes``

    Args:
        limit (int): Results limit. By default ``limit = 25``.
        offset (int): Displacement. Result from which it is returned.  By default
            ``offset = 0``.
        query (string): Query to filter the results.
        orderby (string): Field by which to sort the results.

    Examples:
        >>> get_structuralresources_category_schemes()
        >>> get_structuralresources_category_schemes(
        ...    query="ID EQ 2090",
        ...    orderby="ID ASC"
        ... )
    """
    path = 'categoryschemes'
    url = services.build_entrypoint_url(
        API, path, limit=limit, offset=offset, query=query, orderBy=orderby
    )
    return services.get_content(url)


def get_structuralresources_category_schemes_agency(
    agencyid, limit=25, offset=0, query='', orderby=''
):
    """Get category schemes agency

    This function returns the content from ``/v1.0/categoryschemes/{agencyID}``

    Args:
        agencyid (string): Identifier of the agency that publishes.
        limit (int): Results limit. By default ``limit = 25``.
        offset (int): Displacement. Result from which it is returned.  By default
            ``offset = 0``.
        query (string): Query to filter the results.
        orderby (string): Field by which to sort the results.

    Examples:
        >>> get_structuralresources_category_schemes_agency(
        ...     "ISTAC",
        ...     query="ID EQ 2090",
        ...     orderby="ID ASC"
        ...)
    """
    path = os.path.join('categoryschemes', agencyid)
    url = services.build_entrypoint_url(
        API, path, limit=limit, offset=offset, query=query, orderBy=orderby
    )
    return services.get_content(url)


def get_structuralresources_category_schemes_agency_resource(
    agencyid, resourceid, limit=25, offset=0, query='', orderby=''
):
    """Get category schemes agency resource

    This function returns the content from ``/v1.0/categoryschemes/{agencyID}/{resourceID}``

    Args:
        agencyid (string): Identifier of the agency that publishes.
        resourceid (string): Resource identifier.
        limit (int): Results limit. By default ``limit = 25``.
        offset (int): Displacement. Result from which it is returned. By default
            ``offset = 0``.
        query (string): Query to filter the results.
        orderby (string): Field by which to sort the results.

    Examples:
        >>> get_structuralresources_category_schemes_agency_resource(
        ...     "ISTAC",
        ...     "TEMAS_CANARIAS"
        ... )
    """
    path = os.path.join('categoryschemes', agencyid, resourceid)
    url = services.build_entrypoint_url(
        API, path, limit=limit, offset=offset, query=query, orderBy=orderby
    )
    return services.get_content(url)


def get_structuralresources_category_schemes_agency_resource_version(
    agencyid, resourceid, version
):
    """Get category schemes agency resource version

    This function returns the content from
    ``/v1.0/categoryschemes/{agencyID}/{resourceID}/{version}``

    Args:
        agencyid (string): Identifier of the agency that publishes.
        resourceid (string): Resource identifier.
        version (string): Specific version of the resource.

    Examples:
        >>> get_structuralresources_category_schemes_agency_resource_version(
        ...     "ISTAC",
        ...     "TEMAS_CANARIAS",
        ...     "01.000"
        ... )
    """
    path = os.path.join('categoryschemes', agencyid, resourceid, version)
    url = services.build_entrypoint_url(API, path)
    return services.get_content(url)


def get_structuralresources_category_schemes_agency_resource_version_categories(
    agencyid, resourceid, version, limit=25, offset=0, query='', orderby=''
):
    """Get category schemes agency resource version categories

    This function returns the content from
    ``/v1.0/categoryschemes/{agencyID}/{resourceID}/{version}/categories``

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
        >>> get_structuralresources_category_schemes_agency_resource_version_categories(
        ...     "ISTAC",
        ...     "TEMAS_CANARIAS",
        ...     "01.000"
        ... )
    """
    path = os.path.join('categoryschemes', agencyid, resourceid, version, 'categories')
    url = services.build_entrypoint_url(
        API, path, limit=limit, offset=offset, query=query, orderBy=orderby
    )
    return services.get_content(url)


def get_structuralresources_category_schemes_agency_resource_version_categories_id(
    agencyid, resourceid, version, categoryid
):
    """Get category schemes agency resource version categories (id)

    This function returns the content from
    ``/v1.0/categoryschemes/{agencyID}/{resourceID}/{version}/categories/{categoryID}``

    Args:
        agencyid (string): Identifier of the agency that publishes.
        resourceid (string): Resource identifier.
        version (string): Specific version of the resource.
        categoryid (string): category identifier

    Examples:
        >>> get_structuralresources_category_schemes_agency_resource_version_categories_id(
        ...     "ISTAC",
        ...     "TEMAS_CANARIAS",
        ...     "01.000",
        ...     "060"
        ... )
        >>> get_structuralresources_category_schemes_agency_resource_version_categories_id(
        ...     "ISTAC",
        ...     "TEMAS_CANARIAS",
        ...     "01.000",
        ...     "060.060_010.060_010_010"
        ... )
    """
    path = os.path.join(
        'categoryschemes', agencyid, resourceid, version, 'categories', categoryid
    )
    url = services.build_entrypoint_url(API, path)
    return services.get_content(url)
