# class Cat:
#     def __init__(self, name):
#         self.name = name
#
#     def __repr__(self):        #возвращает новое имя при вызове класса при отладке, в консоле например
#         return f'{self.__class__}: {self.name}'
#
#     def __str__(self):          #Это для пользователя, в тех же принтах
#         return f'{self.name}'
#
#
#
#
# cat = Cat('kot')
# print(cat.name)
# print(cat)


class Point:
    def __init__(self, *args):
        self.__coords = args

    def __len__(self):  # разрешает вызывать длину
        return len(self.__coords)

    def __abs__(self):   #аналогично с верхней
        return list(map(abs, self.__coords))


p = Point(1, 2, -6)
print(len(p))
print(abs(p))
