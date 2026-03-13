from sources.BasicMethods import BasicMethods
from sources.ExpressionParser import ExpressionParser


class LogicalFunctions:
    def __init__(self, expression: str):
        self.expression = expression.replace(" ", "")
        self._replaced_expression = self.expression.replace("->", ">").replace("~", "=")
        ExpressionParser.validate(self._replaced_expression)
        self._variables = ExpressionParser.get_variables(self._replaced_expression)
        self._rpn = ExpressionParser.to_rpn(self._replaced_expression)
        self._truth_table = []
        self._function_value_vector = []

    @property
    def variables(self) -> list:
        return self._variables

    @property
    def truth_table(self) -> list:
        return self._truth_table

    @property
    def function_vector(self) -> list:
        return self._function_value_vector

    def build_truth_table(self):
        n = len(self._variables)
        interpretations = BasicMethods.generate_combinations(n)

        print(" | ".join(self._variables) + " | f")
        print("-" * (4 * n + 2))

        for inter in interpretations:
            interpretation = dict(zip(self._variables, inter))
            result = ExpressionParser.evaluate(self._rpn, interpretation)

            self._truth_table.append(inter + [result])
            self._function_value_vector.append(result)
            print(f"{' | '.join(map(str, inter))} | {result}")

    def build_sdnf(self) -> str:
        sdnf = []
        for row in self._truth_table:
            if row[-1] == 1:
                constituent = []
                for variable, value in zip(self._variables, row[:-1]):
                    constituent.append(variable if value == 1 else f"!{variable}")
                sdnf.append(
                    "(" + " ∧ ".join(constituent) + ")"
                    if len(constituent) > 1
                    else constituent[0]
                )

        if not sdnf:
            return "0"
        if len(sdnf) == 1 << len(self._variables):
            return "1"

        return " ∨ ".join(sdnf)

    def build_sknf(self) -> str:
        sknf = []
        for row in self._truth_table:
            if row[-1] == 0:
                constituent = []
                for variable, value in zip(self._variables, row[:-1]):
                    constituent.append(variable if value == 0 else f"!{variable}")
                sknf.append(
                    "(" + " ∨ ".join(constituent) + ")"
                    if len(constituent) > 1
                    else constituent[0]
                )

        if not sknf:
            return "1"
        if len(sknf) == 1 << len(self._variables):
            return "0"

        return " ∧ ".join(sknf)

    def get_numeric_forms_sdnf_and_sknf(self) -> tuple:
        sdnf_indices = [
            str(i) for i, row in enumerate(self._truth_table) if row[-1] == 1
        ]
        sknf_indices = [
            str(i) for i, row in enumerate(self._truth_table) if row[-1] == 0
        ]

        sdnf_numeric_form = f"∨({', '.join(sdnf_indices)})" if sdnf_indices else "∨()"
        sknf_numeric_form = f"∧({', '.join(sknf_indices)})" if sknf_indices else "∧()"

        return sdnf_numeric_form, sknf_numeric_form

    def get_index_form(self) -> int:
        value = 0
        for v in self._function_value_vector:
            value = value * 2 + v
        return value

    def _get_zhegalkin_coefficients(self) -> list:
        current_row = list(self._function_value_vector)
        coefficients = []

        while current_row:
            coefficients.append(current_row[0])
            current_row = [
                current_row[k] ^ current_row[k + 1] for k in range(len(current_row) - 1)
            ]

        return coefficients

    def build_zhegalkin_polynomial(self) -> str:
        coefficients = self._get_zhegalkin_coefficients()
        terms = []
        n = len(self._variables)

        for i, coefficient in enumerate(coefficients):
            if coefficient == 1:
                if i == 0:
                    terms.append("1")
                else:
                    term_part = []
                    for bit in range(n - 1, -1, -1):
                        if (i >> bit) & 1:
                            term_part.append(self._variables[n - bit - 1])
                    terms.append("".join(term_part))

        return " ⊕ ".join(terms) if terms else "0"

    def get_post_classes(self) -> dict:
        result_vector = self._function_value_vector
        length = len(result_vector)

        is_save_zero = result_vector[0] == 0
        is_save_one = result_vector[-1] == 1

        is_self_dual = True
        for i in range(length // 2):
            if result_vector[i] == result_vector[length - 1 - i]:
                is_self_dual = False
                break

        is_monotonic = True
        for i in range(length):
            for j in range(i + 1, length):
                if (i & j) == i:
                    if result_vector[i] > result_vector[j]:
                        is_monotonic = False
                        break
            if not is_monotonic:
                break

        is_linear = True
        coefficients = self._get_zhegalkin_coefficients()
        for i, coeff in enumerate(coefficients):
            bits = BasicMethods.int_to_bits(i)

            if coeff == 1 and bits.count("1") > 1:
                is_linear = False
                break

        return {
            "T0": is_save_zero,
            "T1": is_save_one,
            "S": is_self_dual,
            "M": is_monotonic,
            "L": is_linear,
        }

    def get_dummy_variables(self) -> list[str]:
        dummy_variables = []
        n = len(self._variables)
        result_vector = self._function_value_vector

        for k in range(n):
            variable = self._variables[n - 1 - k]
            step = 1 << k
            is_dummy = True

            for i in range(len(result_vector)):
                if (i & step) == 0:
                    if result_vector[i] != result_vector[i + step]:
                        is_dummy = False
                        break

            if is_dummy:
                dummy_variables.append(variable)

        return sorted(dummy_variables)

    def get_derivative(self, diff_vars: list[str]) -> list[int]:
        n = len(self._variables)
        current_vector = list(self._function_value_vector)

        for var in diff_vars:
            if var not in self._variables:
                continue

            variable_index = self._variables.index(var)
            k = n - 1 - variable_index
            step = 1 << k

            next_vector = [0] * len(current_vector)

            for i in range(len(current_vector)):
                if (i & step) == 0:
                    deriv_value = current_vector[i] ^ current_vector[i + step]
                    next_vector[i] = next_vector[i + step] = deriv_value

            current_vector = next_vector

        return current_vector
