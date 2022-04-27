class Point:
    color = 'red'
    circle = 2

    def __new__(cls, *args, **kwargs):
        print('Вызов __new__ для ' + str(cls))
        return super().__new__(cls)  # возвращаем для создания

    def __init__(self, x, y):  # можно сразу сделать х=0 и у=0, тогда при инициализации класса не надо укащываит
        print('вызов __init__')
        self.x = x
        self.y = y

    # def __del__(self):           #ударяет объект и вызывает себя перед удалением
    #     print('Delite: ' + str(self))

    # def set_coords(self, x, y):
    #     self.x = x
    #     self.y = y
    #
    # def get_coords(self):
    #     return (self.x, self.y)


pr = Point(4, 6)  # сначала создать
print(pr)
# print(pr.__dict__)              #проверяем значения
# pr.set_coords(1, 2)             #потом можно инициализировать значения для метода, но проще через инит
# print(pr.get_coords())        #вызываем чисто метод
# f = getattr(pr, 'get_coords')   #hz
# print(f())                      #печатаем
