#!/usr/bin/python3
"""
0-stats.py
A script that reads the lines from the standard input (stdin)
and then use it to compute matrics which it then displays to the user.
"""
from typing import Mapping
import re
import sys


# Helper function
def print_stats(f_size: int, status_codes: Mapping[str, int]) -> None:
    """
    print_stats(f_size, status_codes)

    Args:
        - f_size (int) -> accumulated file size
        - status_codes (mapping) -> status code mapping

    Returns:
        - None
    """
    print('File size: {}'.format(f_size))
    for status_code in status_codes:
        if status_codes[status_code] > 0:
            print('{}: {}'.format(status_code, status_codes[status_code]))


if __name__ == '__main__':
    line_pattern = ''.join((
        r'^.+\s*-?\s*\[\d{4}-\d{2}-\d{2}\s\d{2}:\d{2}:\d{2}',
        r'\.\d{6}\]\s*".+"\s*\S+\s\S+$'
    ))
    data_pattern = r'\b\S+\s\S+$'
    line_count = 0
    total_size = 0
    s_codes = {"200": 0, "301": 0, "400": 0,
               "401": 0, "403": 0, "404": 0, "405": 0, "500": 0}
    try:
        while True:
            line = sys.stdin.readline()
            if line.strip() == '':
                print_stats(total_size, s_codes)
                break
            if line_count % 10 == 0 and line_count != 0:
                print_stats(total_size, s_codes)
            line_match = re.fullmatch(line_pattern, line.rstrip())
            if not line_match:
                continue
            else:
                data_segment = re.search(data_pattern, line.rstrip())
                s_code, f_size = data_segment.group().split()
                total_size += int(f_size) if f_size.isnumeric() else 0
                if s_code.isnumeric():
                    s_codes[s_code] += 1
            line_count += 1
    except KeyboardInterrupt:
        print_stats(total_size, s_codes)
