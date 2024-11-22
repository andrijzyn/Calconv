import re
from flask import Flask, request, jsonify
from flask_cors import CORS
from operations.converter import Converter
from operations.math.arithmetic import Arithmetic
from typing import Tuple, List

app = Flask(__name__)
CORS(app)

# Process the user input to perform arithmetic operations
def parse_math_expression(expression: str) -> Tuple[str, int, str, int, str]:
    pattern_parse = r'^([\da-fA-F]+)_(\d+)\s*([+\-*/])\s*([\da-fA-F]+)_(\d+)$'
    match_parse = re.match(pattern_parse, expression)
    num1, base1, operator, num2, base2 = match_parse.groups()
    return num1, int(base1), num2, int(base2), operator

def calculate_result(num1: str, base1: int, num2: str, operation: str) -> Tuple[str, List[str]]:
    operation_funcs = {
        '+': Arithmetic.add_in_base,
        '-': Arithmetic.subtract_in_base,
        '*': Arithmetic.multiply_in_base,
        '/': Arithmetic.divide_in_base
    }
    operation_result = operation_funcs[operation](num1, num2, base1)
    return operation_result if isinstance(operation_result, tuple) else (operation_result, [])

# Convert a number from one base to another
def convert_between_bases(expression: str) -> Tuple[str, List[str]]:
    pattern_convert = r"(\w+)_([0-9]+)to([0-9]+)"
    match_convert = re.match(pattern_convert, expression)

    if not match_convert:
        raise ValueError("Invalid input format for conversion.")

    convert_number, convert_base1, convert_base2 = match_convert.groups()
    convert_base1, convert_base2 = int(convert_base1), int(convert_base2)

    convert_decimal_value, convert_steps = Converter.convert_to_decimal(convert_number, convert_base1)
    result_conversion, new_conversion_steps = Converter.convert_from_decimal(convert_decimal_value, convert_base2)

    if isinstance(new_conversion_steps, str):
        new_conversion_steps = [new_conversion_steps]

    return result_conversion, convert_steps + new_conversion_steps

@app.route('/math', methods=['POST'])
def process_math_expression():
    data = request.get_json(silent=True)
    expression = data.get('expression', '')
    parsed_num1, parsed_base1, parsed_num2, parsed_base2, parsed_operator = parse_math_expression(expression)
    calculation_result, calculation_steps = calculate_result(parsed_num1, parsed_base1, parsed_num2, parsed_operator)
    return jsonify({'result': calculation_result, 'steps': calculation_steps})

@app.route('/convert', methods=['POST'])
def process_conversion():
    data = request.get_json(silent=True)
    expression = data.get('expression', '')
    converted_result, conversion_steps = convert_between_bases(expression)

    print(f"# Result: {converted_result}, \n# Steps:\n# {conversion_steps}") // debug
    return jsonify({'result': converted_result, 'steps': conversion_steps})

@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Please use curl/jsonify method data receiving/sending'}), 404

if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)  # pragma: no cover
