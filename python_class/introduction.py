class Dog:
    def __init__(self, name, color, awake: bool = True):
        self.name = name
        self.color = color
        self.awake = awake

    def bark(self):
        print("Au au")

    def sleep(self):
        self.awake = False
        print("Zzzzzzzz...")


dog_1 = Dog("Chappie", "yellow", False)
dog_2 = Dog("Aladim", "black and white")

dog_1.bark()

print(dog_2.awake)
dog_2.sleep()
print(dog_2.awake)
