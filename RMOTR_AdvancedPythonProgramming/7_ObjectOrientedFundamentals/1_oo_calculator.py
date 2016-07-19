# Build a simple calculator using Object Oriented Programming.
# This is the interface it should follow:
#   calculator = Calculator()
#   calculator.add(2, 4)  # 6
#   calculator.subtract(8, 1)  # 7
#   calculator.multiply(3, 5)  # 15
#   calculator.divide(5, 2)  # 2.5


import unittest


class Calculator(object):

    def add(self, x, y):
        return x+y

    def subtract(self, x, y):
        return x - y

    def multiply(self, x, y):
        return x * y

    def divide(self, x, y):
        return float(x) / y


class CalculatorTestCase(unittest.TestCase):

    def setUp(self):
        self.c = Calculator()

    def test_add(self):
       self.assertEqual(self.c.add(5, 2), 7)

    def test_subtract(self):
       self.assertEqual(self.c.subtract(5, 2), 3)

    def test_multiply(self):
       self.assertEqual(self.c.multiply(7, 9), 63)

    def test_divide(self):
       self.assertEqual(self.c.divide(9, 3), 3.0)

    def test_divide_decimal(self):
       self.assertEqual(self.c.divide(9, 2), 4.5)