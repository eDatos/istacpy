import re

from istacpy import config

from .base import CodeStore


class TimeGranularity(CodeStore):
    YEARLY, YEARLY_ID = 'YEARLY', 'Y'
    BIYEARLY, BIYEARLY_ID = 'BIYEARLY', 'B'
    QUARTERLY, QUARTERLY_ID = 'QUARTERLY', 'Q'
    FOUR_MONTHLY, FOUR_MONTHLY_ID = 'FOUR_MONTHLY', 'F'
    MONTHLY, MONTHLY_ID = 'MONTHLY', 'M'
    WEEKLY, WEEKLY_ID = 'WEEK', 'W'
    DAILY, DAILY_ID = 'DAILY', 'D'
    HOURLY, HOURLY_ID = 'HOURLY', 'H'

    CODES = {
        YEARLY_ID: YEARLY,
        BIYEARLY_ID: BIYEARLY,
        QUARTERLY_ID: QUARTERLY,
        FOUR_MONTHLY_ID: FOUR_MONTHLY,
        MONTHLY_ID: MONTHLY,
        WEEKLY_ID: WEEKLY,
        DAILY_ID: DAILY,
        HOURLY_ID: HOURLY,
    }


class TimeRepresentation:
    CODES = {
        TimeGranularity.YEARLY: ('',),
        TimeGranularity.BIYEARLY: ('H1', 'H2'),
        TimeGranularity.QUARTERLY: ('Q1', 'Q2', 'Q3', 'Q4'),
        TimeGranularity.MONTHLY: (
            'M01',
            'M02',
            'M03',
            'M04',
            'M05',
            'M06',
            'M07',
            'M08',
            'M09',
            'M10',
            'M11',
            'M12',
        ),
    }

    MONTHS = {
        'ES': (
            'ENE',
            'FEB',
            'MAR',
            'ABR',
            'MAY',
            'JUN',
            'JUL',
            'AGO',
            'SEP',
            'OCT',
            'NOV',
            'DIC',
        ),
        'EN': (
            'JAN',
            'FEB',
            'MAR',
            'APR',
            'MAY',
            'JUN',
            'JUL',
            'AUG',
            'SEP',
            'OCT',
            'NOV',
            'DEC',
        ),
    }

    @classmethod
    def get_codes(cls, year, granularity):
        return [f'{year}{suffix}' for suffix in cls.CODES[granularity]]

    @classmethod
    def get_title(cls, code):
        if m := re.match(r'^(\d+)M(\d{2})', code):
            year, month = m.groups()
            month_no = int(month) - 1
            month_code = cls.MONTHS[config.LOCALE][month_no]
            return f'{year} {month_code}'
        return code


TimeGranularity.build_swapped_codes()
