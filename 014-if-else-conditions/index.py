# Conditional statements: <, >, <=, >=, ==, !=
age = int(input("Enter your age: "))
if age >= 18:
  print("You can drive")
else:
  print("You cann't drive")

number = int(input("Enter a number? "))
if number < 0:
  print("Number is negative")
  if (number < -100):
    print("Number is very negative")
elif number == 0:
  print("Number is zero")
elif number > 9:
  print("Number is positive and greater than 9")
else:
  print("Number is positive")
  if (number != 7):
    print("Number is not special")
    if (number < 3):
      print("Number is less than 3")
  else:
    print("Number is 7")