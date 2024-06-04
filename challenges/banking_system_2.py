import os
import getpass


class User:
    def __init__(self,
                 username: str,
                 password: str,
                 name: str,
                 date_of_birth: str,
                 cpf: str,
                 address: str,
                 accounts: list[dict[str, str]],
                 extract: list[dict[str, float]],
                 balance: float):
        self.username = username
        self.password = password
        self.name = name
        self.date_of_birth = date_of_birth
        self.cpf = cpf
        self.address = address
        self.accounts = accounts
        self.extract = extract
        self.balance = balance


def cls() -> None:
    os.system('cls' if os.name == 'nt' else 'clear')


def main_menu() -> None:
    cls()
    print(" USER ".center(30, "="))
    print("[c] Create user")
    print("[l] Login")
    print("[q] Quit")
    print("".center(30, "="))


def account_menu() -> None:
    cls()
    print(" Account Menu ".center(30, "="))
    print("[c] Create checking account")
    print("[l] List checking accounts")
    print("[d] Deposit")
    print("[w] Withdraw")
    print("[e] Extract")
    print("[q] Quit")
    print("".center(30, "="))


def back_menu(option: str) -> None:
    cls()
    print("".center(30, "="))
    print("[b] back to main menu")
    if option:
        print(option)
    print("".center(30, "="))


def extract_menu(user: User):
    print("\n")
    print(" Extract ".center(30, "="))
    if len(user.extract) > 0:
        for item in user.extract:
            for key in item:
                print(f"[{key}] R${item[key]:.2f}")
    print()
    print("".center(30, "="))
    print(f"Balance: R${user.balance:.2f}")
    print("".center(30, "="))


def has_dict_in_list(
    dict_list: list[User],
    target_dict: dict[str, str]
):
    for item in dict_list:
        match = True
        for key, value in target_dict.items():
            if not hasattr(item, key) or getattr(item, key) != value:
                match = False
                break
        if match:
            return item
    return False


def create_user(users: list[User]) -> None:
    go_back_text = "Please enter for go back menu..."

    user_data = {
        "username": "",
        "password": "",
        "name": "",
        "date_of_birth": "",
        "cpf": 0,
        "address": "",
        "accounts": [],
        "extract": [],
        "balance": 0
        }

    while True:
        cls()

        try:
            print(" Create user ".center(30, "="))
            user_data["username"] = str(
                input("Username: ").strip())
            if has_dict_in_list(
                users,
                {"username": user_data["username"]}
            ):
                cls()
                print("This USERNAME has already been registered")
                input(go_back_text)
                break

            user_data["password"] = getpass.getpass("Password: ")
            user_data["name"] = str(
                input("Name: "))
            user_data["date_of_birth"] = str(
                input("Date of birth (DD/MM/AAAA): "))
            user_data["address"] = str(
                input("Address: "))
            user_data["cpf"] = int(
                input("CPF (only numbers): "))

            if any(value == "" for value in user_data.values()):
                cls()
                print("Please fill in all fields!")
                input(go_back_text)
                break

            if has_dict_in_list(
                    users,
                    {"cpf": str(user_data["cpf"])}
                    ):
                cls()
                print("This CPF has already been registered")
                input(go_back_text)
                break

        except ValueError:
            print("\nValueError!")
            exit()
        except KeyboardInterrupt:
            cls()
            print("\nKeyboardInterrupt!")
            exit()

        cls()
        new_user = User(**user_data)
        users.append(new_user)
        print("User created!")
        input(go_back_text)
        break


def create_checking_account(user: User):
    go_back_text = "Please enter for go back menu..."
    checking_account = {
        "agency": "0001",
        "account_number": 0
    }

    while True:
        cls()

        try:
            print(" Create checking account ".center(50, "="))
            cpf_input = str(
                input("Enter your CPF to confirm create checking account: "))
            if cpf_input == user.cpf:
                if len(user.accounts) == 0:
                    checking_account["account_number"] += 1
                    user.accounts.append(checking_account)
                else:
                    checking_account["account_number"] = len(
                        user.accounts) + 1
                    user.accounts.append(checking_account)
                cls()
                print("Checking account created!")
                input(go_back_text)
                break
            else:
                cls()
                input("Invalid CPF, please enter for try again...")
                continue
        except ValueError:
            print("\nValueError!")
            exit()
        except KeyboardInterrupt:
            cls()
            print("\nKeyboardInterrupt!")
            exit()


def list_checking_accounts(user: User):
    input_text = "=> "

    while True:
        cls()

        try:
            back_menu("")
            print()
            print(" Accounts ".center(30, "="))
            print()
            if len(user.accounts) > 0:
                for account in user.accounts:
                    for key, value in account.items():
                        print(f"{key}: {value}")
                    print()
                print("".center(30, "="))
                print()
            else:
                print("No checking accounts found.")

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
            cls()
            print("\nKeyboardInterrupt!")
            exit()


def login(users: list[User]) -> User:
    user_credentials = {
        "username": "",
        "password": ""
    }

    while True:
        cls()

        try:
            print(" Login ".center(30, "="))
            user_credentials["username"] = str(input("Username: ")).strip()
            user_credentials["password"] = getpass.getpass("Password: ")
            user = has_dict_in_list(
                    users,
                    {
                        "username": user_credentials["username"],
                        "password": user_credentials["password"]
                    }
                    )
            if user:
                handle_account_options(user)

                return user

        except ValueError:
            print("\nValueError!")
            exit()
        except KeyboardInterrupt:
            cls()
            print("\nKeyboardInterrupt!")
            exit()


def list_users(users: list[User]) -> None:
    cls()
    go_back_text = "Please enter for go back menu..."

    print(" Users ".center(30, "="))
    for user in users:
        for key, value in user.__dict__.items():
            print(f"{key}: {value}")
        print("".center(30, "="))
    print()
    input(go_back_text)


def deposit_funds(user: User) -> None:
    deposit_input_text = "Enter deposit amount => "

    while True:
        cls()

        try:
            DEPOSIT_INPUT = float(input(deposit_input_text))
            if DEPOSIT_INPUT > 0:
                user.balance += DEPOSIT_INPUT
                user.extract.append({"+": DEPOSIT_INPUT})
                print(f"Successfully deposited: R${DEPOSIT_INPUT:.2f}")
                deposit_input_text = "=> "

                while True:
                    cls()

                    try:
                        back_menu("[n] new deposit")
                        NEW_DEPOSIT_INPUT = str(input(deposit_input_text))

                        if NEW_DEPOSIT_INPUT == "n":
                            break
                        elif NEW_DEPOSIT_INPUT == "b":
                            return
                        else:
                            deposit_input_text = "Invalid option, " + \
                                "please enter with a valid option => "
                            continue
                    except ValueError:
                        deposit_input_text = "Invalid option, " + \
                            "please enter with a valid option => "
                        continue
                    except KeyboardInterrupt:
                        cls()
                        print("\nKeyboardInterrupt!")
                        exit()
        except ValueError:
            deposit_input_text = "Invalid amount, " + \
              "please enter with a valid amount => "
            continue
        except KeyboardInterrupt:
            cls()
            print("\nKeyboardInterrupt!")
            exit()


def withdraw_funds(*,
                   user: User,
                   withdrawals: int) -> None:
    LIMIT = 500
    withdraw_text_input = "Enter withdraw amount => "
    go_back_text = "Please enter for go back menu..."

    if withdrawals > 3:
        cls()
        print("Max limit withdrawals per day hit!")
        input(go_back_text)

    while True:
        cls()

        try:
            WITHDRAW_INPUT = float(input(withdraw_text_input))
            if WITHDRAW_INPUT > LIMIT:
                withdraw_text_input = "Max limit for withdraw " + \
                    "is R$500.00, please enter with a new amount => "
                continue
            elif withdrawals <= 3 and WITHDRAW_INPUT <= LIMIT:
                user.extract.append({"-": WITHDRAW_INPUT})
                user.balance -= WITHDRAW_INPUT
                print(f"Successfully withdraw: R${WITHDRAW_INPUT:.2f}")
                break
        except ValueError:
            withdraw_text_input = "Invalid amount, " + \
                "please enter with a valid amount => "
            continue
        except KeyboardInterrupt:
            cls()
            print("\nKeyboardInterrupt!")
            exit()


def view_extract(user: User) -> None:
    input_text = '=> '

    while True:
        cls()

        try:
            back_menu("")
            extract_menu(user)
            BACK_MENU_INPUT = str(input(input_text)).lower()
            if BACK_MENU_INPUT == "b":
                break
            else:
                cls()
                back_menu("")
                input_text = "Invalid input, " + \
                    "please enter with a valid option => "
                continue
        except KeyboardInterrupt:
            cls()
            print("\nKeyboardInterrupt!")
            exit()


def handle_main_options(users: list[User]):
    input_text = '=> '

    while True:
        cls()

        try:
            main_menu()
            option = str(input(input_text)).lower()
            if option == "c":
                input_text = "=> "
                create_user(users)
                continue
            elif option == "l":
                input_text = "=> "
                login(users)
            elif option == "q":
                input_text = "=> "
                print("Exiting...")
                exit()
            elif option == "adm":
                input_text = "=> "
                list_users(users)
                continue
            else:
                input_text = "Invalid input, " + \
                    "please enter with a valid option => "
                continue
        except ValueError:
            cls()
            print("\nValue Error!")
            exit()
        except KeyboardInterrupt:
            cls()
            print("\nKeyboardInterrupt!")
            exit()


def handle_account_options(user: User):
    withdrawals = 0
    input_text = "=> "

    while True:
        cls()

        try:
            account_menu()
            option = str(input(input_text)).lower()

            if option == "c":
                input_text = "=> "
                create_checking_account(user)
            elif option == "l":
                input_text = "=> "
                list_checking_accounts(user)
            elif option == "d":
                input_text = "=> "
                deposit_funds(user)
            elif option == "w":
                input_text = "=> "
                withdrawals += 1
                withdraw_funds(user=user, withdrawals=withdrawals)
                continue
            elif option == "e":
                input_text = "=> "
                view_extract(user)
            elif option == "q":
                print("Exiting...")
                break
            else:
                input_text = "Invalid option, " + \
                    "please enter with a valid option => "
                continue
        except KeyboardInterrupt:
            cls()
            print("\nKeyboardInterrupt!")
            exit()


def main() -> None:
    users = [
        User(
            username="adm",
            password="adm",
            name="Admin",
            date_of_birth="27/02/2003",
            cpf="1",
            address="l, 1, b, sp, sp",
            accounts=[],
            extract=[],
            balance=100000.0
        )
    ]

    handle_main_options(users=users)


if __name__ == "__main__":
    main()
