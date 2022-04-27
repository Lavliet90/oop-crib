'''
методы для арифметики
'''

class Clock:
    __DAY = 86400

    def __init__(self, seconds: int):
        if not isinstance(seconds, int):
            raise TypeError('Секунды должны быть целым числом')
        self.seconds = seconds % self.__DAY

    def get_time(self):
        s = self.seconds % 60
        m = (self.seconds // 60) % 60
        h = (self.seconds // 3600) % 24
        return f'{self.__getformatted(h)}:{self.__getformatted(m)}:{self.__getformatted(s)}'

    @classmethod
    def __getformatted(cls, x):
        return str(x).rjust(2, '0')

    def __add__(self, other):   #__radd__, __iadd__(чтобы не создавать новый экземпляр)
        if not isinstance(other, (int, Clock)):
            raise ArithmeticError('Правое число должно быть интом or Clock')
        sc = other
        if isinstance(other, Clock):
            sc = other.seconds
        return Clock(self.seconds + sc)




c1 = Clock(1000)
c2 = Clock(2000)
c1 += 100   # без add c1.seconds+=100
c3 = c1 + c2
c4 = c3+c1

print(c4.get_time())