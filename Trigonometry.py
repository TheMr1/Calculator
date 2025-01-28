import math
from MainLibrary.MainPackage import BasicFunctions

list_of_operations = ["sin", "cos", "tan", "csc", "sec", "cot"]

print('Available operations: ')
print(list_of_operations)

operation = BasicFunctions.ask_for_string("Choose the desired operation: ", list_of_operations)

def attempt_to_calculate():
    num = BasicFunctions.ask_for_float("Input the number in radians: ", False)

    try:
        if operation == 'sin':
            result1 = math.sin(num)
        elif operation == 'cos':
            result1 = math.cos(num)
        elif operation == 'tan':
            result1 = math.tan(num)
        elif operation == 'csc':
            result1 = 1 / math.sin(num)
        elif operation == 'sec':
            result1 = 1 / math.cos(num)
        elif operation == 'cot':
            result1 = 1 / math.tan(num)

        return result1
    except OverflowError:
        print('Cannot perform operation, try again.')
        return attempt_to_calculate()
    except ZeroDivisionError:
        print('Cannot perform operation, try again.')
        return attempt_to_calculate()

result = attempt_to_calculate()

print('The result is: ' + str(result))
