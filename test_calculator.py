# https://github.com/elizapikulinski/lab11-ep-bd.git
# Partner 1: Eliza Pikulinski
# Partner 2: Briana DeStoppelaire

import unittest
from calculator import *

class TestCalculator(unittest.TestCase):

    #### Partner 2
    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)

    def test_subtract(self):
        self.assertEqual(sub(5, 3), 2)
        self.assertEqual(sub(0, 4), -4)

    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            div(0, 5)

    def test_logarithm(self):
        self.assertEqual(log(2, 8), 3)

    def test_log_invalid_base(self):
        with self.assertRaises(ValueError):
            log(1, 10)







    ######## Partner 1
    # def test_log_invalid_argument(self): # 1 assertion
    #     # call log function inside, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #     logarithm(0, 5)
    #     fill in code

    # def test_hypotenuse(self): # 3 assertions
    #     fill in code

    # def test_sqrt(self): # 3 assertions
    #     # Test for invalid argument, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #    square_root(NUM)
    #     # Test basic function
    #     fill in code
    ##########################
    def test_hypotenuse(self):
        with self.assertRaises(ValueError):
            hypotenuse(0,0)

    def test_multiply:
        assert 1*2 == 2
        assert 5*4 == 20

    def test_divide:
        assert -10/2 == -5
        assert 15/3 == 3

    def test_log_invalid_argument(self):
        with self.assertRaises(ValueError):
            logarithm(0, "hi")
        assert hypotenuse(3,4) == 5
        assert hypotenuse(0,0) == 0

    def test_sqrt(self):
        with self.assertRaises(ValueError):
            square_root("abc")
        assert spare_root(9) == 3
        assert spare_root(16) == 4


# Do not touch this
if __name__ == "__main__":
    unittest.main()