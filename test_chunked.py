from unittest import TestCase
import chunked


class TakeTest(TestCase):
    def test_simple_take(self):
        t = chunked.take(range(10), 5)
        self.assertEqual(t, [0, 1, 2, 3, 4])

    def test_null_take(self):
        t = chunked.take(range(10), 0)
        self.assertEqual(t, [])

    def test_negative_take(self):
        self.assertRaises(ValueError, lambda: chunked.take(-3, range(10)))

    def test_take_too_much(self):
        t = chunked.take(range(5), 10)
        self.assertEqual(t, [0, 1, 2, 3, 4])
