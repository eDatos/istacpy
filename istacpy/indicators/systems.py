from istacpy.resources import *


# @title Get indicators systems
# @description This function returns a list of indicator systems published in
#  the ISTAC-indicators database. The indicators are simple or compound
#  statistics, however a single indicator can rarely provide useful
#  information about complex phenomena such as the economic situation,
#  living conditions, schooling or others. Indicator systems are generally
#  designed to generate more and more accurate information about the
#  conditions of a phenomenon; and for this they are organized in dimensions
#  or areas of analysis, under which the indicators are integrated.
# @param limit (int) Results limit. By default \code{limit = 25}.
# @param offset (int) Displacement. Result from which it is returned. By default \code{offset = 0}.
# @examples
# get_indicators_systems()
def get_indicators_systems(limit=25, offset=0):
    # Build URL
    api = "indicators"
    path = "indicatorsSystems"

    path = path + "?limit=" + str(limit) + "&offset=" + str(offset)
    url = get_url(api, path)

    # Get content
    content = get_content(url)

    return content


# @title Get indicators system code
# @description This function returns metadata of a system of indicators
#  published in the ISTAC-indicators database. The indicators are simple or
#  compound statistics, however a single indicator can rarely provide useful
#  information about complex phenomena such as the economic situation, living
#  conditions, schooling or others.
# @param indicatorsystemcode (string) an indicator system code
# @examples
# get_indicators_systems_code("C00075H")
def get_indicators_systems_code(indicatorsystemcode):
    # Build URL
    api = "indicators"
    path = "indicatorsSystems"
    resource = indicatorsystemcode
    url = get_url(api, path, resource)

    # Get content
    content = get_content(url)

    return content


# @title Get indicators system code instances
# @description This function returns instances of indicators associated
#  with a specific indicator system. An instance of an indicator is nothing
#  more than a spatio-temporal query of an indicator when it is incorporated
#  into a specific indicator system.
# @param indicatorsystemcode (string) with an indicator system code
# @param q (string) Query of metadata on which the searches can be built are:
#  \code{id} and \code{geographicalValue}.
# @param order (string) Order. Possible values are: \code{update} and
#   \code{id} and order criteria are \code{ASC} and \code{DESC}.
# @param limit (int) Results limit. By default \code{limit = 25}.
# @param offset (int) Displacement. Result from which it is returned.  By default \code{offset = 0}.
# @param fields (string) Use of the answer by adding new fields.
#  Possible values are: \code{+metadata}, \code{+data} and \code{+observationsMetadata}.
# @param representation (string) Allows filtering the observations by their value.
#  Its use only makes sense when \code{+data} and/or \code{+observationsMetadata} has been included.
# @param granularity (string) Allows to filter the observations through the
#  granularities of the same. Its use only makes sense when \code{+data} and/or
#  \code{+observationsMetadata} has been included.
# @examples
# get_indicators_systems_code_instances("C00075H")
# get_indicators_systems_code_instances("C00075H", q = 'id EQ "INDICADORES_MUNICIPALES"')
def get_indicators_systems_code_instances(indicatorsystemcode, q="", order="", limit=25, offset=0, fields="",
                                          representation="", granularity=""):
    # Parse order
    if order is not None:
        order = parse_param(order)

    # Parse fields
    if fields is not None:
        fields = parse_param(fields)

    # Parse representation
    if representation is not None:
        representation = parse_param(representation)

    # Parse granularity
    if granularity is not None:
        granularity = parse_param(granularity)

    # Build URL
    api = "indicators"
    path = "indicatorsSystems"
    resource = indicatorsystemcode + "/indicatorsInstances"
    if q is not None:
        q = parse_param(q)
        params = "?q=" + q + "&order=" + order + "&limit=" + str(limit) + "&offset=" + str(
            offset) + "&fields=" + fields + "&representation=" + representation + "&granularity=" + granularity
    else:
        params = "?order=" + order + "&limit=" + str(limit) + "&offset=" + str(
            offset) + "&fields=" + fields + "&representation=" + representation + "&granularity=" + granularity

    resource = resource + params
    url = get_url(api, path, resource)

    # Get content
    content = get_content(url)

    return content


# @title Get indicators system code instances code
# @description This function returns metadata of an indicator set associated
#  with a specific indicator system. An instance of an indicator is nothing
#  more than a spatio-temporal query of an indicator when it is incorporated
#  into a specific indicator system.
# @param indicatorsystemcode (string) indicator system code
# @param indicatorinstancecode (string) indicator instance code
# @examples
# get_indicators_systems_code_instances_code("C00075H", "21af0477-d63b-493b-ad02-4ab181547223")
def get_indicators_systems_code_instances_code(indicatorsystemcode, indicatorinstancecode):
    # Build URL
    api = "indicators"
    path = "indicatorsSystems"
    resource = indicatorsystemcode + "/indicatorsInstances/" + indicatorinstancecode
    url = get_url(api, path, resource)

    # Get content
    content = get_content(url)

    return content


# @title Get indicators system code instances code data
# @description This function returns data of an indicator unit associated with
#  a specific indicator system. An instance of an indicator is nothing more
#  than a spatio-temporal query of an indicator when it is incorporated into
#  a specific indicator system.
# @param indicatorsystemcode (string) Indicator system code
# @param indicatorinstancecode (string) Indicator instance code
# @param representation (string) Allows filtering the observations by their value.
# @param granularity (string) Allows to filter the observations through the granularities of the same.
# @param fields (string) Allows you to customize the response by excluding fields. The possible values are:
#  \code{-observationsMetadata}.
# @examples
# get_indicators_systems_code_instances_code_data("C00075H", "21af0477-d63b-493b-ad02-4ab181547223")
# get_indicators_systems_code_instances_code_data("C00075H", "21af0477-d63b-493b-ad02-4ab181547223",
#   granularity = "GEOGRAPHICAL[MUNICIPALITIES]")
def get_indicators_systems_code_instances_code_data(indicatorsystemcode, indicatorinstancecode, representation="",
                                                    granularity="", fields=""):
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
    path = "indicatorsSystems"
    resource = indicatorsystemcode + "/indicatorsInstances/" + indicatorinstancecode + "/data"
    params = "?representation=" + representation + "&granularity=" + granularity + "&fields=" + fields
    resource = resource + params
    url = get_url(api, path, resource)

    # Get content
    content = get_content(url)

    return content
