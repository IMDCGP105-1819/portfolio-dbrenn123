class Fraction(object):
    def __init__(self, numerator, denominator):
        self._num = numerator
        self._denom = denominator

    def _common_factor(*args, **kwargs):
        if args:
            return Fraction._common_factor(*args[1:], factor=kwargs.get('factor', 1) * abs(args[0]))
        else:
            return kwargs.get('factor')

    # Calculate lowest common denominator
    def lcd(*fractions):
        # Get common factor between denominators
        # Reduce until sum of numerators cannot be reduced further
        ...

    def __add__(self, other):
        # Get common denominator
        # Add numerator
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

    def __str__(self):
        return f"{self._num}/{self._denom}"

import unittest

class TestCommonFactor(unittest.TestCase):
    def test_ints(self):
        cd = Fraction._common_factor(2, -3, 5)

        self.assertEqual(30, cd)

if __name__ == '__main__':
    unittest.main(verbosity=2)
