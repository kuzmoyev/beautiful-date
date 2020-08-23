from datetime import date, datetime


class BeautifulDate(date):
    """Date object that can be extended to datetime by using Python indexing/slicing:

    Examples:
        >>> (Oct / 16 / 1995)[:]
        datetime.datetime(1995, 10, 16, 0, 0)

        >>> (Oct / 16 / 1995)[23]
        datetime.datetime(1995, 10, 16, 23, 0)

        >>> (Oct / 16 / 1995)[23:14]
        datetime.datetime(1995, 10, 16, 23, 14)

        >>> (Oct / 16 / 1995)[23:14:10]
        datetime.datetime(1995, 10, 16, 23, 14, 10)
    """

    def __getitem__(self, t):
        """
        Converts date to datetime with provided time [hours[:minutes[:seconds]]]
        :return: datetime object.
        """

        if isinstance(t, slice):
            h, m, s = t.start or 0, t.stop or 0, t.step or 0
        elif isinstance(t, int):
            h, m, s = t, 0, 0
        else:
            raise TypeError("Time values must be integer or slice, not {!r}".format(t.__class__.__name__))

        return datetime(self.year, self.month, self.day, hour=h, minute=m, second=s)


# Classes to build date
#   D @ 16/10/1995 (16/Oct/1995)
#   D @ 5/19/2006 (May/19/2006)

class _PartialDate:
    """Date builder that uses operator "/" or "-" between values of day, month and year

    Examples:
        >>> D @ 11/12/2000
        BeautifulDate(2000, 12, 11)

        >>> D @ 22-10-2000
        BeautifulDate(2000, 10, 22)
    """

    def __init__(self, first, _format):
        self._date_values = [first]
        self._format = _format

    def __truediv__(self, value):
        self._date_values.append(value)
        if len(self._date_values) == 3:
            return BeautifulDate(**dict(zip(self._format, self._date_values)))
        else:
            return self

    __sub__ = __truediv__

    def __str__(self):
        return '/'.join(str(v) for v in self._date_values)

    def __repr__(self):
        return '{}({})'.format(self.__class__.__name__, self.__str__())


class BaseDateFormat:
    """Base class for date format.

    Used to create PartialDate with a format specified in the inherited classes.

    Examples:
        >>> D @ 11
        _PartialDate(11)

        >>> D @ 22/10
        _PartialDate(22/10)
    """

    # List of strings 'day', 'month', and 'year' in desired order.
    # Should be overridden in the inherited classes
    _format = None

    def __matmul__(self, first):
        return _PartialDate(first, self._format)

    def __str__(self):
        return '{}{}'.format(self.__class__.__name__, self._format)

    @staticmethod
    def today():
        today = date.today()
        return BeautifulDate(year=today.year, month=today.month, day=today.day)

    @staticmethod
    def now():
        return datetime.now()


class DMY(BaseDateFormat):
    _format = 'day', 'month', 'year'


class MDY(BaseDateFormat):
    _format = 'month', 'day', 'year'


class YMD(BaseDateFormat):
    _format = 'year', 'month', 'day'


class YDM(BaseDateFormat):
    _format = 'year', 'day', 'month'


D = DMY()


# Classes to build date with month name
#   16/Oct/1995
#   May-19-2006

class _Day:
    """Second step of creating date object

    Stores month and day numbers. If applied operator '/' or '-', returns BeautifulDate with provided value of the year

    Examples:
        >>> 16/Oct/1995
        BeautifulDate(1995, 10, 16)

        >>> May-19-2006
        BeautifulDate(2006, 5, 19)

    """

    def __init__(self, d, m):
        self.d = d
        self.m = m

    def __sub__(self, y):
        return BeautifulDate(year=y, month=self.m, day=self.d)

    def __repr__(self):
        return '{}({}, {})'.format(self.__class__.__name__, self.d, self.m)

    __truediv__ = __sub__


class _Month:
    """First step of creating date object

    Stores month number. If applied operator '/' or '-', returns _Day with provided value of the day.

    Examples:
        >>> 16/Oct
        _Day(16, 10)

        >>> May-19
        _Day(19, 5)
    """

    def __init__(self, m):
        self.m = m

    def __sub__(self, d):
        return _Day(d, self.m)

    __rtruediv__ = __rsub__ = __truediv__ = __sub__


M = _, Jan, Feb, Mar, Apr, May, Jun, Jul, Aug, Sept, Oct, Nov, Dec = [_Month(i) for i in range(13)]
