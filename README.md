# 🧮 bN: Converter and Calculator
The Python script is a simple yet effective tool that enables the user to perform fundamental arithmetic operations, including addition, subtraction, multiplication, and division, on numbers with varying bases and to return the result in the higher base between the two operands. Additionally, the script is capable of converting numbers from one base to another.

> [!NOTE]
> Enter mathematical expressions in the format:
>
> operand1_base1 operator operand2_base2
>
> Examples:
>
>     Addition: 101_2 + A_16 (Result: 111110011_16)
>     Base Conversion: 10_10to4 (Result: 22_4)
>
> Explanation:
>
>     Operand and Base: operand_base represents a number in the specified base. For example, 101_2 is 101 in binary.
>     Operator: Supported operators are +, -, *, and /.
>     Output Base: The result will be displayed in the larger base of the two operands.
For a better understanding of the structure and more readable documentation, we have described below the main functions that you will need when using the application

---

### Functions
1. **convert_to_decimal(number, base)**:

        Input: A string representing a number in a given base and the base itself.
        Output: The decimal equivalent of the number and a list of steps involved in the conversion.
        Functionality: Converts a number from a specified base to its decimal equivalent.

2. **convert_from_decimal(number, base)**:

        Input: A decimal number and the target base.
        Output: The number in the specified base as a string and a list of steps.
        Functionality: Converts a decimal number to a specified base.

3. **add_in_base(num1, num2, base)**:

        Input: Two numbers in a given base and the base itself.
        Output: The sum of the two numbers in the same base.
        Functionality: Performs addition in a specified base.

4. **subtract_in_base(num1, num2, base)**:
    
        Input: Two numbers in a given base and the base itself.
        Output: The difference of the two numbers in the same base.
        Functionality: Performs subtraction in a specified base.
    
5. **multiply_in_base(num1, num2, base)**:

        Input: Two numbers in a given base and the base itself.
        Output: The product of the two numbers in the same base.
        Functionality: Performs multiplication in a specified base, showing detailed steps.

6. **divide_in_base(num1, num2, base)**:

        Input: Two numbers in a given base and the base itself.
        Output: The quotient of the division in the same base.
        Functionality: Performs division in a specified base, showing detailed steps and handling potential errors.

7. **compare_in_base(num1, num2, base)**:

        Input: Two numbers in a given base and the base itself.
        Output: The difference between the two numbers in decimal form.
        Functionality: Compares two numbers in a given base by converting them to decimal and subtracting.

8. **convert_to_base(num, base)**:

        Input: A decimal number and the target base.
        Output: The number in the specified base as a string.
        Functionality: Converts a decimal number to a specified base.

9. parse_math_expression(expression):

        Input: A mathematical expression in the format 'operand1_base1 operator operand2_base2'.
        Output: A tuple containing the operands, their bases, and the operator.
        Functionality: Parses the input expression and extracts the relevant information.
