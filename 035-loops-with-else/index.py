for item in range(5):
  print(item)
  if item == 2:
    break
else:
  print("Not available")

numbers = [1, 2, 3, 4, 5]
for number in numbers:
  if number % 2 == 0:
    continue
  print(number)
else:
  print("Not avaialable")

i = 0
while i < 6:
  print(i)
  i += 1
  if i == 2:
    break
else:
  print("Not avaialable")