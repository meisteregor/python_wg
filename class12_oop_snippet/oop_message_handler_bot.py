class Bot:
    def init(self, name):
        self.name = name

    def is_command(self, msg):
        if msg.startswith("/"):
            return True
        else:
            return False

    def process_message(self, msg):
        return "smth"


class PoliteBot(Bot):

    def process_message(self, msg):
        if self.is_command(msg):
            return 'ok'
        else:
            return "not ok"


class PizzaBot(Bot):

    def process_message(self, msg):
        if self.is_command(msg):
            return 'pizza'
        else:
            return 'not pizza'


if name == 'main':
    user_input = input('Select bot:')
    if user_input == 'pizza':
        bot = PizzaBot('Pizza')
    elif user_input == 'ok':
        bot = PoliteBot('Вася ок')
    else:
        exit()

    while True:
        msg = input('> ')
        print(bot.process_message(msg))