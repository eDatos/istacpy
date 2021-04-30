from istacpy import services

API = 'statistical-resources'


def get_statisticalresources_queries(lang='es', limit=25, offset=0, orderby='', query=''):
    """Get queries

    This function allows consulting all existing statistical queries.

    Args:
        lang (string): Language in which you want to get the answer.
        limit (int): Results limit. By default ``limit=25``.
        offset (int): Displacement. Result from which it is returned. By default
            ``offset=0``.
        orderby (string): Order. Possible values are ``ID ASC`` or ``ID DESC``,
        query (string): Metadata query on which the searches can be built.

    Examples:
        >>> get_statisticalresources_queries()
    """
    path = 'queries'
    url = services.build_entrypoint_url(
        API, path, lang=lang, limit=limit, offset=offset, orderBy=orderby, query=query
    )
    return services.get_content(url)


def get_statisticalresources_queries_agency(
    agencyid, lang='es', limit=25, offset=0, orderby='', query=''
):
    """Get queries (agencyID)

    This function allows to consult all the queries maintained by a certain organization.

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
        >>> get_statisticalresources_queries_agency(agencyid="ISTAC")
    """
    path = '/'.join(['queries', agencyid])
    url = services.build_entrypoint_url(
        API, path, lang=lang, limit=limit, offset=offset, orderBy=orderby, query=query
    )
    return services.get_content(url)


def get_statisticalresources_queries_agency_resource(
    agencyid,
    resourceid,
    fields='',
    lang='es',
    as_dataframe=False,
):
    """Get queries (agencyID / resourceID)

    This function allows to obtain final data of a statistical query with a certain
    identifier and that also maintains a certain organization.

    Args:
        agencyid (string): Identifier of the maintainer organization of the resource.
            A possible value is ``ISTAC``.
        resourceid (string): Resource identifier. A possible value is ``C00010A_000002``.
        fields (string): Allows you to customize the response by excluding fields from it.
            The possible values are ``-metadata`` and ``-data``.
        lang (string): Language in which you want to get the answer.
        as_dataframe (bool): If True, this function returns a namedtuple with:
          - dataframe: pandas dataframe built from API response.
          - codelists: mapping between codes and representations for each column.

    Examples:
        >>> get_statisticalresources_queries_agency_resource(
        ...     agencyid="ISTAC",
        ...     resourceid="C00017A_000001"
        ... )

    """
    path = '/'.join(['queries', agencyid, resourceid])
    url = services.build_entrypoint_url(API, path, fields=fields, lang=lang)
    api_response = services.get_content(url)
    if as_dataframe:
        return services.build_resolved_api_response(api_response)
    else:
        return api_response
