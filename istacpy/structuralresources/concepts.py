import os

from istacpy import services

API = 'structural-resources'


def get_structuralresources_concept_types():
    """Get concept types

    This function returns the content from ``/v1.0/conceptTypes``

    Examples:
        >>> get_structuralresources_concept_types()
    """
    path = 'conceptTypes'
    url = services.build_entrypoint_url(API, path)
    return services.get_content(url)


def get_structuralresources_concept_schemes(limit=25, offset=0, query='', orderby=''):
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
    path = 'conceptschemes'
    url = services.build_entrypoint_url(
        API, path, limit=limit, offset=offset, query=query, orderBy=orderby
    )
    return services.get_content(url)


def get_structuralresources_concept_schemes_agency(
    agencyid, limit=25, offset=0, query='', orderby=''
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
    path = os.path.join('conceptschemes', agencyid)
    url = services.build_entrypoint_url(
        API, path, limit=limit, offset=offset, query=query, orderBy=orderby
    )
    return services.get_content(url)


def get_structuralresources_concept_schemes_agency_resource(
    agencyid, resourceid, limit=25, offset=0, query='', orderby=''
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
        ...     resourceid="CSM_C00010A_SIE"
        ... )
    """
    path = os.path.join('conceptschemes', agencyid, resourceid)
    url = services.build_entrypoint_url(
        API, path, limit=limit, offset=offset, query=query, orderBy=orderby
    )
    return services.get_content(url)


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
        ...     resourceid="CSM_C00010A_SIE",
        ...     version="01.000"
        ... )
    """
    path = os.path.join('conceptschemes', agencyid, resourceid, version)
    url = services.build_entrypoint_url(API, path)
    return services.get_content(url)


def get_structuralresources_concept_schemes_agency_resource_version_concepts(
    agencyid, resourceid, version, limit=25, offset=0, query='', orderby='', fields=''
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
        fields (string): Additional fields that you want to show in the answer.

    Examples:
        >>> get_structuralresources_concept_schemes_agency_resource_version_concepts(
        ...     agencyid="ISTAC",
        ...     resourceid="CSM_C00010A_SIE",
        ...     version="01.000"
        ... )
    """
    path = os.path.join('conceptschemes', agencyid, resourceid, version, 'concepts')
    url = services.build_entrypoint_url(
        API, path, limit=limit, offset=offset, query=query, orderBy=orderby, fields=fields
    )
    return services.get_content(url)


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
        ...     resourceid="CSM_C00010A_SIE",
        ...     version="01.000",
        ...     conceptID="ELECTORES"
        ... )
    """
    path = os.path.join(
        'conceptschemes', agencyid, resourceid, version, 'concepts', conceptid
    )
    url = services.build_entrypoint_url(API, path)
    return services.get_content(url)
