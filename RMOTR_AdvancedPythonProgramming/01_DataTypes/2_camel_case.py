# Write a function that receives a string and returns a camel case version of it.
# Example:
#     >>> camel_case('hello world')
#     "Hello World"


import unittest


def camel_case(a_string):

    #return a_string.title()

    #return ' '.join(word.capitalize() for word in a_string.split(' '))

    str_list = a_string.split(' ')
    for i, word in enumerate(str_list):
        if (word):
            str_list[i] = word[0].upper() + word[1:]
    return ' '.join(str_list)


class CamelCaseTestCase(unittest.TestCase):

    def test_word_with_spaces(self):
        self.assertEqual(camel_case("testing 123 hello"), 'Testing 123 Hello')

    def test_single_word(self):
        self.assertEqual(camel_case("testing"), 'Testing')

    def test_empty_string(self):
        self.assertEqual(camel_case(""), '')