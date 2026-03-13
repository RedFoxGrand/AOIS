class BasicMethods:
    @staticmethod
    def generate_combinations(n: int) -> list:
        interpretations = []
        for i in range(1 << n):
            row = [(i >> bit) & 1 for bit in range(n - 1, -1, -1)]
            interpretations.append(row)
        return interpretations

    @staticmethod
    def int_to_bits(val: int) -> str:
        if val == 0:
            return "0"
        bits = ""
        while val > 0:
            bits = str(val % 2) + bits
            val //= 2
        return bits
