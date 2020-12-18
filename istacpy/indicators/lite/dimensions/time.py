import re

from istacpy.indicators.lite.i18n import Locale

from .base import CodeStore


class TimeGranularity(CodeStore):
    YEARLY, YEARLY_ID = 'YEARLY', 'Y'
    BIYEARLY, BIYEARLY_ID = 'BIYEARLY', 'B'
    QUARTERLY, QUARTERLY_ID = 'QUARTERLY', 'Q'
    FOUR_MONTHLY, FOUR_MONTHLY_ID = 'FOUR_MONTHLY', 'F'
    MONTHLY, MONTHLY_ID = 'MONTHLY', 'M'
    WEEKLY, WEEKLY_ID = 'WEEKLY', 'W'
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
        Locale.ES: (
            'Ene',
            'Feb',
            'Mar',
            'Abr',
            'May',
            'Jun',
            'Jul',
            'Ago',
            'Sep',
            'Oct',
            'Nov',
            'Dic',
        ),
        Locale.EN: (
            'Jan',
            'Feb',
            'Mar',
            'Apr',
            'May',
            'Jun',
            'Jul',
            'Aug',
            'Sep',
            'Oct',
            'Nov',
            'Dec',
        ),
    }

    @classmethod
    def get_codes(cls, year, granularity, use_dash=False):
        sep = '-' if use_dash else ''
        return [f'{year}{sep}{suffix}' for suffix in cls.CODES[granularity]]

    @classmethod
    def get_title(cls, code):
        if m := re.match(r'^(\d+)-?M(\d{2})', code):
            year, month = m.groups()
            month_no = int(month) - 1
            month_code = cls.MONTHS[Locale.DEFAULT_LOCALE][month_no]
            return f'{month_code} {year}'
        return code


TimeGranularity.build_swapped_codes()
