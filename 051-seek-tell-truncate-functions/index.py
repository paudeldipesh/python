with open("file.txt", "r") as file:
    print(type(file))
    file.seek(7)
    tell = file.tell()
    print(tell)
    data = file.read(6)
    print(data)

with open("sample.txt", "w") as file:
    file.write("Hello World!")
    file.truncate(5)

with open("sample.txt", "r") as file:
    print(file.read())
