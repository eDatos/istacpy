from abc import ABC


class IstacPyError(Exception, ABC):
    def __init__(self, value='', message=''):
        self.value = value
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        value = f' "{self.value}" ' if self.value else ' '
        return self.message.format(value)


class IndicatorNotFoundError(IstacPyError):
    def __init__(self, value='', message=r'given indicator{}not found on API'):
        super().__init__(value, message)


class QueryMalformedError(IstacPyError):
    def __init__(
        self, value='', message=r'given query{}is malformed or not properly written'
    ):
        super().__init__(value, message)


class GranularityNotAvailableError(IstacPyError):
    def __init__(
        self, value='', message=r'given granularity{}is not available for this indicator'
    ):
        super().__init__(value, message)


class MeasureNotAvailableError(IstacPyError):
    def __init__(
        self, value='', message=r'given measure{}is not available for this indicator'
    ):
        super().__init__(value, message)


class IslandNotFoundError(IstacPyError):
    def __init__(self, value='', message=r'given island{}not found'):
        super().__init__(value, message)
