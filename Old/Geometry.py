import math

print('Available operations: ')
print('"Area", "Perimeter"')

operation = input("Chose the desired operation: ")

print('Available shapes: ')
print('"Triangle", "Rectangle", "Circle"')

shape = input("Chose the desired operation: ")

result = 0

if operation == "Area":
    if shape == "Triangle":
        num1 = float(input("Input a side length of the triangle: "))
        num2 = float(input("Input the height projected onto this side: "))

        result = num1 * num2 * 1/2
    elif shape == "Rectangle":
        num1 = float(input("Input the first side length: "))
        num2 = float(input("Input the second side length: "))

        result = num1 * num2
    elif shape == "Circle":
        num1 = float(input("Input the length of the radius: "))

        result = num1 * num1 * math.pi
elif operation == "Perimeter":
    if shape == "Triangle":
        num1 = float(input("Input the length of the first side : "))
        num2 = float(input("Input the length of the second side: "))
        num3 = float(input("Input the length of the third side: "))

        result = num1 + num2 + num3
    elif shape == "Rectangle":
        num1 = float(input("Input the length of the first side : "))
        num2 = float(input("Input the length of the second side: "))

        result = num1 * 2 + num2 * 2
    elif shape == "Circle":
        num1 = float(input("Input the length of the radius: "))

        result = 2 * num1 * math.pi

print('The result is: ' + str(result))