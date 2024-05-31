class Vector:
    def __init__(self, i, j, k):
        self.i = i
        self.j = j
        self.k = k

    def __add__(self, x):
        return Vector(self.i + x.i, self.j + x.j, self.k + x.k)

    def __str__(self):
        return f"{self.i}i + {self.j}j + {self.k}k"


vector_one = Vector(3, 4, 5)
vector_two = Vector(6, 7, 8)
vector_three = vector_one + vector_two
print(vector_three)
print(type(vector_three))
