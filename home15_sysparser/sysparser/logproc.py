# !/usr/bin/env python3
# -*- coding: utf-8 -*-
import argparse
import sys

SEVERITIES = ['CRITICAL', 'WARN', 'ERROR', 'INFO', 'DEBUG']

parser = argparse.ArgumentParser()
parser.add_argument('input', help="input logfile")
parser.add_argument('--level', help="severities, all include by default", type=str, nargs='+', default=SEVERITIES,
                    choices=SEVERITIES)
parser.add_argument('--app', help="apps to grep from log", type=str, nargs='+')
parser.add_argument('--output', type=argparse.FileType('w'), help="set file for output, screen by default")
args = parser.parse_args()

severities, apps = args.level, args.app


class NotValidDataError(Exception):
    pass


def is_valid_data(arr):
    for substring in arr:
        checker_array = []
        for level in SEVERITIES:
            if level in substring:
                checker_array.append(level)
        if len(checker_array) != 1:
            return False
    return True


def take_content(filename):
    try:
        with open(filename) as f:
            content = f.readlines()
            if is_valid_data(content):
                return content
            else:
                raise NotValidDataError()
    except IOError as io:
        print(io)
        sys.exit()


def write_content(filename, content):
    with open(filename, "w") as f:
        content = "\n".join(content)
        f.write(content)


def filtering(content_list, filter_array):
    filtered_list = []
    for substring in content_list:
        for element in filter_array:
            if element in substring:
                filtered_list.append(substring)
    return filtered_list


def perform_output(parsed_data):
    if args.output:
        write_content(args.output.name, parsed_data)
    else:
        print("\n".join(parsed_data))


def main():
    data = take_content(args.input)
    data = filtering(data, apps)
    data = filtering(data, severities)
    perform_output(data)


if __name__ == '__main__':
    main()
