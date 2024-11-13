import re
from flask import Flask, request, jsonify
from flask_cors import CORS
from operations.converter import Converter
from operations.math.arithmetic import Arithmetic
from typing import Tuple, List

app = Flask(__name__)
CORS(app)


def process_input(user_input: str) -> Tuple[str, List[str]]:
    def parse_math_expression(expression):
        pattern_parse = r'^([\da-fA-F]+)_(\d+)\s*([+\-*/])\s*([\da-fA-F]+)_(\d+)$'
        match_parse = re.match(pattern_parse, expression)
        if not match_parse:
            raise ValueError("Invalid format or unsupported characters in expression.")
        num1, base1, operator, num2, base2 = match_parse.groups()
        if int(base1) < 2 or int(base1) > 36 or int(base2) < 2 or int(base2) > 36:
            raise ValueError("Invalid base. Base must be between 2 and 36.")
        return num1, int(base1), num2, int(base2), operator

    def calculate_result(num1: str, base1: int, num2: str, operation: str) -> Tuple[str, List[str]]:
        operation_funcs = {
            '+': Arithmetic.add_in_base,
            '-': Arithmetic.subtract_in_base,
            '*': Arithmetic.multiply_in_base,
            '/': Arithmetic.divide_in_base
        }
        if operation in operation_funcs:
            # Проверяем, возвращает ли операция кортеж с результатом и шагами
            operation_result = operation_funcs[operation](num1, num2, base1)
            if isinstance(operation_result, tuple):
                result, steps = operation_result
            else:
                result, steps = operation_result, []  # Если шаги отсутствуют, возвращаем пустой список
        else:
            raise NotImplementedError(f"Operation '{operation}' not implemented for direct base arithmetic.")
        return result, steps

    def convert_between_bases(expression: str) -> Tuple[str, List[str]]:
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
        return converted_result, conversion_steps

    elif user_input:
        parsed_num1, parsed_base1, parsed_num2, parsed_base2, parsed_operator = parse_math_expression(user_input)
        calculation_result, calculation_steps = calculate_result(parsed_num1, parsed_base1, parsed_num2,
                                                                 parsed_operator)
        return calculation_result, calculation_steps

    raise ValueError("Unknown operation format.")


@app.route('/process', methods=['POST'])
def process_expression():
    data = request.get_json(silent=True)
    if not data or 'expression' not in data:
        return jsonify({'error': 'No expression provided'}), 400

    expression = data.get('expression', '')
    try:
        result, steps = process_input(expression)
        return jsonify({'result': result, 'steps': steps})
    except ValueError as ve:
        return jsonify({'error': str(ve)}), 400


if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)
