class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = list(marks)

    def __getitem__(self, item):
        if 0 <= item < len(self.marks):
            return self.marks[item]
        else:
            raise IndexError('Неверный индекс')

    def __setitem__(self, key, value):
        if not isinstance(key, int) or  key < 0:
            raise TypeError('Индекс должен быть целым неотрицательным числом')
        if key >= len(self.marks):
            off = key +1 - len(self.marks)
            self.marks.extend([None]*off)

        self.marks[key] = value

    def __delitem__(self, key):
        if not isinstance(key, int) or key < 0:
            raise TypeError('Индекс должен быть целым неотрицательным числом')
        del self.marks[key]

s1 = Student('jan', [3, 5, 6, 7, 3])
s1[10] = 4   #работает благодаря setitem и расширяется, если индекс больше длины списка

del s1[2]
print(s1.marks)
print(s1[2])  # без гетайтем s1.marks[2]
