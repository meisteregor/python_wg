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
