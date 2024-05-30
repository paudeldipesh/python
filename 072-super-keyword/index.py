class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def employee_method(self):
        print(f"You're {self.name} with ID: {self.id}.")


class Programmer(Employee):
    def __init__(self, name, id, language):
        super().__init__(name, id)
        self.language = language

    def employee_method(self):
        super().employee_method()
        print(f"ID: {self.id}, {self.name} needs to code in {self.language}.")

    def programmer_method(self):
        print(f"Programmer code in {self.language}.")


dinesh = Employee("Dinesh", 123)
dinesh.employee_method()
dipesh = Programmer("Dipesh", 345, "Python")
dipesh.employee_method()
dipesh.programmer_method()
