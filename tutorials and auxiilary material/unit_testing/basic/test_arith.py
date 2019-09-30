
from unittest import TestCase

class ArithTests(TestCase):

    def test_eq_1(self):
        x = 1
        y = 1
        self.assertEqual(x, y)

    def test_eq_2(self):
        x = 1
        y = 2
        self.assertEqual(x, y)
