class Geom:
    name = 'Geom'

    def __init__(self, x1, x2, y1, y2):
        print(f'Initializator Geom for {self.__class__}')
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2

    def draw(self):
        print('Draw')


class Line(Geom):

    def draw(self):
        print('Draw line')


class Rect(Geom):
    def __init__(self, x1, x2, y1, y2, fill=None):
        super().__init__(x1, x2, y1, y2)   #delegation
        print(f'Initializator Rect')
        self.fill = fill

    def draw(self):
        print('Draw line')


l = Line(1, 2, 3, 4)
r = Rect(2, 3, 4, 5)
print(l.__dict__)
print(r.__dict__)
