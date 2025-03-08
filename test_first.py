from unittest import TestCase
from first import first
import traceback


class FirstTest(TestCase):
    def test_many(self):
        self.assertEqual(first(x for x in range(4)), 0)

    def test_one(self):
        self.assertEqual(first([3]), 3)

    def test_default(self):
        self.assertEqual(first([], 'boo'), 'boo')

    def test_empty_stop_iteration(self):
        try:
            first([])
        except ValueError:
            formatted_exc = traceback.format_exc()
            self.assertIn('StopIteration', formatted_exc)
            self.assertIn('The above exception was the direct cause', formatted_exc)
        else:
            self.fail()
