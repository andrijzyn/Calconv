import sys
import unittest

sys.path.insert(0, './')

from main import convert_to_decimal


class TestConvertToDecimal(unittest.TestCase):
    def test_decimal_conversion(self):
        result = convert_to_decimal("1101", 2)
        self.assertEqual(result, (13, ['Digit: 1 in base 2, value: 1 * (base ** 3) = 8',
                                       'Digit: 1 in base 2, value: 1 * (base ** 2) = 4',
                                       'Digit: 0 in base 2, value: 0 * (base ** 1) = 0',
                                       'Digit: 1 in base 2, value: 1 * (base ** 0) = 1']))

        result = convert_to_decimal("A", 16)
        self.assertEqual(result, (10, ['Digit: A in base 16, value: 10 * (base ** 0) = 10']))

    def test_decimal_conversion_base_10(self):
        result = convert_to_decimal("100", 10)
        self.assertEqual(result, (100, []))

    def test_decimal_conversion_base_lt_2(self):
        with self.assertRaises(ValueError) as context:
            convert_to_decimal("10", 1)
        self.assertTrue('Base must be 2 or higher.' in str(context.exception))

    def test_decimal_conversion_invalid_digit(self):
        with self.assertRaises(ValueError) as context:
            convert_to_decimal("2", 2)
        self.assertTrue("Digit '2' is not valid for base 2" in str(context.exception))


if __name__ == '__main__':
    unittest.main()
