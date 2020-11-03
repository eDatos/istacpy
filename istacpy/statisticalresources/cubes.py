import os

from istacpy import services

API = 'statistical-resources'


def get_statisticalresources_datasets(lang='es', limit=25, offset=0, orderby='', query=''):
    """Get datasets

    This function allows consulting all existing statistical data cubes.

    Args:
        lang (string): Language in which you want to get the answer.
        limit (int): Results limit. By default ``limit=25``.
        offset (int): Displacement. Result from which it is returned. By default
            ``offset=0``.
        orderby (string): Order. Possible values are ``ID ASC`` or ``ID DESC``,
        query (string): Metadata query on which the searches can be built.

    Examples:
        >>> get_statisticalresources_datasets()
    """
    path = 'datasets'
    url = services.build_entrypoint_url(
        API, path, lang=lang, limit=limit, offset=offset, orderBy=orderby, query=query
    )
    return services.get_content(url)


def get_statisticalresources_datasets_agency(
    agencyid, lang='es', limit=25, offset=0, orderby='', query=''
):
    """Get datasets (agencyID)

    This function allows to consult all the data sets maintained by a certain organization.

    Args:
        agencyid (string): Identifier of the maintainer organization of the resource.
            A possible value is ``ISTAC``.
        lang (string): Language in which you want to get the answer.
        limit (int): Results limit. By default ``limit=25``.
        offset (int): Displacement. Result from which it is returned. By default
            ``offset=0``.
        orderby (string): Order. Possible values are ``ID ASC`` or ``ID DESC``,
        query (string): Metadata query on which the searches can be built.

    Examples:
        >>> get_statisticalresources_datasets_agency(agencyid="ISTAC")
    """
    path = os.path.join('datasets', agencyid)
    url = services.build_entrypoint_url(
        API, path, lang=lang, limit=limit, offset=offset, orderBy=orderby, query=query
    )
    return services.get_content(url)


def get_statisticalresources_datasets_agency_resource(
    agencyid, resourceid, lang='es', limit=25, offset=0, orderby='', query=''
):
    """Get datasets (agencyID / resourceID)

    This function allows to obtain all the versions of a statistical cube with a certain
    identifier and that also maintains a certain organization.

    Args:
        agencyid (string): Identifier of the maintainer organization of the resource.
            A possible value is ``ISTAC``.
        resourceid (string): Resource identifier. A possible value is ``C00010A_000002``.
        lang (string): Language in which you want to get the answer.
        limit (int): Results limit. By default ``limit=25``.
        offset (int): Displacement. Result from which it is returned. By default
            ``offset=0``.
        orderby (string): Order. Possible values are ``ID ASC`` or ``ID DESC``,
        query (string): Metadata query on which the searches can be built.

    Examples:
        >>> get_statisticalresources_datasets_agency_resource(
        ...     agencyid="ISTAC",
        ...     resourceid="C00010A_000002"
        ... )

    """
    path = os.path.join('datasets', agencyid, resourceid)
    url = services.build_entrypoint_url(
        API, path, lang=lang, limit=limit, offset=offset, orderBy=orderby, query=query
    )
    return services.get_content(url)


def get_statisticalresources_datasets_agency_resource_version(
    agencyid, resourceid, version, dim='', fields='', lang='es'
):
    """Get datasets (agencyID / resourceID / version)

    This function allows to obtain all the versions of a statistical cube with a certain
    identifier and that also maintains a certain organization.

    Args:
        agencyid (string): Identifier of the maintainer organization of the resource.
            A possible value is ``ISTAC``.
        resourceid (string): Resource identifier. A possible value is ``C00010A_000002``.
        version (string): Resource version. A possible value is ``001.000``.
        dim (string): Allows filtering the data obtained in the response. A example is
            ``TIME_PERIOD:2009|2010``.
        fields (string): Allows you to customize the response by excluding fields from it.
            The possible values are ``-metadata`` and ``-data``.
        lang (string): Language in which you want to get the answer.

    Examples:
        >>> get_statisticalresources_datasets_agency_resource_version(
        ...     agencyid="ISTAC",
        ...     resourceid="C00010A_000002",
        ...     version="001.000"
        ... )
    """
    path = os.path.join('datasets', agencyid, resourceid, version)
    url = services.build_entrypoint_url(API, path, dim=dim, fields=fields, lang=lang)
    return services.get_content(url)
