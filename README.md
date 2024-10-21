# Number Base Converter and Calculator
This Python script allows you to perform basic arithmetic operations (+, -, *, /) on numbers of different bases and provides the result in the higher base between the two operands. Additionally, it can convert numbers from one base to another.

## Features
- Convert numbers from any given base to decimal (base-10)
- Convert decimal numbers to any specified base
- Convert from one base to another using `number_base1toBase2`
- Parse mathematical expressions with different bases
- Perform basic arithmetic operations on numbers with different bases

## Prerequisites
- Python 3.12.7

## Installation
1. Clone the repository:
    ```
    git clone https://github.com/pgmtags/DigitsCalculator.git
    cd DigitsCalculator
    ```

## Usage
To use the converter and calculator, run the `main` function:

```
python main.py
```

You will be prompted to enter a mathematical expression in the format: operand1_base1 operator operand2_base2
### Examples
For instance, to add two numbers `101_2` (binary) and `A_16` (hexadecimal), enter: 101_2 + A_16
The script will then output the result in the larger base between the two operands: 
```Result: 111110011_16```

#### Base Conversion
To convert the number `10` from decimal to base 4, enter: 10_10to4
The script will then output the result in base 4: 
```Converted result: 22_4```

### Functions
- **convert_to_decimal(number: str, base: int) -> int**
  Converts a number from a specified base to its decimal equivalent.

- **convert_from_decimal(number: int, base: int) -> str**
  Converts a decimal number to the specified base.

- **parse_math_expression(expression: str)**
  Parses a mathematical expression to extract operands and their bases.

- **calculate_result(num1: str, base1: int, num2: str, base2: int, operation: str) -> str**
  Performs a calculation based on two operands and an operation, returning the result in the larger base.

- **convert_between_bases(expression: str) -> str**
  Converts a number from one base to another specified base.

### Handling Invalid Input
The script will raise a `ValueError` if the input format is invalid. Ensure that the expression follows the format `operand1_base1 operator operand2_base2`.

### Note
Division by zero is handled by returning "Infinity".

## Contributing
Contributions are welcome! Please fork the repository, make your changes, and submit a pull request.
