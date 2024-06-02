def number_generator():
    for i in range(50):
        yield i


gen = number_generator()

for j in gen:
    print(j)
