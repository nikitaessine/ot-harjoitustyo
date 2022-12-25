import unittest
from service.equations import Equations


class TestEquations(unittest.TestCase):

    def setUp(self):
        self.equations = Equations()
        self.equations.num1 = 6
        self.equations.num2 = 7
        self.equations.operat = "+"

    def test_plus_works(self):

        self.assertEqual(self.equations.plus(), 13)

    def test_minus_works(self):
        self.assertEqual(self.equations.minus(), -1)

    def test_return_value(self):
        self.assertEqual(str(self.equations), 'Paljonko on 6 + 7?')
