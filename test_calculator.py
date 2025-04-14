# github link: https://github.com/Thomas-Xiang/lab10-CAJ-YX.git
# Partner 1: Celine Jaime
# Partner 2: Thomas Xiang

import unittest
from calculator import *
import unittest
from calculator import add, subtract, exp, mul, div, logarithm, hypotenuse

class TestCalculator(unittest.TestCase):
    ######### Partner 2
    def test_add(self): # 3 assertions
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 3), 2)
        self.assertEqual(add(-1, -3), -4)

    def test_subtract(self): # 3 assertions
        self.assertEqual(subtract(2, 3), -1)
        self.assertEqual(subtract(4, 3), 1)
        self.assertEqual(subtract(5, 5), 0)
    # ##########################

    ######## Partner 1
    def test_mul(self): # 3 assertions
        self.assertEqual(mul(4,3), 12)
        self.assertEqual(mul(-1,7), -7)

    def test_div(self): # 3 assertions
        self.assertEqual(div(2, 8), 4)
        self.assertAlmostEqual(div(0.5, 2.0), 4.0)
    # ##########################

    ######## Partner 2
    def test_divide_by_zero(self): # 1 assertion
        # call division function inside, example:
        with self.assertRaises(ZeroDivisionError):
            div(0, 5)
        self.assertEqual(div(2, 6), 3)
        self.assertEqual(div(1, 6), 6)
        

    def test_logarithm(self): # 3 assertions
        self.assertEqual(logarithm(4, 2), 0.5)
        self.assertEqual(logarithm(3, 9), 2)
        self.assertEqual(logarithm(3, 3), 1)

    def test_log_invalid_base(self): # 1 assertion
        # use same technique from test_divide_by_zero
        self.assertEqual(exp(2, 2), 4)
        self.assertEqual(exp(2, 3), 8)
        self.assertEqual(exp(4, 2), 16)
    # ##########################
    
    ######## Partner 1
    def test_log_invalid_argument(self): # 1 assertion
        with self.assertRaises(ValueError):
            logarithm(1, 10)
        with self.assertRaises(ValueError):
            logarithm(2, 0)
        with self.assertRaises(ValueError):
            logarithm(-3, -3)

    def test_hypotenuse(self): # 3 assertions
        self.assertAlmostEqual(hypotenuse(3, 4), 5)
        self.assertAlmostEqual(hypotenuse(-3, 4), 5.0)

    def test_sqrt(self): # 3 assertions
        self.assertEqual(square_root(4), 2)
        self.assertAlmostEqual(square_root(10), math.sqrt(10))
        with self.assertRaises(ValueError):
            square_root(-1)
    ##########################

# Do not touch this
if __name__ == "__main__":
    unittest.main()