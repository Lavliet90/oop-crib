# class Point:
#     MAX_COORD = 100
#     MIN_COORD = 0


class Meta(type):
    def __new__(cls, name, base, attrs):
        attrs.update({'MAX_COORD': 100, 'MIN_COORD': 0})
        return type.__new__(cls, name, base, attrs)

    # def __init__(cls, name, base, attrs):
    #     super().__init__(name, base, attrs)
    #     cls.MAX_COORD = 100
    #     cls.MIN_COORD = 0


# def create_class_point(name, base, attrs):
#     attrs.update({'MAX_COORD': 100, 'MIN_COORD': 0})
#     return type(name, base, attrs)

class Point(metaclass=Meta):
    def get_coord(self):
        return (0, 0)


pt = Point()
print(pt.MAX_COORD)
print(pt.MIN_COORD)

# A = type('Point2',  {'MAX_COORD': 100, 'MIN_COORD': 0})  # то же самое
# print(A.__mro__)
#
#
# def method1(self):
#     print(self.__dict__)
#
# A = type('Point2', {'MAX_COORD': 100, 'method1': method1})  # то же самое
# pt = A()
