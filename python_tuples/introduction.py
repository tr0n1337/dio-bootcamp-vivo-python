# Tuple is unchangeable
fruits = ("orange", "grape", "apple")
print(f"Fruits: {fruits}")
print(f"Fruits 1: {fruits[0]}")
print(f"Fruits 2: {fruits[1]}")
print(f"Fruits -1: {fruits[-1]}")

letters = tuple("python")
print(f"Letters: {letters}")

numbers = tuple(range(1, 5))
print(f"Numbers: {numbers}")

country = ("Brasil",)  # is a tuple
# country = ("Brasil")  not is a tuple
print(f"Country: {country}")

matriz = (
  (1, "a", 2),
  ("b", 3, 4),
  (5, 6, "c")
  )

print(f"Matriz: {matriz[0]}")
print(f"Matriz: {matriz[0][0]}")
print(f"Matriz: {matriz[0][-1]}")
print(f"Matriz: {matriz[-1][-1]}")

tuple = list("Python")
print(f"Tuple '2:': {tuple[2:]}")
print(f"Tuple ':2': {tuple[2:]}")
print(f"Tuple '1:3': {tuple[1:3]}")
print(f"Tuple '0:3:2': {tuple[0:3:2]}")
print(f"Tuple '::': {tuple[::]}")
print(f"Tuple '::-1': {tuple[::-1]}")

cars = ("gol", "civic", "celta")
for car in cars:
    print(f"Car: {car}")

for index, car in enumerate(cars):
    print(f"[{index}]: {car}")
