# Normal
index = 0
marks = [12, 56, 32, 98, 12, 45]
for mark in marks:
  print(mark)
  if index == 3:
    print("Awesome!")
  index += 1

print("\n-------------------\n")

# Enumerate
marks = [12, 56, 32, 98, 12, 45]
for index, mark in enumerate(marks):
  print(mark)
  if index == 3:
    print("Awesome!")