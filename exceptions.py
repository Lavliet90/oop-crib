def func2():
    return 1 / 0


def func1():
    try:
        return func2()
    except:
        print('func1 error')


func1()

try:
    x, y = map(int, input().split())
    res = x / y
except ZeroDivisionError as z:
    print(z)
except ValueError as z:
    print(z)
except:
    print('другая ошибка')
else:
    print('Все круто')
'''
выполнится, если выполнилось успешно.
еще можно использовать finally, которое выполняется полюбому
'''
