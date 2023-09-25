import unittest
import two_unittest as two


class Unitest(unittest.TestCase):
    def test_add(self):
        self.assertEqual(two.add(8, 4), 12)
        self.assertEqual(two.add(-4, 2), -2)

    def test_subtract(self):
        self.assertEqual(two.subtract(8, 4), 4)
        self.assertEqual(two.subtract(-4, 2), -6)

    def test_multiply(self):
        self.assertEqual(two.multiply(8, 4), 32)
        self.assertEqual(two.multiply(-4, 2), -8)

    def test_division(self):
        self.assertEqual(two.division(8, 4), 2)
        self.assertEqual(two.division(-4, 2), -2)
        self.assertRaises(ZeroDivisionError, two.division, 4, 0)


if __name__ == '__main__':
    unittest.main()
