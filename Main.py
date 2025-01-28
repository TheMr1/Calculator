import math
from MainLibrary.MainPackage import BasicFunctions

list_of_operations = ["+","-","*","/","^"]

print('Available operations: ')
print(list_of_operations)
operation = BasicFunctions.ask_for_string("Choose the desired operation: ", list_of_operations)

result = 0

if operation == '+':
    num1 = BasicFunctions.ask_for_float("Choose the first number: ", False)
    num2 = BasicFunctions.ask_for_float("Choose the second number: ", False)

    result = num1 + num2
elif operation == '-':
    num1 = BasicFunctions.ask_for_float("Choose the first number: ", False)
    num2 = BasicFunctions.ask_for_float("Choose the second number: ", False)

    result = num1 - num2
elif operation == '*':
    num1 = BasicFunctions.ask_for_float("Choose the first number: ", False)
    num2 = BasicFunctions.ask_for_float("Choose the second number: ", False)

    result = num1 * num2
elif operation == '/':
    num1 = BasicFunctions.ask_for_float("Choose the first number: ", False)

    def ask_for_num2():
        num2_1 = BasicFunctions.ask_for_float("Choose the second number: ", False)
        if num2_1 == 0:
            print('Cannot divide by zero, try again.')
            return ask_for_num2()
        else:
            return num2_1

    num2 = ask_for_num2()

    result = num1 / num2
elif operation == '^':
    def attempt_to_calculate_exponentiation():
        num11 = BasicFunctions.ask_for_float("Choose the base: ", False)
        num22 = BasicFunctions.ask_for_float("Choose the exponent: ", False)

        try:
            result1 = math.pow(num11, num22)
            return result1
        except ValueError:
            print('Cannot perform exponentiation, try again.')
            return attempt_to_calculate_exponentiation()

    result = attempt_to_calculate_exponentiation()

print('The result is: ' + str(result))
