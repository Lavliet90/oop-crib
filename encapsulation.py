from accessify import private, protected


class Point:
    def __init__(self, x=0, y=0, z=0):
        self.__x = self.__y = self.__z = 0
        if self.__check_value(x) and self.__check_value(y) and self.__check_value(z):
            self.__x = x
            self.__y = y
            self.__z = z

    @private  # никак не обратишься потом, для очень сильной защиты методов
    @classmethod
    def __check_value(cls, x):
        return type(x) in (int, float)

    def set_coord(self, x, y, z):
        if self.__check_value(x) and self.__check_value(y) and self.__check_value(z):
            self.__x = x
            self.__y = y
            self.__z = z
        else:
            raise ValueError('Координаты должны быть числами')

    def get_coords(self):
        return self.__z, self.__y, self.__x


pt = Point(1, 2, 3)
pt.x = 300
pt.y = 'fwefw'
pt.z = 2324  # создаст. но не переопределит
# pt.set_coord(23, 'efe', 35) #не переопределит, т.к. второй параметр не пройдет валидность и вызовет ошибку
pt.set_coord(15, 4, 99)
print(pt.get_coords())

print(pt.y, pt.x,
      pt.z)  # т.к. они приватные, то без черточки посто вызывает овые выдуманные объекты. Z имеем из переопределения
# print(pt.__y, pt.x)#те, что при создании метода. К х нельзя обращаться как к закрытой переменной
# print(pt.__z) #нельзя обращаться вне класса

print(dir(pt))
print(pt._Point__y)  # но так делать нельзя
'''
для улучшения приватности pip install accessify
'''
