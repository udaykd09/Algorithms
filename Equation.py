from fractions import Fraction
from math import ceil


class Solution(object):

    def isSolution(self, n):
        """
        :type n: int
        :return: bool
        """
        a, b, c = 0, 0, 0
        original_fraction = Fraction(4, n)
        temp_fraction = Fraction(1, 1)

        if n > 4:
            a = Fraction(1, int(ceil(n/4))+1)
            temp_fraction = original_fraction - a
            if temp_fraction <= 0:
                return False
            b = Fraction(1, int(ceil(temp_fraction.denominator/temp_fraction.numerator))+1)
            temp_fraction -= b
            if temp_fraction <= 0:
                return False
            c = Fraction(1, int(ceil(temp_fraction.denominator / temp_fraction.numerator)) + 1)
            temp_fraction -= c
            if a + b + c == original_fraction:
                print(a, b, c)
                return True

        return False


mySol = Solution()
for i in range(3, 200):
    print(i, mySol.isSolution(i))