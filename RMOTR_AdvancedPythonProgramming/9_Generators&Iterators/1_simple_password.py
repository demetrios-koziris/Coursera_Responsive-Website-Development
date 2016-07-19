# Write a simple random password generator using iterators. The generator can accept two parameters:
# available_chars: The characters to use to generate the password. OPTIONAL. Default: A set of lowercase characters, digits and symbols. (hint, check the string module)
# length: The length of the password. OPTIONAL. Default: 8
#     pass_generator = SimplePasswordGenerator()
#     next(pass_generator)  # %58a$d8a (length=8)
#     pass_generator = SimplePasswordGenerator()
#     next(pass_generator)  # '%58a$d8a' (length=8)
#     pass_generator = SimplePasswordGenerator(available_chars=['a', 'b'], length=4)
#     next(pass_generator)  # 'abba'
# Note: Make sure you implement the generator in a way that supports both Python2.7 and Python3


import string
import random
import unittest


class SimplePasswordGenerator(object):

    def __init__(self, available_chars=string.ascii_lowercase+string.digits, length=8):
        self.available_chars = available_chars
        self.length = length


    def __iter__(self):
        return self

    def __next__(self):  # use __next__ in Python 3.x
        return ''.join(random.choice(self.available_chars) for i in range(self.length))

    next = __next__


class SimplePasswordGeneratorTestCase(unittest.TestCase):

    def test_password_generator_characters(self):
        it = SimplePasswordGenerator(available_chars=['a', 'b'], length=2)
        password = next(it)
        self.assertTrue(
            set(password) == set(['a', 'b']) or
            set(password) == set(['a']) or
            set(password) == set(['b']))

    def test_password_generator_length(self):
        self.assertEqual(len(next(SimplePasswordGenerator(length=2))), 2)
        self.assertEqual(len(next(SimplePasswordGenerator(length=4))), 4)
        self.assertEqual(len(next(SimplePasswordGenerator(length=16))), 16)

    def test_password_largest_length_than_available_chars(self):
        it = SimplePasswordGenerator(available_chars=['a', 'b'], length=8)
        password = next(it)
        self.assertTrue(
            set(password) == set(['a', 'b']) or
            set(password) == set(['a']) or
            set(password) == set(['b']))
        self.assertEqual(len(password), 8)
