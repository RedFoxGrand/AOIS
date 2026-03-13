from sources.minimization.BaseMinimizer import BaseMinimizer


class TableMinimizer(BaseMinimizer):
    def minimize(self) -> str:
        if not self.terms:
            return "1" if self.is_sknf else "0"
        if len(self.terms) == 1 << len(self.variables):
            return "0" if self.is_sknf else "1"

        primes = self.get_prime_implicants()
        terms = self.terms
        print(f"Результат стадии склеивания: {primes}")

        print(f"Таблица покрытий ({'КНФ' if self.is_sknf else 'ДНФ'}):")
        header = f"{'Импликанты':<15} | " + " | ".join(terms)
        print("-" * (len(header) + 1))
        print(header)
        print("-" * (len(header) + 1))

        for prime in primes:
            row_cells = []
            for term in terms:
                if self._covers(prime, term):
                    row_cells.append(f"{'X':^{len(term)}}")
                else:
                    row_cells.append(" " * len(term))
            print(f"{self._format_result([prime]):<15} | " + " | ".join(row_cells))
        print("-" * (len(header) + 1))

        essential_primes = self._get_minimal_cover(primes)
        return self._format_result(essential_primes)
