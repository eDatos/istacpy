import os

from istacpy import services

API = 'structural-resources'


def get_structuralresources_codelist_families(limit=25, offset=0, orderby='', query=''):
    """Get codelist families

    This function returns the list of families of classifications

    Args:
        limit (int): Results limit. By default ``limit = 25``.
        offset (int): Displacement. Result from which it is returned. By default
            ``offset = 0``.
        orderby (string): Field by which to sort the results.
        query (string): Query to filter the results.

    Examples:
        >>> get_structuralresources_codelist_families()
    """
    path = 'codelistfamilies'
    url = services.build_entrypoint_url(
        API, path, limit=limit, offset=offset, orderBy=orderby, query=query
    )
    return services.get_content(url)


def get_structuralresources_codelist_families_id(id):
    """Get codelist families

    This function allows to obtain a family of classifications in particular.

    Args:
        id (string): codelist family identificator

    Examples:
        >>> get_structuralresources_codelist_families_id('CODELIST_ID')
    """
    path = os.path.join('codelistfamilies', id)
    url = services.build_entrypoint_url(API, path)
    return services.get_content(url)


def get_structuralresources_codelists(limit=25, offset=0, query='', orderby=''):
    """Get codelists

    This function allows to obtain the list of classifications.

    Args:
        limit (int): Results limit. By default ``limit = 25``.
        offset (int): Displacement. Result from which it is returned. By default
            ``offset = 0``.
        query (string): Query to filter the results.
        orderby (string): Field by which to sort the results.

    Examples:
         >>> get_structuralresources_codelists()
    """
    path = 'codelists'
    url = services.build_entrypoint_url(
        API, path, limit=limit, offset=offset, query=query, orderBy=orderby
    )
    return services.get_content(url)


def get_structuralresources_codelists_agency(
    agencyid, limit=25, offset=0, query='', orderby=''
):
    """Get codelists agency

    This function allows obtaining the list of all the classifications maintained by a
    certain organization.

    Args:
        agencyid (string): Agency identificator.
        limit (int): Results limit. By default ``limit = 25``.
        offset (int): Displacement. Result from which it is returned. By default
            ``offset = 0``.
        query (string): Query to filter the results.
        orderby (string): Field by which to sort the results.

    Examples:
        >>> get_structuralresources_codelists_agency("ISTAC")
        >>> get_structuralresources_codelists_agency("ESTAT")
    """
    path = os.path.join('codelists', agencyid)
    url = services.build_entrypoint_url(
        API, path, limit=limit, offset=offset, query=query, orderBy=orderby
    )
    return services.get_content(url)


def get_structuralresources_codelists_agency_resource(
    agencyid, resourceid, limit=25, offset=0, query='', orderby=''
):
    """Get codelists agency resource

    This function allows to obtain all the versions of a classification with a certain
    identifier and that is also kept by a certain organization.

    Args:
        agencyid (string): Agency identificator.
        resourceid (string): Resource identificator.
        limit (int): Results limit. By default ``limit = 25``.
        offset (int): Displacement. Result from which it is returned. By default
            ``offset = 0``.
        query (string): Query to filter the results.
        orderby (string): Field by which to sort the results.

    Examples:
        >>> get_structuralresources_codelists_agency_resource("ISTAC", "CL_AREA_ES")
    """
    path = os.path.join('codelists', agencyid, resourceid)
    url = services.build_entrypoint_url(
        API, path, limit=limit, offset=offset, query=query, orderBy=orderby
    )
    return services.get_content(url)


def get_structuralresources_codelists_agency_resource_version(
    agencyid, resourceid, version
):
    """Get codelists agency resource version

    This function allows you to consult a particular version of a classification.

    Args:
        agencyid (string): Agency identificator.
        resourceid (string): Resource identificator.
        version (string): Specific resource version.

    Examples:
        >>> get_structuralresources_codelists_agency_resource_version(
        ...     "ISTAC",
        ...     "CL_AREA_ES",
        ...     "01.000"
        ... )
    """
    path = os.path.join('codelists', agencyid, resourceid, version)
    url = services.build_entrypoint_url(API, path)
    return services.get_content(url)


def get_structuralresources_codelists_agency_resource_version_codes(
    agencyid,
    resourceid,
    version,
    limit=25,
    offset=0,
    query='',
    orderby='',
    openness='',
    order='',
    fields='',
):
    """Get codelists agency resource version codes

    This function allows to consult the codes of a version of a classification. Note that
    if wildcards are used as ``~all`` or one of the ``limit``, ``offset``, ``query`` or
    ``orderBy`` parameters, the list will be automatically paginated.

    Args:
        agencyid (string): Agency identificator.
        resourceid (string): Resource identificator.
        version (string): Specific resource version.
        limit (int): Results limit. By default ``limit = 25``.
        offset (int): Displacement. Result from which it is returned. By default
            ``offset = 0``.
        query (string): Query to filter the results.
        orderby (string): Field by which to sort the results.
        openness (string): Opening established for viewing.
        order (string): Order established for visualization.
        fields (string): Additional fields that you want to show in the answer.

    Examples:
        >>> get_structuralresources_codelists_agency_resource_version_codes(
        ...     "ISTAC",
        ...     "CL_AREA_ES",
        ...     "01.000"
        ... )
    """
    path = os.path.join('codelists', agencyid, resourceid, version, 'codes')
    url = services.build_entrypoint_url(
        API,
        path,
        limit=limit,
        offset=offset,
        query=query,
        orderBy=orderby,
        openness=openness,
        order=order,
        fields=fields,
    )
    return services.get_content(url)


def get_structuralresources_codelists_agency_resource_version_codes_codeid(
    agencyid, resourceid, version, codeid
):
    """Get codelists agency resource version codes (codeID)

    This function allows to consult a specific code of a version of a classification.

    Args:
        agencyid (string): Agency identificator.
        resourceid (string): Resource identificator.
        version (string): Specific resource version.
        codeid (string): Code identificator.

    Examples:
        >>> get_structuralresources_codelists_agency_resource_version_codes_codeid(
            "ISTAC", "CL_AREA_ES", "01.000", "ES706A01")
    """
    path = os.path.join('codelists', agencyid, resourceid, version, 'codes', codeid)
    url = services.build_entrypoint_url(API, path)
    return services.get_content(url)
