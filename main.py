import re
import argparse
from operations.converter import Converter
from operations.math.arithmetic import Arithmetic


def parse_math_expression(expression):
    pattern = r'^(\d+)_(\d+)\s*([+\-*/])\s*(\d+)_(\d+)$'
    match = re.match(pattern, expression)

    if not match:
        raise ValueError("Invalid format or unsupported characters in expression.")

    num1, base1, operator, num2, base2 = match.groups()

    if int(base1) < 2 or int(base1) > 36 or int(base2) < 2 or int(base2) > 36:
        raise ValueError("Invalid base. Base must be between 2 and 36.")

    return num1, int(base1), num2, int(base2), operator


def calculate_result(num1: str, base1: int, num2: str, operation: str) -> tuple[str, list[str]]:
    steps = []
    operations = {
        '+': Arithmetic.add_in_base,
        '-': Arithmetic.subtract_in_base,
        '*': Arithmetic.multiply_in_base,
        '/': Arithmetic.divide_in_base
    }

    if operation in operations:
        result = operations[operation](num1, num2, base1)
    else:
        raise NotImplementedError(f"Operation '{operation}' not implemented for direct base arithmetic.")

    return result, steps


def convert_between_bases(expression: str) -> tuple[str, list[str]]:
    pattern = r"(\w+)_([0-9]+)to([0-9]+)"
    match = re.match(pattern, expression)

    if not match:
        raise ValueError("Invalid input format for conversion.")

    number, base1, base2 = match.groups()
    base1, base2 = int(base1), int(base2)

    if base1 < 2 or base2 < 2:
        raise ValueError("Bases must be 2 or higher.")

    if base1 == base2:
        return number, []

    decimal_value, steps = Converter.convert_to_decimal(number, base1)
    result_conversion, conversion_steps = Converter.convert_from_decimal(decimal_value, base2)

    steps += conversion_steps
    return result_conversion, steps


def process_input(user_input: str):
    if "to" in user_input:
        result, steps = convert_between_bases(user_input)
        return f"Converted result: {result}\nSteps:\n" + "\n".join(steps)
    if "-" or "+" in user_input:
        num1, base1, num2, base2, operator = parse_math_expression(user_input)
        result, steps = calculate_result(num1, base1, num2, operator)
        return f"Result: {result}"


def main(args=None):
    parser = argparse.ArgumentParser(description="Number Base Converter and Calculator")
    parser.add_argument('expression', metavar='E', type=str, nargs='?',
                        help='Expression to evaluate (e.g., 2_10+2_10 or 10_10to2)')
    parsed_args = parser.parse_args(args)

    if parsed_args.expression:
        try:
            print(process_input(parsed_args.expression))
        except ValueError as ve:
            print(f"Error: {ve}")
        return

    while True:
        try:
            user_input = input("Enter expression like (x_base1 + y_base2) or (number_base1toBase2) or 'exit' to quit: ")
            if user_input.lower() == 'exit': break
            print(process_input(user_input))
        except ValueError as ve:
            print(f"Error: {ve}")


if __name__ == "__main__":
    import sys

    main(sys.argv[1:])