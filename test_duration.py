import unittest
import datetime
from duration import Duration


class TestDuration(unittest.TestCase):
    def test_duration(self):
        start_dt = '2020-02-18 09:48:21,847'
        end_dt = '2020-02-19 03:02:22,157'
        duration = Duration(start_dt, end_dt, '%Y-%m-%d %H:%M:%S,%f')
        self.assertIsNotNone(duration)
        self.assertIsInstance(duration, Duration)
        self.assertIsInstance(duration.start_datetime, datetime.datetime)
        self.assertIsInstance(duration.end_datetime, datetime.datetime)

    def test_datetime_delta(self):
        start_dt = '2020-02-18 09:48:21,847'
        end_dt = '2020-02-19 03:02:22,157'
        duration = Duration(start_dt, end_dt, '%Y-%m-%d %H:%M:%S,%f')
        self.assertIsNotNone(duration.datetime_delta)
        self.assertIsInstance(duration.datetime_delta, datetime.timedelta)
        self.assertEqual(duration.datetime_delta.days, 0)        
        