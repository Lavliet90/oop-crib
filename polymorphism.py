class Geom:
    def get_pr(self):
        raise NotImplementedError('The get_pr method must be overridden in the child class')

class Rectangle(Geom):
    def __init__(self, w, h):
        self.w = w
        self.h = h

    def get_pr(self):
        return 2*(self.w + self.h)

class Square(Geom):
    def __init__(self, a):
        self.a = a

    def get_pr(self):
        return 4*self.a


class Triangle(Geom):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def get_pr(self):
        return self.b + self.c + self.a


r1 = Rectangle(1, 2)
r2 = Rectangle(4, 10)

s1 = Square(5)
s2 = Square(54)

t1 = Triangle(4, 6, 3)
t2 = Triangle(2, 4, 7)

geom = [r1, r2, s1, s2, t1, t2]

for g in geom:
    print(g.get_pr())

