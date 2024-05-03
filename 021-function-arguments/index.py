def average(a, b=3):
  return print(f"The average is {(a+b)/2}")


average(2, 4)
average(1)
average(a=3)


def custom_average(*numbers):  # *numbers is a tuple
  print(type(numbers))
  sum = 0
  for digit in numbers:
    sum += digit
  return f"The custom average is {sum/len(numbers)}"


get_custom_average = custom_average(1, 2, 3, 4, 5)
print(get_custom_average)


def say_hello(**name):  # **name is a dictionary
  print(type(name))
  return print(f"Hello {name['first_name']} {name['last_name']}")


say_hello(first_name="Dipesh", last_name="Paudel")