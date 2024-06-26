BALANCE = 1000
WITHDRAW = 200
LIMIT = 100
EMERGENCY_CONTACTS = []
SPECIAL_ACCOUNT = True

# AND operator
AND_OPERATOR = BALANCE >= WITHDRAW and BALANCE <= LIMIT
print(f"And: {AND_OPERATOR}")  # False

# OR operator
OR_OPERATOR = BALANCE >= WITHDRAW or BALANCE <= LIMIT
print(f"Or: {OR_OPERATOR}")  # True

# NOT operator
NOT_OPERATOR_1 = not 1000 > 1500
print(f"Not: {NOT_OPERATOR_1}")  # True

NOT_OPERATOR_2 = not EMERGENCY_CONTACTS
print(f"Not: {NOT_OPERATOR_2}")  # True

NOT_OPERATOR_3 = not "withdraw 1500;"
print(f"Not: {NOT_OPERATOR_3}")  # False

NOT_OPERATOR_4 = not ""
print(f"Not: {NOT_OPERATOR_4}")  # True

# Parentheses
PARENTHESES_1 = (BALANCE >= WITHDRAW and BALANCE <= LIMIT) or (
  SPECIAL_ACCOUNT and BALANCE >= WITHDRAW)

print(f"Parentheses: {PARENTHESES_1}")  # True
