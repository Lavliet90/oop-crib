'''
протектед с __ не дает доступ любому дочернему классу
_ дает, это чисто условность
'''


class Geom:
    name = 'Geom'
    __name_figure = 'Figure'

    def __init__(self, x1, x2, y1, y2):
        print(f'Initialization Geom for {self.__class__}')
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2
        self._name_figure = self.__name_figure

    def __veryfy_cord(self, coord):   #тоже можно вызвать только внутри этого класса
        return 0 <= coord <= 100


class Rect(Geom):
    def __init__(self, x1, x2, y1, y2, fill='red'):
        super().__init__(x1, x2, y1, y2)
        self.__fill = fill

    def get_coords(self):
        print(self._x1, self._y1)


r = Rect(0, 0, 10, 20)
print(r.__dict__)
print(r.name)
# print(r.__name_figure)   #не покажет, т.к. тоже приватна
print(r._name_figure)  # выводит, т.к. уровень доступа ниже
r.get_coords()