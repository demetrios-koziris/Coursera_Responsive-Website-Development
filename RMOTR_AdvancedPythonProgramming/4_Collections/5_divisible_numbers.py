import unittest


def divisible_numbers(a_list, term):
    return [el for el in a_list if el%term == 0]


class DivisibleNumbersTestCase(unittest.TestCase):
    def test_many_divisible_number(self):
        self.assertEqual(
            divisible_numbers([9, 8, 7, 6, 5, 4, 3, 2, 1], 3), [9, 6, 3])

    def test_empty_list(self):
        self.assertEqual(divisible_numbers([], 2), [])

    def test_no_result(self):
        self.assertEqual(divisible_numbers([2, 4, 8], 5), [])