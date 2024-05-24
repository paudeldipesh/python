first = 899
second = 89

if first > second:
  print(f"{first} is greater than {second}")
else:
  print(f"{second} is greater than {first}")

print(f"{first} is greater than {second}") if first > second else print(
    f"{first} is equal to {second}") if first == second else print(
        f"{second} is greater than {first}")

third = 7 if first > second else 0
print(third)