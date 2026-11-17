import unittest

import calculator

from calculator import *

class TestCalculator(unittest.TestCase):
    def test_add(self): # 3 assertions
        self.assertEqual(calculator.add(2, 3), 5)
        self.assertEqual(calculator.add(-3, 3), 0)
        self.assertEqual(calculator.add(-2, -3), -5)

    def test_subtract(self): # 3 assertions
        self.assertEqual(calculator.sub(2, 3), -1)
        self.assertEqual(calculator.sub(16, 3), 3)

    def test_divide_by_zero(self): # 1 assertion
        with self.assertRaises(ZeroDivisionError):
            calculator.div(5, 0)

    def test_logarithm(self): # 3 assertions
        self.assertAlmostEqual(calculator.log(2, 16), 4.0)
        self.assertAlmostEqual(calculator.log(10, 1000), 3.0)
        self.assertAlmostEqual(calculator.log(25, 625), 2.0)

    def test_log_invalid_base(self): # 1 assertion
        with self.assertRaises(ValueError):
            calculator.log(1, 8)



# Do not touch this
if __name__ == "__main__":
    unittest.main()