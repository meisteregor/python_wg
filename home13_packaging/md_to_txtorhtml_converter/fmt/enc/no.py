from fmt.enc.base import BaseFormat


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
