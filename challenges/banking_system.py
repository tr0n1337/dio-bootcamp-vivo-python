import os


def cls() -> None:
    os.system('cls' if os.name == 'nt' else 'clear')


def main_menu() -> None:
    print("===============")
    print("[d] Deposit")
    print("[w] Withdraw")
    print("[e] Extract")
    print("[q] Quit")
    print("===============")


def back_menu(option: str) -> None:
    print("======================")
    print("[b] back to main menu")
    if option:
        print(option)
    print("======================")


def deposit_funds(balance: float, extract: str) -> tuple[float, str]:
    deposit_input_text = "Enter the deposit amount => "

    while True:
        cls()

        try:
            DEPOSIT_INPUT = float(input(deposit_input_text))
        except ValueError:
            deposit_input_text = "Invalid amount, " + \
              "please enter with a valid amount => "
            continue
        except KeyboardInterrupt:
            cls()
            print("\nKeyboardInterrupt!")
            exit()

        if DEPOSIT_INPUT > 0:
            balance += DEPOSIT_INPUT
            extract += f"\n[+] => R${DEPOSIT_INPUT:.2f}"
            print(f"Successfully deposited: R${DEPOSIT_INPUT:.2f}")
            deposit_input_text = "=> "

            while True:
                cls()

                try:
                    back_menu("[n] new deposit")
                    NEW_DEPOSIT_INPUT = str(input(deposit_input_text))
                except ValueError:
                    deposit_input_text = "Invalid option, " + \
                        "please enter with a valid option => "
                    exit()
                except KeyboardInterrupt:
                    cls()
                    print("\nKeyboardInterrupt!")
                    exit()

                if NEW_DEPOSIT_INPUT == "n":
                    return deposit_funds(balance, extract)
                elif NEW_DEPOSIT_INPUT == "b":
                    return balance, extract
        else:
            deposit_input_text = "Invalid amount, " + \
              "please enter with a valid amount => "
            continue


def withdraw_funds(withdrawals: int,
                   balance: float,
                   extract: str) -> tuple[float, str]:
    LIMIT = 500
    withdraw_text_input = "Enter the withdraw amount => "

    while True:
        cls()

        try:
            WITHDRAW_INPUT = float(input(withdraw_text_input))
        except ValueError:
            withdraw_text_input = "Invalid amount, " + \
                "please enter with a valid amount => "
            continue
        except KeyboardInterrupt:
            cls()
            print("\nKeyboardInterrupt!")
            exit()

        if WITHDRAW_INPUT > LIMIT:
            withdraw_text_input = "Max limit for withdraw is R$500.00, " + \
                "please enter with a new amount => "
            continue
        elif withdrawals > 3:
            cls()
            print("Max limit withdrawals per day hit!")
            input("Please enter for continue...")
            break
        elif withdrawals <= 3 and WITHDRAW_INPUT <= LIMIT:
            extract += f"\n[-] => R${WITHDRAW_INPUT:.2f}"
            balance -= WITHDRAW_INPUT
            print(f"Successfully withdraw: R${WITHDRAW_INPUT:.2f}")
            break

    return (balance, extract)


def view_extract(extract: str, balance: float):
    input_text = '=> '

    while True:
        cls()

        try:
            back_menu("")
            print("\n")
            print(" Extract ".center(30, "="))
            if extract:
                print(extract, "\n------------------------------")
            print(f"Balance: R${balance:.2f}")
            print("".center(30, "="))
            BACK_MENU_INPUT = str(input(input_text)).lower()
        except KeyboardInterrupt:
            print("\nKeyboardInterrupt!")
            exit()

        if BACK_MENU_INPUT == "b":
            break
        else:
            cls()
            back_menu("")
            input_text = "Invalid input, please enter with a valid option => "
            continue


def main():
    balance = 0
    withdrawals = 0
    extract = ""
    option_input_text = "=> "
    menu_options = ["d", "e", "w", "q"]

    while True:
        cls()

        try:
            main_menu()
            option = str(input(option_input_text)).lower()
        except KeyboardInterrupt:
            cls()
            print("\nKeyboardInterrupt!")
            exit()

        if option not in menu_options:
            option_input_text = "Invalid option, " + \
              "please enter with a valid option => "
            continue
        elif option == "d":
            (balance, extract) = deposit_funds(balance, extract)
        elif option == "w":
            withdrawals += 1
            (balance, extract) = withdraw_funds(withdrawals, balance, extract)
        elif option == "e":
            view_extract(extract, balance)
        elif option == "q":
            print("Exiting...")
            quit()
        else:
            break


if __name__ == "__main__":
    main()
