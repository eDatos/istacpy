from istacpy.resources import *


# @title Get geographic granularities
# @description This function returns a list of geographic granularities treated
#  in the ISTAC-indicators database. For example provincial, insular or
#  municipal granularity.
# @examples
# get_geographic_granularities()
def get_geographic_granularities():
    # Build URL
    api = "indicators"
    path = "geographicGranularities"
    url = get_url(api, path)

    # Get content
    content = get_content(url)

    return content


# @title Get geographical values
# @description This function returns values of a geographical granularity that
#  in turn are part of a specific theme or system of indicators.
# @param geographicalGranularityCode (string) geographical granularity code
# @param subjectCode (string) subject code
# @param systemCode (string) system code
# @examples
# get_geographical_values("REGIONS")
# get_geographical_values("REGIONS", subjectCode = "051", systemCode = "C00067A")
def get_geographical_values(geographicalgranularitycode, subjectcode="", systemcode=""):
    # Build URL
    api = "indicators"
    path = "geographicalValues"
    if subjectcode is not None:
        if systemcode is not None:
            path = path + "?subjectCode=" + subjectcode + "&systemCode=" + systemcode + "&geographicalGranularityCode="\
                   + geographicalgranularitycode
        else:
            path = path + "?subjectCode=" + subjectcode + "&geographicalGranularityCode=" + geographicalgranularitycode
    else:
        if systemcode is not None:
            path = path + "?systemCode=" + systemcode + "&geographicalGranularityCode=" + geographicalgranularitycode
        else:
            path = path + "?geographicalGranularityCode=" + geographicalgranularitycode

    url = get_url(api, path)

    # Get content
    content = get_content(url)

    return content


# @title Get subjects
# @description This function returns all subjects which the ISTAC classifies
#  its statistical operations.
# @examples
# get_subjects()
def get_subjects():
    # Build URL
    api = "indicators"
    path = "subjects"

    # Get content
    url = get_url(api, path)
    content = get_content(url)

    return content


# @title Get time granularities
# @description This function returns a list of temporary granularity treated
#  in the ISTAC data bank-indicators ordered from highest to lowest granularity.
#  For example annual, quarterly or monthly granularity.
# @examples
# get_time_granularities()
def get_time_granularities():
    # Build URL
    api = "indicators"
    path = "timeGranularities"

    # Get content
    url = get_url(api, path)
    content = get_content(url)

    return content
