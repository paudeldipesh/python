# Tuples and strings are immutable, while lists are mutable
tuple_one = (1, True, "Dipesh")

print(type(tuple_one), len(tuple_one), tuple_one)
print(tuple_one[0])
print(tuple_one[2])
print(tuple_one[1:2])

search_value = 2
if search_value in tuple_one:
  print("Yes")
else:
  print("No")