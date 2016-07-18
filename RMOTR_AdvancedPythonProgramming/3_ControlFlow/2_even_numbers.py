import unittest


def even_numbers(list_of_numbers, limit):

    # return [num for num in list_of_numbers if num%2==0][:limit]

    # return list(filter(lambda num: num % 2 == 0, list_of_numbers))[:limit]

    list_of_evens = []
    for num in list_of_numbers:
        if num%2 == 0:
            list_of_evens.append(num)
        if len(list_of_evens) == limit:
            break
    return list_of_evens


class EvenNumbersTestCase(unittest.TestCase):

    def test_even_numbers(self):
        self.assertEqual(even_numbers([1,2,3,4,5,6,7,8,9,10], 3), [2,4,6])

    def test_even_numbers_limit_exceeded(self):
        self.assertEqual(even_numbers([1,2,3,4,5,6,7,8,9,10], 30),
                         [2,4,6,8,10])

    def test_even_numbers_limit_zero(self):
        self.assertEqual(even_numbers([1,2,3,4,5,6,7,8,9,10], 0), [])

    def test_even_numbers_limit_one(self):
        self.assertEqual(even_numbers([1,2,3,4,5,6,7,8,9,10], 1), [2])