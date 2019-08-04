# -*- coding: utf-8 -*-
import argparse
import os
from fmt.enc.html import HtmlFormat
from fmt.enc.no import NoFormat
from fmt.dec.parser import Parser
from fmt.enc.converter import convert


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
