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
    NON_AVAILABLE = auto()
    AVAILABLE_YEARS = auto()


MESSAGES = {
    Message.NON_AVAILABLE: {Locale.ES: 'No disponible', Locale.EN: 'Non available'},
    Message.AVAILABLE_YEARS: {Locale.ES: 'Años disponibles', Locale.EN: 'Available years'},
}


def gettext(msg_code, locale=None):
    if locale is None:
        locale = Locale.DEFAULT_LOCALE
    return MESSAGES.get(msg_code)[locale]
