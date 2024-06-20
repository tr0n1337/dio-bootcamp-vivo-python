class Vehicle:
    def __init__(self, color, plate, wheels):
        self.color = color
        self.plate = plate
        self.wheels = wheels

    def start_engine(self):
        print("Starting engine..")


class Motorcycle(Vehicle):
    pass


class Car(Vehicle):
    def __init__(self, color, plate, wheels, exhaust):
        self.exhaust = exhaust

    def has_exhaust(self):
        print(
          f"{ 'Have exhaust' if self.exhaust else 'No exhaust, VRUMMMM'}")


motorcycle = Motorcycle('red', "123", 2)
motorcycle.start_engine()

car = Car('black', "321", 4, False)
car.start_engine()
car.has_exhaust()
