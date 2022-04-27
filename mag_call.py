import math


class Derivate:  # Counter, StripChars

    def __init__(self, func):
        self.__fn = func

    def __call__(self, x, dx=0.0001, *args, **kwargs):
        return (self.__fn(x + dx) - self.__fn(x)) / dx

@Derivate
def df_sin(x):
    return math.sin(x)


# df_sin = Derivate(df_sin)  #вместо декоратора
print(df_sin(math.pi / 3))

# c = Counter()
# c2 = Counter()
# c()
# c(2)
# res = c(10)
# res2 = c2(-4)
# print(res, res2)
#
# s1=StripChars('?:!.; ')
# res = s1(' Hello world!? ')
# print(res)
