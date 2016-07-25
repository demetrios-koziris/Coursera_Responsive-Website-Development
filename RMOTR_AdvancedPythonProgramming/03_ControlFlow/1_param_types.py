# Write a function that receives one single param, and returns a String explaining which type of object the param is.
# If given param is not instance of any of the basic data types, say you don't know what it is.
# hint: you might want to use the isinstance() Python built-in function to determine which type a param is.
# Examples:
#     >>> what_is_this(1)
#     "This is an Integer."
#     >>> what_is_this("Hello World!")
#     "This is a String."
#     >>> what_is_this(True)
#     "This is a Boolean."
#     >>> what_is_this(2.8)
#     "This is an Float."
#     >>> what_is_this(object())
#     "I have no idea what this is"


import unittest


def what_is_this(param):
    if type(param) == int:
        return 'This is an Integer.'
    elif type(param) == float:
        return 'This is a Float.'
    elif type(param) == str:
        return  'This is a String.'
    elif type(param) == bool:
        return 'This is a Boolean.'
    else:
        return 'I have no idea what this is'


class WhatIsThisTestCase(unittest.TestCase):

    def test_what_is_this_integer(self):
        self.assertEqual(what_is_this(10), "This is an Integer.")

    def test_what_is_this_string(self):
        self.assertEqual(what_is_this("Hello"), "This is a String.")

    def test_what_is_this_boolean(self):
        self.assertEqual(what_is_this(True), "This is a Boolean.")

    def test_what_is_this_float(self):
        self.assertEqual(what_is_this(10.92), "This is a Float.")

    def test_what_is_this_float(self):
        self.assertEqual(what_is_this(object()), "I have no idea what this is")

