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
                print("Divided by zero is not possible")
                quit()
        else:
            print("Incorrect date")
            quit()

    def operation(self):
        print(Fraction(self.__numerator, self.__denominator))

    def calculation(self):
        return self.__numerator/self.__denominator


obj1 = Rational(2, 6)
obj1.operation()
print(obj1.calculation())
