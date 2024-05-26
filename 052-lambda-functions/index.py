average = lambda number_one, number_two: (number_one + number_two) / 2
print(average(2, 4))


def apply(function, value):
    return function(value)


print(apply(lambda number: number * 2, 6))
print(apply(lambda number: number * 3, 6))
