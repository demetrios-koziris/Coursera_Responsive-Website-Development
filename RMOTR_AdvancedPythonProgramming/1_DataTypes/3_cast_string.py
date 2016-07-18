import unittest


def string2number(a_string):

    # if type(a_string) is str:
    #     if is_int(a_string):
    #         return int(a_string)
    #     elif is_float(a_string):
    #         return float(a_string)
    # raise ValueError

    conversions = [int, float]
    if type(a_string) is str:
        for conversion in conversions:
            try:
                return conversion(a_string)
            except ValueError:
                pass
    raise ValueError


def is_int(a_string):
    try:
        int(a_string)
        return True
    except ValueError:
        return False


def is_float(a_string):
    try:
        float(a_string)
        return True
    except ValueError:
        return False


class String2NumberTestCase(unittest.TestCase):

    def test_cast_string_into_integer(self):
        self.assertEqual(string2number('2'), 2)

    def test_cast_string_into_float(self):
        self.assertEqual(string2number('2.8'), 2.8)

    def test_cast_invalid_string_value(self):
        with self.assertRaises(ValueError):
            string2number('invalid-value')

    def test_cast_invalid_data_type(self):
        with self.assertRaises(ValueError):
            string2number(True)



