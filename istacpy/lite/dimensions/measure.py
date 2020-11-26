from .base import Granularity


class MeasureGranularity(Granularity):
    ABSOLUTE, ABSOLUTE_ID = 'ABSOLUTE', 'A'
    ANNUAL_PERCENTAGE_RATE, ANNUAL_PERCENTAGE_RATE_ID = 'ANNUAL_PERCENTAGE_RATE', 'N'
    INTERPERIOD_PERCENTAGE_RATE, INTERPERIOD_PERCENTAGE_RATE_ID = (
        'INTERPERIOD_PERCENTAGE_RATE',
        'I',
    )
    ANNUAL_PUNTUAL_RATE, ANNUAL_PUNTUAL_RATE_ID = 'ANNUAL_PUNTUAL_RATE', 'M'
    INTERPERIOD_PUNTUAL_RATE, INTERPERIOD_PUNTUAL_RATE_ID = (
        'INTERPERIOD_PUNTUAL_RATE',
        'J',
    )

    CODES = {
        ABSOLUTE_ID: ABSOLUTE,
        ANNUAL_PERCENTAGE_RATE_ID: ANNUAL_PERCENTAGE_RATE,
        INTERPERIOD_PERCENTAGE_RATE_ID: INTERPERIOD_PERCENTAGE_RATE,
        ANNUAL_PUNTUAL_RATE_ID: ANNUAL_PUNTUAL_RATE,
        INTERPERIOD_PUNTUAL_RATE_ID: INTERPERIOD_PUNTUAL_RATE,
    }


MeasureGranularity.build_swapped_codes()
