from enum import Enum, auto


class Locale:
    ES = 'es'
    EN = 'en'

    DEFAULT_LOCALE = ES


def set_english():
    Locale.DEFAULT_LOCALE = Locale.EN


def set_spanish():
    Locale.DEFAULT_LOCALE = Locale.ES


class Message(Enum):
    AVAILABLE_YEARS = auto()
    CLASS = auto()
    COLUMNS = auto()
    DATA = auto()
    DESCRIPTION = auto()
    GRANULARITIES = auto()
    GRANULARITY = auto()
    INDEX = auto()
    INDICATOR_CODE = auto()
    MEASURE = auto()
    MEASURES = auto()
    NON_AVAILABLE = auto()
    NUM_OBSERVATIONS = auto()
    SHAPE = auto()
    SUBJECT = auto()
    TITLE = auto()
    YEARS_RANGE = auto()


MESSAGES = {
    Message.NON_AVAILABLE: {Locale.ES: 'No disponible', Locale.EN: 'Not available'},
}


def gettext(msg_code, locale=None):
    if locale is None:
        locale = Locale.DEFAULT_LOCALE
    return MESSAGES.get(msg_code)[locale]
