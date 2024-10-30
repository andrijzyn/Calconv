import sys
import unittest
from operations.math.arithmetic import Arithmetic


class DivideInBaseTestCase(unittest.TestCase):
    def test_divide_in_base(self):
        self.assertEqual(Arithmetic.divide_in_base('11', '10', 2), '1') # Only solid chars, so 1.1 = 1
        self.assertEqual(Arithmetic.divide_in_base('0', '10', 2), '0')
        self.assertEqual(Arithmetic.divide_in_base('101', '10', 2), '10') # Fixed BUG
        self.assertEqual(Arithmetic.divide_in_base('11', '0', 2), 'Infinity')

    def test_empty_input(self):
        with self.assertRaises(TypeError):
            Arithmetic.divide_in_base()

    def test_wrong_type(self):
        with self.assertRaises(TypeError):
            Arithmetic.divide_in_base(11, 10, 2)


if __name__ == "__main__":
    unittest.main()
