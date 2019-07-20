# !/usr/bin/env python
# -*- coding: utf-8 -*-
import argparse
import subprocess
import sys

UTILITY = "netstat.py"

parser = argparse.ArgumentParser(description='netstat parser that reads from file')
parser.add_argument('--output', type=argparse.FileType('w'), help="set file for output")
parser.add_argument('--state', help="connection status", type=str, nargs='+',
                    default=['ESTABLISHED'], choices=['ESTABLISHED', 'CLOSE_WAIT'])
args = parser.parse_args()


def write_content(filename, content):
    with open(filename, "w") as f:
        f.write(content)


def intersection(lst1, lst2):
    return list(set(lst1) & set(lst2))


def filtering(content, filter_array):
    filtered_list = []
    for substring in content.split("\n"):
        tmp_list = intersection(substring.upper().split(), filter_array)
        if tmp_list:
            filtered_list.append(substring)
    filtered = "\n".join(filtered_list)
    return filtered


def main():
    data_to_parse = subprocess.check_output([sys.executable, UTILITY])
    parsed_data = filtering(data_to_parse, args.state)
    if args.output:
        write_content(args.output.name, parsed_data)
    else:
        print(parsed_data)


if __name__ == '__main__':
    main()
