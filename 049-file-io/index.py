# Reading a file
file = open("text.txt", "r")
content = file.read()
print(content)
file.close()

# Writing a file
file = open("another.txt", "w")
file.write("Hello World. ")
file.close()

# There is no need to close the file
with open("another.txt", "a") as file:
    file.write("This is inside the file. ")

# Appending a content
file = open("another.txt", "a")
file.write("Dipesh Paudel")
file.close()
