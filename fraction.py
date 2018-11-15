class Fraction(object):
    def __init__(self, numerator, denominator):
        self._num = numerator
        self._denom = denominator

    @classmethod
    def _common_factor(cls, *args, **kwargs):
        if args:
            return cls._common_factor(*args[1:], factor=kwargs.get('factor', 1) * abs(args[0]))
        else:
            return kwargs.get('factor')

    # Calculate lowest common denominator
    def lcd(*fractions):
        # Get common factor between denominators
        # Reduce until sum of numerators cannot be reduced further
        ...

    def __repr__(self):
        return f"Fraction({self._num!r}, {self._denom!r})"

    def __str__(self):
        return f"{self._num}/{self._denom}"

    def __int__(self):
        return self._num // self._denom

    def __float__(self):
        return self._num / self._denom

    def __eq__(self, other):
        ...

    def __add__(self, other):
        ...

    def __sub__(self, other):
        # Get common denominator
        # Subtract numerator
        ...

    def __mul__(self, other):
        # Multiply numerators
        # Multiply denominators
        ...

    def __truediv__(self, other):
        # Invert other
        # Multiply
        ...

import unittest

class TestRepr(unittest.TestCase):
    def test_(self):
        x = Fraction(1, 2)

        self.assertEqual(repr(x), "Fraction(1, 2)")

class TestToString(unittest.TestCase):
    def test_(self):
        x = Fraction(1, 2)

        self.assertEqual(str(x), "1/2")

class TestToInt(unittest.TestCase):
    def test_(self):
        x = Fraction(10, 3)

        self.assertEqual(int(x), 3)

class TestToFloat(unittest.TestCase):
    def test_(self):
        x = Fraction(1, 2)

        self.assertEqual(float(x), 0.5)

class TestCommonFactor(unittest.TestCase):
    def test_ints(self):
        cd = Fraction._common_factor(2, -3, 5)

        self.assertEqual(30, cd)

class TestAdd(unittest.TestCase):
    def test_common(self):
        x = Fraction(1, 4)
        y = Fraction(2, 4)

        z = x + y

        self.assertEqual(z, 123)

if __name__ == '__main__':
    unittest.main(verbosity=2)
