# Write a function that combines list comprehensions and lambdas to transform temperatures given in celsius to fahrenheit.
#     to_fahrenheit([0, 10, 25, 30, 100]) == [32.0, 50.0, 77.0, 86.0, 212.0]


import unittest


def to_fahrenheit(a_list):
    return [(lambda t: t*1.8+32)(el) for el in a_list]


class ToFahrenheitTestCase(unittest.TestCase):
    def test_to_fahrenheit(self):
        self.assertEqual(to_fahrenheit([0, 10, 25, 30, 100]),
                         [32.0, 50.0, 77.0, 86.0, 212.0])

    def test_to_fahrenheit_repeated_values(self):
        self.assertEqual(to_fahrenheit([0, 10, 10, 100]),
                         [32.0, 50.0, 50.0, 212.0])

    def test_to_fahrenheit_empty_list(self):
        self.assertEqual(to_fahrenheit([]), [])