from dateutil.relativedelta import relativedelta
from datetime import date, datetime
from beautiful_date import *


class _RelativeDelta(relativedelta):
    """Same as relativedelta, but returns BeautifulDate in the result.

    Examples:
        >>> 16/Jan/2005 + 5*days
        BeautifulDate(2005, 1, 21)
    """

    def __add__(self, d):
        new_date = super().__add__(d)
        if isinstance(new_date, date) and not isinstance(new_date, datetime):
            return BeautifulDate(new_date.year, new_date.month, new_date.day)
        else:
            return new_date

    __radd__ = __add__


class BeautifulTimedelta:
    """Creates timedelta with specified time unit using operator '*'

    Examples:
        >>> 3*years
        _RelativeDelta(years=+3)

        >>> -5*weeks
        _RelativeDelta(days=-35)
    """

    def __init__(self, name):
        self.name = name

    def __rmul__(self, n):
        return _RelativeDelta(**{self.name: n})


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
        BeautifulDate(1995, 10, 16)

        >>> d1 = D @ 1 /1/1999
        >>> d1 <<= 10*month << 16*day << 1995*year
        >>> d1
        BeautifulDate(1995, 10, 16)
    """

    def __add__(self, d):
        new_date = super().__add__(d)
        if isinstance(new_date, date) and not isinstance(new_date, datetime):
            return BeautifulDate(new_date.year, new_date.month, new_date.day)
        else:
            return new_date

    __lshift__ = __rlshift__ = __radd__ = __add__


class BeautifulSetter:
    def __init__(self, name):
        self.name = name

    def __rmul__(self, n):
        return _RelativeSetter(**{self.name: n})


_ = BeautifulSetter

year = _('year')
month = _('month')
day = _('day')
hour = _('hour')
minute = _('minute')
second = _('second')
microsecond = _('microsecond')
