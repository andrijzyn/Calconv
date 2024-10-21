from re import findall

def to_decimal(number, base): return int(number, base)

def from_decimal(number, base):
    conversion_functions = {
        2: lambda x: bin(x)[2:],
        4: base_n,
        8: lambda x: oct(x)[2:],
        10: str,
        12: base_n,
        16: lambda x: hex(x)[2:]
    }
    conversion_function = conversion_functions.get(base)
    if conversion_function is None: raise ValueError("Incorrect base of the number system.")
    return conversion_function(number)

def base_n(number, base):
    """Convert characters larger than 10."""
    chars = "0123456789AB"
    result = ''
    while number > 0:
        result = chars[number % base] + result
        number //= base
    return result if result else '0'

def parse_input(expression):
    """User Input parsing."""
    pattern = r"([A-Za-z0-9]+)_([0-9]+)"
    numbers = findall(pattern, expression)
    operators = findall(r"[+\-*/]", expression)

    if len(numbers) != 2 or len(operators) != 1: raise ValueError("Invalid input format.")

    num1, base1 = numbers[0]
    num2, base2 = numbers[1]

    return num1, int(base1), num2, int(base2), operators[0]

def calculate(num1, base1, num2, base2, operation):
    dec1, dec2 = to_decimal(num1, base1), to_decimal(num2, base2)

    operations = {
        '+': lambda x, y: x + y,
        '-': lambda x, y: x - y,
        '*': lambda x, y: x * y,
        '/': lambda x, y: x // y if y != 0 else "Infinity"
    }

    operation_func = operations.get(operation)
    if operation_func is None: return "In valid operation"
    result = operation_func(dec1, dec2)

    return from_decimal(result, 16) if isinstance(result, int) else result

def main():
    try:
        num1, base1, num2, base2, operation = parse_input(input("Enter expression like- e(x_10 + y_10): "))
        print(f"Result: {calculate(num1, base1, num2, base2, operation)}")
    except ValueError as e: print(e)

if __name__ == "__main__":
    main()
