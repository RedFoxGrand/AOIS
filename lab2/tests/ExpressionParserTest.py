import unittest
from sources.ExpressionParser import ExpressionParser


class ExpressionParserTest(unittest.TestCase):
    def test_validate_valid_expression(self):
        try:
            ExpressionParser.validate("!(a&b)|c")
        except ValueError:
            self.fail("Некорректная логическая формула!")

    def test_validate_invalid_expression(self):
        with self.assertRaises(ValueError):
            ExpressionParser.validate("a&&b")
        with self.assertRaises(ValueError):
            ExpressionParser.validate("(a&b")
        with self.assertRaises(ValueError):
            ExpressionParser.validate("")
        with self.assertRaises(ValueError):
            ExpressionParser.validate("a$b")
        with self.assertRaises(ValueError):
            ExpressionParser.validate("a&")
        with self.assertRaises(ValueError):
            ExpressionParser.validate("(a&b))")
        with self.assertRaises(ValueError):
            ExpressionParser.validate("a!")
        with self.assertRaises(ValueError):
            ExpressionParser.validate("&a")

    def test_get_variables(self):
        self.assertEqual(ExpressionParser.get_variables("!c|b&a"), ["a", "b", "c"])

    def test_to_rpn(self):
        self.assertEqual(ExpressionParser.to_rpn("a|b"), ["a", "b", "|"])

    def test_evaluate(self):
        self.assertEqual(
            ExpressionParser.evaluate(["a", "b", "&"], {"a": 1, "b": 1}), 1
        )
        self.assertEqual(
            ExpressionParser.evaluate(["a", "b", "&"], {"a": 1, "b": 0}), 0
        )
        self.assertEqual(ExpressionParser.evaluate(["a", "!"], {"a": 0}), 1)
        self.assertEqual(
            ExpressionParser.evaluate(["a", "b", "|"], {"a": 0, "b": 1}), 1
        )
        self.assertEqual(
            ExpressionParser.evaluate(["a", "b", ">"], {"a": 1, "b": 0}), 0
        )
        self.assertEqual(
            ExpressionParser.evaluate(["a", "b", "="], {"a": 1, "b": 1}), 1
        )
