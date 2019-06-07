import time
import random
import sys

MANUAL_MESSAGE = """Try to earn 21 points. You can draw one card with its own value from 1 to
 10 until you'll decide its enought"""
MAIN_MENU_MESSAGE = "Welcome to O4KO\n1. Game\n2. Rules\n3. Exit"
GOODBYE_MESSAGE = "BYE!!"
UNKNOWN_BEHAVIOUR_MESSAGE = "Unknown decision. Shutting down..."
IN_GAME_INSTRUCTION_MESSAGE = "To draw a card press Enter, to stop press n\n"
CURRENT_SCORE_MESSAGE = "Your current score is: {}"
WIN_MESSAGE = "\nYOU WIN"
LOOSE_MESSAGE = "\nYOU LOOSE"
SPLIT_MESSAGE = "\nSPLIT"
BUSTED_MESSAGE = "\nLOOSE, busted: {}"


def calculate(ars):
    return sum(ars)


def generate_value():
    return random.randint(1, 10)


def call_menu():
    print(MAIN_MENU_MESSAGE)
    while True:
        entry = input("Select your decision: ")
        if entry == '1':
            start_game()
        elif entry == '2':
            print(MANUAL_MESSAGE)
            sys.exit()
        elif entry == '3':
            print(GOODBYE_MESSAGE)
            sys.exit()
        else:
            print(UNKNOWN_BEHAVIOUR_MESSAGE)
            sys.exit()


def dealer_function():
    dealer_container = []
    while sum(dealer_container) < 17:
        fresh_value = generate_value()
        dealer_container.append(fresh_value)
        curr_value = calculate(dealer_container)
        print("W8ing for dealers decision..")
        time.sleep(1)
        print("Dealer picks a card..")
        print("Current dealer score is {}\n".format(curr_value))
    return dealer_container


def start_game():
    player_container = []
    while sum(player_container) < 22:
        game_input = input(IN_GAME_INSTRUCTION_MESSAGE)
        if not game_input:
            fresh_value = generate_value()
            player_container.append(fresh_value)
            curr_value = calculate(player_container)
            print(CURRENT_SCORE_MESSAGE.format(curr_value))
        elif game_input.lower() == 'n':
            dealer_score = dealer_function()
            if sum(player_container) > sum(dealer_score):
                print(WIN_MESSAGE)
                sys.exit()
            elif sum(player_container) < sum(dealer_score) and sum(dealer_score) > 21:
                print(WIN_MESSAGE)
                sys.exit()
            elif sum(player_container) < sum(dealer_score):
                print(LOOSE_MESSAGE)
                sys.exit()
            else:
                print(SPLIT_MESSAGE)
                sys.exit()
        else:
            print(IN_GAME_INSTRUCTION_MESSAGE)
            continue
    print(BUSTED_MESSAGE.format(calculate(player_container)))
    sys.exit()


if name == 'main':
    call_menu()