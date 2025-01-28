import math
from MainLibrary.MainPackage import BasicFunctions

list_of_operations = ["exp", "ln", "log"]

print('Available operations: ')
print(list_of_operations)

operation = BasicFunctions.ask_for_string("Chose the desired operation: ", list_of_operations)

def attempt_to_calculate():
    try:
        if operation == 'log':
            num1 = BasicFunctions.ask_for_float("Input the base: ", False)
            num2 = BasicFunctions.ask_for_float("Input the value: ", False)

            result1 = math.log(num2, num1)
        elif operation == 'exp':
            num1 = BasicFunctions.ask_for_float("Input the number: ", False)

            result1 = math.exp(num1)
        elif operation == 'ln':
            num1 = BasicFunctions.ask_for_float("Input the number: ", False)
            result1 = math.log(num1, math.e)
        return result1
    except OverflowError:
        print('Cannot perform operation, try again.')
        return attempt_to_calculate()
    except ValueError:
        print('Cannot perform operation, try again.')
        return attempt_to_calculate()
    except ZeroDivisionError:
        print('Cannot perform operation, try again.')
        return attempt_to_calculate()

result = attempt_to_calculate()

print('The result is: ' + str(result))