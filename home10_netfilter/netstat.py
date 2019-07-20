# !/usr/bin/env python
# -*- coding: utf-8 -*-
FILE_TO_READ_FROM = "netstat.txt"
BREAKER_STRING = "Active Multipath Internet connections"


def get_content(filename):
    with open(filename, "r") as f:
        content = f.readlines()
        return content


def truncate(callback, breaker_string):
    truncated_list = []
    for line in callback(FILE_TO_READ_FROM):
        if breaker_string in line:
            break
        else:
            truncated_list.append(line)
    truncated = "\n".join(truncated_list)
    return truncated


print(truncate(get_content, BREAKER_STRING))
