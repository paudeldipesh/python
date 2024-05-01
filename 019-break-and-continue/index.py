for digit in range(12):
  if digit == 10:
    break  # Skips the loop
  print(f"5 X {digit+1} = {5 * (digit+1)}")

for digit in range(10):
  if digit > 3 and digit < 7:
    print("Skip the iteration")
    continue  # Skips the iteration
  print(f"6 X {digit+1} = {6 * (digit+1)}")

count = 0  # Mimicking do-while
while True:
  print(count)
  count += 1
  if count == 3:
    break