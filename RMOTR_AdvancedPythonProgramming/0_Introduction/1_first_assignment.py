# Modify the provided function to return the string "Hello World". Make sure you check the test cases to see what is the expected behavior of your code.


import unittest


def hello_world():
    return 'Hello World'


class FirstAssignmentTestCase(unittest.TestCase):
    def test_hello_world_function(self):
        "Should return the string 'Hello World'"
        self.assertEqual(hello_world(), "Hello World")