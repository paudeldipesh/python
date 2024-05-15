ability_one = {
    1: 68,
    2: 90,
    3: 78,
    4: 89,
    5: 67,
}

ability_two = {
    6: 78,
    7: 89,
}

ability_one.update(ability_two)
print(ability_one)

ability_one.popitem()
print(ability_one)

# del ability_one
del ability_one[6]
print(ability_one)
ability_one.clear()
print(ability_one)

empty_dict = {}
print(empty_dict)