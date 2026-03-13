from sources.minimization.BaseMinimizer import BaseMinimizer
from sources.BasicMethods import BasicMethods


class KarnaughMinimizer(BaseMinimizer):
    def minimize(self) -> str:
        if not self.terms:
            return "1" if self.is_sknf else "0"
        if len(self.terms) == 1 << len(self.variables):
            return "0" if self.is_sknf else "1"

        n = len(self.variables)

        split_index = n // 2
        row_variables = self.variables[:split_index]
        column_variables = self.variables[split_index:]

        print(
            f"Оси карты: cтроки - {''.join(row_variables)}, cтолбцы - {''.join(column_variables)}"
        )

        def get_gray_codes(bits):
            if bits == 0:
                return [""]
            return [
                BasicMethods.int_to_bits(i ^ (i >> 1)).zfill(bits)
                for i in range(1 << bits)
            ]

        row_gray = get_gray_codes(len(row_variables))
        column_gray = get_gray_codes(len(column_variables))

        header = " " * (len(row_variables) + 1) + "| " + " | ".join(column_gray)
        print("-" * (len(header) + 1))
        print(header)
        print("-" * (len(header) + 1))

        for row_code in row_gray:
            row_str = f"{row_code:<{len(row_variables)}}"
            for column_code in column_gray:
                binary = row_code + column_code
                value = 0
                for row in self.truth_table:
                    if "".join(map(str, row[:-1])) == binary:
                        value = row[-1]
                        break
                row_str += f" | {value:^{len(column_code)}}"
            print(row_str)

        print("-" * (len(header) + 1))

        primes = self.get_prime_implicants()
        essential_primes = self._solve_petrick(primes)
        return self._format_result(essential_primes)
