import math
from MainLibrary.MainPackage import BasicFunctions

list_of_operations = ["nthroot", "!", "mod", "floor", "round", "ceil"]

print('Available operations: ')
print(list_of_operations)

operation = BasicFunctions.ask_for_string("Choose the desired operation: ", list_of_operations)

def attempt_to_calculate():
    try:
        if operation == 'nthroot':
            num1 = BasicFunctions.ask_for_float("Input the radicand: ", False)
            num2 = BasicFunctions.ask_for_float("Input the index: ", False)

            result1 = math.pow(num1, 1 / num2)
        elif operation == 'mod':
            num1 = BasicFunctions.ask_for_float("Input the first number: ", False)
            num2 = BasicFunctions.ask_for_float("Input the second number: ", False)

            result1 = num1 % num2
        else:
            num = BasicFunctions.ask_for_float("Input the number: ", False)
            result1 = 0

            if operation == "!":
                result1 = math.gamma(num + 1)
            elif operation == "floor":
                result1 = math.floor(num)
            elif operation == "round":
                fraction = math.modf(num)[0]
                if fraction >= 0.5:
                    fraction = 1
                else:
                    fraction = 0
                result1 = math.floor(num) + fraction
            elif operation == "ceil":
                result1 = math.ceil(num)
        return result1
    except ValueError:
        print("Cannot perform operation, try again.")
        return attempt_to_calculate()
    except OverflowError:
        print("Cannot perform operation, try again.")
        return attempt_to_calculate()
    except ZeroDivisionError:
        print("Cannot perform operation, try again.")
        return attempt_to_calculate()

result = attempt_to_calculate()

print('The result is: ' + str(result))
