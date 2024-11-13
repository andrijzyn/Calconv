import re
import argparse
from operations.converter import Converter
from operations.math.arithmetic import Arithmetic


def process_input(user_input: str) -> str:
    def parse_math_expression(expression):
        # Modify the regex pattern to support hexadecimal characters (a-f, A-F)
        pattern_parse = r'^([\da-fA-F]+)_(\d+)\s*([+\-*/])\s*([\da-fA-F]+)_(\d+)$'
        match_parse = re.match(pattern_parse, expression)
        if not match_parse:
            raise ValueError("Invalid format or unsupported characters in expression.")
        num1, base1, operator, num2, base2 = match_parse.groups()
        if int(base1) < 2 or int(base1) > 36 or int(base2) < 2 or int(base2) > 36:
            raise ValueError("Invalid base. Base must be between 2 and 36.")
        return num1, int(base1), num2, int(base2), operator

    def calculate_result(num1: str, base1: int, num2: str, operation: str) -> tuple[str, list[str]]:
        result_steps = []
        operation_funcs = {
            '+': Arithmetic.add_in_base,
            '-': Arithmetic.subtract_in_base,
            '*': Arithmetic.multiply_in_base,
            '/': Arithmetic.divide_in_base
        }
        if operation in operation_funcs:
            operation_result = operation_funcs[operation](num1, num2, base1)
        else:
            raise NotImplementedError(f"Operation '{operation}' not implemented for direct base arithmetic.")
        return operation_result, result_steps

    def convert_between_bases(expression: str) -> tuple[str, list[str]]:
        pattern_convert = r"(\w+)_([0-9]+)to([0-9]+)"
        match_convert = re.match(pattern_convert, expression)

        if not match_convert:
            raise ValueError("Invalid input format for conversion.")

        convert_number, convert_base1, convert_base2 = match_convert.groups()
        convert_base1, convert_base2 = int(convert_base1), int(convert_base2)

        if convert_base1 < 2 or convert_base2 < 2:
            raise ValueError("Bases must be 2 or higher.")

        if convert_base1 == convert_base2:
            return convert_number, []

        convert_decimal_value, convert_steps = Converter.convert_to_decimal(convert_number, convert_base1)
        result_conversion, new_conversion_steps = Converter.convert_from_decimal(convert_decimal_value, convert_base2)

        convert_steps += new_conversion_steps
        return result_conversion, convert_steps

    if "to" in user_input:
        converted_result, conversion_steps = convert_between_bases(user_input)
        return f"Converted result: {converted_result}\nSteps:\n" + "\n".join(conversion_steps)

    elif user_input:
        parsed_num1, parsed_base1, parsed_num2, parsed_base2, parsed_operator = parse_math_expression(user_input)
        calculation_result, calculation_steps = calculate_result(parsed_num1, parsed_base1, parsed_num2,
                                                                 parsed_operator)
        return f"Result: {calculation_result}"

    raise ValueError("Unknown operation format.")


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
            print(process_input(input("Enter expression like (x_base1 + y_base2) or (number_base1toBase2): ")))
        except ValueError as ve:
            print(f"Error: {ve}")


if __name__ == "__main__":
    import sys

    main(sys.argv[1:])
