#import math

from MainLibrary.MainPackage import BasicFunctions
from MainLibrary.MainPackage import AdvancedFunctions
from MainLibrary.MainPackage import GeneralFunctions

from_file1 = False

num1 = False
num2 = False
operation = False
result = BasicFunctions.calculate("+", "0", "0")

list_of_operations = ["+","-","*","/","^","nthroot"]
list_of_inputs = ["Manual", "File"]
list_of_styles = ["Expression", "Old", "RPN"]

print('Available options: ')
print(list_of_inputs)

input_type = BasicFunctions.ask_for_string("Choose, whether to input numbers manually or from a file: ", list_of_inputs)

print('Available styles: ')
print(["Expression", "Old", "RPN (Reverse Polish Notation)"])

style = BasicFunctions.ask_for_string("Choose the expression style: ", list_of_styles)

if input_type == "File":
    try:
        file = open("Inputs.txt", 'r')
        line1 = file.readline()
        operation = line1[0: line1.__len__() - 1]

        if not list_of_operations.__contains__(operation):
            operation = 1 / 0

        line2 = file.readline()
        num1 = float(line2[0: line2.__len__() - 1])

        line3 = file.readline()
        num2 = float(line3[0: line3.__len__()])

        from_file1 = True
        result = BasicFunctions.calculate(operation, num1, num2)
    except FileNotFoundError:
        pass
    except IndexError:
        pass
    except ValueError:
        pass
    except ZeroDivisionError:
        pass

if input_type == "File":
    pass
elif input_type == "Manual":
    print('Available operations: ')
    print(list_of_operations)

    if style == "Old":
        operation = BasicFunctions.ask_for_string("Choose the desired operation: ", list_of_operations)

        num1 = BasicFunctions.ask_for_float("Choose the first number: ", False)
        num2 = BasicFunctions.ask_for_float("Choose the second number: ", False)

        result = BasicFunctions.calculate(operation, num1, num2)
    elif style == "Expression":
        expression = input("Input your desired expression (parentheses are ignored): ")
        expression_value = 0
        try:
            expression_value = AdvancedFunctions.solve_expression(expression)
            result['OK'] = True
            result['calculated_value'] = expression_value
        except IndexError:
            result['OK'] = False
            result['error_message'] = 'IndexError'
        except ZeroDivisionError:
            result['OK'] = False
            result['error_message'] = 'ZeroDivisionError'
    elif style == "RPN":
        result = GeneralFunctions.rpn_style(list_of_operations)
        #3 2 ^ 16 sqrt + 10 6 - * 5 / 2 3 ^ + 25 sqrt -


if result["OK"]:
    print('The result is: ' + str(float(result["calculated_value"])))
else:
    print('An error has occurred: ' + str(result["error_message"]))