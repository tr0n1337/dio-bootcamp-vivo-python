class Animal:
    def __init__(self, n_paws):
        self.n_paws = n_paws

    def __str__(self):
        return f"{self.__class__.__name__}: \
{', '.join([f'{key}={value}' for key, value in self.__dict__.items()])}"


class Mammal(Animal):
    def __init__(self, fur_color, **kw):
        self.fur_color = fur_color
        super().__init__(**kw)


class Bird(Animal):
    def __init__(self, beak_color, **kw):
        self.beak_color = beak_color
        super().__init__(**kw)


class Dog(Mammal):
    pass


class Platypus(Mammal, Bird):
    def __init__(self, n_paws, beak_color, fur_color):
        super().__init__(
          n_paws=n_paws, beak_color=beak_color, fur_color=fur_color)


dog = Dog(n_paws=4, fur_color='red')
print(dog)

platypus = Platypus(n_paws=2, beak_color='orange', fur_color='red')
print(platypus)
