import unittest
import one


class Unitest(unittest.TestCase):
    def test_add(self):
        self.assertEqual(one.add(8, 4), 12)
        self.assertEqual(one.add(-4, 2), -2)

    def test_subtract(self):
        self.assertEqual(one.subtract(8, 4), 4)
        self.assertEqual(one.subtract(-4, 2), -6)

    def test_multiply(self):
        self.assertEqual(one.multiply(8, 4), 32)
        self.assertEqual(one.multiply(-4, 2), -8)

    def test_division(self):
        self.assertEqual(one.division(8, 4), 2)
        self.assertEqual(one.division(-4, 2), -2)
        self.assertRaises(ZeroDivisionError, one.division, 4, 0)


if __name__ == '__main__':
    unittest.main()
