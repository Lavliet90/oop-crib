'''
Вводится семизначное целое положительное число. С помощью list comprehension сформировать список lst, содержащий
цифры этого числа (в списке должны быть записаны числа, а не строки). Результат вывести на экран список командой:
'''
# x = input()
# lst = [int(z) for z in x]
# print(lst)


'''
Вводится натуральное число N. С помощью list comprehension сформировать двумерный список размером N x N, состоящий 
из нулей, а по главной диагонали - единицы. (Главная диагональ - это элементы, идущие по диагонали от верхнего левого 
угла матрицы до ее нижнего правого угла). Результат вывести в виде таблицы чисел как показано в примере ниже.
'''
# lengh_1 = int(input())
#
# [print([1 if i == j else 0 for i in range(lengh_1)]) for j in range(lengh_1)]


'''
Вводятся названия городов в строку через пробел. Необходимо сформировать список с помощью list comprehension, 
содержащий названия длиной более пяти символов. Результат вывести в строчку через пробел.
'''

# print(*[x for x in input().split() if len(x) > 5])

# a = [1, 4, 6, 3]
# k = iter(a)
#
# print(next(k))
# print(next(k))
# print(next(k))


# k = iter([a ** 2 for a in range(6)])
#
# print(next(k))
# print(next(k))
# print(next(k))
# print(next(k))
# print(next(k))
#
#
# class SimpleIterator:
#     def __init__(self, limit):
#         self.limit = limit
#         self.counter = 0
#
#     def __next__(self):
#         if self.counter < self.limit:
#             self.counter += 1
#             return self.counter
#         else:
#             raise StopIteration
#
#
# s_iter1 = SimpleIterator(3)
# print(next(s_iter1))
# print(next(s_iter1))
#

# print(next(s_iter1))
# print(next(s_iter1))
#
# from datetime import datetime
#
# def timeit(func):
#     def wrapper(*args, **kwargs):
#         stat = datetime.now()
#         result = func(*args, **kwargs)
#         print(datetime.now() - stat)
#         return result
#
#     return wrapper
#
# @timeit
# def one(n):
#     l = []
#     for i in range(n):
#         if i % 2 == 0:
#             l.append(i)
#     return l
#
# @timeit
# def two(n):
#     return [x for x in range(n) if x % 2 == 0]
#
#
#
# l1 = one
# l1(1000)
# l2 = two(10000)
#
# # print(l1)
# # print(l2)


a = []
b = a
a.append('fefef')
print(b)

c = 'fefef'
v = c
c = 'efe'
print(v)






def one():
    x = ['one', 'two']

    def inner():
        print(x)
        print(id(x))

    return inner


print(one())

print(dir(one()))
