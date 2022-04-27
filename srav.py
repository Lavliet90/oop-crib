'''
__eq__  - ==
__ne__  - !=
__lt__  - <
__le__  - <=
__gt__  - >
__ge__  - >=

можно использовать противоположную
'''


class Clock:
    __DAY = 86400

    def __init__(self, seconds: int):
        if not isinstance(seconds, int):
            raise TypeError('Not int')
        self.seconds = seconds % self.__DAY

    @classmethod
    def __verify_data(cls, other):
        if not isinstance(other, (int, Clock)):
            raise TypeError('Clock or int')

        return other if isinstance(other, int) else other.seconds

    def __eq__(self, other):  # Для сравнения, чтобы при сравнении классов сравнялись не айдишники класса
        sc = self.__verify_data(other)
        return self.seconds == sc

    def __lt__(self, other):
        sc = self.__verify_data(other)
        return self.seconds < sc


c1 = Clock(1000)
c2 = Clock(2000)
print(c1 == c2)
print(c1 != c2)  # работает благодяра тому, что есть ==
print(c1 > c2)
print(c1 < c2)
