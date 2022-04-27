'''
Чтобы не держать много геттеров и сеттеров в голове
'''


class Person:
    def __init__(self, name, old):
        self.__name = name
        self.__old = old

    @property
    def old(self):
        return self.__old

    @old.setter
    def old(self, old):
        self.__old = old

    @old.deleter
    def old(self):
        del self.__old

    # old = property()
    # old = old.setter(set_old)
    # old = old.setter(get_old)


p = Person('Yan', 43)
# p.set_olf(34)
# print(p.get_old())
# print(p.old)
del p.old  # ударяем
p.old = 54  # опять создаем
print(p.__dict__)
