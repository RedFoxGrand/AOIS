import unittest
from sources.minimization.TableMinimizer import TableMinimizer


class TableMinimizerTest(unittest.TestCase):
    def setUp(self):
        self.truth_table = [[0, 0, 0], [0, 1, 0], [1, 0, 0], [1, 1, 1]]
        self.variables = ["a", "b"]

    def test_minimize_sdnf(self):
        minimizer = TableMinimizer(self.truth_table, self.variables, is_sknf=False)
        self.assertEqual(minimizer.minimize(), "(a ∧ b)")

    def test_minimize_sknf(self):
        minimizer = TableMinimizer(self.truth_table, self.variables, is_sknf=True)
        self.assertTrue("a" in minimizer.minimize() and "b" in minimizer.minimize())

    def test_minimize_or_sdnf(self):
        truth_table_or = [[0, 0, 0], [0, 1, 1], [1, 0, 1], [1, 1, 1]]
        minimizer = TableMinimizer(truth_table_or, self.variables, is_sknf=False)
        result = minimizer.minimize()
        self.assertTrue("a" in result and "b" in result)