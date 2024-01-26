import argparse
import logging
from log_parser import LogParser


def setup_argument_parser() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description='Log file parser.')
    parser.add_argument('-f', '--file', required=True, help='Path to the LOG file')
    parser.add_argument('-d', '--date', help='Date in the format YYYY-MM-DD')
    return parser.parse_args()


if __name__ == '__main__':
    # start logging
    logging.basicConfig(level=logging.INFO,
                        format='[%(asctime)s]: %(message)s',
                        datefmt='%d-%b-%y %H:%M:%S')
    logging.info("Logging app "+__file__)
    logging.info("")
    # parse command line arguments
    parsed_args = setup_argument_parser()

    most_active_cookies = LogParser.get_most_active_cookies(LogParser.get_log_content(parsed_args.file),
                                                            parsed_args.date)
    if most_active_cookies:
        logging.info("")
        logging.info("Most active cookie(s): ")
        for cookie in most_active_cookies:
            logging.info(cookie)

