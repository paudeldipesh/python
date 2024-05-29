class Employee:
    company = "Apple"

    def show(self):
        print(f"{self.name} works on {self.company}.")

    @classmethod
    def change_company(self, new_company):
        self.company = new_company


employee_one = Employee()
employee_one.name = "Dipesh"
employee_one.show()
employee_one.change_company("Microsoft")
employee_one.show()
print(
    Employee.company
)  # Prints Apple, after adding the class with the @classmethod decorator, it will print Microsoft
