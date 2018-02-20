# Name: SelfCheck4.py
# Author: InteractivePython.org, Robin Goyal
# Last-Modified: February 1, 2018
# Purpose: Enhance functionality of original Fraction class


def gcd(num, den):
    if num % den == 0:
        return den
    return gcd(den, num % den)


class Fraction:

    def __init__(self, top, bottom):
        self.num = top
        self.den = bottom

    def __add__(self, other):
        new_num = self.num * other.den + self.den * other.num
        new_den = self.den * other.den
        common = gcd(new_num, new_den)

        return Fraction(new_num // common, new_den // common)

    def __mul__(self, other):
        new_num = self.num * other.num
        new_den = self.den * other.den
        common = gcd(new_num, new_den)

        return Fraction(new_num // common, new_den // common)

    def __sub__(self, other):
        new_num = self.num * other.den - self.den * other.num
        new_den = self.den * other.den
        common = gcd(new_num, new_den)

        return Fraction(new_num // common, new_den // common)

    def __truediv__(self, other):
        new_num = self.num * other.den
        new_den = self.den * other.num
        common = gcd(new_num, new_den)

        return Fraction(new_num // common, new_den // common)

    def __eq__(self, other):
        return self.num * other.den == other.num * self.den

    def __lt__(self, other):
        return self.num * other.den < other.num * self.den

    def __gt__(self, other):
        return self.num * other.den > other.num * self.den

    def __str__(self):
        return "{}/{}".format(self.num, self.den)


a = Fraction(1, 3)
b = Fraction(2, 3)

print(a == b)
