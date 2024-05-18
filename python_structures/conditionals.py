BALANCE = 2000

try:
    WITHDRAW = float(input("Withdrawal amount: "))
except ValueError:
    print("Invalid input. Please enter a valid number.")
    exit()
except KeyboardInterrupt:
    print("Interrupt!")
    exit()
except Exception as e:
    print(f"Error: {e}")
    exit()

if WITHDRAW <= 0:
    print("Invalid value. Please enter a positive amount for withdrawal.")
elif BALANCE >= WITHDRAW:
    print("Withdrawal made!")
else:
    print("Insufficient balance")

# Ternary
STATUS = "Success" if BALANCE >= WITHDRAW else "Error"
print(STATUS)
