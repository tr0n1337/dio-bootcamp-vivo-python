numbers = set([1, 2, 3, 1, 3, 4])
fruit = set("abacaxi")
cars = set(("palio", "gol", "celta", "palio"))

print(f"Numbers: {numbers}")
print(f"Fruit: {fruit}")
print(f"Cars: {cars}")

languages = {"python", "java", "python"}
print(f"Languages: {languages}")

numbers = list(numbers)
print(f"Number [0]: {numbers[0]}")

for car in cars:
    print(f"Car: {car}")

for index, car in enumerate(cars):
    print(f"{index}: {car}")
