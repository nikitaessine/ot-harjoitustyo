import unittest
from service.equations import Equations


class TestEquations(unittest.TestCase):

    def setUp(self):
        self.equations = Equations()
        self.equations.num1 = 6
        self.equations.num2 = 7
        self.equations.operat = "+"
        self.entry_value = 13

    def test_plus_works(self):

        self.assertEqual(self.equations.plus(), 13)

    def test_minus_works(self):
        self.assertEqual(self.equations.minus(), -1)
    
    def test_result_checker_returns_true(self):
        self.assertEqual(self.equations.result_checker(self.entry_value), True)

    def test_result_checker_returns_false_if_wrong_input(self):
        self.assertEqual(self.equations.result_checker(10), False)
    
    def test_cheer_if_right_result(self):
        self.assertIn(self.equations.cheer_if_right_result(), self.equations.cheers)

    def test_cheer_if_wrong_result(self):
        self.assertIn(self.equations.cheer_if_wrong_result(), self.equations.cheers_if_wrong_answer)

    def test_return_value(self):
        self.assertEqual(str(self.equations), 'Paljonko on 6 + 7?')
