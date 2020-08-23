from dateutil.relativedelta import relativedelta, weekdays
from datetime import date, datetime

from beautiful_date import BeautifulDate


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
leapdays = _('leapdays')
leapday = 1 * leapdays

year = _('year')
month = _('month')
day = _('day')
hour = _('hour')
minute = _('minute')
second = _('second')
microsecond = _('microsecond')

yearday = _('yearday')
nlyearday = _('nlyearday')

_weekday = _('weekday')


class BeautifulWeekday:
    """

    Examples:
        Get next Monday:
        >>> d = 29/Mar/2018  # Thursday
        >>> d + MO  # Equivalent to MO(1)
        BeautifulDate(2018, 4, 2)

        Get second to next Monday:
        >>> d = 29/Mar/2018
        >>> d + MO(2)
        BeautifulDate(2018, 4, 9)

        Get last Saturday:
        >>> d = 29/Mar/2018
        >>> d - SA
        BeautifulDate(2018, 3, 24)

        Get second to last Saturday:
        >>> d = 29/Mar/2018
        >>> d - SA(2)
        BeautifulDate(2018, 3, 17)

        Get second to last Saturday (same as previous):
        >>> d = 29/Mar/2018
        >>> d + SA(-2)
        BeautifulDate(2018, 3, 17)
    """

    def __init__(self, wd, n=1):
        self.wd = wd
        self.n = n

    def __radd__(self, other):
        return other + self.wd(self.n) * _weekday

    def __rsub__(self, other):
        return other + self.wd(-self.n) * _weekday

    def __call__(self, n):
        return BeautifulWeekday(self.wd, n)


weekdays = MO, TU, WE, TH, FR, SA, SU = [BeautifulWeekday(weekdays[i]) for i in range(7)]
