class Math:
    def __init__(self, number):
        self.number = number

    def add_to_number(self, digit):
        self.number = self.number + digit

    @staticmethod  # Independent of object or instance of the class
    def add(a, b):
        return a + b


instance_one = Math(5)
print(instance_one.number)
instance_one.add_to_number(7)
print(instance_one.number)
print(instance_one.add(1, 99))
print(Math.add(8, 9))
