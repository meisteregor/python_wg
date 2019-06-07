BYN_TO_USD_RATIO = 0.5
BYN_TO_EUR_RATIO = 0.46
BYN_TO_RUB_RATIO = 30
BORDER_SYMBOL = "*"
SPACE_SYMBOL = " "

while True:
    value = input('Enter amount of BYN:\n')  # keep it in string form
    try:
        convert = float(value)  # if it's a valid float, then it's also a valid int
        assert convert >= 0
        break
    except:
        print("enter a valid number")


def num_digits(n):
    count = 0
    curr = n  # remaining string you're currently evaluating
    while curr != '':
        digit = curr[len(curr) - 1]  # get final char
        curr = curr[:len(curr) - 1]  # trim last char off the string
        if not digit.isdigit():
            # ignore things like decimal points or negative signs
            continue
        count += 1
    return count


def is_float(n):
    symbols_count = len(n)
    digits_count = sum(1 for _ in n if _.isdigit())
    return True if symbols_count != digits_count else False


def num_symbols(n):
    number_of_symbols = num_digits(n) + 1 if is_float(n) else num_digits(n)
    return number_of_symbols


def take_diff_count(n):
    diff_count = longest_length - len(str(n))
    return diff_count


BYN = float(value) if is_float else int(value)
BYN = round(BYN, 2)
USD = round(BYN * BYN_TO_USD_RATIO, 2)
EUR = round(BYN * BYN_TO_EUR_RATIO, 2)
RUB = round(BYN * BYN_TO_RUB_RATIO, 2)

longest_length = len(str(RUB))
horizontal_separator = BORDER_SYMBOL * (10 + longest_length)

print(horizontal_separator)
print(BORDER_SYMBOL, SPACE_SYMBOL, "BYN", SPACE_SYMBOL, BORDER_SYMBOL, SPACE_SYMBOL, BYN,
      SPACE_SYMBOL * take_diff_count(BYN), SPACE_SYMBOL, BORDER_SYMBOL, sep='')
print(horizontal_separator)
print(BORDER_SYMBOL, SPACE_SYMBOL, "USD", SPACE_SYMBOL, BORDER_SYMBOL, SPACE_SYMBOL, USD,
      SPACE_SYMBOL * take_diff_count(USD), SPACE_SYMBOL, BORDER_SYMBOL, sep='')
print(horizontal_separator)
print(BORDER_SYMBOL, SPACE_SYMBOL, "EUR", SPACE_SYMBOL, BORDER_SYMBOL, SPACE_SYMBOL, EUR,
      SPACE_SYMBOL * take_diff_count(EUR), SPACE_SYMBOL, BORDER_SYMBOL, sep='')
print(horizontal_separator)
print(BORDER_SYMBOL, SPACE_SYMBOL, "RUB", SPACE_SYMBOL, BORDER_SYMBOL, SPACE_SYMBOL, RUB,
      SPACE_SYMBOL * take_diff_count(RUB), SPACE_SYMBOL, BORDER_SYMBOL, sep='')
print(horizontal_separator)
