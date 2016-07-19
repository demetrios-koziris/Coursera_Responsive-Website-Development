# Write a function that receives multiple arguments and returns the sum of them. Example:
#     sum_multiple(2, 3, 5, 7) == 17
#     sum_multiple(2, 3) == 5
# If no arguments are provided, an Exception should be raised. Check the test cases for the complete spec.


import unittest


def sum_multiple(*numbers):
    if len(numbers) > 0:
        return sum(numbers)
    else:
        raise AttributeError


class MultipleSumTestCase(unittest.TestCase):

    def test_sum_multiple_terms(self):
        self.assertEqual(sum_multiple(2, 3), 5)
        self.assertEqual(sum_multiple(2, 3, 5, 7), 17)

    def test_sum_with_no_elements_raises_error(self):
        with self.assertRaises(AttributeError):
            sum_multiple()