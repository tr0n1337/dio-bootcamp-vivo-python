BALANCE = 450
WITHDRAW = 200

# Equal
EQUAL = BALANCE == WITHDRAW
print(f"Equal: {EQUAL}")  # False

# Inequality
INEQUALITY = BALANCE != WITHDRAW
print(f"Inequality :{INEQUALITY}")  # True

# Bigger than
BIGGER_THEN = BALANCE > WITHDRAW
print(f"Bigger than: {BIGGER_THEN}")  # True

# Bigger than or equal
BIGGER_THAN_OR_EQUAL = BALANCE >= WITHDRAW
print(f"Bigger then or equal: {BIGGER_THAN_OR_EQUAL}")  # True

# Less than
LESS_THAN = BALANCE < WITHDRAW
print(f"Less than: {LESS_THAN}")  # False

# Less than or equal
LESS_THAN_OR_EQUAL = BALANCE <= WITHDRAW
print(f"Less than or equal: {LESS_THAN_OR_EQUAL}")  # False
