word = "Elephant"
for letter in word:
  print(letter, end="\n")
  if (letter == "p"):
    print("This is something special")

colors = ["red", "green", "blue", "yellow"]
for color in colors:
  print(color)
  for letter in color:
    print(letter)

for number in range(1, 13, 2):
  print(number)