list_one = [34, 89, 12, 53, 11, 11, 11]
list_one.append(7)

list_one.sort(reverse=True)
print(list_one)

list_one.reverse()
print(list_one)
print(list_one.index(12))
print(list_one.count(11))

list_two = list_one.copy()
list_two[0] = 0
print(list_two)
print(list_one)

list_two.insert(0, 99)
print(list_two)

list_three = [100, 200, 300]
list_two.extend(list_three)
print(list_two)

digit_list_one = [1, 2]
digit_list_two = [3, 4]
digit_list_three = digit_list_one + digit_list_two
print(digit_list_three)