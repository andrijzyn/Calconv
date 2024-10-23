import re
import argparse

chars = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def convert_to_decimal(number: str, base: int) -> tuple[int, list[str]]:
    """
    :param number: The number in string format to be converted to decimal.
    :param base: The base of the number to be converted.
    :return: A tuple containing the decimal value and a list of steps taken during conversion.
    """
    if base < 2:
        raise ValueError("Base must be 2 or higher.")
    if base == 10:
        return int(number), []

    steps = []
    decimal_value = 0
    power = len(number) - 1

    for digit in number:
        if digit.isdigit():
            digit_value = int(digit)
        else:
            digit_value = ord(digit.upper()) - ord('A') + 10

        if digit_value >= base:
            raise ValueError(f"Digit '{digit}' is not valid for base {base}.")

        decimal_value += digit_value * (base ** power)

        if power >= 0:
            steps.append(
                f"Digit: {digit} in base {base}, value: {digit_value} * (base ** {power}) = {digit_value * (base ** power)}")
        power -= 1

    return decimal_value, steps


def convert_from_decimal(number: int, base: int) -> tuple[str, list[str]]:
    """
    :param number: The decimal number to be converted.
    :param base: The base to which the number should be converted.
    :return: A tuple containing the converted number as a string in the specified base, and a list of steps detailing the conversion process.
    """
    if base < 2:
        raise ValueError("Base must be 2 or higher.")
    if base == 10:
        return str(number), ["0"] if number == 0 else []

    if base > len(chars):
        raise ValueError(f"Base cannot be greater than {len(chars)}.")

    result = ''
    steps = []
    num = number

    while num > 0:
        remainder = num % base
        steps.append(f"{num} divided by {base} gives quotient {num // base} and remainder {remainder}")
        result = chars[remainder] + result
        num //= base

    return result or '0', steps


def add_in_base(num1: str, num2: str, base: int) -> str:
    """
    :param num1: A string representing the first number in the specified base.
    :param num2: A string representing the second number in the specified base.
    :param base: An integer representing the numeric base for the input numbers.
    :return: A string representing the sum of the two numbers in the specified base.
    """
    if base < 2:
        raise ValueError("Base must be 2 or higher.")
    if base > len(chars):
        raise ValueError(f"Base cannot be greater than {len(chars)}.")

    max_length = max(len(num1), len(num2))
    num1 = num1.zfill(max_length)
    num2 = num2.zfill(max_length)
    result = []
    carry = 0

    for i in range(max_length - 1, -1, -1):
        digit1 = chars.index(num1[i].upper())
        digit2 = chars.index(num2[i].upper())
        digit_sum = digit1 + digit2 + carry
        carry = digit_sum // base
        result.append(chars[digit_sum % base])

    if carry:
        result.append(chars[carry])

    return ''.join(reversed(result))


def subtract_in_base(num1: str, num2: str, base: int) -> str:
    """
    :param num1: The first number as a string in the given base.
    :param num2: The second number as a string in the given base.
    :param base: The numerical base for the numbers (e.g., base 10 for decimal, base 16 for hexadecimal).
    :return: The result of subtracting num2 from num1 in the given base, represented as a string.
    """
    if base > len(chars):
        raise ValueError(f"Base cannot be greater than {len(chars)}.")

    if len(num1) < len(num2) or (len(num1) == len(num2) and num1 < num2):
        return '-' + subtract_in_base(num2, num1, base)

    max_length = max(len(num1), len(num2))
    num1 = num1.zfill(max_length)
    num2 = num2.zfill(max_length)

    result = []
    borrow = 0

    for i in range(max_length - 1, -1, -1):
        digit1 = chars.index(num1[i].upper()) - borrow
        digit2 = chars.index(num2[i].upper())

        if digit1 < digit2:
            digit1 += base
            borrow = 1
        else:
            borrow = 0

        result.append(chars[digit1 - digit2])

    return ''.join(reversed(result)).lstrip('0') or '0'


def multiply_in_base(num1: str, num2: str, base: int) -> str:
    """
    :param num1: The first number as a string in the specified base.
    :param num2: The second number as a string in the specified base.
    :param base: The base in which to perform the multiplication.
    :return: The product of num1 and num2 as a string in the specified base.
    """
    if base > len(chars):
        raise ValueError(f"Base cannot be greater than {len(chars)}.")

    num1 = num1.upper()[::-1]
    num2 = num2.upper()[::-1]

    result = [0] * (len(num1) + len(num2))

    for i in range(len(num1)):
        digit1 = chars.index(num1[i])

        for j in range(len(num2)):
            digit2 = chars.index(num2[j])

            product = digit1 * digit2
            result[i + j] += product
            result[i + j + 1] += result[i + j] // base
            result[i + j] %= base

    result = ''.join(chars[d] for d in reversed(result)).lstrip('0') or '0'

    return result


def divide_in_base(num1: str, num2: str, base: int) -> str:
    """
    :param num1: The dividend represented as a string in the specified base.
    :param num2: The divisor represented as a string in the specified base.
    :param base: The numerical base in which the division is to be performed.
    :return: The quotient of the division represented as a string in the specified base, or an error message if the operation could not complete.
    """
    if num2 == '0':
        return "Infinity"

    quotient = ''
    remainder = num1

    max_iterations = 499  # Limit the number of iterations to avoid looping
    iteration_count = 0

    while len(remainder) >= len(num2):
        if iteration_count > max_iterations:
            return "Error: Too many iterations. Potential infinite loop detected."

        temp = num2
        count = 0

        # Keep subtracting until remainder is smaller than divisor
        while compare_in_base(remainder, temp, base) >= 0:
            remainder = subtract_in_base(remainder, temp, base)
            count += 1
            print(f"Iteration {iteration_count}: Remainder after subtraction: {remainder}")
            iteration_count += 1

        # Convert the count to the appropriate base and append to quotient
        quotient += convert_to_base(count, base)

    return quotient.lstrip('0') or '0'


def compare_in_base(num1: str, num2: str, base: int) -> int:
    """
    :param num1: The first number represented as a string in the specified base.
    :param num2: The second number represented as a string in the specified base.
    :param base: The base in which the numbers are represented.
    :return: The difference between the two numbers in decimal form.
    """
    num1_decimal, _ = convert_to_decimal(num1, base)
    num2_decimal, _ = convert_to_decimal(num2, base)
    return num1_decimal - num2_decimal


def convert_to_base(num: int, base: int) -> str:
    """
    :param num: The number to be converted to a different base. Must be a non-negative integer.
    :param base: The base to convert the number to. Must be an integer between 2 and 36.
    :return: A string representing the number in the specified base.
    """
    if num == 0:
        return '0'
    result = ''
    while num > 0:
        result = str(num % base) + result
        num //= base
    return result


def parse_math_expression(expression: str):
    """
    :param expression: A string representing a mathematical expression that includes numbers in specific bases and a single operator.
                       The expected format is 'number_base operator number_base'.
    :return: A tuple containing the first number, its base, the second number, its base, and the operator.
    :raises ValueError: If the input format is invalid or if any of the bases are less than 2.
    """
    pattern = r"([A-Za-z0-9]+)_([0-9]+)"
    numbers = re.findall(pattern, expression)
    operators = re.findall(r"[+\-*/]", expression)

    if len(numbers) != 2 or len(operators) != 1:
        raise ValueError("Invalid input format.")

    (num1, base1), (num2, base2) = numbers

    if int(base1) < 2 or int(base2) < 2:
        raise ValueError("Bases must be 2 or higher.")

    return num1, int(base1), num2, int(base2), operators[0]


def calculate_result(num1: str, base1: int, num2: str, operation: str) -> tuple[str, list[str]]:
    """
    :param num1: The first number as a string in the given base.
    :param base1: The base of the numbers (e.g., 2 for binary, 10 for decimal).
    :param num2: The second number as a string in the given base.
    :param operation: The arithmetic operation to perform. Supported operations are '+', '-', '*', and '/'.
    :return: A tuple containing the result of the arithmetic operation in the given base as a string
             and a list of steps involved in the calculation.
    """
    steps = []
    if operation == '+':
        result = add_in_base(num1, num2, base1)
    elif operation == '-':
        result = subtract_in_base(num1, num2, base1)
    elif operation == '*':
        result = multiply_in_base(num1, num2, base1)
    elif operation == '/':
        result = divide_in_base(num1, num2, base1)
    else:
        raise NotImplementedError(f"Operation '{operation}' not implemented for direct base arithmetic.")

    return result, steps


def convert_between_bases(expression: str) -> tuple[str, list[str]]:
    """
    :param expression: A string representing the number and the bases to convert from and to, in the format "number_base1tobase2".
                       For example, "101_2to10" would convert binary 101 to its decimal equivalent.
    :return: A tuple where the first element is the converted number as a string, and the second element is a list of steps
             taken during the conversion process.
    """
    pattern = r"([A-Za-z0-9]+)_([0-9]+)to([0-9]+)"
    match = re.match(pattern, expression)

    if not match:
        raise ValueError("Invalid input format for conversion.")

    number, base1, base2 = match.groups()
    base1, base2 = int(base1), int(base2)

    if base1 < 2 or base2 < 2:
        raise ValueError("Bases must be 2 or higher.")

    if base1 == base2:
        return number, []

    decimal_value, steps = convert_to_decimal(number, base1)
    result_conversion, conversion_steps = convert_from_decimal(decimal_value, base2)

    steps += conversion_steps
    return result_conversion, steps


def process_input(user_input: str):
    """
    :param user_input: The string containing either a conversion command or a mathematical expression in different bases.
    :return: A string containing the result of the conversion or computation, along with the detailed steps taken.
    """
    if "to" in user_input:
        result, steps = convert_between_bases(user_input)
        return f"Converted result: {result}\nSteps:\n" + "\n".join(steps)
    else:
        num1, base1, num2, base2, operator = parse_math_expression(user_input)
        result, steps = calculate_result(num1, base1, num2, operator)
        return f"Result: {result}\nSteps:\n" + "\n".join(steps)


def main(args=None):
    """
    :param args: A list of command-line arguments passed to the script
    :return: None
    """
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