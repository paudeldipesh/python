def factorial(number):
  """
  This function returns the factorial of a given number.
  """
  if (number == 0 or number == 1):
    return 1
  else:
    return number * factorial(number - 1)


print(factorial(3))


def fibonacci(digit):
  """
  This function calculates the fibonacci of a given number.
  """
  if digit == 0 or digit == 1:
    return digit
  else:
    return fibonacci(digit - 1) + fibonacci(digit - 2)


print(fibonacci(5))