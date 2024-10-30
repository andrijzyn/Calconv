import unittest
from operations.converter import Converter


class TestConvertFromDecimal(unittest.TestCase):
    def test_binary_conversion(self):
        result, steps = Converter.convert_from_decimal(10, 2)
        self.assertEqual(result, '1010')
        self.assertEqual(steps[0], '10 divided by 2 gives quotient 5 and remainder 0')
        self.assertEqual(steps[1], '5 divided by 2 gives quotient 2 and remainder 1')
        self.assertEqual(steps[2], '2 divided by 2 gives quotient 1 and remainder 0')
        self.assertEqual(steps[3], '1 divided by 2 gives quotient 0 and remainder 1')

    def test_hexadecimal_conversion(self):
        result, steps = Converter.convert_from_decimal(31, 16)
        self.assertEqual(result, '1F')
        self.assertEqual(steps[0], '31 divided by 16 gives quotient 1 and remainder 15')

    def test_zero_number(self):
        result, steps = Converter.convert_from_decimal(0, 2)
        self.assertEqual(result, '0')
        self.assertEqual(len(steps), 0)

    def test_base_10(self):
        result, steps = Converter.convert_from_decimal(12345, 10)
        self.assertEqual(result, '12345')
        self.assertEqual(len(steps), 0)

    def test_base_over_36(self):
        with self.assertRaises(ValueError) as context:
            Converter.convert_from_decimal(10, 37)
        self.assertTrue("Base cannot be greater than 36." in str(context.exception))

    def test_base_less_than_2(self):
        with self.assertRaises(ValueError) as context:
            Converter.convert_from_decimal(10, 1)
        self.assertTrue("Base must be 2 or higher." in str(context.exception))


if __name__ == '__main__':
    unittest.main()
