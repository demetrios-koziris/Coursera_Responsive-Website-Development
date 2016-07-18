import unittest


def convert_temperature(temp, to='celsius'):
    if to == 'celsius':
        return to_celsius(temp)
    else:
        return to_fahrenheit(temp)


def to_fahrenheit(temp):
    return temp * 1.8 + 32


def to_celsius(temp):
    return (temp - 32) / 1.8


class ConvertTemperatureTestCase(unittest.TestCase):
    def test_fahrenheit_to_celsius(self):
        self.assertEqual(convert_temperature(32, to='celsius'), 0)

    def test_celsius_to_fahrenheit(self):
        self.assertEqual(convert_temperature(40, to='fahrenheit'), 104)

    def test_default_parameter_is_celsius(self):
        self.assertEqual(convert_temperature(32), 0)