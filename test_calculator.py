# https://github.com/adronadula/lab11--AD---CC
# Partner 1: Aditya Dronaula
# Partner 2: Canran Cui

import unittest

import calculator

from calculator import *

class TestCalculator(unittest.TestCase):
    def test_add(self): # 3 assertions
        self.assertEqual(calculator.add(2, 3), 5)
        self.assertEqual(calculator.add(-3, 3), 0)
        self.assertEqual(calculator.add(-2, -3), -5)

    def test_subtract(self): # 3 assertions
        self.assertEqual(calculator.subtract(13, 3), 10)
        self.assertEqual(calculator.subtract(16, 3), 13)

    def test_divide_by_zero(self): # 1 assertion
        with self.assertRaises(ZeroDivisionError):
            calculator.div(5, 0)

    def test_logarithm(self): # 3 assertions
        self.assertAlmostEqual(calculator.logarithm(2, 16), 4.0)
        self.assertAlmostEqual(calculator.logarithm(10, 1000), 3.0)
        self.assertAlmostEqual(calculator.logarithm(25, 625), 2.0)

    def test_log_invalid_base(self): # 1 assertion
        with self.assertRaises(ValueError):
            calculator.logarithm(1, 8)

    ######## Partner 1
    # def test_multiply(self): # 3 assertions
    def test_multiply(self):
        self.assertEqual(calculator.mul(3, 4), 12)
        self.assertEqual(calculator.mul(-2, 5), -10)
        self.assertEqual(calculator.mul(0, 7), 0)


    # def test_divide(self): # 3 assertions
    def test_divide(self):
        self.assertEqual(calculator.div(2, 10), 5)
        self.assertAlmostEqual(calculator.div(3, 1), 1 / 3)
    # ##########################

    ######## Partner 2
    # def test_divide_by_zero(self): # 1 assertion
    #     # call division function inside, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #     div(0, 5)
    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            calculator.div(0, 5)
    # def test_logarithm(self): # 3 assertions
    #     fill in code
    def test_logarithm(self):
        self.assertAlmostEqual(calculator.logarithm(2, 8), 3.0)
        self.assertAlmostEqual(calculator.logarithm(10, 100), 2.0)


    # def test_log_invalid_base(self): # 1 assertion
    #     # use same technique from test_divide_by_zero
    #     fill in code
    def test_log_invalid_base(self):
        with self.assertRaises(ValueError):
            calculator.logarithm(1, 8)
        with self.assertRaises(ValueError):
            calculator.logarithm(-2, 8)

    ######## Partner 1
    # def test_log_invalid_argument(self): # 1 assertion
    #     # call log function inside, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #     logarithm(0, 5)
    def test_log_invalid_argument(self):
        with self.assertRaises(ValueError):
            calculator.logarithm(2, 0)
        with self.assertRaises(ValueError):
            calculator.logarithm(2, -8)

    # def test_hypotenuse(self): # 3 assertions
    def test_hypotenuse(self):
        self.assertAlmostEqual(calculator.hypotenuse(3, 4), 5.0)
        self.assertAlmostEqual(calculator.hypotenuse(-3, 4), 5.0)

    # def test_sqrt(self): # 3 assertions
    #     # Test for invalid argument, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #    square_root(NUM)
    #     # Test basic function
    def test_sqrt(self):
        self.assertEqual(calculator.square_root(9), 3)
        self.assertAlmostEqual(calculator.square_root(2), 1.41421356, places=5)
        with self.assertRaises(ValueError):
            calculator.square_root(-1)    ##########################


# Do not touch this
if __name__ == "__main__":
    unittest.main()