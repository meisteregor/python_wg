from fmt.enc.base import BaseFormat


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
