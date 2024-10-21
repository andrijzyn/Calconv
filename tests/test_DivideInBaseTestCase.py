import sys
import unittest

sys.path.insert(0, './')

from main import divide_in_base


class DivideInBaseTestCase(unittest.TestCase):
    def test_divide_in_base(self):
        self.assertEqual(divide_in_base('11', '10', 2), '1') # Only solid chars, so 1.1 = 1
        self.assertEqual(divide_in_base('0', '10', 2), '0')
        self.assertEqual(divide_in_base('101', '10', 2), '10') # Fixed BUG
        self.assertEqual(divide_in_base('11', '0', 2), 'Infinity')

    # noinspection PyArgumentList
    def test_empty_input(self):
        with self.assertRaises(TypeError):
            divide_in_base()

    def test_wrong_type(self):
        with self.assertRaises(TypeError):
            divide_in_base(11, 10, 2)


if __name__ == "__main__":
    unittest.main()
