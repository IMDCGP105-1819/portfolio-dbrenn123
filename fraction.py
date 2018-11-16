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
    @staticmethod
    def lcd(a, b):
        # Find greatest common divisor
        def gcd(a, b):
            if(b == 0):
                return a

            return gcd(b, a % b)

        return int(a._denom * b._denom / gcd(a._denom, b._denom));

    def reciprocal(self):
        ...

    def __repr__(self):
        return f"Fraction({self._num!r}, {self._denom!r})"

    def __str__(self):
        return f"{self._num}/{self._denom}"

    def __int__(self):
        return self._num // self._denom

    def __float__(self):
        return float(self._num) / float(self._denom)

    def __eq__(self, other):
        return float(self) == float(other)

    def __add__(self, other):
        denom = Fraction.lcd(self, other)
        num = self.denominator(denom)._num + other.denominator(denom)._num

        return Fraction(num, denom)

    def __sub__(self, other):
        denom = Fraction.lcd(self, other)
        num = self.denominator(denom)._num - other.denominator(denom)._num

        return Fraction(num, denom)

    def __mul__(self, other):
        return Fraction(self._num * other._num, self._denom * other._denom)

    def __truediv__(self, other):
        return self * other.inverse()

    def denominator(self, int):
        if(int != self._denom):
            min_ = min(self._denom, int)
            max_ = max(self._denom, int)
            f = max_ / min_

            return Fraction(self._num * f, int)
        else:
            return self

    def inverse(self):
        return Fraction(self._denom, self._num)

import unittest

class TestConstruct(unittest.TestCase):
    def test_ints(self):
        x = Fraction(2, 3)

        self.assertEqual(x._num, 2)
        self.assertEqual(x._denom, 3)

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

        self.assertEqual(z, Fraction(3, 4))

    def test_uncommon(self):
        x = Fraction(1, 4)
        y = Fraction(1, 2)
        z = x + y

        self.assertEqual(z, Fraction(3, 4))

class TestSub(unittest.TestCase):
    def test_common(self):
        x = Fraction(3, 4)
        y = Fraction(1, 4)
        z = x - y

        self.assertEqual(z, Fraction(2, 4))

    def test_uncommon(self):
        x = Fraction(1, 2)
        y = Fraction(1, 4)
        z = x - y

        self.assertEqual(z, Fraction(1, 4))

class TestDenom(unittest.TestCase):
    def test_(self):
        x = Fraction(1, 2)
        y = x.denominator(4)

        self.assertEqual(y._denom, 4)
        self.assertEqual(y._num, 2)

class TestEquality(unittest.TestCase):
    def test_equal(self):
        x = Fraction(1, 2)
        y = Fraction(1, 2)

        self.assertEqual(x, y)

    def test_notEqual(self):
        x = Fraction(1, 2)
        y = Fraction(3, 4)

        self.assertNotEqual(x, y)

class TestLCD(unittest.TestCase):
    def test_(self):
        x = Fraction(1, 12)
        y = Fraction(1, 18)
        lcd = Fraction.lcd(x, y)

        self.assertEqual(lcd, 36)

class TestInverse(unittest.TestCase):
    def test_(self):
        x = Fraction(3, 5)
        y = x.inverse()

        self.assertEqual(y, Fraction(5, 3))

class TestMultiply(unittest.TestCase):
    def test_(self):
        x = Fraction(1, 4)
        y = Fraction(1, 2)
        z = x * y

        self.assertEqual(z, Fraction(1, 8))

class TestDivide(unittest.TestCase):
    def test_(self):
        x = Fraction(1, 8)
        y = Fraction(1, 2)
        z = x / y

        self.assertEqual(z, Fraction(1, 4))
        
if __name__ == '__main__':
    unittest.main(verbosity=2)
