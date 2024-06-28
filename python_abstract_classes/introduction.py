class Student:
    school = "DIO"

    def __init__(self, name, number):
        self.name = name
        self.number = number

    def __str__(self) -> str:
        return f"{self.name} - {self.number} - {self.school}"


th = Student('Thiago', 56413)
an = Student('Anna', 56422)

print(th)
print(an)


class Person:
    def __init__(self, name=None, age=None) -> None:
        self.name = name
        self.age = age

    @classmethod
    def create_date_of_birth(cls, year, month, day, name):
        age = 2024 - year
        return cls(name, age)

    @staticmethod
    def is_of_legal_age(age) -> bool:
        return age >= 18


# p = Person('Thiago', 21)
# print(p.age, p.name)

p2 = Person.create_date_of_birth(2003, 2, 27, 'Thiago')
print(p2.age)

p3 = Person.is_of_legal_age(18)
p4 = Person.is_of_legal_age(16)
print(p3, p4)
