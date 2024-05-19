fruits = ["orange", "grape", "apple"]
print(f"Fruits: {fruits}")
print(f"Fruit 0: {fruits[0]}")
print(f"Fruit 2: {fruits[2]}")
print(f"Fruit -1: {fruits[-1]}")
print(f"Fruit -2: {fruits[-2]}")
print(f"Fruit -3: {fruits[-2]}")

fruits = []
print(f"Fruits: {fruits}")

letters = list("Python")
print(f"Letters: {letters}")

numbers = list(range(10))
print(f"Numbers: {numbers}")

car = ["Ferrari", "F8", 4200000, 2020, 2900, "São Paulo", True]
print(f"Car: {car}")

matriz = [
  [1, "a", 2],
  ["b", 3, 4],
  [6, 5, "c"]
]

print(f"Matriz 1: {matriz[0]}")
print(f"Matriz 2: {matriz[0][0]}")
print(f"Matriz 3: {matriz[0][-1]}")
print(f"Matriz 4: {matriz[-1][-1]}")

list = list("Python")
print(f"List 1: {list[2:]}")
print(f"List 2: {list[:2]}")
print(f"List 3: {list[1:3]}")
print(f"List 4: {list[0:3:2]}")
print(f"List 5: {list[::]}")
print(f"List 6: {list[::-1]}")

cars = ["gol", "golf", "eclipse", "civic"]

for car in cars:
    print(f"Car: {car}")

for index, car in enumerate(cars):
    print(f"[{index}]: {car}")

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pairs = []

for number in numbers:
    if number % 2 == 0:
        pairs.append(number)

print(f"Pairs: {pairs}")

pairs = [number for number in numbers if number % 2 == 0]
print(f"Pairs: {pairs}")

pairs = [number ** 2 for number in numbers]
print(f"Pairs: {pairs}")
