file = open("marks.txt", "r")
iterator = 0
while True:
    iterator += 1
    line = file.readline()
    if not line:
        break
    mark_one = line.split(",")[0]
    mark_two = line.split(",")[1]
    mark_three = line.split(",")[2]
    print(f"Mark of student '{iterator}' in Mathematics is {mark_one}")
    print(f"Mark of student '{iterator}' in Science is {mark_two}")
    print(f"Mark of student '{iterator}' in Computer is {mark_three}")

file = open("ai.txt", "w")
lines = ["line 1\n", "line 2\n", "line 3\n"]
file.writelines(lines)
file.close()
