class Student:
    school_name = "Krishna School"
    number_of_students = 0

    def __init__(self, name, raise_amount):
        self.name = name
        self.raise_amount = raise_amount
        Student.number_of_students += 1

    def show_details(self):
        print(f"Student name is {self.name} and raise amount is {self.raise_amount}.")


student_one = Student("Dipesh Paudel", 0.4)
student_one.show_details()

print(student_one.school_name)
student_one.school_name = "Shiva School"
print(student_one.school_name)

student_two = Student("Dinesh Paudel", 0.5)
student_three = Student("Dikesh Paudel", 0.6)
print(Student.number_of_students)
