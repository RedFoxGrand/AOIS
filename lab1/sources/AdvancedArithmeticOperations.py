from sources.BasicFunctions import BasicFunctions
from sources.BinaryConverter import BinaryConverter
from sources.BasicArithmeticOperations import BasicArithmeticOperations
from sources.BasicFunctions import LENGTH_OF_BITS
from sources.BasicFunctions import LENGTH_OF_INT_PART


class AdvancedArithmeticOperations:
    @staticmethod
    def multiply_in_sign_magnitude(input_number1: str, input_number2: str) -> list[int]:
        number1 = BinaryConverter.converting_to_sign_magnitude(input_number1)
        number2 = BinaryConverter.converting_to_sign_magnitude(input_number2)

        sign1 = number1[0]
        sign2 = number2[0]

        number1[0] = 0
        number2[0] = 0

        product = BasicFunctions.create_empty_bits()

        for i in range(LENGTH_OF_BITS - 1, 0, -1):
            if number2[i] == 1:
                shift = LENGTH_OF_BITS - 1 - i
                shifted_num1 = BasicFunctions.create_empty_bits()
                for j in range(LENGTH_OF_BITS):
                    if j + shift < LENGTH_OF_BITS:
                        shifted_num1[j] = number1[j + shift]

                product = BasicArithmeticOperations._add_lists(product, shifted_num1)

        product[0] = 1 if sign1 != sign2 else 0

        return product

    @staticmethod
    def _is_greater_or_equal(bits1: list[int], bits2: list[int]) -> bool:
        for i in range(LENGTH_OF_BITS):
            if bits1[i] == bits2[i]:
                continue
            return bits1[i] > bits2[i]
        return True

    @staticmethod
    def _subtract_lists_positive(bits1: list[int], bits2: list[int]) -> list[int]:
        result = BasicFunctions.create_empty_bits()
        borrow = 0
        for i in range(LENGTH_OF_BITS - 1, -1, -1):
            diff = bits1[i] - bits2[i] - borrow
            if diff < 0:
                diff += 2
                borrow = 1
            else:
                borrow = 0
            result[i] = diff
        return result

    @staticmethod
    def divide_in_sign_magnitude(input_number1: str, input_number2: str) -> list[int]:
        number1 = BinaryConverter.converting_to_sign_magnitude(input_number1)
        number2 = BinaryConverter.converting_to_sign_magnitude(input_number2)

        if BasicFunctions.bin_to_int(number2[1:]) == 0:
            raise ZeroDivisionError("Division by zero")

        sign1 = number1[0]
        sign2 = number2[0]

        number1[0] = 0
        number2[0] = 0

        quotient_int = BasicFunctions.create_empty_bits()
        remainder = BasicFunctions.create_empty_bits()

        for i in range(1, LENGTH_OF_BITS):
            for j in range(LENGTH_OF_BITS - 1):
                remainder[j] = remainder[j + 1]
            remainder[LENGTH_OF_BITS - 1] = number1[i]

            if AdvancedArithmeticOperations._is_greater_or_equal(remainder, number2):
                remainder = AdvancedArithmeticOperations._subtract_lists_positive(
                    remainder, number2
                )
                quotient_int[i] = 1

        quotient_frac = BasicFunctions.create_empty_bits(LENGTH_OF_INT_PART)
        for i in range(LENGTH_OF_INT_PART):
            for j in range(LENGTH_OF_BITS - 1):
                remainder[j] = remainder[j + 1]
            remainder[LENGTH_OF_BITS - 1] = 0

            if AdvancedArithmeticOperations._is_greater_or_equal(remainder, number2):
                remainder = AdvancedArithmeticOperations._subtract_lists_positive(
                    remainder, number2
                )
                quotient_frac[i] = 1

        final_result = BasicFunctions.create_empty_bits()
        final_result[0] = 1 if sign1 != sign2 else 0
        final_result[1:LENGTH_OF_INT_PART] = quotient_int[
            LENGTH_OF_BITS - LENGTH_OF_INT_PART + 1 :
        ]
        final_result[LENGTH_OF_INT_PART:] = quotient_frac

        return final_result
