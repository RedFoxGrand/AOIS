from abc import ABC, abstractmethod


class BaseMinimizer(ABC):
    def __init__(
        self, truth_table: list[list[int]], variables: list[str], is_sknf: bool = False
    ):
        self._truth_table = truth_table
        self._variables = variables
        self._is_sknf = is_sknf
        self._terms = self._get_terms()

    @property
    def truth_table(self) -> list[list[int]]:
        return self._truth_table

    @property
    def variables(self) -> list[str]:
        return self._variables

    @property
    def is_sknf(self) -> bool:
        return self._is_sknf

    @property
    def terms(self) -> list[str]:
        return self._terms

    def _get_terms(self) -> list[str]:
        target_value = 0 if self.is_sknf else 1
        return [
            "".join(str(val) for val in row[:-1])
            for row in self.truth_table
            if row[-1] == target_value
        ]

    @staticmethod
    def _differs_by_one(constituent1: str, constituent2: str) -> str:
        difference_count = 0
        merged = []
        for c1, c2 in zip(constituent1, constituent2):
            if c1 == "X" or c2 == "X":
                if c1 != c2:
                    return ""
                merged.append("X")
            elif c1 != c2:
                difference_count += 1
                merged.append("X")
            else:
                merged.append(c1)
        return "".join(merged) if difference_count == 1 else ""

    def get_prime_implicants(self) -> list[str]:
        current_terms = set(self.terms)
        prime_implicants = set()

        while current_terms:
            next_terms = set()
            used_terms = set()
            terms_list = list(current_terms)

            for i in range(len(terms_list)):
                for j in range(i + 1, len(terms_list)):
                    merged = self._differs_by_one(terms_list[i], terms_list[j])
                    if merged:
                        next_terms.add(merged)
                        used_terms.add(terms_list[i])
                        used_terms.add(terms_list[j])

            unmerged = current_terms - used_terms
            prime_implicants.update(unmerged)
            current_terms = next_terms

        return list(prime_implicants)

    def _covers(self, implicant: str, term: str) -> bool:
        return all(i == "X" or i == j for i, j in zip(implicant, term))

    def _format_result(self, implicants: list[str]) -> str:
        result_terms = []
        for implicant in implicants:
            terms = []
            for i, char in enumerate(implicant):
                if self.is_sknf:
                    if char == "0":
                        terms.append(self.variables[i])
                    elif char == "1":
                        terms.append(f"!{self.variables[i]}")
                else:
                    if char == "1":
                        terms.append(self.variables[i])
                    elif char == "0":
                        terms.append(f"!{self.variables[i]}")

            if not terms:
                return "1" if not self.is_sknf else "0"

            if self.is_sknf:
                result_terms.append(
                    "(" + " ∨ ".join(terms) + ")" if len(terms) > 1 else terms[0]
                )
            else:
                result_terms.append(
                    "(" + " ∧ ".join(terms) + ")" if len(terms) > 1 else terms[0]
                )

        if not result_terms:
            return "1" if self.is_sknf else "0"

        joiner = " ∧ " if self.is_sknf else " ∨ "
        return joiner.join(result_terms)

    def _get_minimal_cover(self, primes: list[str]) -> list[str]:
        terms = self.terms
        essential_primes = []
        covered_terms = set()

        for term in terms:
            covering_primes = [prime for prime in primes if self._covers(prime, term)]
            if len(covering_primes) == 1:
                prime = covering_primes[0]
                if prime not in essential_primes:
                    essential_primes.append(prime)
                    covered_terms.update(t for t in terms if self._covers(prime, t))

        for term in terms:
            if term in covered_terms:
                continue

            for prime in primes:
                if self._covers(prime, term):
                    essential_primes.append(prime)
                    covered_terms.update(t for t in terms if self._covers(prime, t))
                    break

        return essential_primes

    def _solve_petrick(self, primes: list[str]) -> list[str]:
        term_indices = []
        for term in self.terms:
            indices = {i for i, prime in enumerate(primes) if self._covers(prime, term)}
            if indices:
                term_indices.append(indices)

        if not term_indices:
            return []

        current_product = [{part} for part in term_indices[0]]

        for i in range(1, len(term_indices)):
            next_factor = term_indices[i]
            new_product = []

            for product in current_product:
                for part in next_factor:
                    new_product.append(product | {part})

            new_product.sort(key=len)
            unique_product = []
            for part in new_product:
                if not any(existing.issubset(part) for existing in unique_product):
                    unique_product.append(part)

            current_product = unique_product

        best_indices = min(current_product, key=len)
        return [primes[i] for i in sorted(best_indices)]

    @abstractmethod
    def minimize(self) -> str:
        pass
