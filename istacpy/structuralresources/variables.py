import os

from istacpy import services


def get_structuralresources_variable_families(limit=25, offset=0, query='', orderby=''):
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
    api = 'structural-resources'
    path = 'variablefamilies'
    url = services.build_entrypoint_url(
        api, path, limit=limit, offset=offset, query=query, orderBy=orderby
    )
    return services.get_content(url)


def get_structuralresources_variable_families_id(id):
    """Get variable families (id)

    This function returns data from ``/v1.0/variablefamilies/{id}``

    Args:
        id (string): Variable family identificator.

    Examples:
        >>> get_structuralresources_variable_families_id("VRF_DEMOGRAFICAS")
    """
    api = 'structural-resources'
    path = os.path.join('variablefamilies', id)
    url = services.build_entrypoint_url(api, path)
    return services.get_content(url)


def get_structuralresources_variable_families_id_variables(
    id, limit=25, offset=0, query='', orderby=''
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
    api = 'structural-resources'
    path = os.path.join('variablefamilies', id, 'variables')
    url = services.build_entrypoint_url(
        api, path, limit=limit, offset=offset, query=query, orderBy=orderby
    )
    return services.get_content(url)


def get_structuralresources_variables(limit=25, offset=0, query='', orderby=''):
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
    api = 'structural-resources'
    path = 'variables'
    url = services.build_entrypoint_url(
        api, path, limit=limit, offset=offset, query=query, orderBy=orderby
    )
    return services.get_content(url)


def get_structuralresources_variables_id(id):
    """Get variables (id)

    This function returns data from ``/v1.0/variables/{id}``

    Args:
        id (string): Variable identifier.

    Examples:
      >>> get_structuralresources_variables_id("VR_SEXO")
    """
    api = 'structural-resources'
    path = os.path.join('variables', id)
    url = services.build_entrypoint_url(api, path)
    return services.get_content(url)


def get_structuralresources_variableelements(
    variableid, limit=25, offset=0, query='', orderby=''
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
    api = 'structural-resources'
    path = os.path.join('variables', variableid, 'variableelements')
    url = services.build_entrypoint_url(
        api, path, limit=limit, offset=offset, query=query, orderBy=orderby
    )
    return services.get_content(url)


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
    api = 'structural-resources'
    path = os.path.join('variables', variableid, 'variableelements', resourceid)
    url = services.build_entrypoint_url(api, path)
    return services.get_content(url)


def get_structuralresources_geoinfo(
    variableid, resourceid, fields='', limit=25, offset=0, query='', orderby=''
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
    api = 'structural-resources'
    path = os.path.join('variables', variableid, 'variableelements', resourceid, 'geoinfo')
    url = services.build_entrypoint_url(
        api, path, fields=fields, limit=limit, offset=offset, query=query, orderBy=orderby
    )
    return services.get_content(url)
