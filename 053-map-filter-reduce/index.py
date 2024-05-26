from functools import reduce


def cube(number):
    return number**3


number_list = [1, 2, 3, 4, 5]
print(sum(number_list))
cube_number_list = []
for number in number_list:
    cube_number_list.append(cube(number))
print(cube_number_list)

cube_list = list(map(cube, number_list))
filter_list = list(filter(lambda number: number % 2 != 0, number_list))
product_list = reduce(
    lambda number_one, number_two: number_one * number_two, number_list
)
print(cube_list)
print(filter_list)
print(product_list)
