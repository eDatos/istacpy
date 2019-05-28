from istacpy.resources import resources


def get_indicators_geographic_granularities():
    """Get geographic granularities

    This function returns a list of geographic granularities treated in the ISTAC-indicators database.
    For example provincial, insular or municipal granularity.

    Examples:
        >>> get_indicators_geographic_granularities()
    """
    # Build URL
    api = "indicators"
    path = "geographicGranularities"
    url = resources.get_url(api, path)

    # Get content
    content = resources.get_content(url)

    return content


def get_indicators_geographical_values(geographicalgranularitycode, subjectcode=None, systemcode=None):
    """Get geographical values

    This function returns values of a geographical granularity that in turn are part of a specific theme or system of
    indicators.

    Args:
        geographicalgranularitycode (string): geographical granularity code
        subjectcode (string): subject code
        systemcode (string): system code

    Examples:
        >>> get_indicators_geographical_values("REGIONS")
        >>> get_indicators_geographical_values("REGIONS", subjectcode = "051", systemcode = "C00067A")
    """
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

    url = resources.get_url(api, path)

    # Get content
    content = resources.get_content(url)

    return content


def get_indicators_subjects():
    """Get subjects

    This function returns all subjects which the ISTAC classifies its statistical operations.

    Examples:
        >>> get_indicators_subjects()
    """
    # Build URL
    api = "indicators"
    path = "subjects"

    # Get content
    url = resources.get_url(api, path)
    content = resources.get_content(url)

    return content


def get_indicators_time_granularities():
    """Get time granularities

    This function returns a list of temporary granularity treated in the ISTAC data bank-indicators ordered from
    highest to lowest granularity. For example annual, quarterly or monthly granularity.

    Examples:
        >>> get_indicators_time_granularities()
    """
    # Build URL
    api = "indicators"
    path = "timeGranularities"

    # Get content
    url = resources.get_url(api, path)
    content = resources.get_content(url)

    return content
