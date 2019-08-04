import sys


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
