class Person:
    def __init__(self, name, year_of_birth):
        self.name = name
        self._year_of_birth = year_of_birth

    @property
    def age(self):
        _current_year = 2024
        return _current_year - self._year_of_birth


person = Person('Thiago', 2003)
print(f"Name: {person.name} \tAge: {person.age}")
