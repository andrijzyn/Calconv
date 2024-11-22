import sys
import unittest
from operations.math.arithmetic import Arithmetic


class TestMultiplyInBase(unittest.TestCase):
    def test_multiply_in_base_positive_numbers(self): # Fixed BUG
        self.assertEqual(Arithmetic.multiply_in_base('11', '11', 2), '1001')
        self.assertEqual(Arithmetic.multiply_in_base('123', '456', 10), '56088')
        self.assertEqual(Arithmetic.multiply_in_base('A1', 'B2', 16), '6FF2')

    def test_multiply_in_base_with_zero(self):
        self.assertEqual(Arithmetic.multiply_in_base('0', '11', 2), '0')
        self.assertEqual(Arithmetic.multiply_in_base('123', '0', 10), '0')
        self.assertEqual(Arithmetic.multiply_in_base('0', '0', 16), '0')

    def test_multiply_in_base_with_one(self):
        self.assertEqual(Arithmetic.multiply_in_base('1', '11', 2), '11')
        self.assertEqual(Arithmetic.multiply_in_base('123', '1', 10), '123') # Fixed BUG
        self.assertEqual(Arithmetic.multiply_in_base('1', 'B2', 16), 'B2')

    def test_multiply_in_base_large_numbers(self):
        self.assertEqual(Arithmetic.multiply_in_base('FFFFFF', 'FFFFFF', 16), 'FFFFFE000001')
        self.assertEqual(Arithmetic.multiply_in_base('111111', '111111', 10), '12345654321')
        self.assertEqual(Arithmetic.multiply_in_base('11111', '11111', 2), '1111000001') # Fixed BUG


if __name__ == '__main__':
    unittest.main()
