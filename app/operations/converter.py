import json
from typing import Tuple, List, Any

CHARS = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

class Converter:
    @staticmethod
    def convert_to_decimal(number: str, base: int) -> tuple[int, list[str]]:
        if base < 2:
            raise ValueError("Base must be 2 or higher.")
        if base == 10:
            return int(number), []

        steps = []
        decimal_value = 0
        power = len(number) - 1

        for digit in number:
            if '0' <= digit <= '9':
                digit_value = int(digit)
            else:
                digit_value = ord(digit.upper()) - ord('A') + 10

            if digit_value >= base:
                raise ValueError(f"Digit '{digit}' is not valid for base {base}.")

            decimal_value += digit_value * (base ** power)

            if power >= 0:
                steps.append(
                    f"{digit}_{base} = {digit_value} * ({base}^{power}) = {digit_value * (base ^ power)}")
            power -= 1

        return decimal_value, steps

    @staticmethod
    def convert_from_decimal(number: int, base: int) -> tuple[str, list[str] | list[Any]] | tuple[str | Any, str]:
        if base < 2:
            raise ValueError("Base must be 2 or higher.")
        if base == 10:
            return str(number), ["0"] if number == 0 else []

        if base > len(CHARS):
            raise ValueError(f"Base cannot be greater than {len(CHARS)}.")

        result = ''
        steps = []
        num = number

        while num > 0:
            remainder = num % base
            steps.append(f"{num} / {base} = quotient {num // base} and remainder {remainder}\n")
            result = CHARS[remainder] + result
            num //= base

        return result or '0', json.dumps(steps, indent=4)