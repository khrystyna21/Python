

import math


class Fraction:
    def __init__(self, num, denom):
        self.num = int(num/ math.gcd(num, denom))
        self.denom = int(denom/ math.gcd(num, denom))
        if self.denom == 0:
            raise ZeroDivisionError

    def __add__(self, other):
        self.sum_n = self.num * other.denom + self.denom * other.num
        self.sum_d = self.denom * other.denom
        self.num = math.gcd( self.sum_n, self.sum_d)
        return int(self.sum_n / self.num), int(self.sum_d / self.num)
    def __sub__(self, other):
        self.sub_n = self.num * other.denom - self.denom * other.num
        self.sub_d = self.denom * other.denom
        self.num = math.gcd( self.sub_n, self.sub_d)
        return int(self.sub_n / self.num), int(self.sub_d / self.num)
    def __mul__(self, other):
        self.mul_n = self.num*other.num
        self.mul_d = self.denom*other.denom
        self.num = math.gcd(self.mul_n,  self.mul_d)
        return int(self.mul_n / self.num),int( self.mul_d / self.num)
    def __truediv__(self, other):
        self.div_n = self.num*other.denom
        self.div_d = self.denom*other.num
        self.num = math.gcd(self.div_n,  self.div_d)
        return int(self.div_n / self.num), int(self.div_d / self.num)

    def __str__(self):
        if type(self) is tuple:
            if self[1] == 1:
                return str(self[0])
            else:
                return '{self[0]}/{self[1]}'





x = Fraction(1,2)
y = Fraction(1,4)

print(x + y)
