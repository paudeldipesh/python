class Dog:
    """
    This class defines a Dog object with attributes and methods.
    """

    # Constructor (special method that gets called when creating an instance)
    def __init__(self, breed, age):
        self.breed = breed  # Instance attribute for breed
        self.age = age  # Instance attribute for age

    # Method to bark
    def bark(self):
        print(f"Woof! I'm a {self.breed} dog!")


# Create instances (objects) of the Dog class
dog_one = Dog("Labrador", 3)
dog_two = Dog("Poodle", 2)

# Accessing attributes and methods of the instances
print(dog_one.breed)  # Output: Labrador
print(dog_two.age)  # Output: 2
dog_one.bark()  # Output: Woof! I'm a Labrador dog!

# Accessing the docstring
print(Dog.__doc__)  # This will print the class docstring
