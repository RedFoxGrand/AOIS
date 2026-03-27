import unittest
from Minimizer import Minimizer


class TestMinimizer(unittest.TestCase):
    def test_sdnf_simple_or(self):
        truth_table = [
            [0, 0, 0],
            [0, 1, 1],
            [1, 0, 1],
            [1, 1, 1],
        ]
        variables = ["a", "b"]
        minimizer = Minimizer(truth_table, variables, is_sknf=False)
        self.assertIn(minimizer.minimize(), ["a ∨ b", "b ∨ a"])

    def test_sknf_simple_or(self):
        truth_table = [
            [0, 0, 0],
            [0, 1, 1],
            [1, 0, 1],
            [1, 1, 1],
        ]
        variables = ["a", "b"]
        minimizer = Minimizer(truth_table, variables, is_sknf=True)
        self.assertEqual(minimizer.minimize(), "(a ∨ b)")

    def test_sdnf_simple_and(self):
        truth_table = [
            [0, 0, 0],
            [0, 1, 0],
            [1, 0, 0],
            [1, 1, 1],
        ]
        variables = ["a", "b"]
        minimizer = Minimizer(truth_table, variables, is_sknf=False)
        self.assertEqual(minimizer.minimize(), "(a ∧ b)")

    def test_sknf_simple_and(self):
        truth_table = [
            [0, 0, 0],
            [0, 1, 0],
            [1, 0, 0],
            [1, 1, 1],
        ]
        variables = ["a", "b"]
        minimizer = Minimizer(truth_table, variables, is_sknf=True)
        self.assertIn(minimizer.minimize(), ["a ∧ b", "b ∧ a"])

    def test_sdnf_with_dont_care(self):
        truth_table = [
            [0, 0, 0],
            [0, 1, 1],
            [1, 0, -1],
            [1, 1, -1],
        ]
        variables = ["a", "b"]
        minimizer = Minimizer(truth_table, variables, is_sknf=False)
        self.assertEqual(minimizer.minimize(), "b")

    def test_sknf_with_dont_care(self):
        truth_table = [
            [0, 0, 0],
            [0, 1, 1],
            [1, 0, -1],
            [1, 1, -1],
        ]
        variables = ["a", "b"]
        minimizer = Minimizer(truth_table, variables, is_sknf=True)
        self.assertEqual(minimizer.minimize(), "b")

    def test_always_true_sdnf(self):
        truth_table = [[0, 0, 1], [0, 1, 1], [1, 0, 1], [1, 1, 1]]
        variables = ["a", "b"]
        minimizer = Minimizer(truth_table, variables, is_sknf=False)
        self.assertEqual(minimizer.minimize(), "1")

    def test_always_false_sdnf(self):
        truth_table = [[0, 0, 0], [0, 1, 0], [1, 0, 0], [1, 1, 0]]
        variables = ["a", "b"]
        minimizer = Minimizer(truth_table, variables, is_sknf=False)
        self.assertEqual(minimizer.minimize(), "0")


if __name__ == "__main__":
    unittest.main()
