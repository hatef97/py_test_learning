import unittest
from person import Person

class PersonTest(unittest.TestCase):
    def setUp(self):
        self.p1 = Person('hatef', 'barin')
        self.p2 = Person('john', 'wick')

    def tearDown(self):
        print('Done...')

    def test_fullname(self):

        self.assertEqual(self.p1.fullname(), 'hatef barin')
        self.assertEqual(self.p2.fullname(), 'john wick')

    def test_email(self):

        self.assertEqual(self.p1.email(), 'hatefbarin@email.com')
        self.assertEqual(self.p2.email(), 'johnwick@email.com')


if __name__ == '__main__':
    unittest.main()