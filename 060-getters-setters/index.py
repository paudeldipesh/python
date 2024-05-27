class ControlledAccessMethods:
    def __init__(self, value):
        self._value = value  # Private attribute

    def show(self):
        print(f"Given value is {self._value}.")

    @property
    def double(self):
        return 2 * self._value  # Getter

    @double.setter
    def double(self, new_value):  # Setter
        if new_value < 0:
            print("Error: New value cannot be negative.")
        else:
            self._value = new_value * 3 / 2


first_instance = ControlledAccessMethods(10)
first_instance.show()
print(first_instance.double)  # From getter

first_instance.double = 5
print(first_instance.double)  # From setter
