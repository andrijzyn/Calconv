import sys
import unittest

sys.path.insert(0, './')

from main import subtract_in_base


class TestSubtractInBase(unittest.TestCase):
    def test_base10(self):
        self.assertEqual(subtract_in_base('100', '50', 10), '50')

    def test_base2(self): # Fixed BUG
        self.assertEqual(subtract_in_base('101', '110', 2), '-1')

    def test_base16(self): # Fixed BUG
        self.assertEqual(subtract_in_base('A9', 'B7', 16), '-E')

    def test_base10_borrow(self): # Fixed BUG
        self.assertEqual(subtract_in_base('100', '200', 10), '-100')

    def test_identical_numbers(self):
        self.assertEqual(subtract_in_base('123', '123', 10), '0')

    def test_num1_less_than_num2(self): # Fixed BUG
        self.assertEqual(subtract_in_base('23', '45', 10), '-22')


if __name__ == '__main__':
    unittest.main()
