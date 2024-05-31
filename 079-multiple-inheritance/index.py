class Dancer:
    def __init__(self, dance):
        self.dance = dance

    def show(self):
        print(f"The dance is {self.dance}")


class Employee:
    def __init__(self, name):
        self.name = name

    def show(self):
        print(f"The name is {self.name}")


class DancerEmployee(Dancer, Employee):
    def __init__(self, dance, name, salary):
        Dancer.__init__(self, dance)
        Employee.__init__(self, name)
        self.salary = salary

    def info(self):
        print(f"{self.name} charges {self.salary} for {self.dance}")


mamata = DancerEmployee("Cultural Dance", "Mamata Gautam", "50000")
mamata.info()
print(DancerEmployee.mro())
mamata.show()
