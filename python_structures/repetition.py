# FOR
VOWELS = "AEIOU"
try:
    TEXT = str(input('Enter a text: '))
except ValueError:
    print("Invalid input. Please enter a valid string.")
    exit()
except KeyboardInterrupt:
    print("Interrupt!")
    exit()
except Exception as e:
    print(f"Error: {e}")
    exit()

for letter in TEXT:
    conditional = "VOWEL" if letter.upper() in VOWELS else "CONSONANT"
    print(f"{letter} --- {conditional}")
print("\n")

# RANGE
RANGE_1 = range(10)  # 0, 1, 2, 3, 4, 5, 6, 7, 8, 9
RANGE_2 = range(1, 10)  # 1, 2, 3, 4, 5, 6, 7, 8, 9
RANGE_3 = range(0, 51, 5)  # 0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50

# FOR with RANGE
for number in range(10):
    print(number, end=" ")
print("\n")

# WHILE
INPUT = "[1] To withdraw \n[2] Extract \n[0] Exit \n:"
while True:
    try:
        option = int(input(INPUT))
    except ValueError:
        print("Invalid input. Please enter a valid int number.")
        continue
    except KeyboardInterrupt:
        print("Interrupt!")
        exit()
    except Exception as e:
        print(f"Error: {e}")
        exit()

    if option < 0 or option > 2:
        print("Invalid option!")
    elif option == 1:
        print("Making a withdrawal...")
    elif option == 2:
        print("Viewing extract...")
    elif option == 0:
        print("Exiting...")
        break
