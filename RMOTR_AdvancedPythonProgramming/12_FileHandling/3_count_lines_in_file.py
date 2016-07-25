# Write a function, that receives a path to a text file as parameter, and returns the amount of lines that text file has.
#     count_lines('test-file.txt')  # 10


import unittest
import tempfile


def count_lines(filepath):
    with open(filepath, 'r') as opened_file:
        return len(opened_file.readlines())


class AssignmentTestCase(unittest.TestCase):
    def setUp(self):
        self.fp = tempfile.NamedTemporaryFile(mode="w")
        self.fp.write('this is line 1\n')
        self.fp.write('this is line 2\n')
        self.fp.write('this is line 3\n')
        self.fp.flush()

    def test_1(self):
        self.assertEqual(count_lines(self.fp.name), 3)

    def tearDown(self):
        self.fp.close()