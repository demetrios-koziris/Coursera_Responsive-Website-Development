# Implement a @small_numbers decorator that changes enforces numeric arguments passed to a function to be less or equal than a given passed parameter. If any numeric argument is greater than that specified limit, a ValueError should be raised. The default limit should be 50. Example:
#     @small_numbers(limit=50)
#     def my_func(number_param, string_param):
#       pass


import unittest


def small_numbers(limit=50):
    def small_numbers_decorator(func):
        def wrapper(arg1, arg2):
            if True in [arg > limit for arg in (arg1, arg2) if type(arg) is int or type(arg) is float]:
                raise ValueError()
            else:
                return func(arg1, arg2)
        return wrapper
    return small_numbers_decorator


@small_numbers(limit=100)
def f1(a_str, a_float):
    return 'mock1 - {} {}'.format(a_str, a_float)


@small_numbers()
def f2(an_int, a_str):
    return 'mock2 - {} {}'.format(an_int, a_str)


class AssignmentTestCase(unittest.TestCase):
    def test_default_limit_is_respected(self):
        self.assertEqual(f2(50, 'hello'), "mock2 - 50 hello")

    def test_default_limit_raises(self):
        with self.assertRaises(ValueError):
            f2(51, 'hello')

    def test_specified_limit_is_respected(self):
        self.assertEqual(f1('world', 100.0), "mock1 - world 100.0")

    def test_specified_limit_raises(self):
        with self.assertRaises(ValueError):
            f1('world', 100.1)

