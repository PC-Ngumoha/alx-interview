#!/usr/bin/python3
"""
A simple playground to help me test out my ideas.
"""
import re
import sys


if __name__ == '__main__':
    pattern = ''.join((
        r'^\d{1,3}(?:\.\d{1,3}){3} - \[\d{4}-\d{1,2}-\d{1,2}',
        r' \d{2}:\d{2}:\d{2}\.\d{1,6}\] \"GET \/projects\/260',
        r' HTTP\/1\.1\" [1-5]\d{2} \d+$'
    ))
    for line in sys.stdin:
        if 'exit' == line.rstrip():
            break
        line_match = re.fullmatch(pattern, line.rstrip())
        if not line_match:
            print('> Wrong format, try again')
        else:
            print('\n> ' + line_match.group())
            match2 = re.search(r'\b[1-5]\d{2} \d+$', line.rstrip())
            if match2:
                status, fs_str = match2.group().split(' ')
                print(f'\n> {status} {fs_str}')
            else:
                print(match2)
