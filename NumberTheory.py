import math

print('Available operations: ')
print('"nthroot", "!", "mod", "floor", "round", "ceil"')

operation = input("Chose the desired operation: ")

result = 0

if operation == 'nthroot':
    num1 = float(input("Input the radicand: "))
    num2 = float(input("Input the index: "))

    result = math.pow(num1, 1/num2)
elif operation == 'mod':
    num1 = float(input("Input the first number: "))
    num2 = float(input("Input the second number: "))

    result = num1 % num2
else:
    num = float(input("Input the number: "))

    if operation == "!":
        if num < 0:
            result = "Factorial not defined for negative values"
        else:
            result = math.factorial(math.floor(num))
    elif operation == "floor":
        result = math.floor(num)
    elif operation == "round":
        fraction = math.modf(num)[0]
        if fraction >= 0.5:
            fraction = 1
        else:
            fraction = 0
        result = math.floor(num) + fraction
    elif operation == "ceil":
        result = math.ceil(num)

print('The result is: ' + str(result))
