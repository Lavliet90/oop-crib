class Vector:
    MIN_COORD = 0
    MAX_COORD = 100

    @classmethod
    def validate(cls, arg):
        return cls.MIN_COORD <= arg <= cls.MAX_COORD

    def __init__(self, x, y):
        self.x = self.y = 0
        if Vector.validate(x) and Vector.validate(y):  # можно еще self.validate(x/y)
            self.x = x
            self.y = y

        print('Oke ' + str(self.norm2(self.x, self.y)))

    def get_coord(self):
        return self.x, self.y

    @staticmethod
    def norm2(x, y):
        return x * x + y * y + Vector.MAX_COORD  # но лучше не прибавлять такие переменные. лучше только из самой функции


v = Vector(10, 15)
z = Vector(50, 605)
res = v.get_coord()
res3 = z.get_coord()
res2 = Vector.get_coord(v)
print(res)
print(res2)
print(res3)

print(Vector.validate(5))
print(Vector.validate(500))

print(Vector.norm2(5, 6))
