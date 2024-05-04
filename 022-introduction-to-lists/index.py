list_one = [34, 56, 78, "Dipesh", True]
print(list_one)
print(type(list_one))
print(list_one[0])
print(list_one[4])
print(list_one[-2])
print(list_one[0:5])
print(list_one[0:5:2])

if 7 in list_one:
  print("Yes")
else:
  print("No")

if "pesh" in "Dipesh":
  print("Yes")

list_two = [digit * digit for digit in range(10) if digit % 2 == 0]
print(list_two)