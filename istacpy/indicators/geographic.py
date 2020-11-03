from istacpy import services

API = 'indicators'


def get_indicators_geographic_granularities():
    """Get geographic granularities

    This function returns a list of geographic granularities treated in the
    ISTAC-indicators database. For example provincial, insular or municipal granularity.

    Examples:
        >>> get_indicators_geographic_granularities()
    """
    path = 'geographicGranularities'
    url = services.build_entrypoint_url(API, path)
    return services.get_content(url)


def get_indicators_geographical_values(
    geographicalgranularitycode, subjectcode='', systemcode=''
):
    """Get geographical values

    This function returns values of a geographical granularity that in turn are part of a
    specific theme or system of indicators.

    Args:
        geographicalgranularitycode (string): geographical granularity code
        subjectcode (string): subject code
        systemcode (string): system code

    Examples:
        >>> get_indicators_geographical_values("REGIONS")
        >>> get_indicators_geographical_values(
        ... "REGIONS",
        ... subjectcode="051",
        ... systemcode="C00067A"
        )
    """
    path = 'geographicalValues'
    url = services.build_entrypoint_url(
        API,
        path,
        geographicalGranularityCode=geographicalgranularitycode,
        subjectCode=subjectcode,
        systemCode=systemcode,
    )
    return services.get_content(url)


def get_indicators_subjects():
    """Get subjects

    This function returns all subjects which the ISTAC classifies its statistical
    operations.

    Examples:
        >>> get_indicators_subjects()
    """
    path = 'subjects'
    url = services.build_entrypoint_url(API, path)
    return services.get_content(url)


def get_indicators_time_granularities():
    """Get time granularities

    This function returns a list of temporary granularity treated in the ISTAC data
    bank-indicators ordered from highest to lowest granularity. For example annual,
    quarterly or monthly granularity.

    Examples:
        >>> get_indicators_time_granularities()
    """
    path = 'timeGranularities'
    url = services.build_entrypoint_url(API, path)
    return services.get_content(url)
