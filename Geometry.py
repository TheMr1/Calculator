import math
from MainLibrary.MainPackage import BasicFunctions

list_of_operations = ["Area", "Perimeter"]

print('Available operations: ')
print(list_of_operations)

operation = BasicFunctions.ask_for_string("Choose the desired operation: ", list_of_operations)

list_of_shapes = ["Triangle", "Rectangle", "Circle"]

print('Available shapes: ')
print(list_of_shapes)

shape = BasicFunctions.ask_for_string("Choose the desired shape: ", list_of_shapes)

result = 0

if operation == "Area":
    if shape == "Triangle":
        num1 = BasicFunctions.ask_for_float("Input a side length of the triangle: ", False)
        num2 = BasicFunctions.ask_for_float("Input the height projected onto this side: ", False)

        result = num1 * num2 * 1/2
    elif shape == "Rectangle":
        num1 = BasicFunctions.ask_for_float("Input the first side length: ", False)
        num2 = BasicFunctions.ask_for_float("Input the second side length: ", False)

        result = num1 * num2
    elif shape == "Circle":
        num1 = BasicFunctions.ask_for_float("Input the length of the radius: ", False)

        result = num1 * num1 * math.pi
elif operation == "Perimeter":
    if shape == "Triangle":
        num1 = BasicFunctions.ask_for_float("Input the first side length: ", False)
        num2 = BasicFunctions.ask_for_float("Input the second side length: ", False)
        num3 = BasicFunctions.ask_for_float("Input the third side length: ", False)

        result = num1 + num2 + num3
    elif shape == "Rectangle":
        num1 = BasicFunctions.ask_for_float("Input the first side length: ", False)
        num2 = BasicFunctions.ask_for_float("Input the second side length: ", False)

        result = num1 * 2 + num2 * 2
    elif shape == "Circle":
        num1 = BasicFunctions.ask_for_float("Input the length of the radius: ", False)

        result = 2 * num1 * math.pi

print('The result is: ' + str(result))