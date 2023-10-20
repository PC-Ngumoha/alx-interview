#!/usr/bin/python3
"""
0-stats.py
A script that reads the lines from the standard input (stdin)
and then use it to compute matrics which it then displays to the user.
"""
import re
import sys


if __name__ == '__main__':
    pattern1 = ''.join((
        r'^\d{1,3}(?:\.\d{1,3}){3} - \[\d{4}-\d{1,2}-\d{1,2}',
        r' \d{2}:\d{2}:\d{2}\.\d{1,6}\] \"GET \/projects\/260',
        r' HTTP\/1\.1\" [1-5]\d{2} \d+$'
    ))
    pattern2 = r'\b[1-5]\d{2} \d+$'
    count = 0
    total_size = 0
    s_codes = {"200": 0, "301": 0, "400": 0,
                  "401": 0, "403": 0, "404": 0, "405": 0, "500": 0}
    try:
        for line in sys.stdin:
            if not line:
                break
            if count % 10 == 0 and count != 0:
                print('File size: {}'.format(total_size))
                for s_code in s_codes:
                    if s_codes[s_code] > 0:
                        print('{}: {}'.format(s_code, s_codes[s_code]))
            line_match = re.fullmatch(pattern1, line.rstrip())
            if not line_match:
                continue
            else:
                segment_match = re.search(pattern2, line.rstrip())
                s_code, file_size = segment_match.group().split(' ')
                total_size += int(file_size)
                s_codes[s_code] += 1
            count += 1
    except KeyboardInterrupt:
        print('File size: {}'.format(total_size))
        for s_code in s_codes:
            if s_codes[s_code] > 0:
                print('{}: {}'.format(s_code, s_codes[s_code]))
