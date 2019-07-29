# -*- coding: utf-8 -*-

import argparse
import sys
import os


class Text(object):

    def __init__(self, text):
        self.text = text

    @staticmethod
    def test(text):
        return True if text else False

    def __str__(self):
        return "{}: {}".format(type(self), self.text)


class Header(Text):
    MIN_LEVEL = 1
    MAX_LEVEL = 6

    def __init__(self, text, level):
        text = text.strip("#" * level + " ")
        super(Header, self).__init__(text)
        self.level = level

    @staticmethod
    def test(text, level):
        return text.startswith("#" * level + " ")


class Em(Text):

    def __init__(self, text):
        text = text.strip("_").strip("*")
        super(Em, self).__init__(text)

    @staticmethod
    def test(text):
        return not Strong.test(text) and (
                text.startswith("_") and text.endswith("_") or text.startswith("*") and text.endswith("*"))


class Strong(Text):

    def __init__(self, text):
        text = text.strip("__").strip("**")
        super(Strong, self).__init__(text)

    @staticmethod
    def test(text):
        return text.startswith("__") and text.endswith("__") or text.startswith("**") and text.endswith("**")


class Parser:

    def __init__(self):
        pass

    def parse_file(self, filename):
        result = []
        with open(filename) as file:
            for line in file:
                result.append(self.parse_line(line))
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


class BaseFormat:

    @staticmethod
    def name():
        """ Вернуть название выходного формата, например, html, pdf, etc"""
        sys.exit("Implement me")

    def convert_header(self, header):
        """ Вернуть header в соответствующем формате"""
        sys.exit("Implement me")

    def convert_strong(self, strong):
        """ Вернуть header в соответствующем формате"""
        sys.exit("Implement me")

    def convert_em(self, em):
        """ Вернуть header в соответствующем формате"""
        sys.exit("Implement me")

    def convert_text(self, text):
        """ Вернуть header в соответствующем формате"""
        sys.exit("Implement me")


class NoFormat(BaseFormat):
    @staticmethod
    def name():
        """ Вернуть название выходного формата, например, html, pdf, etc"""
        return "no"

    def convert_header(self, header):
        """ Вернуть header в соответствующем формате"""
        return header.text.upper()

    def convert_strong(self, strong):
        """ Вернуть header в соответствующем формате"""
        return strong.text

    def convert_em(self, em):
        """ Вернуть header в соответствующем формате"""
        return em.text

    def convert_text(self, text):
        """ Вернуть header в соответствующем формате"""
        return text.text


class HtmlFormat(BaseFormat):
    @staticmethod
    def name():
        """ Вернуть название выходного формата, например, html, pdf, etc"""
        return "html"

    def convert_header(self, header):
        """ Вернуть header в соответствующем формате"""
        return "<h{}>{}</h{}>".format(header.level, header.text, header.level)

    def convert_strong(self, strong):
        """ Вернуть header в соответствующем формате"""
        return "<b>" + strong.text + "</b>"

    def convert_em(self, em):
        """ Вернуть header в соответствующем формате"""
        return "<em>" + em.text + "</em>"

    def convert_text(self, text):
        """ Вернуть header в соответствующем формате"""
        return "<br>" if not text.text else text.text


def convert(tokens, format):
    result = []
    for token in tokens:
        if isinstance(token, Header):
            result.append(format.convert_header(token))
        elif isinstance(token, Em):
            result.append(format.convert_em(token))
        elif isinstance(token, Strong):
            result.append(format.convert_strong(token))
        else:
            result.append(format.convert_text(token))
    return result


FORMATS = {
    NoFormat.name(): NoFormat,
    HtmlFormat.name(): HtmlFormat,
}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", help="input file", required=True)
    parser.add_argument("--output-format", help="output format", required=True)
    args = parser.parse_args()

    parser = Parser()
    tokens = parser.parse_file(args.input)
    converted = convert(tokens, FORMATS[args.output_format]())

    print(os.linesep.join(converted))


if __name__ == '__main__':
    main()
