def show_message():
    print('Hello World!')


def show_message_2(name: str):
    print(f"Welcome {name}!")


def show_message_3(name: str = 'Anonym'):
    print(f"Welcome {name}!")


show_message()
show_message_2(name="Thiago")
show_message_2("Fernandes")
show_message_3()
show_message_3("Souza")


def calc(numbers: list[int]) -> int:
    return sum(numbers)


def predecessor_and_successor(number: int) -> tuple[int, int]:
    predecessor = number - 1
    successor = number + 1

    return predecessor, successor


print(calc([10, 20, 34]))
print(predecessor_and_successor(10))


def save_car(brand: str, model: str, year: int, plate: str):
    print(f"Car saved with successfully! {brand}/{model}/{year}/{plate}")


save_car("Fiat", "Palio", 1999, "ABC-1234")
save_car(**{
  "brand": "Fiat",  "model": "Palio", "year": 1999, "plate": "abc-1234"
  })


def show_poem(data: str, *args, **kwargs):
    text = "\n".join(args)
    meta_data = "\n".join([f"{key.title()}: {value}" for key, value in
                           kwargs.items()])
    message = f"{data}\n\n{text}\n\n{meta_data}"
    print(message)


show_poem(
          "Zen of Python", "Beautiful is better than ugly",
          "Explicit is better than ugly.",
          autor="Tim petters",
          ano=1999
        )


# Positional Only
def create_car(model, year, plate,  /, brand, motor, fuel):
    print(model, year, plate, brand, motor, fuel)


create_car("Palio", 1999, "ABC-1234", brand="Fiat", motor="1.0",
           fuel="Gasolina1")


# Keyword only
def create_car_2(*, model, year, plate, brand, motor, fuel):
    print(model, year, plate, brand, motor, fuel)


create_car_2(model="Palio", year=1999, plate="ABC-1234", brand="Fiat",
             motor="1.0", fuel="Gasolina")


# Keyword and Positional only
def create_car_3(model, year, plate, /, *, brand, motor, fuel):
    print(model, year, plate, brand, motor, fuel)


create_car_3("Palio", 1999, "ABC-1234", brand="Fiat",
             motor="1.0", fuel="Gasolina")


# First class objects
def sum_2(a: int, b: int):
    return a + b


def subtract(a: int, b: int):
    return a - b


def show_result(a: int, b: int, func) -> None:
    result = func(a, b)
    print(f"Result is: {result}")


show_result(5, 3, sum_2)
show_result(5, 3, subtract)
