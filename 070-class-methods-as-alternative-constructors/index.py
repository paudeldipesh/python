class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    @classmethod
    def from_string(self, string):
        return self(string.split("-")[0], int(string.split("-")[1]))


string_one = "Dipesh Paudel-100000"
employee_one = Employee.from_string(string_one)
print(employee_one.name, employee_one.salary)


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def from_string(self, string):
        name, age = string.split(", ")
        return self(name, int(age))


person_one = Person.from_string("Dinesh Paudel, 50000")
print(person_one.name, person_one.age)
