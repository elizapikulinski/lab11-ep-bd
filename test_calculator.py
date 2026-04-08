# https://github.com/elizapikulinski/lab11-ep-bd.git
# Partner 1: Eliza Pikulinski
# Partner 2: Briana DeStoppelaire

import unittest
from calculator import *

class TestCalculator(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)

    def test_subtract(self):
        self.assertEqual(subtract(5, 3), 2)
        self.assertEqual(subtract(0, 4), -4)

    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            div(0, 5)

    def test_logarithm(self):
        self.assertEqual(logarithm(2, 8), 3)

    def test_log_invalid_base(self):
        with self.assertRaises(ValueError):
            logarithm(1, 10)

    def test_hypotenuse(self):
        self.assertEqual(hypotenuse(3, 4), 5)
        self.assertEqual(hypotenuse(0, 0), 0)

    def test_multiply(self):
        self.assertEqual(mul(1, 2), 2)
        self.assertEqual(mul(5, 4), 20)

    def test_divide(self):
        self.assertEqual(div(2, -10), -5)
        self.assertEqual(div(3, 15), 5)

    def test_log_invalid_argument(self):
        with self.assertRaises(ValueError):
            logarithm(0, "hi")

    def test_sqrt(self):
        with self.assertRaises(TypeError):
            square_root("abc")
        self.assertEqual(square_root(9), 3)
        self.assertEqual(square_root(16), 4)


if __name__ == "__main__":
    unittest.main()