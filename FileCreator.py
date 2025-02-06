import math
import time
from MainLibrary.MainPackage import AdvancedFunctions

start_time = time.time()

list_of_operations = ["+","-","*","/","^","nthroot"]

expressions = open("Expressions.txt", 'w')

for i in range(0, 1000):
    current_expression = AdvancedFunctions.generate_expression(4, list_of_operations)

    expressions.write(current_expression + "\n")

expressions.close()

results = open("Results.txt", 'w')

with open('Expressions.txt', mode='r') as readable_file:
    for i in range(0, 1000):
        expression = readable_file.readline()
        expression = expression[0:expression.__len__() -2]
        result = AdvancedFunctions.solve_expression(expression)

        results.write(expression + " = " + str(result) + "\n")

print('Time (s): ' + str(time.time() - start_time))
print('Time (ms): ' + str(math.floor((time.time() - start_time) * 1000)))