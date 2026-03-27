from BaseMinimizer import BaseMinimizer


class Minimizer(BaseMinimizer):
    def minimize(self) -> str:
        primes = self.get_prime_implicants()
        minimal_cover = self._solve_petrick(primes)
        return self._format_result(minimal_cover)
