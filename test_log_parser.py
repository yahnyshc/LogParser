import unittest
from log_parser import LogParser

class TestStringMethods(unittest.TestCase):
    LOG_NAME = 'cookie_log.csv'

    def test_get_log_content(self):
        with self.assertRaises(ValueError):
            LogParser.get_log_content(None)

        expected_log_content = """cookie,timestamp
AtY0laUfhglK3lC7,2018-12-09T14:19:00+00:00
SAZuXPGUrfbcn5UA,2018-12-09T10:13:00+00:00
5UAVanZf6UtGyKVS,2018-12-09T07:25:00+00:00
AtY0laUfhglK3lC7,2018-12-09T06:19:00+00:00
SAZuXPGUrfbcn5UA,2018-12-08T22:03:00+00:00
4sMM2LxV07bPJzwf,2018-12-08T21:30:00+00:00
fbcn5UAVanZf6UtG,2018-12-08T09:30:00+00:00
4sMM2LxV07bPJzwf,2018-12-07T23:30:00+00:00
"""
        self.assertEqual(LogParser.get_log_content(self.LOG_NAME), expected_log_content)

    def test_filter_log_by_date(self):
        log_content = LogParser.get_log_content(self.LOG_NAME)
        filtered_log_content = {
            'header': ["cookie", "timestamp"],
            'content': [
                ["SAZuXPGUrfbcn5UA","2018-12-08T22:03:00+00:00"],
                ["4sMM2LxV07bPJzwf", "2018-12-08T21:30:00+00:00"],
                ["fbcn5UAVanZf6UtG", "2018-12-08T09:30:00+00:00"],
            ]
        }
        self.assertEqual(LogParser.filter_log_by_date(log_content, "2018-12-08"), filtered_log_content)

        filtered_log_content = {
            'header': ["cookie", "timestamp"],
            'content': [
                ["AtY0laUfhglK3lC7", "2018-12-09T14:19:00+00:00"],
                ["SAZuXPGUrfbcn5UA", "2018-12-09T10:13:00+00:00"],
                ["5UAVanZf6UtGyKVS", "2018-12-09T07:25:00+00:00"],
                ["AtY0laUfhglK3lC7", "2018-12-09T06:19:00+00:00"],
            ]
        }
        self.assertEqual(LogParser.filter_log_by_date(log_content, "2018-12-09"), filtered_log_content)

        filtered_log_content = {
            'header': ["cookie", "timestamp"],
            'content': []
        }
        self.assertEqual(LogParser.filter_log_by_date(log_content, "2018-10-02"), filtered_log_content)

        filtered_log_content = {
            'header': ["cookie", "timestamp"],
            'content': [
                ["AtY0laUfhglK3lC7", "2018-12-09T14:19:00+00:00"],
                ["SAZuXPGUrfbcn5UA", "2018-12-09T10:13:00+00:00"],
                ["5UAVanZf6UtGyKVS", "2018-12-09T07:25:00+00:00"],
                ["AtY0laUfhglK3lC7", "2018-12-09T06:19:00+00:00"],
                ["SAZuXPGUrfbcn5UA", "2018-12-08T22:03:00+00:00"],
                ["4sMM2LxV07bPJzwf", "2018-12-08T21:30:00+00:00"],
                ["fbcn5UAVanZf6UtG", "2018-12-08T09:30:00+00:00"],
                ["4sMM2LxV07bPJzwf", "2018-12-07T23:30:00+00:00"],
            ]
        }
        self.assertEqual(LogParser.filter_log_by_date(log_content, ""), filtered_log_content)

    def test_get_most_active_cookies(self):
        most_active_cookies = ['AtY0laUfhglK3lC7']
        self.assertEqual(
            LogParser.get_most_active_cookies(LogParser.get_log_content(self.LOG_NAME), "2018-12-09"),
            most_active_cookies)

        most_active_cookies = ["SAZuXPGUrfbcn5UA",
                               "4sMM2LxV07bPJzwf",
                               "fbcn5UAVanZf6UtG"]
        self.assertEqual(
            LogParser.get_most_active_cookies(LogParser.get_log_content(self.LOG_NAME), "2018-12-08"),
            most_active_cookies)

        most_active_cookies = ["4sMM2LxV07bPJzwf"]
        self.assertEqual(
            LogParser.get_most_active_cookies(LogParser.get_log_content(self.LOG_NAME), "2018-12-07"),
            most_active_cookies)

        most_active_cookies = []
        self.assertEqual(
            LogParser.get_most_active_cookies(LogParser.get_log_content(self.LOG_NAME), "2018-12-23"),
            most_active_cookies)

        self.assertEqual(
            LogParser.get_most_active_cookies("", "2018-12-07"),
            most_active_cookies)

        most_active_cookies = ['AtY0laUfhglK3lC7',
                               'SAZuXPGUrfbcn5UA',
                               '4sMM2LxV07bPJzwf']
        self.assertEqual(
            LogParser.get_most_active_cookies(LogParser.get_log_content(self.LOG_NAME), ""),
            most_active_cookies)

if __name__ == '__main__':
    unittest.main()
