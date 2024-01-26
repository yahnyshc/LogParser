import unittest
from timestamp_parser import TimestampParser


class TestStringMethods(unittest.TestCase):

    def test_trim_timestamp_to_date(self):
        expected_timestamp = "2018-12-09"
        self.assertEqual(TimestampParser.trim_timestamp_to_date("2018-12-09T14:19:00+00:00"), expected_timestamp)

        expected_timestamp = "2018-12-08"
        self.assertEqual(TimestampParser.trim_timestamp_to_date("2018-12-08T14:19:00"), expected_timestamp)

        expected_timestamp = "2017-10-07"
        self.assertEqual(TimestampParser.trim_timestamp_to_date("2017-10-07"), expected_timestamp)

        expected_timestamp = "2017-10-07"
        self.assertNotEqual(TimestampParser.trim_timestamp_to_date("2018-10-07"), expected_timestamp)

    def test_compare_timestamps_simple(self):
        expected_cmp = 1
        self.assertEqual(
            TimestampParser.compare_timestamps_simple(
                "2018-12-09T14:19:00+00:00", "2018-12-07T11:13:00+00:00"
            ),
            expected_cmp)

        expected_cmp = 0
        self.assertEqual(
            TimestampParser.compare_timestamps_simple(
                "2018-12-09T14:19:00+00:00", "2018-12-09T13:09:21+00:00"
            ),
            expected_cmp)

        expected_cmp = -1
        self.assertEqual(
            TimestampParser.compare_timestamps_simple(
                "2018-12-09T13:09:21+00:00", "2018-12-10T14:19:00+00:00",
            ),
            expected_cmp)

        expected_cmp = 0
        self.assertEqual(
            TimestampParser.compare_timestamps_simple(
                "2018-12-09T13:09:21+00:00", "2018-12-09",
            ),
            expected_cmp)

        expected_cmp = 1
        self.assertEqual(
            TimestampParser.compare_timestamps_simple(
                "2018-12-09T13:09:21+00:00", "2018-12-08",
            ),
            expected_cmp)

    def test_timestamp_to_hash_map(self):
        expected_result = {
            'year': '2018',
            'month': '12',
            'day': '09',
            'hour': '13',
            'minute': '09',
            'second': '21',
            'timezone': '+00:00'
        }
        self.assertEqual(TimestampParser.timestamp_to_hash_map("2018-12-09T13:09:21+00:00"), expected_result)

        expected_result = {
            'year': '2000',
            'month': '08',
            'day': '23',
            'hour': '00',
            'minute': '32',
            'second': '20',
            'timezone': '-02:00'
        }
        self.assertEqual(TimestampParser.timestamp_to_hash_map("2000-08-23T00:32:20-02:00"), expected_result)

    def test_compare_timestamps(self):
        expected_cmp = 1
        self.assertEqual(
            TimestampParser.compare_timestamps(
                "2018-12-09T14:19:00+00:00", "2018-12-07T11:13:00+00:00"
            ),
            expected_cmp)

        expected_cmp = 0
        self.assertEqual(
            TimestampParser.compare_timestamps(
                "2018-12-09T14:19:00+00:00", "2018-12-09T13:09:21+00:00"
            ),
            expected_cmp)

        expected_cmp = -1
        self.assertEqual(
            TimestampParser.compare_timestamps(
                "2018-12-09T13:09:21+00:00", "2018-12-10T14:19:00+00:00",
            ),
            expected_cmp)

        expected_cmp = 0
        self.assertEqual(
            TimestampParser.compare_timestamps(
                "2018-12-09T13:09:21+00:00", "2018-12-09",
            ),
            expected_cmp)

        expected_cmp = 1
        self.assertEqual(
            TimestampParser.compare_timestamps(
                "2018-12-09T13:09:21+00:00", "2018-12-08",
            ),
            expected_cmp)


if __name__ == '__main__':
    unittest.main()
