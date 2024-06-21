class Bird():
    def flight(self):
        print("Flying...")


class Ostrich(Bird):
    def flight(self):
        super().flight()


class Sparrow(Bird):
    def flight(self):
        print("Sparrow don't flight")


# FIXME: bad example
class Plane(Bird):
    def flight(self):
        print("Taking off...")


def flight_plan(obj):
    obj.flight()


flight_plan(Plane())
flight_plan(Ostrich())
flight_plan(Sparrow())
