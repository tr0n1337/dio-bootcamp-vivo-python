class Account:
    def __init__(self, n_agency, balance=0):
        self._balance = balance  # _ is equal to private
        self.n_agency = n_agency

    def deposit(self, value):
        self._balance += value

    def withdraw(self, value):
        self._balance -= value

    def show_balance(self,):
        return self._balance


account = Account('0001', 100)
print(account.n_agency)
account.withdraw(10)
account.deposit(120)
print(account.show_balance())
