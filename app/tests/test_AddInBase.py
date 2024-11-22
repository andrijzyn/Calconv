import sys
import unittest
from operations.math.arithmetic import Arithmetic


class TestAddInBase(unittest.TestCase):
    def test_add_in_base_with_base_2(self):
        self.assertEqual(Arithmetic.add_in_base("1010", "1111", 2), "11001")

    def test_add_in_base_with_base_10(self):
        self.assertEqual(Arithmetic.add_in_base("123", "456", 10), "579")

    def test_add_in_base_with_base_16(self): # Fixed BUG
        self.assertEqual(Arithmetic.add_in_base("AB", "F", 16), "BA")

    def test_add_in_base_with_invalid_base(self):
        with self.assertRaises(ValueError):
            Arithmetic.add_in_base("10", "11", 1)

    def test_add_in_base_with_carry(self):
        self.assertEqual(Arithmetic.add_in_base("999", "1", 10), "1000")

    def test_add_in_base_with_padding(self):
        self.assertEqual(Arithmetic.add_in_base("123", "45", 10), "168")


if __name__ == "__main__":
    unittest.main()
