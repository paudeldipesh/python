number = 7
print(f"Global: {number}")


def hello_dipesh():
    number = 14
    name = "Dipesh"
    global country
    country = "Nepal"
    print(f"Local: {number}")
    print(f"Hello {name}!")


hello_dipesh()
print(f"Global: {number}")
# print(name) # This is local variable and not accessible outside of the function
print(f"Global: {country}")
