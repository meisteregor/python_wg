import os
from fmt.tokens import Header, Strong, Em, Text
from fmt.error import MyIOError


class Parser:

    def __init__(self):
        pass

    def parse_file(self, filename):
        result = []
        try:
            with open(filename) as file:
                for line in file:
                    result.append(self.parse_line(line))
        except IOError:
            raise MyIOError
        return result

    def parse_line(self, line):
        line = line.strip(os.linesep)
        for header_level in range(Header.MIN_LEVEL, Header.MAX_LEVEL + 1):
            if Header.test(line, header_level):
                return Header(line, header_level)
        if Strong.test(line):
            return Strong(line)
        elif Em.test(line):
            return Em(line)
        else:
            return Text(line)
