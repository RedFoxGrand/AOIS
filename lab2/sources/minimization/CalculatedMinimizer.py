from sources.minimization.BaseMinimizer import BaseMinimizer


class CalculatedMinimizer(BaseMinimizer):
    def minimize(self) -> str:
        if not self.terms:
            return "1" if self.is_sknf else "0"
        if len(self.terms) == 1 << len(self.variables):
            return "0" if self.is_sknf else "1"

        primes = self.get_prime_implicants()
        print(f"Результат стадии склеивания: {primes}")

        essential_primes = self._solve_petrick(primes)
        return self._format_result(essential_primes)
