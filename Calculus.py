import math

print('Available operations: ')
print('"exp", "ln", "log"')

operation = input("Chose the desired operation: ")
result = 0

if operation == 'log':
    num1 = float(input("Input the base: "))
    num2 = float(input("Input the value: "))

    result = math.log(num2, num1)
elif operation == 'exp':
    num = float(input("Input the number: "))
    result = math.exp(num)
elif operation == 'ln':
    num = float(input("Input the number: "))
    result = math.log(num, math.e)

print('The result is: ' + str(result))
