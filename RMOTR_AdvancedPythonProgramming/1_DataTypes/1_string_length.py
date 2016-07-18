import unittest


def length(a_string):
    str_length = 0
    for char in a_string:
        str_length += 1
    return str_length


class LengthTestCase(unittest.TestCase):

    def test_length_multiple_words(self):
        self.assertEqual(length('hello world'), 11)

    def test_length_single_word(self):
        self.assertEqual(length('hello'), 5)

    def test_length_empty_string(self):
        self.assertEqual(length(''), 0)