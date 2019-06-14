import sys

forbidden_words = ["hui", "govno", "muravei"]


def make_filtration(word):
    if not word.lower() in forbidden_words:
        return word
    else:
        return len(word) * '*'


def analyze_input(str_):
    for _ in str_:
        if not _.isalpha():
            print("Bad input")
            sys.exit()


def censor_gateway():
    intercept = input("Enter a word to check if forbidden: ")
    analyze_input(intercept)
    print(make_filtration(intercept))


if __name__ == '__main__':
    censor_gateway()
