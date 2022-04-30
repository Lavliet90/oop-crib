'''
три плюса:
-ограничение создаваемых локальных свойств
-уменьшение занимаемой памяти
-ускорение работы с локальными свойствами
'''


class Point:
    '''
    120 байт, работает медленно
    '''

    def __init__(self, a, b):
        self.a = a
        self.b = b


class Point2D:
    '''
    32  байта только весит и ускоряет работу
    '''
    __slots__ = ('b', 'a', '__length')
    # можно создавать только с этими именами, в классе выше можно придумать любое другое свойство
    MAX_COORD = 100  # тут проблем нет

    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.__length = (a * a + b * b) ** 0.5

    @property
    def length(self):
        return self.__length

    @length.setter
    def length(self, value):
        self.__length = value

class Point3D(Point2D):
    __slots__ = ('z') #возьмет свойства из родителя + дописанные тут
    pass


pt1 = Point2D(1, 2)
print(pt1.MAX_COORD)
print(pt1.length)
pt1.length = 10
print(pt1.length)
pt3 = Point3D(23, 2)
pt3.z = 34
print(pt3.z)