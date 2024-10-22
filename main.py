import re
import argparse

chars = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def convert_to_decimal(number: str, base: int) -> tuple[int, list[str]]:
    """
    :param number: The number in string format to be converted to decimal.
    :param base: The base of the number to be converted. Must be 2 or higher.
    :return: A tuple containing the decimal value of the number and a list of strings describing each conversion step.
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
        
        if power >= 0:  # Only add step if there is a meaningful power
            steps.append(
                f"Digit: {digit} in base {base}, value: {digit_value} * (base ** {power}) = {digit_value * (base ** power)}")
        power -= 1

    return decimal_value, steps


def convert_from_decimal(number: int, base: int) -> tuple[str, list[str]]:
    """
    :param number: The decimal number to be converted.
    :param base: The base to which the decimal number should be converted.
    :return: A tuple containing the converted number as a string and a list of steps showing the division and remainder operations performed during the conversion process.
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
    if num2 == '0': return "Infinity"

    quotient = ''
    remainder = num1

    while len(remainder) >= len(num2):
        temp = num2
        count = 0

        # Keep subtracting until remainder is smaller than divisor
        while compare_in_base(remainder, temp, base) >= 0:
            remainder = subtract_in_base(remainder, temp, base)
            count += 1

        # Convert the count to the appropriate base and append to quotient
        quotient += convert_to_base(count, base)

    return quotient.lstrip('0') or '0'

def compare_in_base(num1: str, num2: str, base: int) -> int:
    # Compare two numbers in the given base
    if len(num1) != len(num2):
        return len(num1) - len(num2)
    for i in range(len(num1)):
        if num1[i] != num2[i]:
            return int(num1[i], base) - int(num2[i], base)
    return 0

def convert_to_base(num: int, base: int) -> str:
    if num == 0:
        return '0'
    result = ''
    while num > 0:
        result = str(num % base) + result
        num //= base
    return result

def parse_math_expression(expression: str):
    """
    :param expression: A mathematical expression in the custom format 'num_base operator num_base',
                       where 'num' is a number, 'base' is the base of that number, and 'operator' is
                       a single arithmetic operator (+, -, *, /).
    :return: A tuple containing the first number, its base, the second number, its base,
             and the operator as separate elements.
    :raises ValueError: If the input expression does not match the expected format or
                        if the base of any number is less than 2.
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
    :param num1: The first number in string format.
    :param base1: The base of the first number.
    :param num2: The second number in string format.
    :param operation: The mathematical operation to be performed ('+', '-', '*', '/').
    :return: A tuple containing the result of the operation in string format and a list of steps detailing the conversion process.
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
    :param expression: A string representing the number and the bases to convert from and to,
                       in the format 'number_base1tobase2'. For example '101_2to10'.
    :return: A tuple containing the converted number as a string and a list of conversion steps.
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
    :param user_input: A string that either represents a base conversion command or a mathematical expression. For base conversion, the command should contain "to". For mathematical expressions, the command should include the numbers, their bases, and the operator.
    :return: A formatted string with either the base conversion result and steps, or the mathematical calculation result and steps.
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
    :param args: List of command-line arguments passed to the program, defaults to None.
    :return: None. Executes expression from command-line args or interactive prompt.
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