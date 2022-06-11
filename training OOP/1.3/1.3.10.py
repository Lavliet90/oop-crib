'''
Declare a class named Person and attributes:

name: 'Сергей Балакирев'
job: 'Программист'
city: 'Москва'

Create an instance p1 of this class and check if it has a local property named job. Print True if it is present
in the p1 object and False if it is absent.
'''

class Person:
    name = 'Сергей Балакирев'
    job = 'Программист'
    city = 'Москва'

p1 = Person()

print('job' in p1.__dict__)