class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def show_details(self):
        print(f"Name: {self.name} and Species: {self.species}")


animal = Animal("Parrot", "Kakapo")
animal.show_details()


class Dog(Animal):
    def __init__(self, name, breed):
        Animal.__init__(self, name, species="Dog")
        self.breed = breed

    def show_details(self):
        Animal.show_details(self)
        print(f"Breed: {self.breed}")


dog = Dog("Tommy", "Saint Bernard")
dog.show_details()


class GoldenRetriever(Dog):
    def __init__(self, name, color):
        Dog.__init__(self, name, breed="Golden Retriever")
        self.color = color

    def show_details(self):
        Dog.show_details(self)
        print(f"Color: {self.color}")


golden_retriever = GoldenRetriever("Bob", "White")
golden_retriever.show_details()
print(GoldenRetriever.mro())
