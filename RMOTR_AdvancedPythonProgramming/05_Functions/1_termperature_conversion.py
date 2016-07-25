# Write a function convert_temperature that receives two parameters, a number (indicating degrees of temperature) and an optional second parameter indicating if it should convert the temperature to Celsius or Fahrenheit (default is Celsius). The function should have two inner functions to_celsius and to_fahrenheit that receive NO parameters and must be used to return the expected result. Example:
#     convert_temperature(32)  == 0  # celsius is default
#     convert_temperature(32, to='celsius')  == 0
#     convert_temperature(40, to='fahrenheit') == 104


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