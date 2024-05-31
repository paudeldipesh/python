class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def make_sound(self):
        print("Sound made by the animal.")


class Dog(Animal):
    def __init__(self, name, species, breed):
        super().__init__(name, species)
        self.breed = breed

    def make_sound(self):
        super().make_sound()


dog = Dog("Tommy", "Dog", "German Shepherd")
dog.make_sound()
