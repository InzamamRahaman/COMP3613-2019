from unittest import TestCase
from complex import Complex

class ComplexTest(TestCase):

    def test_add_1(self):
        x = Complex(1, 2)
        y = Complex(3, 4)
        z = x + y
        self.assertEqual(z.real, 4)
        self.assertEqual(z.img, 6)

    def test_add_2(self):
        x = Complex(1, 2)
        y = 3
        z = x + y
        self.assertEqual(z.real, 4)
        self.assertEqual(z.img, 2)
