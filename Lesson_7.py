#=====#1=====

import numpy

a = [[10, 10, 10, 10], ['4','4', '4', '4'], ['1', '1', '1', '1']]
b = [['10', '10', '10', '100'], [-4, -4, -4, -4], ['-1', '-1', '-1', '-1']]

class M:
    def __init__(self, l):
        self.l = l

    def __str__(self):
        return "\n".join(map(str,self.l))

    def __add__(self, other):
        return numpy.array(self.l, dtype=int) + numpy.array(other.l, dtype=int)

print(f" 1я матрица: \n{M(a)}\n {'*'*20}\n вторая матрица: \n{M(b)}\n {'*'*20}\n "
      f"cложение 2я матриц: \n{M(a)+ M(b)}")

#=====#2=====

import abc as a

class x(a.ABC):
    res = 0

    def __init__(self,y):
        self.y = y

    def c(self):
        pass

    def __add__(self, other):
        x.res += self.c + other.c
        return Costume(0)

    def __str__(self):
        return f'{x.res}'

class Coat(x):
    @property
    def c(self):
        return round(self.y / 6.5 + 0.5)

class Costume(x):
    @property
    def c(self):
        return round((2 * self.y + 0.3) / 100)

print(Coat(2000)+Costume(2000)+Coat(2000))

#=====#3=====

class x():

    def __init__(self,y):
        self.y = y

    def make_order(self,r):
        return print(str(z.join([z1 * r for i in range(self.y // r)]) + z + z1 * (self.y % r)))

    def __add__(self, other):
        return x(self.y + other.y)

    def __sub__(self, other):
        return x(self.y - other.y)

    def __mul__(self, other):
        return x(self.y * other.y)

    def __floordiv__(self, other):
        return x(self.y // other.y)

z = '\n\t|||\t\n'
z1 = '<>'
a,b,t = 10,5,7
n = '*'

(x(a)+x(b)).make_order(t)

#'x(a)' + n + 'x(b)).make_order(t)' (в excel есть функция ДВССЫЛ, которая оживляет данное выражение,
#                                      как оживить в Пайтон?)