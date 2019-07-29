class BankAccount:

    def init(self, number):
        self.money = 0
        self.number = number

    def str(self):
        return "{} {}".format(self.number, self.money)

    def deposit(self, amount):
        self.money += amount

    def withdraw(self, amount):
        if self.money >= amount:
            self.money -= amount
        else:
            print('Not enough money for transaction')

    def transfer(self, destination, amount):
        self.withdraw(amount)
        destination.deposit(amount)


class OverdraftBankAccount(BankAccount):
    def init(self, limit=1000):
        self.limit = limit
        super(OverdraftBankAccount, self).init()

    def withdraw(self, amount):
        if amount <= self.limit:
            self.money -= amount


# пример не хардкодного доабления аргумента "ставка" в наследника
# если надо прокинуть обязательный арг "номер"
class SavingAccount(BankAccount):
    def init(self, number, stavka):
        super().init(number)
        self.stavka = stavka


bank_account1 = SavingAccount("ABCD-DEFG-1234-1234", 20)
print(bank_account1)