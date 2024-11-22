import re
from flask import Flask, request, jsonify
from flask_cors import CORS
from operations.converter import Converter
from operations.math.arithmetic import Arithmetic
from typing import Tuple, List

app = Flask(__name__)
CORS(app)

######## Math

def calculate_result(num1: str, num2: str, base: int, operation: str) -> Tuple[str, List[str]]:
    operation_funcs = {
        '+': Arithmetic.add_in_base,
        '-': Arithmetic.subtract_in_base,
        '*': Arithmetic.multiply_in_base,
        '/': Arithmetic.divide_in_base
    }

    operation_result = operation_funcs[operation](num1, num2, base)

    return operation_result if isinstance(operation_result, tuple) else (operation_result, [])

@app.route('/math', methods=['POST'])
def process_math_expression():
    data = request.get_json(silent=True)

    if not data or 'expression' not in data:
        return jsonify({'error': 'No expression provided or invalid structure'}), 400

    expression = data['expression']

    required_keys = ['num1', 'num2', 'base', 'operator']
    missing_keys = [key for key in required_keys if key not in expression]
    if missing_keys:
        return jsonify({'error': f'Missing keys in expression: {", ".join(missing_keys)}'}), 400

    try:
        num1 = expression['num1']
        num2 = expression['num2']
        base = int(expression['base'])
        operator = expression['operator']

        calculation_result, calculation_steps = calculate_result(num1, num2, base, operator)
        return jsonify({'result': calculation_result, 'steps': calculation_steps})

    except ValueError as ve:
        return jsonify({'error': str(ve)}), 400
    except Exception as e:
        return jsonify({'error': f'Unexpected error: {str(e)}'}), 500

######## Converter

@app.route('/convert', methods=['POST'])
def process_conversion():
    try:
        data = request.get_json(silent=True)

        if not data or 'expression' not in data:
            return jsonify({'error': 'No expression provided or invalid structure'}), 400

        expression = data['expression']

        pattern_convert = r"(\w+)_([0-9]+)to([0-9]+)"
        match_convert = re.match(pattern_convert, expression)

        if not match_convert:
            return jsonify({'error': 'Invalid input format for conversion. Expected format: number_base1tobase2'}), 400

        convert_number, convert_base1, convert_base2 = match_convert.groups()
        convert_base1, convert_base2 = int(convert_base1), int(convert_base2)

        if convert_base1 < 2 or convert_base2 < 2:
            return jsonify({'error': 'Bases must be 2 or higher.'}), 400
        if convert_base1 > 36 or convert_base2 > 36:
            return jsonify({'error': 'Bases must not exceed 36.'}), 400

        convert_decimal_value, convert_steps = Converter.convert_to_decimal(convert_number, convert_base1)
        result_conversion, new_conversion_steps = Converter.convert_from_decimal(convert_decimal_value, convert_base2)

        if isinstance(new_conversion_steps, str):
            new_conversion_steps = [new_conversion_steps]

        return jsonify({
            'result': result_conversion,
            'steps': convert_steps + new_conversion_steps
        })

    except ValueError as ve:
        return jsonify({'error': str(ve)}), 400
    except Exception as e:
        return jsonify({'error': f'Unexpected error: {str(e)}'}), 500

######## end

@app.errorhandler(404)
def not_found():
    return jsonify({'error': 'Please use curl/jsonify method data receiving/sending'}), 404

if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)  # pragma: no cover
