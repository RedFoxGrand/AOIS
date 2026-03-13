import unittest
from sources.minimization.CalculatedMinimizer import CalculatedMinimizer


class CalculatedMinimizerTest(unittest.TestCase):
    def setUp(self):
        self.truth_table = [[0, 0, 0], [0, 1, 1], [1, 0, 1], [1, 1, 1]]
        self.truth_table_tautology = [[0, 0, 1], [0, 1, 1], [1, 0, 1], [1, 1, 1]]
        self.variables = ["a", "b"]

    def test_minimize_sdnf(self):
        minimizer = CalculatedMinimizer(
            self.truth_table, self.variables, is_sknf=False
        )
        result = minimizer.minimize()
        self.assertTrue("a" in result and "b" in result and "∨" in result)

    def test_minimize_tautology(self):
        minimizer = CalculatedMinimizer(
            self.truth_table_tautology, self.variables, is_sknf=False
        )
        self.assertEqual(minimizer.minimize(), "1")
        minimizer_sknf = CalculatedMinimizer(
            self.truth_table_tautology, self.variables, is_sknf=True
        )
        self.assertEqual(minimizer_sknf.minimize(), "1")