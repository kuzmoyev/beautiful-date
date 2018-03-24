from dateutil.relativedelta import relativedelta
from beautiful_date import *


class BeautifulTimedelta:
    """Creates timedelta with specified time unit using operator '*'

    Examples:
        >>> 3*years
        relativedelta(years=+3)

        >>> -5*weeks
        relativedelta(days=-35)
    """

    def __init__(self, name):
        self.name = name

    def __rmul__(self, n):
        return relativedelta(**{self.name: n})


_ = BeautifulTimedelta

years = _('years')
months = _('months')
weeks = _('weeks')
days = _('days')
hours = _('hours')
minutes = _('minutes')
seconds = _('seconds')
microseconds = _('microseconds')


class _RelativeSetter(relativedelta):
    """Sets given time unit on a date

    Examples:
        >>> 11/Jan/2017 << 5 * month << 10 * second
        datetime.datetime(2017, 5, 11, 0, 0, 10)

        >>> (D @ 1/1/1999)[0:10] << 2 * month << 25 * day << 22 * hour
        datetime.datetime(1999, 2, 25, 22, 10)

        >>> d1 = D @ 1 /1/1999
        >>> d1 <<= 10*month + 16*day + 1995*year
        >>> d1
        datetime.date(1995, 10, 16)

        >>> d1 = D @ 1 /1/1999
        >>> d1 <<= 10*month << 16*day << 1995*year
        >>> d1
        datetime.date(1995, 10, 16)
    """

    __lshift__ = __rlshift__ = relativedelta.__radd__


class BeautifulSetter:
    def __init__(self, name):
        self.name = name

    def __rmul__(self, n):
        return _RelativeSetter(**{self.name: n})


_ = BeautifulSetter

year = _('year')
month = _('month')
week = _('week')
day = _('day')
hour = _('hour')
minute = _('minute')
second = _('second')
microsecond = _('microsecond')
