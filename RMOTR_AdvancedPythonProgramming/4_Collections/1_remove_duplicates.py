import unittest


def remove_duplicates_in_order(a_list):
    return [el for i, el in enumerate(a_list) if el not in a_list[:i]]


class RemoveDuplicatesTestCase(unittest.TestCase):

    def test_remove_duplicates_in_order(self):
        self.assertEqual(remove_duplicates_in_order([2,1,1,3,4]), [2,1,3,4])

    def test_remove_duplicates_in_order_with_empty_list(self):
        self.assertEqual(remove_duplicates_in_order([]), [])