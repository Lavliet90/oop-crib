class Geom:
    name = 'Geom'

    def set_coords(self, x1, x2, y1, y2):
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2


class Line(Geom):
    def draw(self):
        print('Draw line')


class Rect(Geom):
    def draw(self):
        print('Draw rectangle')


#
g = Rect()
l = Line()
l.set_coords(1, 1, 2, 2)
g.set_coords(2, 3, 2, 2)
# l.draw()
# g.draw()
# print(l.__dict__)
# print(g.__dict__)
print(issubclass(Line, Geom))
print(isinstance(l, Geom))