import math
from MainLibrary.MainPackage import BasicFunctions

from_file1 = False

num1 = False
num2 = False
operation = False

list_of_operations = ["+","-","*","/","^"]

try:
    file = open("Inputs.txt", 'r')
    line1 = file.readline()
    operation = line1[0: line1.__len__() - 1]

    if not list_of_operations.__contains__(operation):
        operation = 1/0

    line2 = file.readline()
    num1 = float(line2[0: line2.__len__() - 1])

    line3 = file.readline()
    num2 = float(line3[0: line3.__len__()])

    from_file1 = True
except FileNotFoundError:
    pass
except IndexError:
    pass
except ValueError:
    pass
except ZeroDivisionError:
    pass

if not from_file1:
    print('Available operations: ')
    print(list_of_operations)
    operation = BasicFunctions.ask_for_string("Choose the desired operation: ", list_of_operations)

def attempt_to_calculate(from_file, num1, num2):
    try:
        if operation == '+':
            if not from_file:
                num1 = BasicFunctions.ask_for_float("Choose the first number: ", False)
                num2 = BasicFunctions.ask_for_float("Choose the second number: ", False)

            result1 = num1 + num2
        elif operation == '-':
            if not from_file:
                num1 = BasicFunctions.ask_for_float("Choose the first number: ", False)
                num2 = BasicFunctions.ask_for_float("Choose the second number: ", False)

            result1 = num1 - num2
        elif operation == '*':
            if not from_file:
                num1 = BasicFunctions.ask_for_float("Choose the first number: ", False)
                num2 = BasicFunctions.ask_for_float("Choose the second number: ", False)

            result1 = num1 * num2
        elif operation == '/':
            if not from_file:
                num1 = BasicFunctions.ask_for_float("Choose the first number: ", False)
                num2 = BasicFunctions.ask_for_float("Choose the second number: ", False)

            result1 = num1 / num2
        elif operation == '^':
            if not from_file:
                num1 = BasicFunctions.ask_for_float("Choose the base: ", False)
                num2 = BasicFunctions.ask_for_float("Choose the exponent: ", False)

            result1 = math.pow(num1, num2)
        return result1
    except ValueError:
        print('Cannot calculate operation, try again.')
        return attempt_to_calculate(from_file, num1, num2)
    except OverflowError:
        print('Cannot calculate operation, try again.')
        return attempt_to_calculate(from_file, num1, num2)
    except ZeroDivisionError:
        print('Cannot calculate operation, try again.')
        return attempt_to_calculate(from_file, num1, num2)
    except UnboundLocalError:
        print('Cannot calculate operation.')
        #return attempt_to_calculate(from_file, num1, num2)
    except RecursionError:
        print('Cannot calculate operation.')
        #return attempt_to_calculate(from_file, num1, num2)

result = attempt_to_calculate(from_file1, num1, num2)

if from_file1:
    print('The result (file numbers) is: ' + str(result))
else:
    print('The result (input numbers) is: ' + str(result))


