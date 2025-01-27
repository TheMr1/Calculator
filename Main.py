import math
from MainLibrary.MainPackage import BasicFunctions

list_of_operations = ["+","-","*","/","^"]

print('Available operations: ')
print(list_of_operations)
operation = BasicFunctions.ask_for_string("Choose the desired operation: ", list_of_operations)

num1 = BasicFunctions.ask_for_float("Choose the first number: ", False)
num2 = BasicFunctions.ask_for_float("Choose the second number: ", False)

result = 0

if operation == '+':
    result = num1 + num2
elif operation == '-':
    result = num1 - num2
elif operation == '*':
    result = num1 * num2
elif operation == '/':
    result = num1 / num2
elif operation == '^':
    result = math.pow(num1, num2)

print('The result is: ' + str(result))
