from abc import ABC


class Dimension:
    GEOGRAPHICAL = 'GEOGRAPHICAL'
    TIME = 'TIME'
    MEASURE = 'MEASURE'


class CodeStore(ABC):
    CODES = dict()

    @classmethod
    def get_code(cls, id):
        return cls.CODES[id]

    @classmethod
    def build_swapped_codes(cls):
        cls.SWAPPED_CODES = {}
        for id, code in cls.CODES.items():
            cls.SWAPPED_CODES[code] = id

    @classmethod
    def get_id(cls, id):
        return cls.SWAPPED_CODES[id]
