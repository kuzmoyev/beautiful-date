import unittest
from datetime import date, datetime
from beautiful_date import D, MDY, M, Jan, Feb, May, Oct, BeautifulDate


class TestBeautifulDate(unittest.TestCase):

    def test_date_create_by_month_name(self):
        self.assertEqual(16 / Oct / 1995, date(day=16, month=10, year=1995))
        self.assertEqual(May / 19 / 2006, date(day=19, month=5, year=2006))
        self.assertEqual(29 / Feb / 1996, date(day=29, month=2, year=1996))

        self.assertEqual(4 - Jan - 1970, date(day=4, month=1, year=1970))
        self.assertEqual(Feb - 7 - 1973, date(day=7, month=2, year=1973))
        self.assertEqual(29 - Feb - 1992, date(day=29, month=2, year=1992))

    def test_date_create_by_month_number(self):
        self.assertEqual(D @ 21 / 12 / 1995, date(day=21, month=12, year=1995))
        self.assertEqual(D @ 21 - 12 - 1994, date(day=21, month=12, year=1994))
        self.assertEqual(D @ 29 / 2 / 1988, date(day=29, month=2, year=1988))

        self.assertEqual(21 / M[12] / 1995, date(day=21, month=12, year=1995))
        self.assertEqual(21 - M[12] - 1994, date(day=21, month=12, year=1994))
        self.assertEqual(29 / M[2] / 1988, date(day=29, month=2, year=1988))

    def test_date_create_by_prefix_MDY(self):
        D = MDY()
        self.assertEqual(D @ 9 - 23 - 1996, date(day=23, month=9, year=1996))
        self.assertEqual(D @ 10 / 31 / 1995, date(day=31, month=10, year=1995))
        self.assertEqual(D @ 2 - 29 - 1984, date(day=29, month=2, year=1984))

    def test_datetime_create_by_month_name(self):
        self.assertEqual((30 / Jan / 1996)[23], datetime(day=30, month=1, year=1996, hour=23, minute=0))
        self.assertEqual((Feb - 23 - 1975)[1:22], datetime(day=23, month=2, year=1975, hour=1, minute=22))
        self.assertEqual((29 / Feb / 1992)[23:59:59],
                         datetime(day=29, month=2, year=1992, hour=23, minute=59, second=59))

    def test_datetime_create_by_prefix(self):
        self.assertEqual((D @ 8 - 6 - 1947)[5], datetime(day=8, month=6, year=1947, hour=5, minute=0))
        self.assertEqual((D @ 22 / 7 / 1938)[20:11], datetime(day=22, month=7, year=1938, hour=20, minute=11))
        self.assertEqual((D @ 29 - 2 - 1988)[10:11:12],
                         datetime(day=29, month=2, year=1988, hour=10, minute=11, second=12))

    def test_today_now(self):
        self.assertIsInstance(D.today(), BeautifulDate)
        self.assertIsInstance(D.now(), datetime)

    def test_time_type_error(self):
        with self.assertRaises(TypeError):
            _ = (15 / Jan / 2020)['evening']
