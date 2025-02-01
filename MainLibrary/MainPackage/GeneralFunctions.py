from MainLibrary.MainPackage import BasicFunctions
from MainLibrary.MainPackage import AdvancedFunctions

def old_style(list_of_operations):
    operation = BasicFunctions.ask_for_string("Choose the desired operation: ", list_of_operations)

    num1 = BasicFunctions.ask_for_float("Choose the first number: ", False)
    num2 = BasicFunctions.ask_for_float("Choose the second number: ", False)

    return BasicFunctions.calculate(operation, num1, num2)

def expression_style():
    result = {
        "OK": False,
        "calculated_value": 0,
        "error_message": ""
    }

    expression = input("Input your desired expression (parentheses are ignored): ")
    try:
        expression_value = AdvancedFunctions.solve_expression(expression)
        result['OK'] = True
        result['calculated_value'] = expression_value
    except IndexError:
        result['OK'] = False
        result['error_message'] = 'IndexError'
    except ZeroDivisionError:
        result['OK'] = False
        result['error_message'] = 'ZeroDivisionError'

    return result

def rpn_style(list_of_operations):
    result = {
        "OK": False,
        "calculated_value": 0,
        "error_message": ""
    }

    stacks = {"Stack1": 0, "Stack2": 0, "Stack3": 0}

    current_stack = 0
    list_of_operations1 = list(list_of_operations)
    list_of_operations1.append('end')

    while True:
        value = BasicFunctions.ask_for_operator_or_float('Input an operator, a number or "end": ', list_of_operations1)

        if value == "end":
            break

        if list_of_operations.__contains__(value):
            if stacks["Stack2"] != 0 and stacks["Stack3"] != 0:
                stacks["Stack2"] = BasicFunctions.calculate(value, stacks["Stack2"], stacks["Stack3"])[
                    "calculated_value"]
                stacks["Stack3"] = 0
            else:
                stacks["Stack1"] = BasicFunctions.calculate(value, stacks["Stack1"], stacks["Stack2"])[
                    "calculated_value"]
                stacks["Stack2"] = 0

            current_stack = 1
        else:
            current_stack += 1

            if current_stack > 3:
                current_stack = 3

            if stacks["Stack" + str(current_stack)] == 0:
                stacks["Stack" + str(current_stack)] = value
            else:
                stacks["Stack" + str(current_stack + 1)] = value

        print("Stack1: " + str(stacks["Stack1"]))
        print("Stack2: " + str(stacks["Stack2"]))
        print("Stack3: " + str(stacks["Stack3"]))
        print(current_stack)

    result["OK"] = True
    result["calculated_value"] = stacks["Stack1"]

    return result