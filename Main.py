#import math

from MainLibrary.MainPackage import BasicFunctions
#from MainLibrary.MainPackage import AdvancedFunctions
from MainLibrary.MainPackage import GeneralFunctions

from_file1 = False

num1 = False
num2 = False
operation = False
result = BasicFunctions.calculate("+", "0", "0")

list_of_operations = ["+","-","*","/","^","nthroot"]
#list_of_inputs = ["Manual", "File"]
list_of_styles = ["Expression", "Old", "RPN"]

#print('Available options: ')
#print(list_of_inputs)

#input_type = BasicFunctions.ask_for_string("Choose, whether to input numbers manually or from a file: ", list_of_inputs)

print('Available styles: ')
print(["Expression", "Old", "RPN (Reverse Polish Notation)"])

style = BasicFunctions.ask_for_string("Choose the expression style: ", list_of_styles)

print('Available operations: ')
print(list_of_operations)

if style == "Old":
    result = GeneralFunctions.old_style(list_of_operations)
elif style == "Expression":
    result = GeneralFunctions.expression_style()
elif style == "RPN":
    result = GeneralFunctions.rpn_style(list_of_operations)
    #3 2 ^ 9 2 nthroot + 8 6 - * 5 / 2 3 ^ + 16 2 nthroot -

if result["OK"]:
    print('The result is: ' + str(float(result["calculated_value"])))
else:
    print('An error has occurred: ' + str(result["error_message"]))

# if input_type == "File":
#     try:
#         file = open("Inputs.txt", 'r')
#         line1 = file.readline()
#         operation = line1[0: line1.__len__() - 1]
#
#         if not list_of_operations.__contains__(operation):
#             operation = 1 / 0
#
#         line2 = file.readline()
#         num1 = float(line2[0: line2.__len__() - 1])
#
#         line3 = file.readline()
#         num2 = float(line3[0: line3.__len__()])
#
#         from_file1 = True
#         result = BasicFunctions.calculate(operation, num1, num2)
#     except FileNotFoundError:
#         pass
#     except IndexError:
#         pass
#     except ValueError:
#         pass
#     except ZeroDivisionError:
#         pass
# elif input_type == "Manual":
