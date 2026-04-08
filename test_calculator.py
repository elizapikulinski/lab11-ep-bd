# https://github.com/elizapikulinski/lab11-ep-bd.git
# Partner 1:
# Partner 2: Briana DeStoppelaire
import pytest
from calculator import add, sub, div, log

class TestCalculator(unittest.TestCase):
#### Partner 2
def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0

def test_subtract():
    assert sub(5, 3) == 2
    assert sub(0, 4) == -4

def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        div(0, 5)

def test_logarithm():
    assert log(2, 8) == 3  # log base 2 of 8 = 3

def test_log_invalid_base():
    with pytest.raises(ValueError):
        log(1, 10)  # base cannot be 1






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

# Do not touch this
if __name__ == "__main__":
    unittest.main()