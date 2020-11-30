class Locale:
    ES = 'es'
    EN = 'en'

    NON_AVAILABLE = {ES: 'No disponible', EN: 'Non available'}

    DEFAULT_LOCALE = ES

    @classmethod
    def set_english(cls):
        cls.DEFAULT_LOCALE = cls.EN

    @classmethod
    def set_spanish(cls):
        cls.DEFAULT_LOCALE = cls.ES

    @classmethod
    def non_available_msg(cls, locale=None):
        if locale is None:
            locale = cls.DEFAULT_LOCALE
        return cls.NON_AVAILABLE[locale]
