from istacpy.resources import *

#' @title Get variable families
#' @description This function returns data from /v1.0/variablefamilies
#' @param limit (int) Results limit. By default \code{limit = 25}.
#' @param offset (int) Displacement. Result from which it is returned.  By default \code{offset = 0}.
#' @param query (string) Query to filter the results.
#' @param orderBy (string) Field by which to sort the results.
#' @examples
#' get_variable_families()
def get_variable_families(limit = 25, offset = 0, query="", orderBy=""):

  # Parse query
  if query is not None:
    query = parse_param(query)

  # Parse orderBy
  if orderBy is not None:
    orderBy = parse_param(orderBy)

  # Build URL
  api =  "structural-resources"
  path = "variablefamilies" + ".json"
  params = "?limit=" + str(limit) + "&offset=" + str(offset) + "&query=" + query + "&orderBy=" + orderBy
  path = path + params
  url = get_url(api, path)

  # Get content
  content = get_content(url)

  return content

#' @title Get variable families (id)
#' @description This function returns data from /v1.0/variablefamilies/{id}
#' @param id (string) Variable family identificator.
#' @examples
#' get_variable_families_id("VRF_DEMOGRAFICAS")
def get_variable_families_id(id):

  # Build URL
  api =  "structural-resources"
  path = "variablefamilies"
  resource = id  + ".json"
  url = get_url(api, path, resource)

  # Get content
  content = get_content(url)

  return content

#' @title Get variable families (id) variables
#' @description This function returns data from /v1.0/variablefamilies/{id}/variables
#' @param id (string) Variable family identificator.
#' @param limit (int) Results limit. By default \code{limit = 25}.
#' @param offset (int) Displacement. Result from which it is returned.  By default \code{offset = 0}.
#' @param query (string) Query to filter the results.
#' @param orderBy (string) Field by which to sort the results.
#' @examples
#' get_variable_families_id_variables("VRF_DEMOGRAFICAS")
def get_variable_families_id_variables(id, limit = 25, offset = 0, query="", orderBy=""):

  # Parse query
  if query is not None:
    query = parse_param(query)

  # Parse orderBy
  if orderBy is not None:
    orderBy = parse_param(orderBy)

  # Build URL
  api =  "structural-resources"
  path = "variablefamilies"
  resource = id + "/variables" + ".json"
  params = "?limit=" + str(limit) + "&offset=" + str(offset) + "&query=" + query + "&orderBy=" + orderBy
  resource = resource + params
  url = get_url(api, path, resource)

  # Get content
  content = get_content(url)

  return content

#' @title Get variables
#' @description This function returns data from /v1.0/variables
#' @param limit (int) Results limit. By default \code{limit = 25}.
#' @param offset (int) Displacement. Result from which it is returned.  By default \code{offset = 0}.
#' @param query (string) Query to filter the results.
#' @param orderBy (string) Field by which to sort the results.
#' @examples
#' get_variables()
def get_variables(limit = 25, offset = 0, query="", orderBy=""):

  # Parse query
  if query is not None:
    query = parse_param(query)

  # Parse orderBy
  if orderBy is not None:
    orderBy = parse_param(orderBy)

  # Build URL
  api =  "structural-resources"
  path = "variables" + ".json"
  url = get_url(api, path)

  # Get content
  content = get_content(url)

  return content


#' @title Get variables (id)
#' @description This function returns data from /v1.0/variables/{id}
#' @param id (string) Variable identificator.
#' @examples
#' get_variables_id("VR_SEXO")
def get_variables_id(id):

  # Build URL
  api =  "structural-resources"
  path = "variables"
  resource = id + ".json"
  url = get_url(api, path, resource)

  # Get content
  content = get_content(url)

  return content

#' @title Get variableelements
#' @description This function returns data from /v1.0/variables/{variableID}/variableelements
#' @param variableID (string) Variable identificator.
#' @param limit (int) Results limit. By default \code{limit = 25}.
#' @param offset (int) Displacement. Result from which it is returned.  By default \code{offset = 0}.
#' @param query (string) Query to filter the results.
#' @param orderBy (string) Field by which to sort the results.
#' @examples
#' get_variableelements("VR_SEXO")
def get_variableelements(variableID, limit = 25, offset = 0, query="", orderBy=""):

  # Parse query
  if query is not None:
    query = parse_param(query)

  # Parse orderBy
  if orderBy is not None:
    orderBy = parse_param(orderBy)

  # Build URL
  api =  "structural-resources"
  path = "variables"
  resource = variableID + "/variableelements" + ".json"
  params = "?limit=" + str(limit) + "&offset=" + str(offset) + "&query=" + query + "&orderBy=" + orderBy
  resource = resource + params
  url = get_url(api, path, resource)

  # Get content
  content = get_content(url)

  return content


#' @title Get variableelements resource
#' @description This function returns data from /v1.0/variables/{variableID}/variableelements/{resourceID}
#' @param resourceID (string) Resource identificator.
#' @param variableID (string) Variable identificator.
#' @examples
#' get_variableelements_resource("VR_SEXO", "FEMALE")
#' get_variableelements_resource("VR_TERRITORIO", "CCAA_CANARIAS")
def get_variableelements_resource(variableID, resourceID):

  # Build URL
  api =  "structural-resources"
  path = "variables"
  resource = variableID + "/variableelements/" + resourceID + ".json"
  url = get_url(api, path, resource)

  # Get content
  content = get_content(url)

  return content

#' @title Get geoinfo
#' @description This function returns data from /v1.0/variables/{variableID}/variableelements/{resourceID}/geoinfo
#' @param variableID (string) Variable identificator.
#' @param resourceID (string) Resource identificator.
#' @param fields (string) Additional fields that you want to show in the answer.
#' @param limit (int) Results limit. By default \code{limit = 25}.
#' @param offset (int) Displacement. Result from which it is returned.  By default \code{offset = 0}.
#' @param query (string) Query to filter the results.
#' @param orderBy (string) Field by which to sort the results.
#' @examples
#' get_geoinfo("VR_TERRITORIO", "CCAA_CANARIAS")
def get_geoinfo(variableID, resourceID, fields="", limit = 25, offset = 0, query="", orderBy=""):

  # Parse fields
  if fields is not None:
    fields = parse_param(fields)

  # Parse query
  if query is not None:
    query = parse_param(query)

  # Parse orderBy
  if orderBy is not None:
    orderBy = parse_param(orderBy)

  # Build URL
  api =  "structural-resources"
  path = "variables"
  resource = variableID + "/variableelements/" + resourceID + "/geoinfo" + ".json"
  params = "?fields=" + fields + "&limit=" + str(limit) + "&offset=" + str(offset) + "&query=" + query + "&orderBy=" + orderBy
  resource = resource + params
  url = get_url(api, path, resource)

  # Get content
  content = get_content(url)

  return content

#print(get_geoinfo("VR_TERRITORIO", "CCAA_CANARIAS"))