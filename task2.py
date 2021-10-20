import math
from fractions import Fraction


class Rational:
    def __init__(self, numerator=1, denominator=1):
        if not isinstance(numerator, int) or not isinstance(denominator, int):
            raise TypeError("Incorrect data")
        if not denominator:
            raise ZeroDivisionError("Incorrect data")
        self.__numerator = numerator
        self.__denominator = denominator

    def operation(self):
        return Fraction(self.__numerator, self.__denominator)

    def calculation(self):
        return self.__numerator / self.__denominator


obj1 = Rational(2, 4)
print(obj1.operation())
print(obj1.calculation())
