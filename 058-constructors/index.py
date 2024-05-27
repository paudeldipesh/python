class Person:
    def __init__(self, name, occupation):
        self.name = name
        self.occupation = occupation

    def information(self):
        print(f"{self.name} is a {self.occupation}.")


dipesh = Person("Dipesh Paudel", "Python Django Developer")
dipesh.information()
dinesh = Person("Dinesh Paudel", "Stock Market Trader")
dinesh.information()
