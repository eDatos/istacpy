from istacpy.resources import *


# Instituto Canario de Estadística (ISTAC)

# @title Get codelist families
# @description This function returns the list of families of classifications
# @param limit (int) Results limit. By default \code{limit=25}.
# @param offset (int) Displacement. Result from which it is returned.  By default \code{offset=0}.
# @param orderby (string) Field by which to sort the results.
# @param query (string) Query to filter the results.
# @examples
# get_codelist_families()
def get_codelist_families(limit=25, offset=0, orderby="", query=""):
    # Parse orderby
    if orderby is not None:
        orderby = parse_param(orderby)

    # Parse query
    if query is not None:
        query = parse_param(query)

    # Build URL
    api = "structural-resources"
    path = "codelistfamilies" + ".json"
    params = "?limit=" + str(limit) + "&offset=" + str(offset) + "&orderby=" + orderby + "&query=" + query
    path = path + params
    url = get_url(api, path)

    # Get content
    content = get_content(url)

    return content


# @title Get codelist families
# @description This function allows to obtain a family of classifications in particular.
# @param id (string) codelist family identificator
# @examples
# get_codelist_families_id()
def get_codelist_families_id(id=""):
    # Build URL
    api = "structural-resources"
    path = "codelistfamilies"
    resource = id + ".json"
    url = get_url(api, path, resource)

    # Get content
    content = get_content(url)

    return content


# @title Get codelists
# @description This function allows to obtain the list of classifications.
# @param limit (int) Results limit. By default \code{limit=25}.
# @param offset (int) Displacement. Result from which it is returned.  By default \code{offset=0}.
# @param query (string) Query to filter the results.
# @param orderby (string) Field by which to sort the results.
# @examples
# get_codelists()
def get_codelists(limit=25, offset=0, query="", orderby=""):
    # Parse query
    if query is not None:
        query = parse_param(query)

    # Parse orderby
    if orderby is not None:
        orderby = parse_param(orderby)

    # Build URL
    api = "structural-resources"
    path = "codelists" + ".json"
    params = "?limit=" + str(limit) + "&offset=" + str(offset) + "&query=" + query + "&orderby=" + orderby
    path = path + params
    url = get_url(api, path)

    # Get content
    content = get_content(url)

    return content


# @title Get codelists agency
# @description This function allows obtaining the list of all the classifications
#  maintained by a certain organization.
# @param agencyid (string) Agency identificator.
# @param limit (int) Results limit. By default \code{limit=25}.
# @param offset (int) Displacement. Result from which it is returned.  By default \code{offset=0}.
# @param query (string) Query to filter the results.
# @param orderby (string) Field by which to sort the results.
# @examples
# get_codelists_agency("ISTAC")
# get_codelists_agency("ESTAT")
def get_codelists_agency(agencyid, limit=25, offset=0, query="", orderby=""):
    # Parse query
    if query is not None:
        query = parse_param(query)

    # Parse orderby
    if orderby is not None:
        orderby = parse_param(orderby)

    # Build URL
    api = "structural-resources"
    path = "codelists"
    resource = agencyid + ".json"
    params = "?limit=" + str(limit) + "&offset=" + str(offset) + "&query=" + query + "&orderby=" + orderby
    resource = resource + params
    url = get_url(api, path, resource)

    # Get content
    content = get_content(url)

    return content


# @title Get codelists agency resource
# @description This function allows to obtain all the versions of a
#  classification with a certain identifier and that is also kept by a
#  certain organization.
# @param agencyid (string) Agency identificator.
# @param resourceid (string) Resource identificator.
# @param limit (int) Results limit. By default \code{limit=25}.
# @param offset (int) Displacement. Result from which it is returned.  By default \code{offset=0}.
# @param query (string) Query to filter the results.
# @param orderby (string) Field by which to sort the results.
# @examples
# get_codelists_agency_resource("ISTAC", "CL_AREA_ES")
def get_codelists_agency_resource(agencyid, resourceid, limit=25, offset=0, query="", orderby=""):
    # Parse query
    if query is not None:
        query = parse_param(query)

    # Parse orderby
    if orderby is not None:
        orderby = parse_param(orderby)

    # Build URL
    api = "structural-resources"
    path = "codelists"
    resource = agencyid + "/" + resourceid + ".json"
    params = "?limit=" + str(limit) + "&offset=" + str(offset) + "&query=" + query + "&orderby=" + orderby
    resource = resource + params
    url = get_url(api, path, resource)

    # Get Content
    content = get_content(url)

    return content


# @title Get codelists agency resource version
# @description This function allows you to consult a particular version of a classification.
# @param agencyid (string) Agency identificator.
# @param resourceid (string) Resource identificator.
# @param version (string) Specific resource version.
# @examples
# get_codelists_agency_resource_version("ISTAC", "CL_AREA_ES", "01.000")
def get_codelists_agency_resource_version(agencyid, resourceid, version):
    # Build URL
    api = "structural-resources"
    path = "codelists"
    resource = agencyid + "/" + resourceid + "/" + version + ".json"
    url = get_url(api, path, resource)

    # Get content
    content = get_content(url)

    return content


# @title Get codelists agency resource version codes
# @description This function allows to consult the codes of a version of a
#  classification. Note that if wildcards are used as \code{~all} or one of the
#  \code{limit}, \code{offset}, \code{query} or \code{orderby} parameters,
#  the list will be automatically paginated.
# @param agencyid (string) Agency identificator.
# @param resourceid (string) Resource identificator.
# @param version (string) Specific resource version.
# @param limit (int) Results limit. By default \code{limit=25}.
# @param offset (int) Displacement. Result from which it is returned.  By default \code{offset=0}.
# @param query (string) Query to filter the results.
# @param orderby (string) Field by which to sort the results.
# @param openness (string) Opening established for viewing.
# @param order (string) Order established for visualization.
# @param fields (string) Additional fields that you want to show in the answer.
# @examples
# get_codelists_agency_resource_version_codes("ISTAC", "CL_AREA_ES", "01.000")
def get_codelists_agency_resource_version_codes(agencyid, resourceid, version, limit=25, offset=0, query="", orderby="",
                                                openness="", order="", fields=""):
    # Parse query
    if query is not None:
        query = parse_param(query)

    # Parse orderby
    if orderby is not None:
        orderby = parse_param(orderby)

    # Parse fields
    if fields is not None:
        fields = parse_param(fields)

    # Build URL
    api = "structural-resources"
    path = "codelists"
    resource = agencyid + "/" + resourceid + "/" + version + "/codes" + ".json"
    params = "?limit=" + str(limit) + "&offset=" + str(offset) + "&query=" + query + "&orderby=" + orderby + \
             "&openness=" + openness + "&order=" + order + "&fields=" + fields
    resource = resource + params
    url = get_url(api, path, resource)

    # Get content
    content = get_content(url)

    return content


# @title Get codelists agency resource version codes (codeid)
# @description This function allows to consult a specific code of a version of a classification.
# @param agencyid (string) Agency identificator.
# @param resourceid (string) Resource identificator.
# @param version (string) Specific resource version.
# @param codeid (string) Code identificator.
# @examples
# get_codelists_agency_resource_version_codes_codeid("ISTAC", "CL_AREA_ES", "01.000", "ES706A01")
def get_codelists_agency_resource_version_codes_codeid(agencyid, resourceid, version, codeid):
    # Build URL
    api = "structural-resources"
    path = "codelists"
    resource = agencyid + "/" + resourceid + "/" + version + "/codes/" + codeid + ".json"
    url = get_url(api, path, resource)

    # Get content
    content = get_content(url)

    return content
