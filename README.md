# LogParser
Parses log file to find the most active cookies. Supports log file filtering by date and various timestamp processing.

To run the tests use:

python3 test_log_parser.py

and/or

python3 test_timestamp_parser.py

Run the command below to find the most active cookies on the given date in a log file:

python3 most_active_cookies.py -f cookie_log.csv -d YYYY-MM-DD

Example output:

![image](https://github.com/yahnyshc/LogParser/assets/143096926/313b2939-fb1f-469d-815d-16afd0251877)

Run the command below to find the most active cookies in the whole log file:

python3 most_active_cookies.py -f cookie_log.csv

Example output:

![image](https://github.com/yahnyshc/LogParser/assets/143096926/4b51acd5-3181-4619-8233-1896bd715e9f)

