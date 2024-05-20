value = int(input("Enter a number between 3 and 9: "))

if value < 3 or value > 9:
  raise ValueError("Value should be between 3 and 9")