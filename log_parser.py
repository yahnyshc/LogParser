import logging
import time
from timestamp_parser import TimestampParser


class LogParser:

    @staticmethod
    def get_log_content(log_name):
        if not log_name:
            raise ValueError('Log name is not defined')
        with open(log_name, 'r') as file:
            return file.read()

    @staticmethod
    def filter_log_by_date(log_content: str, date: str) -> dict:
        """Returns dictionary with 'header' and 'content' of the log after filtering by date
        :param log_content: content of the log file to filter
        :param date: date to filter by. If date is None, every row will be grabbed
        :return: dictionary with 'header' and 'content' keys
        """
        res = {'header': '', 'content': []}
        log_lines = log_content.split('\n')
        res['header'] = log_lines.pop(0).split(',')
        for line in log_lines:
            if ',' not in line:
                break
            cookie, timestamp = line.split(',')
            # We can either compare_timestamps_simple or compare_timestamps. Same output expected.
            # Second function will be easier to maintain if timestamp format will change.
            if date:
                cmp = TimestampParser.compare_timestamps_simple(timestamp, date)
                if cmp == -1:
                    break
                elif cmp == 0:
                    res['content'].append([cookie, timestamp])
            else:
                res['content'].append([cookie, timestamp])
        return res

    @staticmethod
    def get_most_active_cookies(log_content: str, date: str) -> list:
        """Returns array of most active cookies
        :param log_content: content of the log file to parse
        :param date: date to look for
        :return: array of most active cookies names
        """
        if not log_content:
            return []
        start_time = time.perf_counter()
        logging.info(f"Starting to look for most active cookies with date {date}...")

        filtered_log = LogParser.filter_log_by_date(log_content, date)
        cookies_freq = {}
        max_cookie_count = 0
        result = []

        for cookie, timestamp in filtered_log['content']:
            cookies_freq[cookie] = cookies_freq.get(cookie, 0) + 1
            count = cookies_freq[cookie]

            logging.info(str(count) + ("th" if count > 3 else ['st', 'nd', 'rd'][count - 1]) + \
                         " occurrence of cookie " + cookie + " " + \
                         "at " + timestamp.replace('T', ' ').strip('\n'))

            if count > max_cookie_count:
                max_cookie_count = count
                result = [cookie]
            elif count == max_cookie_count:
                result.append(cookie)
        if not result:
            logging.info("No cookies found with given date.")
        logging.info("Done gathering most active cookies in " + '{:.2f}'.format(time.perf_counter()-start_time) + "s")

        return result