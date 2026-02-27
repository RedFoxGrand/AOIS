from sources.BinaryConverter import BinaryConverter
from sources.BasicArithmeticOperations import BasicArithmeticOperations
from sources.AdvancedArithmeticOperations import AdvancedArithmeticOperations
from sources.IEEE754 import IEEE754
from sources.BCD2421 import BCD2421
from sources.Verification import Verification


if __name__ == "__main__":

    def print_info(bits: list[int], text: str, converter=None) -> None:
        val = converter(bits) if converter else None
        if converter == Verification.sign_magnitude_division_to_decimal:
            val_str = f" ({val:.5f})" if val is not None else ""
            s = "".join(map(str, bits))
            print(f"{text}: {s[:16]}.{s[16:]}{val_str}")
        else:
            if isinstance(val, float):
                val_str = f" ({val:.5f})" if val is not None else ""
            else:
                val_str = f" ({val})" if val is not None else ""
            print(f"{text}: {''.join(map(str, bits))}{val_str}")

    print_info(
        BinaryConverter.converting_to_sign_magnitude("25"),
        "25 в прямом коде",
        Verification.sign_magnitude_to_decimal,
    )
    print_info(
        BinaryConverter.converting_to_ones_complement("25"),
        "25 в обратном коде",
        Verification.ones_complement_to_decimal,
    )
    print_info(
        BinaryConverter.converting_to_twos_complement("25"),
        "25 в дополнительном коде",
        Verification.twos_complement_to_decimal,
    )

    print_info(
        BinaryConverter.converting_to_sign_magnitude("-25"),
        "-25 в прямом коде",
        Verification.sign_magnitude_to_decimal,
    )
    print_info(
        BinaryConverter.converting_to_ones_complement("-25"),
        "-25 в обратном коде",
        Verification.ones_complement_to_decimal,
    )
    print_info(
        BinaryConverter.converting_to_twos_complement("-25"),
        "-25 в дополнительном коде",
        Verification.twos_complement_to_decimal,
    )

    print()
    print_info(
        BasicArithmeticOperations.add_in_twos_complement("25", "-25"),
        "Сумма 25 и -25",
        Verification.twos_complement_to_decimal,
    )
    print_info(
        BasicArithmeticOperations.add_in_twos_complement("-25", "9"),
        "Сумма -25 и 9",
        Verification.twos_complement_to_decimal,
    )
    print_info(
        BasicArithmeticOperations.add_in_twos_complement("25", "-9"),
        "Сумма 25 и -9",
        Verification.twos_complement_to_decimal,
    )

    print()
    print_info(
        BasicArithmeticOperations.subtract_in_twos_complement("25", "25"),
        "Разность 25 и 25",
        Verification.twos_complement_to_decimal,
    )
    print_info(
        BasicArithmeticOperations.subtract_in_twos_complement("-25", "-9"),
        "Разность -25 и -9",
        Verification.twos_complement_to_decimal,
    )
    print_info(
        BasicArithmeticOperations.subtract_in_twos_complement("25", "9"),
        "Разность 25 и 9",
        Verification.twos_complement_to_decimal,
    )

    print()
    print_info(
        AdvancedArithmeticOperations.multiply_in_sign_magnitude("5", "5"),
        "Произведение 5 и 5",
        Verification.sign_magnitude_to_decimal,
    )
    print_info(
        AdvancedArithmeticOperations.multiply_in_sign_magnitude("-5", "5"),
        "Произведение -5 и 5",
        Verification.sign_magnitude_to_decimal,
    )
    print_info(
        AdvancedArithmeticOperations.multiply_in_sign_magnitude("11", "0"),
        "Произведение 11 и 0",
        Verification.sign_magnitude_to_decimal,
    )

    print()
    print_info(
        AdvancedArithmeticOperations.divide_in_sign_magnitude("19", "4"),
        "Частное 19 и 4",
        Verification.sign_magnitude_division_to_decimal,
    )
    print_info(
        AdvancedArithmeticOperations.divide_in_sign_magnitude("-36", "9"),
        "Частное -36 и 9",
        Verification.sign_magnitude_division_to_decimal,
    )
    print_info(
        AdvancedArithmeticOperations.divide_in_sign_magnitude("-22", "-7"),
        "Частное -22 и -7",
        Verification.sign_magnitude_division_to_decimal,
    )
    try:
        print_info(
            AdvancedArithmeticOperations.divide_in_sign_magnitude("0", "0"),
            "Частное 0 и 0",
            Verification.sign_magnitude_division_to_decimal,
        )
    except ZeroDivisionError as e:
        print(f"Частное 0 и 0: Ошибка {e}")

    print()
    print_info(
        IEEE754.converting_from_decimal_to_ieee754("22.15625"),
        "22.15625 в IEEE754",
        Verification.ieee754_to_decimal,
    )
    print_info(
        IEEE754.converting_from_decimal_to_ieee754("-22.15625"),
        "-22.15625 в IEEE754",
        Verification.ieee754_to_decimal,
    )
    print_info(
        IEEE754.converting_from_decimal_to_ieee754("7.25"),
        "7.25 в IEEE754",
        Verification.ieee754_to_decimal,
    )
    print_info(
        IEEE754.converting_from_decimal_to_ieee754("0.0"),
        "0.0 в IEEE754",
        Verification.ieee754_to_decimal,
    )
    print_info(
        IEEE754.converting_from_decimal_to_ieee754("-0"),
        "-0 в IEEE754",
        Verification.ieee754_to_decimal,
    )
    print_info(
        IEEE754.converting_from_decimal_to_ieee754("123.1"),
        "123.1 в IEEE754",
        Verification.ieee754_to_decimal,
    )
    print_info(
        IEEE754.converting_from_decimal_to_ieee754("-0.75"),
        "-0.75 в IEEE754",
        Verification.ieee754_to_decimal,
    )
    
    print()
    print_info(
        IEEE754.add_in_ieee754("22.15625", "0"),
        "Сумма 22.15625 и 0 в IEEE754",
        Verification.ieee754_to_decimal,
    )
    print_info(
        IEEE754.add_in_ieee754("22.15625", "11.25"),
        "Сумма 22.15625 и 11.25 в IEEE754",
        Verification.ieee754_to_decimal,
    )
    print_info(
        IEEE754.add_in_ieee754("22.15625", "-27"),
        "Сумма 22.15625 и -27 в IEEE754",
        Verification.ieee754_to_decimal,
    )
    print_info(
        IEEE754.add_in_ieee754("22.15625", "1.1"),
        "Сумма 22.15625 и 1.1 в IEEE754",
        Verification.ieee754_to_decimal,
    )

    print()
    print_info(
        IEEE754.subtract_in_ieee754("0", "22.15625"),
        "Разность 0 и 22.15625 в IEEE754",
        Verification.ieee754_to_decimal,
    )
    print_info(
        IEEE754.subtract_in_ieee754("22.15625", "56.75"),
        "Разность 22.15625 и 56.75 в IEEE754",
        Verification.ieee754_to_decimal,
    )
    print_info(
        IEEE754.subtract_in_ieee754("22.15625", "-27"),
        "Разность 22.15625 и -27 в IEEE754",
        Verification.ieee754_to_decimal,
    )
    print_info(
        IEEE754.subtract_in_ieee754("22.15625", "1.1"),
        "Разность 22.15625 и 1.1 в IEEE754",
        Verification.ieee754_to_decimal,
    )

    print()
    print_info(
        IEEE754.multiply_in_ieee754("0", "22.15625"),
        "Произведение 0 и 22.15625 в IEEE754",
        Verification.ieee754_to_decimal,
    )
    print_info(
        IEEE754.multiply_in_ieee754("22.15625", "8.75"),
        "Произведение 22.15625 и 8.75 в IEEE754",
        Verification.ieee754_to_decimal,
    )
    print_info(
        IEEE754.multiply_in_ieee754("22.15625", "-4"),
        "Произведение 22.15625 и -4 в IEEE754",
        Verification.ieee754_to_decimal,
    )
    print_info(
        IEEE754.multiply_in_ieee754("22.15625", "1.1"),
        "Произведение 22.15625 и 1.1 в IEEE754",
        Verification.ieee754_to_decimal,
    )

    print()
    try:
        print_info(
            IEEE754.divide_in_ieee754("22.15625", "0"),
            "Частное 22.15625 и 0 в IEEE754",
            Verification.ieee754_to_decimal,
        )
    except ZeroDivisionError as e:
        print(f"Частное 22.15625 и 0 в IEEE754: Ошибка {e}")
    print_info(
        IEEE754.divide_in_ieee754("0", "8.75"),
        "Частное 0 и 8.75 в IEEE754",
        Verification.ieee754_to_decimal,
    )
    print_info(
        IEEE754.divide_in_ieee754("22.15625", "8.75"),
        "Частное 22.15625 и 8.75 в IEEE754",
        Verification.ieee754_to_decimal,
    )
    print_info(
        IEEE754.divide_in_ieee754("22.15625", "-4"),
        "Частное 22.15625 и -4 в IEEE754",
        Verification.ieee754_to_decimal,
    )
    print_info(
        IEEE754.divide_in_ieee754("22.15625", "1.1"),
        "Частное 22.15625 и 1.1 в IEEE754",
        Verification.ieee754_to_decimal,
    )

    print()
    print_info(
        BCD2421.decimal_number_to_2421("12"),
        "12 в BCD2421",
        Verification.bcd2421_to_decimal,
    )
    print_info(
        BCD2421.add_in_bcd_2421("19", "-7"),
        "Сумма 19 и -7",
        Verification.bcd2421_to_decimal,
    )
    print_info(
        BCD2421.add_in_bcd_2421("180", "-168"),
        "Сумма 180 и -168",
        Verification.bcd2421_to_decimal,
    )
    print_info(
        BCD2421.decimal_number_to_2421("-12"),
        "-12 в BCD2421",
        Verification.bcd2421_to_decimal,
    )
    print_info(
        BCD2421.add_in_bcd_2421("-19", "7"),
        "Сумма -19 и 7",
        Verification.bcd2421_to_decimal,
    )
    print_info(
        BCD2421.decimal_number_to_2421("542"),
        "542 в BCD2421",
        Verification.bcd2421_to_decimal,
    )
    print_info(
        BCD2421.add_in_bcd_2421("163", "379"),
        "Сумма 163 и 379",
        Verification.bcd2421_to_decimal,
    )
    print_info(
        BCD2421.decimal_number_to_2421("123456789"),
        "123456789 в BCD2421",
        Verification.bcd2421_to_decimal,
    )   
    print_info(
        BCD2421.add_in_bcd_2421("0", "0"),
        "Сумма 0 и 0 в 2421 BCD",
        Verification.bcd2421_to_decimal,
    )
    print_info(
        BCD2421.add_in_bcd_2421("30", "0"),
        "Сумма 30 и 0 в 2421 BCD",
        Verification.bcd2421_to_decimal,
    )
    print_info(
        BCD2421.add_in_bcd_2421("78", "5"),
        "Сумма 78 и 5 в 2421 BCD",
        Verification.bcd2421_to_decimal,
    )
    print_info(
        BCD2421.add_in_bcd_2421("5", "-17"),
        "Сумма 5 и -17 в 2421 BCD",
        Verification.bcd2421_to_decimal,
    )
    print_info(
        BCD2421.add_in_bcd_2421("56794", "8675"),
        "Сумма 5674 и 8675 в 2421 BCD",
        Verification.bcd2421_to_decimal,
    )
