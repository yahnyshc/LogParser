
# This class provides functionality to help comparing timestamps
class TimestampParser:
    # this separates date and time in the stamp
    DATE_TIME_SEPARATOR = 'T'
    # this separates date attributes in the stamp
    DATE_SEPARATOR = '-'
    # this separates time attributes in the stamp
    TIME_SEPARATOR = ':'
    # attributes of log timestamp
    TIMESTAMP_KEYS = ['year', 'month', 'day', 'hour', 'minute', 'second', 'timezone']

    @staticmethod
    def split_time_and_timezone(time_and_timezone: str) -> list:
        """ splits string with time and timezone into separate values
            handles timezone sign
        :param time_and_timezone: string with time and timezone in the format of "HH:MM:SS+HH:MM"
        :return: time and timezone in array with format ["HH:MM:SS", "+HH:MM"]
        """
        # check if timezone is positive
        if '+' in time_and_timezone:
            time, sign, timezone = time_and_timezone.partition('+')
        else:
            time, sign, timezone = time_and_timezone.partition('-')
        return [time, sign+timezone.strip('\n')]

    # convert timestamp to hashmap
    @staticmethod
    def timestamp_to_hash_map(timestamp: str) -> dict:
        """ Returns dictionary representation of timestamp keys and values
        :param timestamp: timestamp to parse
        :return: dictionary in the following format: {'year': 'YYYY', ..., 'timestamp':'+HH:MM'}
        """
        result = {}
        date_keys = iter(TimestampParser.TIMESTAMP_KEYS)

        def record_to_result(values: list) -> None:
            for v in values:
                result[next(date_keys)] = v

        # check if timestamp includes time
        if 'T' in timestamp:
            date, time_and_timezone = timestamp.split(TimestampParser.DATE_TIME_SEPARATOR)
            record_to_result(date.split(TimestampParser.DATE_SEPARATOR))
            time, timezone = TimestampParser.split_time_and_timezone(time_and_timezone)
            record_to_result(time.split(TimestampParser.TIME_SEPARATOR)+[timezone])
        else:
            # record with 0 time
            record_to_result(timestamp.split(TimestampParser.DATE_SEPARATOR)+[['00'], ['00'], ['00'], ["+00:00"]])
        return result

    @staticmethod
    def compare_timestamps(timestamp_a: str, timestamp_b: str, stop_at='day') -> int:
        """ Compares two time stamps
        :param timestamp_a: timestamp a
        :param timestamp_b: timestamp b
        :param stop_at: compare every key stopping on this one
        :return: 1 if timestamp_a > timestamp_b, 0 if timestamp_a == timestamp_b, -1 otherwise
        """
        # convert timestamps to hashmaps
        time_a = TimestampParser.timestamp_to_hash_map(timestamp_a)
        time_b = TimestampParser.timestamp_to_hash_map(timestamp_b)
        # iterate over keys in order.
        # this makes code more scalable and simplifies comparison if timestamp format changes
        for key in TimestampParser.TIMESTAMP_KEYS:
            if time_a[key] > time_b[key]:
                return 1
            if time_a[key] < time_b[key]:
                return -1
            if key == stop_at:
                return 0
        return 0

    @staticmethod
    def trim_timestamp_to_date(timestamp):
        """ Returns timestamp with time excluded
        :param timestamp: timestamp in format "YYYY-MM-DDTHH:MM:SS+HH:MM"
        :return: return timestamp trimmed to date in format "YYYY-MM-DD"
        """
        if TimestampParser.DATE_TIME_SEPARATOR not in timestamp:
            return timestamp
        return timestamp.split(TimestampParser.DATE_TIME_SEPARATOR)[0]

    @staticmethod
    def compare_timestamps_simple(timestamp_a: str, timestamp_b: str) -> int:
        """ Compares two time stamps by simple bython comparison
        :param timestamp_a: timestamp a
        :param timestamp_b: timestamp b
        :return: 1 if timestamp_a > timestamp_b, 0 if timestamp_a == timestamp_b, -1 otherwise
        """
        # trim timestamps to date and compare
        date_a = TimestampParser.trim_timestamp_to_date(timestamp_a)
        date_b = TimestampParser.trim_timestamp_to_date(timestamp_b)
        if date_a > date_b:
            return 1
        if date_a < date_b:
            return -1
        return 0

