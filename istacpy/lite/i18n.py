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
    Message.NON_AVAILABLE: {Locale.ES: 'No disponible', Locale.EN: 'Non available'},
    Message.AVAILABLE_YEARS: {Locale.ES: 'Años disponibles', Locale.EN: 'Available years'},
    Message.INDICATOR_CODE: {
        Locale.ES: 'Código del indicador',
        Locale.EN: 'Indicator code',
    },
    Message.TITLE: {Locale.ES: 'Título', Locale.EN: 'Title'},
    Message.DESCRIPTION: {Locale.ES: 'Descripción', Locale.EN: 'Description'},
    Message.YEARS_RANGE: {Locale.ES: 'Rango de años', Locale.EN: 'Years range'},
    Message.SUBJECT: {Locale.ES: 'Tema', Locale.EN: 'Subject'},
    Message.GRANULARITIES: {Locale.ES: 'Granularidades', Locale.EN: 'Granularities'},
    Message.MEASURES: {Locale.ES: 'Medidas', Locale.EN: 'Measures'},
    Message.GRANULARITY: {Locale.ES: 'Granularidad', Locale.EN: 'Granularity'},
    Message.MEASURE: {Locale.ES: 'Medida', Locale.EN: 'Measure'},
    Message.INDEX: {Locale.ES: 'Índice', Locale.EN: 'Index'},
    Message.SHAPE: {Locale.ES: 'Forma', Locale.EN: 'Shape'},
    Message.DATA: {Locale.ES: 'Datos', Locale.EN: 'Data'},
    Message.COLUMNS: {Locale.ES: 'Columnas', Locale.EN: 'Columns'},
    Message.NUM_OBSERVATIONS: {
        Locale.ES: 'Número de observaciones',
        Locale.EN: 'Number of observations',
    },
    Message.CLASS: {Locale.ES: 'Clase', Locale.EN: 'Class'},
}


def gettext(msg_code, locale=None):
    if locale is None:
        locale = Locale.DEFAULT_LOCALE
    return MESSAGES.get(msg_code)[locale]
