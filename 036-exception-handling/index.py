number = input("Enter a number: ")
print(f"Multiplication Table of {number}.")

try:
  for digit in range(1, 11):
    print(f"{number} X {digit} = {int(number) * digit}")
except Exception as error:
  print(error)

index = input("Enter a index: ")
list_of_numbers = [1, 2, 3, 4, 5]
try:
  print(list_of_numbers[int(index)])
except ValueError:
  print("Number is not an integer")
except IndexError:
  print("Invalid index")