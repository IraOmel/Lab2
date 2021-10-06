import math
from fractions import Fraction


class Rational:
    def __init__(self, numerator=1, denominator=1):
        self.__numerator = numerator
        self.__denominator = denominator

        if type(self.__numerator) is int and type(self.__denominator) is int:
            try:
                reduce_form = Fraction(self.__numerator, self.__denominator)
            except ZeroDivisionError:
                quit("Division by zero")
        else:
            raise TypeError("Incorrect date")

    def operation(self):
        return Fraction(self.__numerator, self.__denominator)

    def calculation(self):
        return self.__numerator / self.__denominator


obj1 = Rational(2, 4)
print(obj1.operation())
print(obj1.calculation())
