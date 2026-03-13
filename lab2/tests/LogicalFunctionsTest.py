import unittest
from sources.LogicalFunctions import LogicalFunctions


class LogicalFunctionsTest(unittest.TestCase):
    def setUp(self):
        self.function = LogicalFunctions("a&b")
        self.function.build_truth_table()
        self.func_tautology = LogicalFunctions("a|!a")
        self.func_tautology.build_truth_table()

    def test_truth_table_generation(self):
        expected = [[0, 0, 0], [0, 1, 0], [1, 0, 0], [1, 1, 1]]
        self.assertEqual(self.function.truth_table, expected)

    def test_build_sdnf_and_sknf(self):
        self.assertEqual(self.function.build_sdnf(), "(a ∧ b)")
        self.assertTrue("∨" in self.function.build_sknf())

    def test_tautology_constants(self):
        self.assertEqual(self.func_tautology.build_sdnf(), "1")
        self.assertEqual(self.func_tautology.build_sknf(), "1")

    def test_zhegalkin_polynomial(self):
        self.assertEqual(self.function.build_zhegalkin_polynomial(), "ab")

    def test_dummy_variables(self):
        self.assertEqual(self.function.get_dummy_variables(), [])
        self.assertEqual(self.func_tautology.get_dummy_variables(), ["a"])

    def test_get_derivative(self):
        self.assertEqual(self.function.get_derivative(["a"]), [0, 1, 0, 1])

    def test_replacements(self):
        lf = LogicalFunctions("a->b~c")
        self.assertEqual(lf._replaced_expression, "a>b=c")

    def test_numeric_and_index_forms(self):
        sdnf_n, sknf_n = self.function.get_numeric_forms_sdnf_and_sknf()
        self.assertEqual(sdnf_n, "∨(3)")
        self.assertEqual(sknf_n, "∧(0, 1, 2)")
        self.assertEqual(self.function.get_index_form(), 1)

    def test_post_classes(self):
        classes = self.function.get_post_classes()
        self.assertEqual(
            classes, {"T0": True, "T1": True, "S": False, "M": True, "L": False}
        )

    def test_derivative_multivar(self):
        self.assertEqual(self.function.get_derivative(["a", "b"]), [1, 1, 1, 1])
