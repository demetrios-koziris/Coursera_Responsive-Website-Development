# Implement a @pretty_result decorator that changes the result of any function, returning the result plus a pretty message. Example, the function sum(1, 2) should return 3. If applied @pretty_result it should return "The result of the function 'sum' is: 3".


import unittest


def pretty_result(original_function):
    def wrapper(x, y):
        return "The result of the function '" + original_function.__name__ + "' is: " + str(original_function(x, y))
    return wrapper

@pretty_result
def add(x, y):
    return x + y

@pretty_result
def subtract(x, y):
    return x - y


class AssignmentTestCase(unittest.TestCase):
    def test_add_function(self):
        self.assertEqual(add(2, 5), "The result of the function 'add' is: 7")

    def test_subtract_function(self):
        self.assertEqual(
            subtract(13, 8), "The result of the function 'subtract' is: 5")