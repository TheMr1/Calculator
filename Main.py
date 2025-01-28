import math
from MainLibrary.MainPackage import BasicFunctions

list_of_operations = ["+","-","*","/","^"]

print('Available operations: ')
print(list_of_operations)
operation = BasicFunctions.ask_for_string("Choose the desired operation: ", list_of_operations)

def attempt_to_calculate():
    try:
        if operation == '+':
            num1 = BasicFunctions.ask_for_float("Choose the first number: ", False)
            num2 = BasicFunctions.ask_for_float("Choose the second number: ", False)

            result1 = num1 + num2
        elif operation == '-':
            num1 = BasicFunctions.ask_for_float("Choose the first number: ", False)
            num2 = BasicFunctions.ask_for_float("Choose the second number: ", False)

            result1 = num1 - num2
        elif operation == '*':
            num1 = BasicFunctions.ask_for_float("Choose the first number: ", False)
            num2 = BasicFunctions.ask_for_float("Choose the second number: ", False)

            result1 = num1 * num2
        elif operation == '/':
            num1 = BasicFunctions.ask_for_float("Choose the first number: ", False)
            num2 = BasicFunctions.ask_for_float("Choose the second number: ", False)

            result1 = num1 / num2
        elif operation == '^':
            num11 = BasicFunctions.ask_for_float("Choose the base: ", False)
            num22 = BasicFunctions.ask_for_float("Choose the exponent: ", False)

            result1 = math.pow(num11, num22)
        return result1
    except ValueError:
        print('Cannot calculate operation, try again.')
        return attempt_to_calculate()
    except OverflowError:
        print('Cannot calculate operation, try again.')
        return attempt_to_calculate()
    except ZeroDivisionError:
        print('Cannot calculate operation, try again.')
        return attempt_to_calculate()

result = attempt_to_calculate()

print('The result is: ' + str(result))
