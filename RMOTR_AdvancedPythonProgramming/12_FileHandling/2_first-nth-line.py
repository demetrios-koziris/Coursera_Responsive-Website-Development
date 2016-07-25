# Write a function, that receives a path to a text file and a line number as parameter, and returns the N-th line of that file.
# Example:
#     read_line_number('test-file.txt', 2)  # "this is the line number 2"


import unittest
import tempfile


def read_line_number(filepath, line_number):
    with open(filepath, 'r') as opened_file:
        return opened_file.readlines[line_number - 1]


class AssignmentTestCase(unittest.TestCase):
    def setUp(self):
        self.fp = tempfile.NamedTemporaryFile(mode="w")
        self.fp.write('this is line 1\n')
        self.fp.write('this is line 2\n')
        self.fp.write('this is line 3\n')
        self.fp.flush()

    def test_read_second_line(self):
        self.assertEqual(read_line_number(self.fp.name, 2),
                        'this is line 2\n')

    def test_read_last_line(self):
        self.assertEqual(read_line_number(self.fp.name, 3),
                        'this is line 3\n')

    def tearDown(self):
        self.fp.close()