from istacpy.resources import *


# @title Get indicators
# @description This function returns a list of indicators published in the
#  ISTAC-indicators database. An indicator is a measure used to know the
#  intensity of a phenomenon in spacetime. This measure can refer to
#  different spatial or temporal granularities.
# @title Get indicators
# @description This function returns a list of indicators published in the
#  ISTAC-indicators database. An indicator is a measure used to know the
#  intensity of a phenomenon in spacetime. This measure can refer to
#  different spatial or temporal granularities.
# @param q (string) Metadata query on which the searches can be built using:
#   \code{id}, \code{subjectCode} or \code{geographicValue}.
# @param order (string) Order. Possible values are: \code{update} and
#   \code{id} and order criteria are \code{ASC} and \code{DESC}.
# @param limit (int) Results limit. By default \code{limit = 25}.
# @param offset (int) Displacement. Result from which it is returned.  By default \code{offset = 0}.
# @param fields (string) Use of the answer by adding new fields.
#  Possible values are: \code{+metadata}, \code{+data} and \code{+observationsMetadata}.
# @param representation (string) Allows filtering the observations by their value.
#  Its use only makes sense when \code{+data} and/or \code{+observationsMetadata} has been included.
# @examples
# get_indicators()
# get_indicators(q = 'subjectCode EQ 051')
# get_indicators(q = 'id EQ "PARO_REGISTRADO"')
# get_indicators(q = 'id IN ("AFILIACIONES", "EMPLEO_REGISTRADO_AGRICULTURA")')
# get_indicators(q = 'id IN ("AFILIACIONES", "EMPLEO_REGISTRADO_AGRICULTURA")', order = "id ASC")
# get_indicators(q = 'id IN ("AFILIACIONES", "EMPLEO_REGISTRADO_AGRICULTURA")', order = "id ASC",
#  fields = "+metadata")
# get_indicators(q = 'id IN ("AFILIACIONES", "EMPLEO_REGISTRADO_AGRICULTURA")', order = "id ASC",
#  fields = "+data", representation = "GEOGRAPHICAL[35003|35005],MEASURE[ABSOLUTE]")
def get_indicators(q="", order="", limit=25, offset=0, fields="", representation=""):
    # URL params
    api = "indicators"
    path = "indicators"

    # Parse order
    if order is not None:
        order = parse_param(order)

    # Parse fields
    if fields is not None:
        fields = parse_param(fields)

    # Parse representation
    if representation is not None:
        representation = parse_param(representation)

    # Get indicators using query (q) parameter
    if q is not None:
        q = parse_param(q)
        params = "&order=" + order + "&limit=" + str(limit) + "&offset=" + str(
            offset) + "&fields=" + fields + "&representation=" + representation
        path = path + "?q=" + q + params
    else:
        params = "?order=" + order + "&limit=" + str(limit) + "&offset=" + str(
            offset) + "&fields=" + fields + "&representation=" + representation
        path = path + params

    # Get URL
    url = get_url(api, path)

    # Get content
    content = get_content(url)

    return content


# @title Get indicators code
# @description This function returns the metadata that describe the characteristics
#  of a specific indicator, allowing the compression of the measured fact;
#  also through the data request the complete data (for all spacetime) of the
#  indicator is provided.
# @param indicatorcode (string) an indicator code
# @examples
# get_indicators_code("AFILIACIONES")
# get_indicators_code("PARO_REGISTRADO")
def get_indicators_code(indicatorcode):
    # URL params
    api = "indicators"
    path = "indicators"

    # Get URL
    url = get_url(api, path, resource=indicatorcode)

    # Get content
    content = get_content(url)

    return content


# @title Get indicators code data
# @description This function returns complete data (for all spacetime) of the indicator.
#  On the other hand, metadata describing the characteristics of a specific
#  indicator are offered through the metadata request, allowing the compression
#  of the measured fact.
# @param indicatorCode (string) an indicator code
# @param representation (string) Allows filtering the observations by their value.
# @param granularity (string) Allows to filter the observations through the granularities of the same.
# @param fields (string) Allows you to customize the response by excluding fields.
#  The possible values are: \code{-observationsMetadata}.
# @examples
# get_indicators_code_data("AFILIACIONES")
# get_indicators_code_data("AFILIACIONES", representation =
#  "GEOGRAPHICAL[35003|35005],MEASURE[ABSOLUTE]")
# get_indicators_code_data("AFILIACIONES", granularity =
#  "GEOGRAPHICAL[MUNICIPALITIES]")
# get_indicators_code_data("AFILIACIONES", granularity =
#  "GEOGRAPHICAL[MUNICIPALITIES]", fields = "-observationsMetadata")
def get_indicators_code_data(indicatorcode, representation="", granularity="", fields=""):
    # Parse representation
    if representation is not None:
        representation = parse_param(representation)

    # Parse granularity
    if granularity is not None:
        granularity = parse_param(granularity)

    # Parse fields
    if fields is not None:
        fields = parse_param(fields)

    # Build URL
    api = "indicators"
    path = "indicators"
    resource = indicatorcode + "/data" + "?representation=" + representation + "&granularity=" + granularity + \
               "&fields=" + fields
    url = get_url(api, path, resource=resource)

    # Get content
    content = get_content(url)

    return content