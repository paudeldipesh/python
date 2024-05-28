class Person:
    def __init__(self, name):
        self.name = name

    def introduce(self):
        print(f"Hello, my name is {self.name}.")


class Developer(Person):
    def __init__(self, name, language):
        super().__init__(name)
        self.language = language

    def introduce(self):
        super().introduce()
        print(f"I am a developer specializing in {self.language}.")


class Trader(Person):
    def __init__(self, name, market):
        super().__init__(name)
        self.market = market

    def introduce(self):
        super().introduce()
        print(f"I am a trader in the {self.market}.")


developer = Developer("Dipesh Paudel", "Python")
trader = Trader("Dinesh Paudel", "Stock Market")

developer.introduce()
trader.introduce()
