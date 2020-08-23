from datetime import date, datetime

from beautiful_date import BeautifulDate, days


def timedelta_is_negative(td):
    """Checks whether timedelta is negative (would move date/datetime to the past)."""
    return datetime.now() > datetime.now() + td


class drange:
    """
    drange(stop) -> drange object
    drange(start, stop[, step]) -> drange object

    Return an object that produces a sequence of dates/datetimes (depending on parameter type)
    from start (inclusive) to stop (exclusive) by step.

    drange(stop) produces range of dates/datetimes from now to given stop date/datetime.
    drange(start, stop[, step]) produces range of dates/datetimes from start to stop.

    When step is given, it specifies the increment (or decrement).
    When step is not given, 1-day step is used.
    """

    def __init__(self, start_or_stop, stop=None, step=1 * days):
        if stop is None:
            if isinstance(start_or_stop, date):
                now = date.today()
            else:
                now = datetime.now()
            start = BeautifulDate(now.year, now.month, now.day)
            stop = start_or_stop
        else:
            start = start_or_stop

        if not step:
            raise ValueError('drange() step must be positive or negative step, not 0')

        self._backwards = timedelta_is_negative(step)

        self._start = start
        self._stop = stop
        self._step = step

    def __repr__(self):
        return 'drange({}, {}, {})'.format(self._start, self._stop, self._step)

    def __iter__(self):
        return self

    def __next__(self):
        if (self._backwards and self._start <= self._stop) or (not self._backwards and self._start >= self._stop):
            raise StopIteration

        ret = self._start
        self._start += self._step
        return ret
