class Point:
    MAX_COORDS = 100
    MIN_COORDS = 0

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def set_coords(self, x, y):
        if self.MIN_COORDS <= x <= self.MAX_COORDS:
            self.x = x
            self.y = y

    # @classmethod
    # def set_bound(cls, left):     #только так можно менять атрибуты класса
    #     cls.MIN_COORDS = left

    def __getattribute__(self,
                         item):  # вызываается, когда вызывают переменную. например для формирования исключений, чтобы не пытались получить какие-то атрибуты
        if item == 'x':
            raise ValueError('Доступ запрещен')
        else:
            return object.__getattribute__(self, item)

    def __setattr__(self, key, value):  # вызывается каждый раз, когда идет присвоение атрибуту значения
        if key == 'z':
            raise AttributeError('Плохое имя для атрибута')
        else:
            object.__setattr__(self, key, value)
            # self.x = value  #чисто рекурсию разгонит

    def __getattr__(self, item):  # когда обращение к несуществующему
        return False
        print('не существует: ' + item)

    def __delattr__(self, item):  # при удалении любого атрибута класса
        print('delite ' + item)
        object.__delattr__(self, item)


pt1 = Point(1, 4)
pt2 = Point(34, 32)
print(pt2.MAX_CS)
del pt1.x
# a = pt1.x
# print(a)
# print(pt1.MAX_COORDS)
# pt1.set_bound(-100)
# print(pt1.__dict__)
# print(Point.__dict__)
