import math

print('Available operations: ')
print('"+", "-", "*", "/", "^"')

operation = input("Chose the desired operation: ")

num1 = float(input("Input the first number: "))
num2 = float(input("Input the second number: "))

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
