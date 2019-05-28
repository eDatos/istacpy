from istacpy.resources import resources


def get_structuralresources_codelist_families(limit=25, offset=0, orderby=None, query=None):
    """Get codelist families

    This function returns the list of families of classifications

    Args:
        limit (int): Results limit. By default ``limit = 25``.
        offset (int): Displacement. Result from which it is returned.  By default ``offset = 0``.
        orderby (string): Field by which to sort the results.
        query (string): Query to filter the results.

    Examples:
        >>> get_structuralresources_codelist_families()
    """
    # Parse orderby
    orderby = resources.parse_param(orderby)

    # Parse query
    query = resources.parse_param(query)

    # Build URL
    api = "structural-resources"
    path = "codelistfamilies" + ".json"
    params = "?limit=" + str(limit) + "&offset=" + str(offset) + "&orderby=" + orderby + "&query=" + query
    path = path + params
    url = resources.get_url(api, path)

    # Get content
    content = resources.get_content(url)

    return content


def get_structuralresources_codelist_families_id(id=None):
    """Get codelist families

    This function allows to obtain a family of classifications in particular.

    Args:
        id (string): codelist family identificator

    Examples:
        >>> get_structuralresources_codelist_families_id()
    """
    # Build URL
    api = "structural-resources"
    path = "codelistfamilies"
    resource = id + ".json"
    url = resources.get_url(api, path, resource)

    # Get content
    content = resources.get_content(url)

    return content


def get_structuralresources_codelists(limit=25, offset=0, query=None, orderby=None):
    """Get codelists

    This function allows to obtain the list of classifications.

    Args:
        limit (int): Results limit. By default ``limit = 25``.
        offset (int): Displacement. Result from which it is returned.  By default ``offset = 0``.
        query (string): Query to filter the results.
        orderby (string): Field by which to sort the results.

    Examples:
         >>> get_structuralresources_codelists()
    """
    # Parse query
    query = resources.parse_param(query)

    # Parse orderby
    orderby = resources.parse_param(orderby)

    # Build URL
    api = "structural-resources"
    path = "codelists" + ".json"
    params = "?limit=" + str(limit) + "&offset=" + str(offset) + "&query=" + query + "&orderby=" + orderby
    path = path + params
    url = resources.get_url(api, path)

    # Get content
    content = resources.get_content(url)

    return content


def get_structuralresources_codelists_agency(agencyid, limit=25, offset=0, query=None, orderby=None):
    """Get codelists agency

    This function allows obtaining the list of all the classifications maintained by a certain organization.

    Args:
        agencyid (string): Agency identificator.
        limit (int): Results limit. By default ``limit = 25``.
        offset (int): Displacement. Result from which it is returned.  By default ``offset = 0``.
        query (string): Query to filter the results.
        orderby (string): Field by which to sort the results.

    Examples:
        >>> get_structuralresources_codelists_agency("ISTAC")
        >>> get_structuralresources_codelists_agency("ESTAT")
    """
    # Parse query
    query = resources.parse_param(query)

    # Parse orderby
    orderby = resources.parse_param(orderby)

    # Build URL
    api = "structural-resources"
    path = "codelists"
    resource = agencyid + ".json"
    params = "?limit=" + str(limit) + "&offset=" + str(offset) + "&query=" + query + "&orderby=" + orderby
    resource = resource + params
    url = resources.get_url(api, path, resource)

    # Get content
    content = resources.get_content(url)

    return content


def get_structuralresources_codelists_agency_resource(agencyid, resourceid, limit=25, offset=0, query=None,
                                                      orderby=None):
    """Get codelists agency resource

    This function allows to obtain all the versions of a classification with a certain identifier and that is also kept
    by a certain organization.

    Args:
        agencyid (string): Agency identificator.
        resourceid (string): Resource identificator.
        limit (int): Results limit. By default ``limit = 25``.
        offset (int): Displacement. Result from which it is returned.  By default ``offset = 0``.
        query (string): Query to filter the results.
        orderby (string): Field by which to sort the results.

    Examples:
        >>> get_structuralresources_codelists_agency_resource("ISTAC", "CL_AREA_ES")
    """
    # Parse query
    query = resources.parse_param(query)

    # Parse orderby
    orderby = resources.parse_param(orderby)

    # Build URL
    api = "structural-resources"
    path = "codelists"
    resource = agencyid + "/" + resourceid + ".json"
    params = "?limit=" + str(limit) + "&offset=" + str(offset) + "&query=" + query + "&orderby=" + orderby
    resource = resource + params
    url = resources.get_url(api, path, resource)

    # Get Content
    content = resources.get_content(url)

    return content


def get_structuralresources_codelists_agency_resource_version(agencyid, resourceid, version):
    """Get codelists agency resource version

    This function allows you to consult a particular version of a classification.

    Args:
        agencyid (string): Agency identificator.
        resourceid (string): Resource identificator.
        version (string): Specific resource version.

    Examples:
        >>> get_structuralresources_codelists_agency_resource_version("ISTAC", "CL_AREA_ES", "01.000")
    """
    # Build URL
    api = "structural-resources"
    path = "codelists"
    resource = agencyid + "/" + resourceid + "/" + version + ".json"
    url = resources.get_url(api, path, resource)

    # Get content
    content = resources.get_content(url)

    return content


def get_structuralresources_codelists_agency_resource_version_codes(agencyid, resourceid, version, limit=25, offset=0,
                                                                    query=None, orderby=None, openness=None, order=None,
                                                                    fields=None):
    """Get codelists agency resource version codes

    This function allows to consult the codes of a version of a classification. Note that if wildcards are used
    as ``~all`` or one of the ``limit``, ``offset``, ``query`` or ``orderBy`` parameters,
    the list will be automatically paginated.

    Args:
        agencyid (string): Agency identificator.
        resourceid (string): Resource identificator.
        version (string): Specific resource version.
        limit (int): Results limit. By default ``limit = 25``.
        offset (int): Displacement. Result from which it is returned.  By default ``offset = 0``.
        query (string): Query to filter the results.
        orderby (string): Field by which to sort the results.
        openness (string): Opening established for viewing.
        order (string): Order established for visualization.
        fields (string): Additional fields that you want to show in the answer.

    Examples:
        >>> get_structuralresources_codelists_agency_resource_version_codes("ISTAC", "CL_AREA_ES", "01.000")
    """
    # Parse query
    query = resources.parse_param(query)

    # Parse orderby
    orderby = resources.parse_param(orderby)

    # Parse fields
    fields = resources.parse_param(fields)

    # Build URL
    api = "structural-resources"
    path = "codelists"
    resource = agencyid + "/" + resourceid + "/" + version + "/codes" + ".json"
    params = "?limit=" + str(limit) + "&offset=" + str(offset) + "&query=" + query + "&orderby=" + orderby + \
             "&openness=" + openness + "&order=" + order + "&fields=" + fields
    resource = resource + params
    url = resources.get_url(api, path, resource)

    # Get content
    content = resources.get_content(url)

    return content


def get_structuralresources_codelists_agency_resource_version_codes_codeid(agencyid, resourceid, version, codeid):
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
    # Build URL
    api = "structural-resources"
    path = "codelists"
    resource = agencyid + "/" + resourceid + "/" + version + "/codes/" + codeid + ".json"
    url = resources.get_url(api, path, resource)

    # Get content
    content = resources.get_content(url)

    return content
