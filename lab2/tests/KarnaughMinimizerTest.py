import unittest
from sources.minimization.KarnaughMinimizer import KarnaughMinimizer


class KarnaughMinimizerTest(unittest.TestCase):
    def setUp(self):
        self.truth_table_impossible = [[0, 0, 0], [0, 1, 0], [1, 0, 0], [1, 1, 0]]
        self.variables = ["a", "b"]

    def test_minimize_contradiction_sdnf(self):
        minimizer = KarnaughMinimizer(
            self.truth_table_impossible, self.variables, is_sknf=False
        )
        self.assertEqual(minimizer.minimize(), "0")

    def test_minimize_contradiction_sknf(self):
        minimizer = KarnaughMinimizer(
            self.truth_table_impossible, self.variables, is_sknf=True
        )
        self.assertEqual(minimizer.minimize(), "0")

    def test_minimize_normal_function(self):
        truth_table_or = [[0, 0, 0], [0, 1, 1], [1, 0, 1], [1, 1, 1]]
        minimizer = KarnaughMinimizer(truth_table_or, self.variables, is_sknf=False)
        self.assertTrue("a" in minimizer.minimize() and "b" in minimizer.minimize())
