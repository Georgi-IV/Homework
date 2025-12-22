class Wallet:
    def __init__(self, amount, currency):
        self.amount = amount
        self.currency = currency

    def add_money(self, amount):
        self.amount += amount
        print(f"There are added {amount} {self.currency}")

    def spend_money(self, amount):
        if amount <= self.amount:
            self.amount -= amount
            print(f"There are spent {amount} {self.currency}")
        else:
            print("There are not enough money in the wallet!")

    def show_balance(self):
        print(f"Balance: {self.amount} {self.currency}")

    @staticmethod
    def convert(amount, rate):
        return amount * rate

my_wallet = Wallet(100, "BGN")
my_wallet.show_balance()

my_wallet.add_money(50)
my_wallet.spend_money(30)
my_wallet.spend_money(200) 
my_wallet.show_balance()