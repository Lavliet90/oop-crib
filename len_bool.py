class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __len__(self):
        print('len')
        return  self.x * self.x + self.y * self.y

    def __bool__(self):
        print('bool')
        return self.x == self.y

p = Point(10,10)
print(bool(p))
print(len(p))

if p:
    print('x == y')
else:
    print('x != y')