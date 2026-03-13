import unittest
from sources.minimization.BaseMinimizer import BaseMinimizer


class DummyMinimizer(BaseMinimizer):
    def minimize(self) -> str:
        return ""


class BaseMinimizerTest(unittest.TestCase):
    def setUp(self):
        self.minimizer = DummyMinimizer(
            [[0, 0, 0], [0, 1, 1], [1, 0, 1], [1, 1, 1]], ["a", "b"]
        )

    def test_differs_by_one(self):
        self.assertEqual(self.minimizer._differs_by_one("00", "01"), "0X")
        self.assertEqual(self.minimizer._differs_by_one("0X", "1X"), "XX")
        self.assertEqual(self.minimizer._differs_by_one("00", "11"), "")

    def test_covers(self):
        self.assertTrue(self.minimizer._covers("0X", "01"))
        self.assertFalse(self.minimizer._covers("0X", "11"))

    def test_format_result(self):
        self.assertEqual(self.minimizer._format_result(["1X"]), "a")
        self.assertEqual(self.minimizer._format_result([]), "0")

        minimizer_sknf = DummyMinimizer(
            [[0, 0, 0], [0, 1, 1]], ["a", "b"], is_sknf=True
        )
        self.assertEqual(minimizer_sknf._format_result([]), "1")
        self.assertEqual(minimizer_sknf._format_result(["0X"]), "a")
