import unittest
from datetime import date
from itertools import zip_longest as zipl
from beautiful_date import Mar, Apr, days, hours, drange


class TestDrange(unittest.TestCase):

    def test_beautiful_drange_dates(self):
        dates = [
            27 / Mar / 1994,
            28 / Mar / 1994,
            29 / Mar / 1994,
            30 / Mar / 1994,
            31 / Mar / 1994,
            1 / Apr / 1994,
            2 / Apr / 1994,
            3 / Apr / 1994,
            4 / Apr / 1994,
            5 / Apr / 1994,
        ]

        for d, e in zipl(drange(27 / Mar / 1994, 5 / Apr / 1994), dates[:-1]):
            self.assertEqual(d, e)

        for d, e in zipl(drange(27 / Mar / 1994, 5 / Apr / 1994, 2 * days), dates[:-1:2]):
            self.assertEqual(d, e)

        for d, e in zipl(drange(5 / Apr / 1994, 27 / Mar / 1994, -2 * days), dates[:0:-2]):
            self.assertEqual(d, e)

        today = date.today()
        dates = [
            today,
            today + 2 * days,
            today + 4 * days
        ]

        for d, e in zipl(drange(today + 5 * days, step=2 * days), dates):
            self.assertEqual(d, e)

    def test_beautiful_drange_datetimes(self):
        times = [
            (27 / Mar / 1994)[10:25],
            (27 / Mar / 1994)[22:25],
            (28 / Mar / 1994)[10:25],
            (28 / Mar / 1994)[22:25],
            (29 / Mar / 1994)[10:25],
            (29 / Mar / 1994)[22:25],
            (30 / Mar / 1994)[10:25],
            (30 / Mar / 1994)[22:25],
            (31 / Mar / 1994)[10:25],
            (31 / Mar / 1994)[22:25],
            (1 / Apr / 1994)[10:25],
            (1 / Apr / 1994)[22:25],
            (2 / Apr / 1994)[10:25],
            (2 / Apr / 1994)[22:25],
            (3 / Apr / 1994)[10:25],
            (3 / Apr / 1994)[22:25],
            (4 / Apr / 1994)[10:25],
            (4 / Apr / 1994)[22:25],
            (5 / Apr / 1994)[10:25],
        ]

        for t, e in zip(drange((27 / Mar / 1994)[10:25], (4 / Apr / 1994)[10:10]), times[:-1:2]):
            self.assertEqual(t, e)

        for t, e in zip(drange((27 / Mar / 1994)[10:25], (4 / Apr / 1994)[10:10], 12 * hours), times[:-1]):
            self.assertEqual(t, e)

        for t, e in zip(drange((5 / Apr / 1994)[10:25], (27 / Mar / 1994)[10:25], -12 * hours), times[:0:-1]):
            self.assertEqual(t, e)

    def test_zero_step_error(self):
        with self.assertRaises(ValueError):
            _ = drange((5 / Apr / 1994), step=0 * days)
