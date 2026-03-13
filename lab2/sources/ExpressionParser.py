class ExpressionParser:
    @staticmethod
    def validate(expression: str) -> None:
        if not expression:
            raise ValueError("Выражение не может быть пустым!")

        valid_chars = set("!&|>=()")
        bracket_count = 0
        previous_type = "begin"

        for i, char in enumerate(expression):
            if not (char.isalpha() or char in valid_chars):
                raise ValueError(f"Недопустимый символ '{char}' на позиции {i + 1}!")

            if char == "(":
                bracket_count += 1
                if previous_type in ("variable", "close_bracket"):
                    raise ValueError(
                        f"Пропущен оператор перед открывающей скобкой на позиции {i + 1}!"
                    )
                previous_type = "open_bracket"

            elif char == ")":
                bracket_count -= 1
                if bracket_count < 0:
                    raise ValueError(f"Лишняя закрывающая скобка на позиции {i + 1}!")
                if previous_type in (
                    "open_bracket",
                    "binary_operator",
                    "unary_operator",
                ):
                    raise ValueError(
                        f"Пустые скобки или оператор перед закрывающей скобкой на позиции {i + 1}!"
                    )
                previous_type = "close_bracket"

            elif char.isalpha():
                if previous_type in ("variable", "close_bracket"):
                    raise ValueError(
                        f"Пропущен оператор перед переменной '{char}' на позиции {i + 1}!"
                    )
                previous_type = "variable"

            elif char == "!":
                if previous_type in ("variable", "close_bracket"):
                    raise ValueError(
                        f"Отрицание '!' не может стоять после переменной или скобки на позиции {i + 1}!"
                    )
                previous_type = "unary_operator"

            elif char in "&|>=":
                if previous_type in (
                    "begin",
                    "binary_operator",
                    "unary_operator",
                    "open_bracket",
                ):
                    raise ValueError(
                        f"Бинарный оператор '{char}' стоит в неверном месте на позиции {i + 1}!"
                    )
                previous_type = "binary_operator"

        if bracket_count != 0:
            raise ValueError(
                "Несовпадение количества открывающих и закрывающих скобок!"
            )
        if previous_type in ("binary_operator", "unary_operator"):
            raise ValueError("Выражение не может заканчиваться оператором!")

    @staticmethod
    def get_variables(expression: str) -> list:
        variables_set = set(char for char in expression if char.isalpha())
        return sorted(list(variables_set))

    @staticmethod
    def to_rpn(expression: str) -> list:
        priority = {"!": 4, "&": 3, "|": 2, ">": 1, "=": 1, "(": 0}
        output = []
        stack = []

        for char in expression:
            if char.isalpha():
                output.append(char)
            elif char == "(":
                stack.append(char)
            elif char == ")":
                while stack and stack[-1] != "(":
                    output.append(stack.pop())
                if stack:
                    stack.pop()
            elif char in priority:
                if char == "!":
                    while stack and priority[stack[-1]] > priority[char]:
                        output.append(stack.pop())
                else:
                    while stack and priority[stack[-1]] >= priority[char]:
                        output.append(stack.pop())
                stack.append(char)

        while stack:
            output.append(stack.pop())

        return output

    @staticmethod
    def evaluate(rpn: list, interpretation: dict) -> int:
        stack = []

        for token in rpn:
            if token.isalpha():
                stack.append(interpretation[token])
            elif token == "!":
                value = stack.pop()
                stack.append(1 - value)
            else:
                value2 = stack.pop()
                value1 = stack.pop()

                if token == "&":
                    stack.append(value1 & value2)
                elif token == "|":
                    stack.append(value1 | value2)
                elif token == ">":
                    stack.append(1 if value1 <= value2 else 0)
                elif token == "=":
                    stack.append(1 if value1 == value2 else 0)

        return stack[0]
