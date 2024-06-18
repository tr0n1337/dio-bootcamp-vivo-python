class BicycleShop:
    def __init__(self, color, model, year, value):
        self.color = color
        self.model = model
        self.year = year
        self.value = value

    def show_props(self):
        print(f"{self.color}, {self.model}, {self.year}, {self.value}")

    def buzinar(self):
        print("buzinou...")

    def parar(self):
        print("parando...")

    def correr(self):
        print("correr...")

    def __str__(self):
        return f"{self.__class__.__name__}"


bike_1 = BicycleShop("Red", "titan", "2020", 20000)
bike_1.correr()
bike_1.show_props()
print(bike_1.__str__())
