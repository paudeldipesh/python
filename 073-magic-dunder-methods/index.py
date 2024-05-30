class Person:
    def __init__(self, name, occupation):
        self.name = name
        self.occupation = occupation

    def __len__(self):
        iterator = 0
        for index in self.name:
            iterator = iterator + 1
        return iterator

    def __call__(self):
        print("This is Person class call method.")

    def __repr__(self):
        return f'{self.__class__.__name__}("{self.name}", "{self.occupation}")'


class Employee(Person):
    def __init__(self, name, occupation, company):
        super().__init__(name, occupation)
        self.company = company

    def introduce(self):
        print(f"Hi, I'm {self.name}, a {self.occupation} at {self.company}.")

    def __call__(self):
        print("This is Employee class call method.")

    def __repr__(self):
        return f'{self.__class__.__name__}("{self.name}", "{self.occupation}", "{self.company}")'


dinesh = Person("Dinesh Paudel", "Stock Trader")
print(len(dinesh))
print(dinesh)
dinesh()

dipesh = Employee("Dipesh Paudel", "Software Developer", "Pwnbot")
dipesh.introduce()
print(dipesh)
dipesh()
