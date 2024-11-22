import unittest
from main import parse_math_expression

class ParseMathExpression(unittest.TestCase):

    def test_valid_input(self):
        expression = "10_2 + 33_10"
        result = parse_math_expression(expression)
        self.assertEqual(result, ('10', 2, '33', 10, '+'))

    def test_invalid_format(self):
        expression = "12_2 33_10"
        with self.assertRaises(ValueError):
            parse_math_expression(expression)

    def test_invalid_base(self):
        expression = "12_1 + 33_10"
        with self.assertRaises(ValueError):
            parse_math_expression(expression)

    def test_multiple_operators(self):
        expression = "12_2 + - 33_10"
        with self.assertRaises(ValueError):
            parse_math_expression(expression)

    # Add more tests as needed to cover more cases. For example,
    # you may want to test with different operators (-, *, /) and
    # verify that the function extracts them correctly.


if __name__ == '__main__':
    unittest.main()
