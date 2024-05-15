dict_one = {
    True: "Paudel is developer",
    69: "This is the position",
    "greet": "Hello world"
}

print(dict_one[True])
print(dict_one["greet"])
print(dict_one.get(70))

for key in dict_one.keys():
  print(f"The value of key {key} is {dict_one[key]}")

for key, value in dict_one.items():
  print(f"Key {key} has {value}")