import math
from MainLibrary.MainPackage import BasicFunctions

list_of_operations = ["exp", "ln", "log"]

print('Available operations: ')
print(list_of_operations)

operation = BasicFunctions.ask_for_string("Chose the desired operation: ", list_of_operations)
result = 0

if operation == 'log':
    def attempt_to_calculate_log():
        num1 = BasicFunctions.ask_for_float("Input the base: ", False)
        num2 = BasicFunctions.ask_for_float("Input the value: ", False)

        try:
            result1 = math.log(num2, num1)
            return result1
        except ZeroDivisionError:
            print('One cannot be a base, try again')
            return attempt_to_calculate_log()
        except ValueError:
            print('Cannot calculate log with given numbers, try again.')
            return attempt_to_calculate_log()

    result = attempt_to_calculate_log()

elif operation == 'exp':
    num = BasicFunctions.ask_for_float("Input the number: ", False)

    result = math.exp(num)
elif operation == 'ln':
    def attempt_to_calculate_natural_log():
        num1 = BasicFunctions.ask_for_float("Input the number: ", False)

        try:
            result1 = math.log(num1, math.e)
            return result1
        except ValueError:
            print('Cannot calculate natural log with the given number, try again.')
            return attempt_to_calculate_natural_log()

    result = attempt_to_calculate_natural_log()

print('The result is: ' + str(result))
