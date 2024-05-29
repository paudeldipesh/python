data = (1, 2, 3, 4, 5)
print(dir(data))
print(data.__add__)


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.version = 1


person_one = Person("Dipesh", 23)
print(person_one.__dict__)

print(help(str))
