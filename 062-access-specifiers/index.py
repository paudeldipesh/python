class Employee:
    # Constructor
    def __init__(self, name, age, role):
        self.name = name  # Public variable
        self._role = role  # Protected variable
        self.__age = age  # Private variable


employee_one = Employee("Dipesh Paudel", "Software Developer", 23)
print(employee_one.name)  # Accessing name
print(employee_one._role)  # Accessing role
# print(employee_one.__age)  # Cannot be accessed directly
print(employee_one.__dir__())  # Name Mangling
print(employee_one._Employee__age)  # Accessing age
