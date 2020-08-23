import unittest
from datetime import date, datetime

from beautiful_date import Feb, Mar, Oct, \
    years, months, weeks, days, hours, minutes, seconds, microseconds, leapday, \
    year, month, day, hour, minute, second, microsecond, yearday, nlyearday, \
    MO, SA


class TestBeautifulTimedelta(unittest.TestCase):

    def test_beautiful_delta_dates(self):
        d = 5 / Oct / 1995

        self.assertEqual(d + 5 * days, date(day=10, month=10, year=1995))
        self.assertEqual(d - 10 * days, date(day=25, month=9, year=1995))
        self.assertEqual(d + 27 * days, date(day=1, month=11, year=1995))
        self.assertEqual(d + 0.5 * days, date(day=5, month=10, year=1995))

        self.assertEqual(d + 3 * weeks, date(day=26, month=10, year=1995))
        self.assertEqual(d - 2 * weeks, date(day=21, month=9, year=1995))
        self.assertEqual(d + 7 * weeks, date(day=23, month=11, year=1995))
        self.assertEqual(d + 3 / 7 * weeks, date(day=8, month=10, year=1995))

        self.assertEqual(d + 2 * months, date(day=5, month=12, year=1995))
        self.assertEqual(d - 4 * months, date(day=5, month=6, year=1995))
        self.assertEqual(d + 5 * months, date(day=5, month=3, year=1996))

        self.assertEqual(d + 3 * years, date(day=5, month=10, year=1998))
        self.assertEqual(d + 10 * years, date(day=5, month=10, year=2005))

        self.assertEqual(d + 2 * days + 10 * months - 3 * years, date(day=7, month=8, year=1993))

        self.assertEqual((25 / Feb / 1996) + 10 * days + leapday, date(day=7, month=3, year=1996))
        self.assertEqual((25 / Feb / 1996) + 255 * yearday, date(day=11, month=9, year=1996))
        self.assertEqual((25 / Feb / 1996) + 255 * nlyearday, date(day=12, month=9, year=1996))
        self.assertEqual((25 / Feb / 1995) + 255 * yearday, date(day=12, month=9, year=1995))
        self.assertEqual((25 / Feb / 1995) + 255 * nlyearday, date(day=12, month=9, year=1995))

    def test_beautiful_delta_dates_inexact(self):
        last_day_of_month = 31 / Oct / 1995
        self.assertEqual(last_day_of_month + 1 * months, date(day=30, month=11, year=1995))
        self.assertEqual(last_day_of_month + 4 * months, date(day=29, month=2, year=1996))
        self.assertEqual(last_day_of_month + 4 * months + 1 * years, date(day=28, month=2, year=1997))

    def test_beautiful_delta_datetimes(self):
        dt = (16 / Oct / 1995)[1:2:3]

        self.assertEqual(dt + 25 * microseconds,
                         datetime(day=16, month=10, year=1995, hour=1, minute=2, second=3, microsecond=25))
        self.assertEqual(dt - 6 * 10 ** 5 * microseconds,
                         datetime(day=16, month=10, year=1995, hour=1, minute=2, second=2, microsecond=4 * 10 ** 5))
        self.assertEqual(dt + 10 ** 6 * microseconds,
                         datetime(day=16, month=10, year=1995, hour=1, minute=2, second=4))

        self.assertEqual(dt + 25 * seconds, datetime(day=16, month=10, year=1995, hour=1, minute=2, second=28))
        self.assertEqual(dt + 65 * seconds, datetime(day=16, month=10, year=1995, hour=1, minute=3, second=8))
        self.assertEqual(dt - 50 * seconds, datetime(day=16, month=10, year=1995, hour=1, minute=1, second=13))
        self.assertEqual(dt + 0.5 * seconds,
                         datetime(day=16, month=10, year=1995, hour=1, minute=2, second=3, microsecond=5 * 10 ** 5))

        self.assertEqual(dt + 13 * minutes, datetime(day=16, month=10, year=1995, hour=1, minute=15, second=3))
        self.assertEqual(dt + 65 * minutes, datetime(day=16, month=10, year=1995, hour=2, minute=7, second=3))
        self.assertEqual(dt - 20 * minutes, datetime(day=16, month=10, year=1995, hour=0, minute=42, second=3))
        self.assertEqual(dt + 1 / 6 * minutes, datetime(day=16, month=10, year=1995, hour=1, minute=2, second=13))

        self.assertEqual(dt + 2 * hours, datetime(day=16, month=10, year=1995, hour=3, minute=2, second=3))
        self.assertEqual(dt + 30 * hours, datetime(day=17, month=10, year=1995, hour=7, minute=2, second=3))
        self.assertEqual(dt - 13 * hours, datetime(day=15, month=10, year=1995, hour=12, minute=2, second=3))
        self.assertEqual(dt + 1 / 4 * hours, datetime(day=16, month=10, year=1995, hour=1, minute=17, second=3))

        self.assertEqual(dt + 3 * hours + 5 * minutes - 25 * seconds,
                         datetime(day=16, month=10, year=1995, hour=4, minute=6, second=38))

        dt += 3 * hours + 5 * minutes - 25 * seconds
        self.assertEqual(dt, datetime(day=16, month=10, year=1995, hour=4, minute=6, second=38))

    def test_beautiful_setter(self):
        dt = (16 / Oct / 1995)[1:2:3]

        self.assertEqual(dt + 5 * day, datetime(day=5, month=10, year=1995, hour=1, minute=2, second=3))
        self.assertEqual(dt + 3 * month, datetime(day=16, month=3, year=1995, hour=1, minute=2, second=3))
        self.assertEqual(dt + 1998 * year, datetime(day=16, month=10, year=1998, hour=1, minute=2, second=3))

        self.assertEqual(dt + 25 * microsecond,
                         datetime(day=16, month=10, year=1995, hour=1, minute=2, second=3, microsecond=25))
        self.assertEqual(dt + 55 * second, datetime(day=16, month=10, year=1995, hour=1, minute=2, second=55))
        self.assertEqual(dt + 56 * minute, datetime(day=16, month=10, year=1995, hour=1, minute=56, second=3))
        self.assertEqual(dt + 22 * hour, datetime(day=16, month=10, year=1995, hour=22, minute=2, second=3))

        self.assertEqual(dt + 1919 * year + 5 * month + 4 * day + 23 * hour + 41 * minute + 34 * second,
                         datetime(day=4, month=5, year=1919, hour=23, minute=41, second=34))

        dt += 1919 * year + 5 * month + 4 * day + 23 * hour + 41 * minute + 34 * second
        self.assertEqual(dt, datetime(day=4, month=5, year=1919, hour=23, minute=41, second=34))

    def test_beautiful_weekdays(self):
        d = 29 / Mar / 2018

        self.assertEqual(d + MO, date(2018, 4, 2))
        self.assertEqual(d + MO(2), date(2018, 4, 9))
        self.assertEqual(d - SA(2), date(2018, 3, 17))
        self.assertEqual(d + SA(-2), date(2018, 3, 17))
