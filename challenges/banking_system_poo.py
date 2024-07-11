import os
import getpass
from abc import ABC, abstractmethod
from datetime import date, datetime
from typing import TypeVar, Union, Literal, List

T = TypeVar('T')


class System:
    def cls(self) -> None:
        os.system('cls' if os.name == 'nt' else 'clear')


class Database:
    def __init__(self):
        mock_data = {
            "username": "adm",
            "password": "adm",
            "name": "Admin",
            "date_of_birth": date(1999, 9, 9),
            "address": "Rua administrador, 999",
            "document": "99988877706"
        }
        mock_pf = PF(**mock_data)
        mock_account = CheckingAccount(mock_pf, 1, 500, 3)
        mock_pf.add_account(mock_account)
        self._db: list['PF'] = [mock_pf]

    @property
    def list(self):
        return self._db

    def create(self, customer: 'PF'):
        self._db.append(customer)


class Menu:
    def main(self) -> None:
        print(" Customer ".center(40, "="))
        print("[c] Create customer")
        print("[l] Login")
        print("[q] Quit")
        print("".center(40, "="))

    def account(self) -> None:
        print(" Account Menu ".center(40, "="))
        print("[c] Create checking account")
        print("[l] List checking accounts")
        print("[d] Deposit")
        print("[w] Withdraw")
        print("[e] Extract")
        print("[q] Quit")
        print("".center(40, "="))

    def back(self) -> None:
        print("".center(40, "="))
        print("[b] back to main menu")
        print("".center(40, "="))
        print()


class Response:
    def ok(self, msg: str):
        print(
            f"{' Success '.center(70, '=')}"
            f"\n[Successfully operation]: {msg}\n{''.center(70, '=')}")

    def err(self, msg):
        print(
            f"{' Error '.center(70, '=')}"
            f"\n[Unsuccessful operation]: {msg}\n{''.center(70, '=')}")


class Customer:
    def __init__(self,
                 username: str,
                 password: str,
                 name: str,
                 date_of_birth: date,
                 address: str):
        self._username = username
        self._password = password
        self.name = name
        self.date_of_birth = date_of_birth
        self.address = address
        self.accounts: List['Account'] = []

    @property
    def username(self) -> str:
        return self._username

    @property
    def password(self) -> str:
        return self._password

    def make_transaction(self,
                         account: 'Account',
                         transaction: 'Transaction'):
        transaction.register(account)

    def add_account(self, account: 'Account'):
        self.accounts.append(account)


class PF(Customer):
    def __init__(self,
                 username: str,
                 password: str,
                 name: str,
                 date_of_birth: date,
                 address: str,
                 document: str
                 ):
        super().__init__(
            username,
            password,
            name,
            date_of_birth,
            address)
        self.document = document


class Account:
    def __init__(self,
                 customer: PF,
                 number: int,
                 ):
        self._balance = 0
        self._number = number
        self._agency = "0001"
        self._customer = customer
        self._history = History()

    @classmethod
    def create_account(cls, customer: PF, number: int) -> 'Account':
        return cls(customer, number)

    @property
    def balance(self) -> float:
        return self._balance

    @property
    def number(self) -> int:
        return self._number

    @property
    def agency(self) -> str:
        return self._agency

    @property
    def customer(self) -> PF:
        return self._customer

    @property
    def history(self) -> 'History':
        return self._history

    def withdraw(self, value: float) -> bool:
        balance = self.balance

        if value > balance:
            Response().err("Insufficient balance.")
            return False
        elif value <= 0:
            Response().err("Invalid value.")
            return False
        else:
            self._balance -= value
            Response().ok(f"Successful withdrawal of R${value:.2f}")
            return True

    def deposit(self, value: float) -> bool:
        if value <= 0:
            Response().err("Invalid value.")
            return False

        self._balance += value
        Response().ok(f"Deposit of R${value:.2f} successfully made")
        return True


class CheckingAccount(Account):
    def __init__(self,
                 customer: PF,
                 number: int,
                 limit: float = 500,
                 withdraw_limit: int = 3,
                 ):
        super().__init__(customer, number)
        self.limit = limit
        self.withdraw_limit = withdraw_limit

    def withdraw(self, value: float) -> bool:
        transactions = self.history.transactions
        withdrawals = [
          transaction
          for transaction in transactions
          if transaction["type"] == Withdraw.__name__
        ]
        number_of_withdrawals = len(withdrawals)

        if value > self.limit:
            Response().err("Amount greater than the withdrawal limit.")
            return False
        elif number_of_withdrawals > 2:
            Response().err("Number of withdrawals allowed reaching.")
            return False
        else:
            return super().withdraw(value)

    def __str__(self) -> str:
        return f"""\nAgency:\t{self.agency}
C/C:\t{self.number}
Holder:\t{self.customer.name}"""


class History:
    def __init__(self):
        self._transactions = []

    @property
    def transactions(self) -> list[dict]:
        return self._transactions

    def add_transaction(self, transaction: 'Transaction'):
        self._transactions.append({
          "type": transaction.__class__.__name__,
          "value": transaction.value,
          "date": datetime.now().strftime("%d-%m-%Y %H:%M:%s")
        })


class Transaction(ABC):
    @property
    def value(self):
        pass

    @classmethod
    @abstractmethod
    def register(cls, account: Account):
        pass


class Withdraw(Transaction):
    def __init__(self, value: float):
        self._value = value

    @property
    def value(self) -> float:
        return self._value

    def register(self, account: Account) -> None:
        success_transaction = account.withdraw(self.value)

        if success_transaction:
            account.history.add_transaction(self)


class Deposit(Transaction):
    def __init__(self, value: float):
        self._value = value

    @property
    def value(self) -> float:
        return self._value

    def register(self, account: 'Account') -> None:
        success_transaction = account.deposit(self.value)

        if success_transaction:
            account.history.add_transaction(self)


class App():
    def __init__(self, db: Database):
        self._db = db

    @property
    def db(self) -> Database:
        return self._db

    def map(
        self,
        list: List[T],
        target_dict: dict[str, Union[str, int]]
    ) -> T | Literal[False]:
        for item in list:
            match = True
            for key, value in target_dict.items():
                if not hasattr(item, key) or getattr(item, key) != value:
                    match = False
                    break
            if match:
                return item
        return False

    def create_checking_account(self, customer: PF) -> None:
        go_back_text = "\nPlease enter for go back menu..."

        while True:
            System().cls()

            try:
                Menu().back()
                print(" Create checking account ".center(50, "="))
                cpf_input = str(
                    input(
                        "Enter your CPF to confirm create checking account: "))

                if cpf_input.lower() == "b":
                    break

                if cpf_input == customer.document:
                    account = CheckingAccount.create_account(
                            customer, len(customer.accounts) + 1)
                    customer.add_account(account)
                    System().cls()
                    Response().ok("Checking account created!")
                    for account in customer.accounts:
                        print(account)
                    input(go_back_text)
                    break
                else:
                    System().cls()
                    input("Invalid CPF, please enter for try again...")
                    continue
            except ValueError:
                System().cls()
                Response().err("ValueError!")
                exit()
            except KeyboardInterrupt:
                System().cls()
                Response().err("KeyboardInterrupt!")
                exit()

    def list_checking_accounts(self, customer: PF) -> None:
        input_text = "=> "

        while True:
            System().cls()

            try:
                Menu().back()
                print(" Accounts ".center(40, "="))
                if len(customer.accounts) > 0:
                    for account in customer.accounts:
                        print(account)
                    print()
                    print("".center(40, "="))
                    print()
                else:
                    print("No checking accounts found.\n")

                option = str(input(input_text))
                if option == "b":
                    break
                else:
                    input_text = "Invalid option, " + \
                                "please enter with a valid option => "
            except ValueError:
                input_text = "Invalid option, " + \
                                "please enter with a valid option => "
                continue
            except KeyboardInterrupt:
                System().cls()
                Response().err("KeyboardInterrupt!")
                exit()

    def transaction(
            self,
            customer: PF,
            type: Literal["Deposit"] | Literal["Withdraw"]) -> None:
        while True:
            account_number_input_text = "Enter with account number => "
            System().cls()

            try:
                Menu().back()
                print(f" {type} ".center(40, "="))
                account_number = input(account_number_input_text)
                if account_number == 'b':
                    break

                account = self.map(
                    customer.accounts, {"number": int(account_number)})

                if account:
                    while True:
                        System().cls()

                        try:
                            print(f" {type} ".center(40, "="))
                            transaction_input = float(
                                input("Enter deposit amount => "))
                            if transaction_input > 0:
                                System().cls()
                                if type == 'Deposit':
                                    transaction = Deposit(transaction_input)
                                else:
                                    transaction = Withdraw(transaction_input)
                                customer.make_transaction(account, transaction)
                                input("\nPlease enter for go back menu...")
                                break
                        except ValueError:
                            System().cls()
                            Response().err("ValueError!")
                            input(
                                "Invalid value, please enter for try again...")
                            continue
                        except KeyboardInterrupt:
                            System().cls()
                            Response().err("KeyboardInterrupt!")
                            exit()
                    break
                else:
                    System().cls()
                    input("Account not found, please enter for try again...")
                    continue
            except ValueError:
                System().cls()
                Response().err("ValueError!")
                input("Invalid value, please enter for try again...")
                continue
            except KeyboardInterrupt:
                System().cls()
                Response().err("KeyboardInterrupt!")
                exit()

    def extract(self, customer: PF) -> None:
        while True:
            account_number_input_text = "Enter with account number => "
            System().cls()

            try:
                Menu().back()
                print(" Extract ".center(40, "="))
                account_number = input(account_number_input_text)
                if str(account_number).lower() == 'b':
                    break

                account = self.map(
                    customer.accounts, {"number": int(account_number)})
                if account:
                    transactions = account.history.transactions
                    if transactions:
                        System().cls()
                        print(" Extract ".center(40, "="))
                        for transaction in transactions:
                            for key, value in transaction.items():
                                print(f"{key}: {value}")
                            print()
                        input("Please enter for back to menu...")
                    else:
                        System().cls()
                        print(" Extract ".center(40, "="))
                        print("No transactions performed.\n")
                        input("Please enter for back to menu...")
                else:
                    System().cls()
                    input(
                        "Account not found, please enter for try again...")
                    continue
            except ValueError:
                System().cls()
                Response().err("ValueError!")
                input("Invalid value, please enter for try again...")
                continue
            except KeyboardInterrupt:
                System().cls()
                Response().err("KeyboardInterrupt!")
                exit()

    def create_customer(self) -> None:
        go_back_text = "Please enter for go back menu..."
        customer_data = {}

        while True:
            System().cls()

            try:
                print(" Create user ".center(30, "="))
                username = str(input("Username: ").strip())
                if self.map(self.db.list, {"username": username}):
                    System().cls()
                    Response().err(
                        "This USERNAME has already been registered.")
                    input(go_back_text)
                    break
                password = getpass.getpass("Password: ")
                name = str(input("Name: "))
                print("\nDate of Birth (Only numbers)")
                date_of_birth = date(
                    int(input("Year: ")),
                    int(input("Month: ")),
                    int(input("Day: ")))
                address = str(input("Address: "))
                document = int(input("Document (only numbers): "))
                customer_data = {
                        "username": username,
                        "password": password,
                        "name": name,
                        "date_of_birth": date_of_birth,
                        "address": address,
                        "document": document
                    }

                if any(value == "" for value in customer_data.values()):
                    System().cls()
                    Response().err("Please fill in all fields!.")
                    input(go_back_text)
                    break
                elif self.map(self.db.list, {"document": str(document)}):
                    System().cls()
                    Response().err(
                        "This Document has already been registered.")
                    input(go_back_text)
                    break
                else:
                    break

            except ValueError:
                Response().err("ValueError!.")
                exit()
            except KeyboardInterrupt:
                System().cls()
                Response().err("KeyboardInterrupt!.")
                exit()

        System().cls()
        new_user = PF(**customer_data)
        self.db.create(new_user)
        Response().ok("User created!")
        input(go_back_text)

    def customer_login(self) -> None:
        while True:
            System().cls()

            try:
                print(" Login ".center(30, "="))
                username = str(
                    input("Username: ")).strip()
                password = getpass.getpass(
                    "Password: ")
                customer = self.map(
                        self.db.list,
                        {
                            "username": username,
                            "password": password
                        })
                if customer:
                    System().cls()
                    input(
                        "Logged with successfully, "
                        "please enter for continue...")
                    self.account_options(customer)
                    break
                else:
                    System().cls()
                    option = str(input(
                        "Customer not found, please enter for try again..."
                        )).lower()
                    if option != "b":
                        continue
                    else:
                        break

            except ValueError:
                Response().err("ValueError!")
                exit()
            except KeyboardInterrupt:
                System().cls()
                Response().err("KeyboardInterrupt!")
                exit()

    def account_options(self, customer: PF) -> None:
        input_text = "=> "

        while True:
            System().cls()

            try:
                print(" Customer ".center(40, "="))
                print(f"Name: {customer.name}")
                print(f"Document: {customer.document}")
                print(f"Address: {customer.address}")
                print("".center(40, "="))
                print()
                Menu().account()
                option = str(input(input_text)).lower()

                if option == "c":
                    input_text = "=> "
                    self.create_checking_account(customer)
                elif option == "l":
                    input_text = "=> "
                    self.list_checking_accounts(customer)
                elif option == "d":
                    input_text = "=> "
                    self.transaction(customer, 'Deposit')
                elif option == "w":
                    input_text = "=> "
                    self.transaction(customer, "Withdraw")
                elif option == "e":
                    input_text = "=> "
                    self.extract(customer)
                elif option == "q":
                    print("Exiting...")
                    break
                else:
                    input_text = "Invalid option, " + \
                        "please enter with a valid option => "
                    continue
            except KeyboardInterrupt:
                System().cls()
                Response().err("KeyboardInterrupt!")
                exit()


def main() -> None:
    db = Database()
    app = App(db)
    input_text = '=> '

    while True:
        System().cls()

        try:
            Menu().main()
            option = str(input(input_text)).lower()
            if option == "c":
                input_text = "=> "
                app.create_customer()
            elif option == "l":
                input_text = "=> "
                app.customer_login()
            elif option == "q":
                input_text = "=> "
                print("Exiting...")
                exit()
            elif option == "adm":
                System().cls()
                print(" Admin ".center(30, "="))
                for item in db.list:
                    for keys in item.__dict__:
                        print(f"{keys}: {item.__dict__[keys]}")
                print("".center(30, "="))
                input("\nPlease enter for back to menu...")
            else:
                input_text = "Invalid input, " + \
                            "please enter with a valid option => "
                continue
        except ValueError:
            System().cls()
            Response().err("Value Error!")
            exit()
        except KeyboardInterrupt:
            System().cls()
            Response().err("KeyboardInterrupt!")
            exit()


if __name__ == "__main__":
    main()
