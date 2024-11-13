from operations.math.utils import Utils

chars = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"


class Arithmetic:
    @staticmethod
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

    @staticmethod
    def subtract_in_base(num1: str, num2: str, base: int) -> str:
        if base > len(chars):
            raise ValueError(f"Base cannot be greater than {len(chars)}.")

        if len(num1) < len(num2) or (len(num1) == len(num2) and num1 < num2):
            return '-' + Arithmetic.subtract_in_base(num2, num1, base)

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

    @staticmethod
    def multiply_in_base(num1: str, num2: str, base: int) -> str:
        if base > len(chars):
            raise ValueError(f"Base cannot be greater than {len(chars)}.")

        num1 = num1.upper()
        num2 = num2.upper()

        intermediate_results = []

        print(f"\nMultiplying {num1} by {num2} in base {base}:")

        for i, digit2 in enumerate(reversed(num2)):
            carry = 0
            temp_result = [0] * i

            digit2_val = chars.index(digit2)

            for digit1 in reversed(num1):
                digit1_val = chars.index(digit1)

                product = digit1_val * digit2_val + carry
                carry = product // base
                temp_result.append(product % base)

            if carry:
                temp_result.append(carry)

            temp_result = temp_result[::-1]
            intermediate_results.append(temp_result)

            step_str = ''.join(chars[d] for d in temp_result)
            print(f"Step {i + 1}: {step_str}")

        max_len = max(len(r) for r in intermediate_results)
        for i in range(len(intermediate_results)):
            intermediate_results[i] = [0] * (max_len - len(intermediate_results[i])) + intermediate_results[i]

        result = [0] * max_len
        carry = 0
        for i in range(max_len - 1, -1, -1):
            column_sum = sum(r[i] for r in intermediate_results) + carry
            carry = column_sum // base
            result[i] = column_sum % base

        if carry:
            result = [carry] + result

        result_str = ''.join(chars[d] for d in result).lstrip('0') or '0'

        return result_str

    @staticmethod
    def divide_in_base(num1: str, num2: str, base: int) -> str:
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
            while Utils.compare_in_base(remainder, temp, base) >= 0:
                remainder = Arithmetic.subtract_in_base(remainder, temp, base)
                count += 1
                print(f"Iteration {iteration_count}: Remainder after subtraction: {remainder}")
                iteration_count += 1

            # Convert the count to the appropriate base and append to quotient
            quotient += Utils.convert_to_base(count, base)

        return quotient.lstrip('0') or '0'