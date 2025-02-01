import math

def ask_for_string(text, possible_values):
    current_string = input(text)
    if possible_values:
        if possible_values.__contains__(current_string):
            return current_string
        else:
            print('Invalid input, try again.')
            return ask_for_string(text, possible_values)
    else:
        return current_string

def ask_for_float(text, input1):
    if input1:
        current_string = input1
    else:
        current_string = input(text)

    try:
        current_string = float(current_string)
        return current_string
    except ValueError:
        if current_string.__contains__(','):
            current_string = current_string.replace(',', '.')
            return ask_for_float(text, current_string)
        else:
            print("Invalid number, try again")
            return ask_for_float(text, False)

def ask_for_operator_or_float(text, possible_values):
    current_string = input(text)

    try:
        current_string = float(current_string)
        return current_string
    except ValueError:
        if possible_values.__contains__(current_string):
            return current_string
        else:
            print('Invalid input, try again.')
            return ask_for_operator_or_float(text, possible_values)


def calculate(operation, num1, num2):
    result = {
        "OK" : False,
        "calculated_value": 0,
        "error_message" : ""
    }

    try:
        if operation == "+":
            result["calculated_value"] = num1 + num2
        elif operation == "-":
            result["calculated_value"] = num1 - num2
        elif operation == "*":
            result["calculated_value"] = num1 * num2
        elif operation == "/":
            result["calculated_value"] = num1 / num2
        elif operation == "^":
            result["calculated_value"] = math.pow(num1, num2)
        elif operation == "nthroot":
            result["calculated_value"] = math.pow(num1, 1/num2)

        result["OK"] = True
    except ValueError:
        result["error_message"] = "ValueError"
    except ZeroDivisionError:
        result["error_message"] = "ZeroDivisionError"
    except OverflowError:
        result["error_message"] = "OverflowError"

    return result
