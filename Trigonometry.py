import math

print('Available operations: ')
print('"sin", "cos", "tan", "csc", "sec", "cot"')

operation = input("Chose the desired operation: ")

num = float(input("Input the number in radians: "))

result = 0

if operation == 'sin':
    result = math.sin(num)
elif operation == 'cos':
    result = math.cos(num)
elif operation == 'tan':
    result = math.tan(num)
elif operation == 'csc':
    if math.sin(num) == 0:
        result = "Cannot divide by zero"
    else:
        result = 1 / math.sin(num)
elif operation == 'sec':
    if math.cos(num) == 0:
        result = "Cannot divide by zero"
    else:
        result = 1 / math.cos(num)
elif operation == 'cot':
    if math.tan(num) == 0:
        result = "Cannot divide by zero"
    else:
        result = 1 / math.tan(num)

print('The result is: ' + str(result))
