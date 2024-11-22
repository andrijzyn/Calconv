from operations.converter import Converter


class Utils:
    @staticmethod
    def compare_in_base(num1: str, num2: str, base: int) -> int:
        num1_decimal, _ = Converter.convert_to_decimal(num1, base)
        num2_decimal, _ = Converter.convert_to_decimal(num2, base)
        return num1_decimal - num2_decimal

    @staticmethod
    def convert_to_base(num: int, base: int) -> str:
        if num == 0:
            return '0'
        result = ''
        while num > 0:
            result = str(num % base) + result
            num //= base
        return result